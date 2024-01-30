# NodeInput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required** | **Dict[str, List[NodeInputRequiredValueInner]]** |  | 
**hidden** | **Dict[str, str]** |  | [optional] 

## Example

```python
from comfy.api.models.node_input import NodeInput

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInput from a JSON string
node_input_instance = NodeInput.from_json(json)
# print the JSON string representation of the object
print NodeInput.to_json()

# convert the object into a dict
node_input_dict = node_input_instance.to_dict()
# create an instance of NodeInput from a dict
node_input_form_dict = node_input.from_dict(node_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


