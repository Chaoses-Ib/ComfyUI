# ApiV1PromptsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | [**Prompt**](Prompt.md) |  | [optional] 
**files** | **List[bytearray]** | Files to upload along with this request.  The filename specified in the content-disposition can be used in your Prompt.  | [optional] 

## Example

```python
from comfy.api.models.api_v1_prompts_post_request import ApiV1PromptsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ApiV1PromptsPostRequest from a JSON string
api_v1_prompts_post_request_instance = ApiV1PromptsPostRequest.from_json(json)
# print the JSON string representation of the object
print ApiV1PromptsPostRequest.to_json()

# convert the object into a dict
api_v1_prompts_post_request_dict = api_v1_prompts_post_request_instance.to_dict()
# create an instance of ApiV1PromptsPostRequest from a dict
api_v1_prompts_post_request_form_dict = api_v1_prompts_post_request.from_dict(api_v1_prompts_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


