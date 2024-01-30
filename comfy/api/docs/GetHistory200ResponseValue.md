# GetHistory200ResponseValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timestamp** | **float** |  | [optional] 
**prompt** | [**QueueTuple**](QueueTuple.md) |  | [optional] 
**outputs** | **object** |  | [optional] 

## Example

```python
from comfy.api.models.get_history200_response_value import GetHistory200ResponseValue

# TODO update the JSON string below
json = "{}"
# create an instance of GetHistory200ResponseValue from a JSON string
get_history200_response_value_instance = GetHistory200ResponseValue.from_json(json)
# print the JSON string representation of the object
print GetHistory200ResponseValue.to_json()

# convert the object into a dict
get_history200_response_value_dict = get_history200_response_value_instance.to_dict()
# create an instance of GetHistory200ResponseValue from a dict
get_history200_response_value_form_dict = get_history200_response_value.from_dict(get_history200_response_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


