# stadiamaps.model.matrix_response.MatrixResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[sources_to_targets](#sources_to_targets)** | list, tuple,  | tuple,  | The matrix of starting and ending locations, along with the computed distance and travel time. The array is row-ordered. This means that the time and distance from the first location to all others forms the first row of the array, followed by the time and distance from the second source location to all target locations, etc. | 
**[sources](#sources)** | list, tuple,  | tuple,  | The list of starting locations | 
**units** | [**ValhallaLongUnits**](ValhallaLongUnits.md) | [**ValhallaLongUnits**](ValhallaLongUnits.md) |  | 
**[targets](#targets)** | list, tuple,  | tuple,  | The list of ending locations | 
**id** | str,  | str,  | An identifier to disambiguate requests (echoed by the server). | [optional] 
**[warnings](#warnings)** | list, tuple,  | tuple,  |  | [optional] 
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
[items](#items) | list, tuple,  | tuple,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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
[items](#items) | list, tuple,  | tuple,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) |  | 

# sources_to_targets

The matrix of starting and ending locations, along with the computed distance and travel time. The array is row-ordered. This means that the time and distance from the first location to all others forms the first row of the array, followed by the time and distance from the second source location to all target locations, etc.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The matrix of starting and ending locations, along with the computed distance and travel time. The array is row-ordered. This means that the time and distance from the first location to all others forms the first row of the array, followed by the time and distance from the second source location to all target locations, etc. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[items](#items) | list, tuple,  | tuple,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MatrixDistance**](MatrixDistance.md) | [**MatrixDistance**](MatrixDistance.md) | [**MatrixDistance**](MatrixDistance.md) |  | 

# warnings

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Warning**](Warning.md) | [**Warning**](Warning.md) | [**Warning**](Warning.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

