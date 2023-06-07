# stadiamaps.model.height_request.HeightRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | An identifier to disambiguate requests (echoed by the server). | [optional] 
**[shape](#shape)** | list, tuple,  | tuple,  | REQUIRED if &#x60;encoded_polyline&#x60; is not present. | [optional] 
**encoded_polyline** | str,  | str,  | REQUIRED if &#x60;shape&#x60; is not present. An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm). | [optional] 
**shape_format** | str,  | str,  | Specifies whether the polyline is encoded with 6 digit precision (polyline6) or 5 digit precision (polyline5). | [optional] must be one of ["polyline6", "polyline5", ] if omitted the server will use the default value of "polyline6"
**range** | bool,  | BoolClass,  | Controls whether or not the returned array is one-dimensional (height only) or two-dimensional (with a range and height). The range dimension can be used to generate a graph or steepness gradient along a route. | [optional] if omitted the server will use the default value of False
**height_precision** | decimal.Decimal, int,  | decimal.Decimal,  | The decimal precision (number of digits after the point) of the output. When 0, integer values are returned. Valid values are 0, 1, and 2. | [optional] if omitted the server will use the default value of 0
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# shape

REQUIRED if `encoded_polyline` is not present.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | REQUIRED if &#x60;encoded_polyline&#x60; is not present. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

