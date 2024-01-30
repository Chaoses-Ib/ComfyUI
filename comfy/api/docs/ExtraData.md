# ExtraData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_pnginfo** | [**ExtraDataExtraPnginfo**](ExtraDataExtraPnginfo.md) |  | [optional] 

## Example

```python
from comfy.api.models.extra_data import ExtraData

# TODO update the JSON string below
json = "{}"
# create an instance of ExtraData from a JSON string
extra_data_instance = ExtraData.from_json(json)
# print the JSON string representation of the object
print ExtraData.to_json()

# convert the object into a dict
extra_data_dict = extra_data_instance.to_dict()
# create an instance of ExtraData from a dict
extra_data_form_dict = extra_data.from_dict(extra_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


