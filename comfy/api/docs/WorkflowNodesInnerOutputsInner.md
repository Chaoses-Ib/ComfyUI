# WorkflowNodesInnerOutputsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**links** | **List[int]** |  | [optional] 
**slot_index** | **int** |  | [optional] 

## Example

```python
from comfy.api.models.workflow_nodes_inner_outputs_inner import WorkflowNodesInnerOutputsInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowNodesInnerOutputsInner from a JSON string
workflow_nodes_inner_outputs_inner_instance = WorkflowNodesInnerOutputsInner.from_json(json)
# print the JSON string representation of the object
print WorkflowNodesInnerOutputsInner.to_json()

# convert the object into a dict
workflow_nodes_inner_outputs_inner_dict = workflow_nodes_inner_outputs_inner_instance.to_dict()
# create an instance of WorkflowNodesInnerOutputsInner from a dict
workflow_nodes_inner_outputs_inner_form_dict = workflow_nodes_inner_outputs_inner.from_dict(workflow_nodes_inner_outputs_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


