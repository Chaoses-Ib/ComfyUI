# QueueTuple

The first item is the queue priority The second item is the hash id of the prompt object The third item is a Prompt The fourth item is optionally an ExtraData The fifth item is optionally a list of \"Good Outputs\" node IDs. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from comfy.api.models.queue_tuple import QueueTuple

# TODO update the JSON string below
json = "{}"
# create an instance of QueueTuple from a JSON string
queue_tuple_instance = QueueTuple.from_json(json)
# print the JSON string representation of the object
print QueueTuple.to_json()

# convert the object into a dict
queue_tuple_dict = queue_tuple_instance.to_dict()
# create an instance of QueueTuple from a dict
queue_tuple_form_dict = queue_tuple.from_dict(queue_tuple_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


