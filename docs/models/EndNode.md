# stadiamaps.model.end_node.EndNode

The node at the end of this edge

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The node at the end of this edge | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[intersecting_edges](#intersecting_edges)** | list, tuple,  | tuple,  | A set of edges intersecting this node. | [optional] 
**elapsed_time** | decimal.Decimal, int, float,  | decimal.Decimal,  | The elapsed time along the path to arrive at this node. | [optional] value must be a 64 bit float
**admin_index** | decimal.Decimal, int,  | decimal.Decimal,  | The index into the &#x60;admins&#x60; list in which this node lies. | [optional] 
**type** | [**NodeType**](NodeType.md) | [**NodeType**](NodeType.md) |  | [optional] 
**fork** | bool,  | BoolClass,  | True if this node is a fork. | [optional] 
**time_zone** | str,  | str,  | The canonical TZDB identifier for the node&#x27;s time zone. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# intersecting_edges

A set of edges intersecting this node.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A set of edges intersecting this node. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IntersectingEdge**](IntersectingEdge.md) | [**IntersectingEdge**](IntersectingEdge.md) | [**IntersectingEdge**](IntersectingEdge.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

