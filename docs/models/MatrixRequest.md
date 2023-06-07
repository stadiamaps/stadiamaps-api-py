# stadiamaps.model.matrix_request.MatrixRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[sources](#sources)** | list, tuple,  | tuple,  | The list of starting locations | 
**costing** | [**MatrixCostingModel**](MatrixCostingModel.md) | [**MatrixCostingModel**](MatrixCostingModel.md) |  | 
**[targets](#targets)** | list, tuple,  | tuple,  | The list of ending locations | 
**id** | str,  | str,  | An identifier to disambiguate requests (echoed by the server). | [optional] 
**costing_options** | [**CostingOptions**](CostingOptions.md) | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**matrix_locations** | decimal.Decimal, int,  | decimal.Decimal,  | Only applicable to one-to-many or many-to-one requests. This defaults to all locations. When specified explicitly, this option allows a partial result to be returned. This is basically equivalent to \&quot;find the closest/best locations out of the full set.\&quot; This can have a dramatic improvement for large requests. | [optional] 
**directions_options** | [**DirectionsOptions**](DirectionsOptions.md) | [**DirectionsOptions**](DirectionsOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# sources

The list of starting locations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of starting locations | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) |  | 

# targets

The list of ending locations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of ending locations | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

