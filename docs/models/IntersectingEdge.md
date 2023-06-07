# stadiamaps.model.intersecting_edge.IntersectingEdge

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**begin_heading** | decimal.Decimal, int,  | decimal.Decimal,  | The direction at the beginning of an edge. The units are degrees clockwise from north. | [optional] 
**from_edge_name_consistency** | bool,  | BoolClass,  | True if this intersecting edge at the end node has consistent names with the path from the other edge. | [optional] 
**to_edge_name_consistency** | bool,  | BoolClass,  | True if this intersecting edge at the end node has consistent names with the path to the other edge. | [optional] 
**driveability** | [**Traversability**](Traversability.md) | [**Traversability**](Traversability.md) |  | [optional] 
**cyclability** | [**Traversability**](Traversability.md) | [**Traversability**](Traversability.md) |  | [optional] 
**walkability** | [**Traversability**](Traversability.md) | [**Traversability**](Traversability.md) |  | [optional] 
**use** | [**EdgeUse**](EdgeUse.md) | [**EdgeUse**](EdgeUse.md) |  | [optional] 
**road_class** | [**RoadClass**](RoadClass.md) | [**RoadClass**](RoadClass.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

