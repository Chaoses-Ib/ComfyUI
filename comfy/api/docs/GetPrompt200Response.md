# GetPrompt200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exec_info** | [**GetPrompt200ResponseExecInfo**](GetPrompt200ResponseExecInfo.md) |  | [optional] 

## Example

```python
from comfy.api.models.get_prompt200_response import GetPrompt200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPrompt200Response from a JSON string
get_prompt200_response_instance = GetPrompt200Response.from_json(json)
# print the JSON string representation of the object
print GetPrompt200Response.to_json()

# convert the object into a dict
get_prompt200_response_dict = get_prompt200_response_instance.to_dict()
# create an instance of GetPrompt200Response from a dict
get_prompt200_response_form_dict = get_prompt200_response.from_dict(get_prompt200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


