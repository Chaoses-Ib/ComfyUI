# PostHistoryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clear** | **bool** |  | [optional] 
**delete** | **List[int]** |  | [optional] 

## Example

```python
from comfy.api.models.post_history_request import PostHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostHistoryRequest from a JSON string
post_history_request_instance = PostHistoryRequest.from_json(json)
# print the JSON string representation of the object
print PostHistoryRequest.to_json()

# convert the object into a dict
post_history_request_dict = post_history_request_instance.to_dict()
# create an instance of PostHistoryRequest from a dict
post_history_request_form_dict = post_history_request.from_dict(post_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


