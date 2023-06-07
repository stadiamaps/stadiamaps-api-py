# stadiamaps.model.locate_edge_info.LocateEdgeInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mean_elevation** | decimal.Decimal, int, float,  | decimal.Decimal,  | The mean elevation, in meters, relative to sea level. | [optional] value must be a 32 bit float
**shape** | str,  | str,  | An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm). Note that the polyline is always encoded with 6 digits of precision, whereas most implementations default to 5. | [optional] 
**[names](#names)** | list, tuple,  | tuple,  | A list of names that the edge goes by. | [optional] 
**bike_network** | [**BikeNetwork**](BikeNetwork.md) | [**BikeNetwork**](BikeNetwork.md) |  | [optional] 
**way_id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# names

A list of names that the edge goes by.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of names that the edge goes by. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

