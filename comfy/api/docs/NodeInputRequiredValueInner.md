# NodeInputRequiredValueInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | **str** |  | [optional] 
**min** | **float** |  | [optional] 
**max** | **float** |  | [optional] 
**step** | **float** |  | [optional] 
**multiline** | **bool** |  | [optional] 

## Example

```python
from comfy.api.models.node_input_required_value_inner import NodeInputRequiredValueInner

# TODO update the JSON string below
json = "{}"
# create an instance of NodeInputRequiredValueInner from a JSON string
node_input_required_value_inner_instance = NodeInputRequiredValueInner.from_json(json)
# print the JSON string representation of the object
print NodeInputRequiredValueInner.to_json()

# convert the object into a dict
node_input_required_value_inner_dict = node_input_required_value_inner_instance.to_dict()
# create an instance of NodeInputRequiredValueInner from a dict
node_input_required_value_inner_form_dict = node_input_required_value_inner.from_dict(node_input_required_value_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


