# PromptRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | [optional] 
**prompt** | [**Prompt**](Prompt.md) |  | 
**extra_data** | [**ExtraData**](ExtraData.md) |  | [optional] 

## Example

```python
from comfy.api.models.prompt_request import PromptRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromptRequest from a JSON string
prompt_request_instance = PromptRequest.from_json(json)
# print the JSON string representation of the object
print PromptRequest.to_json()

# convert the object into a dict
prompt_request_dict = prompt_request_instance.to_dict()
# create an instance of PromptRequest from a dict
prompt_request_form_dict = prompt_request.from_dict(prompt_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


