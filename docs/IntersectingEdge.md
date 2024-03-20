# IntersectingEdge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin_heading** | **int** | The direction at the beginning of an edge. The units are degrees clockwise from north. | [optional] 
**from_edge_name_consistency** | **bool** | True if this intersecting edge at the end node has consistent names with the path from the other edge. | [optional] 
**to_edge_name_consistency** | **bool** | True if this intersecting edge at the end node has consistent names with the path to the other edge. | [optional] 
**driveability** | [**Traversability**](Traversability.md) |  | [optional] 
**cyclability** | [**Traversability**](Traversability.md) |  | [optional] 
**walkability** | [**Traversability**](Traversability.md) |  | [optional] 
**use** | [**EdgeUse**](EdgeUse.md) |  | [optional] 
**road_class** | [**RoadClass**](RoadClass.md) |  | [optional] 

## Example

```python
from stadiamaps.models.intersecting_edge import IntersectingEdge

# TODO update the JSON string below
json = "{}"
# create an instance of IntersectingEdge from a JSON string
intersecting_edge_instance = IntersectingEdge.from_json(json)
# print the JSON string representation of the object
print(IntersectingEdge.to_json())

# convert the object into a dict
intersecting_edge_dict = intersecting_edge_instance.to_dict()
# create an instance of IntersectingEdge from a dict
intersecting_edge_form_dict = intersecting_edge.from_dict(intersecting_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


