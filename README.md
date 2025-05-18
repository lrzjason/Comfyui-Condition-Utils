# Comfyui-Condition-Utils

A collection of utility nodes for handling condition tensors in ComfyUI.

## Nodes
![alt text](https://github.com/lrzjason/Comfyui-Condition-Utils/blob/main/example.png)

### Save Condition

This node allows you to save a condition tensor to a file with a specified filename. The tensor will be saved in the `ComfyUI/models/conditions` folder.

#### Inputs

- **condition**: The `CONDITIONING` tensor to save.
- **filename**: The name to use for the saved file (e.g., `my_condition`). The `.pt` extension will be added automatically if not provided.

#### Behavior

- This is an output node, meaning it doesn't pass any data to subsequent nodes in the workflow.
- It ensures the `ComfyUI/models/conditions` directory exists, creating it if necessary.
- Filenames are sanitized to prevent path traversal issues.
- The condition tensor, which is typically a list of tuples `(tensor, conditioning_info)`, is saved.

### Load Condition

This node allows you to load a previously saved condition tensor from a file.

#### Inputs

- **filename**: A dropdown list of available `.pt` files (displayed without the extension) found in the `ComfyUI/models/conditions` directory. Select the desired condition file to load.

#### Outputs

- **CONDITIONING**: The loaded condition tensor.

#### Behavior

- It ensures the `ComfyUI/models/conditions` directory exists.
- Filenames are sanitized.
- If the selected file is not found, an error is printed, and an empty conditioning is returned as a fallback.

## Key Changes & Features

- **Centralized Condition Storage**: Conditions are now stored in `ComfyUI/models/conditions`, managed via ComfyUI's `folder_paths` system. This makes it easier to manage and locate saved conditions.
- **Dynamic File Loading**: The `Load Condition` node now dynamically lists available condition files from the `conditions` directory, providing a user-friendly dropdown menu.
- **Automatic Directory Creation**: Both nodes automatically create the `conditions` directory if it doesn't exist.
- **Filename Sanitization**: Ensures safe file handling.
- **Automatic `.pt` Extension**: The `.pt` extension is handled automatically for both saving and loading.

## Installation

1. Clone or download this repository into your ComfyUI's `custom_nodes` directory.
2. Restart ComfyUI.
3. The nodes will be available in the "conditioning/utils" category.

## Usage

- **To Save**: Connect a condition tensor to the `Save Condition` node's input, specify a filename, and the tensor will be saved to the `ComfyUI/models/conditions` folder.
- **To Load**: Select a previously saved condition file from the dropdown menu in the `Load Condition` node. The node will output the loaded condition tensor for use in your workflow.


## Contact
- **Twitter**: [@Lrzjason](https://twitter.com/Lrzjason)  
- **Email**: lrzjason@gmail.com  
- **QQ Group**: 866612947  
- **Civitai**: [xiaozhijason](https://civitai.com/user/xiaozhijason)


## Sponsors me for more open source projects:
<div align="center">
  <table>
    <tr>
      <td align="center">
        <p>Buy me a coffee:</p>
        <img src="https://github.com/lrzjason/Comfyui-In-Context-Lora-Utils/blob/main/image/bmc_qr.png" alt="Buy Me a Coffee QR" width="200" />
      </td>
      <td align="center">
        <p>WeChat:</p>
        <img src="https://github.com/lrzjason/Comfyui-In-Context-Lora-Utils/blob/main/image/wechat.jpg" alt="WeChat QR" width="200" />
      </td>
    </tr>
  </table>
</div>
