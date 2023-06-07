# stadiamaps.model.isochrone_request.IsochroneRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**costing** | [**IsochroneCostingModel**](IsochroneCostingModel.md) | [**IsochroneCostingModel**](IsochroneCostingModel.md) |  | 
**[locations](#locations)** | list, tuple,  | tuple,  |  | 
**[contours](#contours)** | list, tuple,  | tuple,  |  | 
**id** | str,  | str,  | An identifier to disambiguate requests (echoed by the server). | [optional] 
**costing_options** | [**CostingOptions**](CostingOptions.md) | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**polygons** | bool,  | BoolClass,  | If true, the generated GeoJSON will use polygons. The default is to use LineStrings. Polygon output makes it easier to render overlapping areas in some visualization tools (such as MapLibre renderers). | [optional] if omitted the server will use the default value of False
**denoise** | decimal.Decimal, int, float,  | decimal.Decimal,  | A value in the range [0, 1] which will be used to smooth out or remove smaller contours. A value of 1 will only return the largest contour for a given time value. A value of 0.5 drops any contours that are less than half the area of the largest contour in the set of contours for that same time value. | [optional] if omitted the server will use the default value of 1value must be a 64 bit float
**generalize** | decimal.Decimal, int, float,  | decimal.Decimal,  | The value in meters to be used as a tolerance for Douglas-Peucker generalization. | [optional] if omitted the server will use the default value of 200.0value must be a 64 bit float
**show_locations** | bool,  | BoolClass,  | If true, then the output GeoJSON will include the input locations as two MultiPoint features: one for the exact input coordinates, and a second for the route network node location that the point was snapped to. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# locations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) |  | 

# contours

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Contour**](Contour.md) | [**Contour**](Contour.md) | [**Contour**](Contour.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

