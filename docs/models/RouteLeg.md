# stadiamaps.model.route_leg.RouteLeg

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**summary** | [**RouteSummary**](RouteSummary.md) | [**RouteSummary**](RouteSummary.md) |  | 
**shape** | str,  | str,  | An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm) with 6 digits of decimal precision. | 
**[maneuvers](#maneuvers)** | list, tuple,  | tuple,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# maneuvers

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RouteManeuver**](RouteManeuver.md) | [**RouteManeuver**](RouteManeuver.md) | [**RouteManeuver**](RouteManeuver.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

