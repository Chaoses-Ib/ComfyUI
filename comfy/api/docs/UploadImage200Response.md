# UploadImage200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name to use in a workflow.  | [optional] 

## Example

```python
from comfy.api.models.upload_image200_response import UploadImage200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UploadImage200Response from a JSON string
upload_image200_response_instance = UploadImage200Response.from_json(json)
# print the JSON string representation of the object
print UploadImage200Response.to_json()

# convert the object into a dict
upload_image200_response_dict = upload_image200_response_instance.to_dict()
# create an instance of UploadImage200Response from a dict
upload_image200_response_form_dict = upload_image200_response.from_dict(upload_image200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


