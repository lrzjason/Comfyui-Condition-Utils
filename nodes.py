import os
import torch
import folder_paths

# Global variable for condition directory path
# condition_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "condition")
condition_dir  = os.path.join(folder_paths.models_dir, "conditions")

# Register the condition directory with folder_paths if not already registered
if "conditions" not in folder_paths.folder_names_and_paths:
    folder_paths.folder_names_and_paths["conditions"] = ([condition_dir], {'.pt'})

class SaveCondition:
    """
    A node that saves a condition tensor to a file with a specified filename.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "condition": ("CONDITIONING",),
                "filename": ("STRING", {"default": "condition_tensor"}),
            },
        }
    
    RETURN_TYPES = ()
    FUNCTION = "save_condition"
    CATEGORY = "conditioning/utils"
    OUTPUT_NODE = True
    
    def save_condition(self, condition, filename):
        # Ensure the condition directory exists
        os.makedirs(condition_dir, exist_ok=True)
        
        # Sanitize filename (remove any path traversal attempts)
        safe_filename = os.path.basename(filename)
        if not safe_filename.endswith(".pt"):
            safe_filename += ".pt"
        
        # Get the condition directory from folder_paths
        save_dir = folder_paths.folder_names_and_paths["conditions"][0][0]
        
        # Full path to save the condition tensor
        save_path = os.path.join(save_dir, safe_filename)
        
        # Save the condition tensor
        try:
            # Extract the tensor from the conditioning format
            # Conditioning is typically a list of tuples (tensor, conditioning_info)
            tensors_to_save = []
            for cond, cond_info in condition:
                tensors_to_save.append((cond.clone(), cond_info))
            
            # Save the tensors
            torch.save(tensors_to_save, save_path)
            print(f"Condition tensor saved to {save_path}")
        except Exception as e:
            print(f"Error saving condition tensor: {e}")
        
        # Return an empty tuple as this is an output node
        return ()

class LoadCondition:
    """
    A node that loads a condition tensor from a file with a specified filename.
    """
    
    @classmethod
    def INPUT_TYPES(cls):
        # Ensure the condition directory exists
        os.makedirs(condition_dir, exist_ok=True)
        
        # Get list of available condition files using folder_paths
        condition_files = []
        try:
            # Get the list of files with .pt extension
            condition_files = folder_paths.get_filename_list("conditions")
            # Remove .pt extension for display
            condition_files = [os.path.splitext(file)[0] for file in condition_files]
        except Exception as e:
            print(f"Error listing condition files: {e}")
        
        # If no files found, add a default entry
        if not condition_files:
            condition_files = ["No files found"]
        
        return {
            "required": {
                "filename": (condition_files, ),
            },
        }
    
    RETURN_TYPES = ("CONDITIONING",)
    FUNCTION = "load_condition"
    CATEGORY = "conditioning/utils"
    
    def load_condition(self, filename):
        # Ensure the condition directory exists
        os.makedirs(condition_dir, exist_ok=True)
        
        # Sanitize filename (remove any path traversal attempts)
        safe_filename = os.path.basename(filename)
        if not safe_filename.endswith(".pt"):
            safe_filename += ".pt"
        
        # Get the condition directory from folder_paths
        load_dir = folder_paths.folder_names_and_paths["conditions"][0][0]
        
        # Full path to load the condition tensor
        load_path = os.path.join(load_dir, safe_filename)
        
        # Load the condition tensor
        try:
            if not os.path.exists(load_path):
                raise FileNotFoundError(f"Condition file not found: {load_path}")
                
            # Load the tensors
            loaded_tensors = torch.load(load_path)
            print(f"Condition tensor loaded from {load_path}")
            return (loaded_tensors,)
        except Exception as e:
            print(f"Error loading condition tensor: {e}")
            # Return an empty conditioning as fallback
            return ([],)

# Node class mappings
NODE_CLASS_MAPPINGS = {
    "SaveCondition": SaveCondition,
    "LoadCondition": LoadCondition,
}

# Display name mappings
NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveCondition": "Save Condition",
    "LoadCondition": "Load Condition",
}