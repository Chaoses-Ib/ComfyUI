# WorkflowNodesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**pos** | **List[float]** |  | [optional] 
**size** | [**WorkflowNodesInnerSize**](WorkflowNodesInnerSize.md) |  | [optional] 
**flags** | **Dict[str, object]** |  | [optional] 
**order** | **int** |  | [optional] 
**mode** | **int** |  | [optional] 
**inputs** | [**List[WorkflowNodesInnerInputsInner]**](WorkflowNodesInnerInputsInner.md) |  | [optional] 
**outputs** | [**List[WorkflowNodesInnerOutputsInner]**](WorkflowNodesInnerOutputsInner.md) |  | [optional] 
**properties** | **object** |  | [optional] 
**widgets_values** | **List[str]** |  | [optional] 

## Example

```python
from comfy.api.models.workflow_nodes_inner import WorkflowNodesInner

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowNodesInner from a JSON string
workflow_nodes_inner_instance = WorkflowNodesInner.from_json(json)
# print the JSON string representation of the object
print WorkflowNodesInner.to_json()

# convert the object into a dict
workflow_nodes_inner_dict = workflow_nodes_inner_instance.to_dict()
# create an instance of WorkflowNodesInner from a dict
workflow_nodes_inner_form_dict = workflow_nodes_inner.from_dict(workflow_nodes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


