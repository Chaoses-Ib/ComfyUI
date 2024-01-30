# QueueTupleInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_pnginfo** | [**ExtraDataExtraPnginfo**](ExtraDataExtraPnginfo.md) |  | [optional] 

## Example

```python
from comfy.api.models.queue_tuple_inner import QueueTupleInner

# TODO update the JSON string below
json = "{}"
# create an instance of QueueTupleInner from a JSON string
queue_tuple_inner_instance = QueueTupleInner.from_json(json)
# print the JSON string representation of the object
print QueueTupleInner.to_json()

# convert the object into a dict
queue_tuple_inner_dict = queue_tuple_inner_instance.to_dict()
# create an instance of QueueTupleInner from a dict
queue_tuple_inner_form_dict = queue_tuple_inner.from_dict(queue_tuple_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


