# Workflow


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_node_id** | **int** |  | [optional] 
**last_link_id** | **int** |  | [optional] 
**nodes** | [**List[WorkflowNodesInner]**](WorkflowNodesInner.md) |  | [optional] 
**links** | **List[List[WorkflowLinksInnerInner]]** |  | [optional] 
**groups** | **List[object]** |  | [optional] 
**config** | **object** |  | [optional] 
**extra** | **object** |  | [optional] 
**version** | **float** |  | [optional] 

## Example

```python
from comfy.api.models.workflow import Workflow

# TODO update the JSON string below
json = "{}"
# create an instance of Workflow from a JSON string
workflow_instance = Workflow.from_json(json)
# print the JSON string representation of the object
print Workflow.to_json()

# convert the object into a dict
workflow_dict = workflow_instance.to_dict()
# create an instance of Workflow from a dict
workflow_form_dict = workflow.from_dict(workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


