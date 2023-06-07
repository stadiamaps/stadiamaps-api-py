# stadiamaps.model.route_response.RouteResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[trip](#trip)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**id** | str,  | str,  | An identifier to disambiguate requests (echoed by the server). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# trip

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**status_message** | str,  | str,  | The response status message | 
**summary** | [**RouteSummary**](RouteSummary.md) | [**RouteSummary**](RouteSummary.md) |  | 
**[legs](#legs)** | list, tuple,  | tuple,  |  | 
**language** | [**ValhallaLanguages**](ValhallaLanguages.md) | [**ValhallaLanguages**](ValhallaLanguages.md) |  | 
**[locations](#locations)** | list, tuple,  | tuple,  |  | 
**units** | [**ValhallaLongUnits**](ValhallaLongUnits.md) | [**ValhallaLongUnits**](ValhallaLongUnits.md) |  | 
**status** | decimal.Decimal, int,  | decimal.Decimal,  | The response status code | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# locations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RoutingResponseWaypoint**](RoutingResponseWaypoint.md) | [**RoutingResponseWaypoint**](RoutingResponseWaypoint.md) | [**RoutingResponseWaypoint**](RoutingResponseWaypoint.md) |  | 

# legs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RouteLeg**](RouteLeg.md) | [**RouteLeg**](RouteLeg.md) | [**RouteLeg**](RouteLeg.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

