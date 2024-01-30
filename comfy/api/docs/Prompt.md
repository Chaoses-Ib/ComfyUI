# Prompt

The keys are stringified integers corresponding to nodes.  You can retrieve the last prompt run using GET /api/v1/prompts 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from comfy.api.models.prompt import Prompt

# TODO update the JSON string below
json = "{}"
# create an instance of Prompt from a JSON string
prompt_instance = Prompt.from_json(json)
# print the JSON string representation of the object
print Prompt.to_json()

# convert the object into a dict
prompt_dict = prompt_instance.to_dict()
# create an instance of Prompt from a dict
prompt_form_dict = prompt.from_dict(prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


