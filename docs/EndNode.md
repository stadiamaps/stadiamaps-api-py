# EndNode

The node at the end of this edge

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intersecting_edges** | [**List[IntersectingEdge]**](IntersectingEdge.md) | A set of edges intersecting this node. | [optional] 
**elapsed_time** | **float** | The elapsed time along the path to arrive at this node. | [optional] 
**admin_index** | **int** | The index into the &#x60;admins&#x60; list in which this node lies. | [optional] 
**type** | [**NodeType**](NodeType.md) |  | [optional] 
**fork** | **bool** | True if this node is a fork. | [optional] 
**time_zone** | **str** | The canonical TZDB identifier for the node&#39;s time zone. | [optional] 

## Example

```python
from stadiamaps.models.end_node import EndNode

# TODO update the JSON string below
json = "{}"
# create an instance of EndNode from a JSON string
end_node_instance = EndNode.from_json(json)
# print the JSON string representation of the object
print EndNode.to_json()

# convert the object into a dict
end_node_dict = end_node_instance.to_dict()
# create an instance of EndNode from a dict
end_node_form_dict = end_node.from_dict(end_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


