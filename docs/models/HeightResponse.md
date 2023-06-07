# stadiamaps.model.height_response.HeightResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | An identifier to disambiguate requests (echoed by the server). | [optional] 
**[shape](#shape)** | list, tuple,  | tuple,  |  | [optional] 
**encoded_polyline** | str,  | str,  | The input polyline. | [optional] 
**[height](#height)** | list, tuple,  | tuple,  | The list of heights for each point, in meters. Present if &#x60;range&#x60; is &#x60;false&#x60;. | [optional] 
**[range_height](#range_height)** | list, tuple,  | tuple,  | The list of horizontal distances and heights (respectively) for each point, in meters. Present if &#x60;range&#x60; is &#x60;true&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# shape

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) |  | 

# height

The list of heights for each point, in meters. Present if `range` is `false`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of heights for each point, in meters. Present if &#x60;range&#x60; is &#x60;false&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

# range_height

The list of horizontal distances and heights (respectively) for each point, in meters. Present if `range` is `true`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of horizontal distances and heights (respectively) for each point, in meters. Present if &#x60;range&#x60; is &#x60;true&#x60;. | 

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
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

