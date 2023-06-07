# stadiamaps.model.locate_object.LocateObject

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | An identifier to disambiguate requests (echoed by the server). | [optional] 
**input_lat** | decimal.Decimal, int, float,  | decimal.Decimal,  | The input (searched) latitude. | [optional] value must be a 64 bit float
**input_lon** | decimal.Decimal, int, float,  | decimal.Decimal,  | The input (searched) longitude. | [optional] value must be a 64 bit float
**[nodes](#nodes)** | list, tuple,  | tuple,  |  | [optional] 
**[edges](#edges)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# nodes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LocateNode**](LocateNode.md) | [**LocateNode**](LocateNode.md) | [**LocateNode**](LocateNode.md) |  | 

# edges

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**LocateEdge**](LocateEdge.md) | [**LocateEdge**](LocateEdge.md) | [**LocateEdge**](LocateEdge.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

