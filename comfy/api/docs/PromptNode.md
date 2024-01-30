# PromptNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**class_type** | **str** | The node&#39;s class type, which maps to a class in NODE_CLASS_MAPPINGS. | 
**inputs** | [**Dict[str, PromptNodeInputsValue]**](PromptNodeInputsValue.md) | The inputs for the node, which can be scalar values or references to other nodes&#39; outputs. | 
**is_changed** | [**PromptNodeIsChanged**](PromptNodeIsChanged.md) |  | [optional] 

## Example

```python
from comfy.api.models.prompt_node import PromptNode

# TODO update the JSON string below
json = "{}"
# create an instance of PromptNode from a JSON string
prompt_node_instance = PromptNode.from_json(json)
# print the JSON string representation of the object
print PromptNode.to_json()

# convert the object into a dict
prompt_node_dict = prompt_node_instance.to_dict()
# create an instance of PromptNode from a dict
prompt_node_form_dict = prompt_node.from_dict(prompt_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


