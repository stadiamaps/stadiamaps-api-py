# stadiamaps.model.route_request.RouteRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**costing** | [**CostingModel**](CostingModel.md) | [**CostingModel**](CostingModel.md) |  | 
**[locations](#locations)** | list, tuple,  | tuple,  |  | 
**id** | str,  | str,  | An identifier to disambiguate requests (echoed by the server). | [optional] 
**costing_options** | [**CostingOptions**](CostingOptions.md) | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**[avoid_locations](#avoid_locations)** | list, tuple,  | tuple,  |  | [optional] 
**[avoid_polygons](#avoid_polygons)** | list, tuple,  | tuple,  | One or multiple exterior rings of polygons in the form of nested JSON arrays. Roads intersecting these rings will be avoided during path finding. Open rings will be closed automatically. | [optional] 
**directions_options** | [**DirectionsOptions**](DirectionsOptions.md) | [**DirectionsOptions**](DirectionsOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# locations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RoutingWaypoint**](RoutingWaypoint.md) | [**RoutingWaypoint**](RoutingWaypoint.md) | [**RoutingWaypoint**](RoutingWaypoint.md) |  | 

# avoid_locations

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RoutingWaypoint**](RoutingWaypoint.md) | [**RoutingWaypoint**](RoutingWaypoint.md) | [**RoutingWaypoint**](RoutingWaypoint.md) |  | 

# avoid_polygons

One or multiple exterior rings of polygons in the form of nested JSON arrays. Roads intersecting these rings will be avoided during path finding. Open rings will be closed automatically.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | One or multiple exterior rings of polygons in the form of nested JSON arrays. Roads intersecting these rings will be avoided during path finding. Open rings will be closed automatically. | 

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
[items](#items) | list, tuple,  | tuple,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

