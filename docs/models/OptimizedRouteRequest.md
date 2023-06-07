# stadiamaps.model.optimized_route_request.OptimizedRouteRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**costing** | [**MatrixCostingModel**](MatrixCostingModel.md) | [**MatrixCostingModel**](MatrixCostingModel.md) |  | 
**[locations](#locations)** | list, tuple,  | tuple,  | The list of locations. The first and last are assumed to be the start and end points, and all intermediate points are locations that you want to visit along the way. | 
**id** | str,  | str,  | An identifier to disambiguate requests (echoed by the server). | [optional] 
**costing_options** | [**CostingOptions**](CostingOptions.md) | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**directions_options** | [**DirectionsOptions**](DirectionsOptions.md) | [**DirectionsOptions**](DirectionsOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# locations

The list of locations. The first and last are assumed to be the start and end points, and all intermediate points are locations that you want to visit along the way.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of locations. The first and last are assumed to be the start and end points, and all intermediate points are locations that you want to visit along the way. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

