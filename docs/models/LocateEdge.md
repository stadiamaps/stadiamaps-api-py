# stadiamaps.model.locate_edge.LocateEdge

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**edge_id** | [**NodeId**](NodeId.md) | [**NodeId**](NodeId.md) |  | [optional] 
**correlated_lat** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**correlated_lon** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**percent_along** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**side_of_street** | str,  | str,  |  | [optional] must be one of ["left", "right", "neither", ] 
**linear_reference** | str,  | str,  | A base64-encoded [OpenLR location reference](https://www.openlr-association.com/fileadmin/user_upload/openlr-whitepaper_v1.5.pdf), for a graph edge of the road network matched by the query. | [optional] 
**outbound_reach** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**heading** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**inbound_reach** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**distance** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 32 bit float
**[predicted_speeds](#predicted_speeds)** | list, tuple,  | tuple,  | Predicted speed information based on historical data. If available, this will include 2016 entries. Each entry represents 5 minutes, where the first entry represents midnight on Monday, the second entry represents 00:05 on Monday, etc. | [optional] 
**edge_info** | [**LocateEdgeInfo**](LocateEdgeInfo.md) | [**LocateEdgeInfo**](LocateEdgeInfo.md) |  | [optional] 
**edge** | [**LocateDetailedEdge**](LocateDetailedEdge.md) | [**LocateDetailedEdge**](LocateDetailedEdge.md) |  | [optional] 
**[warnings](#warnings)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# predicted_speeds

Predicted speed information based on historical data. If available, this will include 2016 entries. Each entry represents 5 minutes, where the first entry represents midnight on Monday, the second entry represents 00:05 on Monday, etc.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Predicted speed information based on historical data. If available, this will include 2016 entries. Each entry represents 5 minutes, where the first entry represents midnight on Monday, the second entry represents 00:05 on Monday, etc. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# warnings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

