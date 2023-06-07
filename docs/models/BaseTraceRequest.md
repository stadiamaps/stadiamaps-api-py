# stadiamaps.model.base_trace_request.BaseTraceRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**costing** | [**MapMatchCostingModel**](MapMatchCostingModel.md) | [**MapMatchCostingModel**](MapMatchCostingModel.md) |  | 
**id** | str,  | str,  | An identifier to disambiguate requests (echoed by the server). | [optional] 
**[shape](#shape)** | list, tuple,  | tuple,  | REQUIRED if &#x60;encoded_polyline&#x60; is not present. Note that &#x60;break&#x60; type locations are only supported when &#x60;shape_match&#x60; is set to &#x60;map_match&#x60;. | [optional] 
**encoded_polyline** | str,  | str,  | REQUIRED if &#x60;shape&#x60; is not present. An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm). Note that the polyline must be encoded with 6 digits of precision rather than the usual 5. | [optional] 
**costing_options** | [**CostingOptions**](CostingOptions.md) | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**shape_match** | str,  | str,  | Three snapping modes provide some control over how the map matching occurs. &#x60;edge_walk&#x60; is fast, but requires extremely precise data that matches the route graph almost perfectly. &#x60;map_snap&#x60; can handle significantly noisier data, but is very expensive. &#x60;walk_or_snap&#x60;, the default, tries to use edge walking first and falls back to map matching if edge walking fails. In general, you should not need to change this parameter unless you want to trace a multi-leg route with multiple &#x60;break&#x60; locations in the &#x60;shape&#x60;. | [optional] must be one of ["edge_walk", "map_snap", "walk_or_snap", ] 
**directions_options** | [**DirectionsOptions**](DirectionsOptions.md) | [**DirectionsOptions**](DirectionsOptions.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# shape

REQUIRED if `encoded_polyline` is not present. Note that `break` type locations are only supported when `shape_match` is set to `map_match`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | REQUIRED if &#x60;encoded_polyline&#x60; is not present. Note that &#x60;break&#x60; type locations are only supported when &#x60;shape_match&#x60; is set to &#x60;map_match&#x60;. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MapMatchWaypoint**](MapMatchWaypoint.md) | [**MapMatchWaypoint**](MapMatchWaypoint.md) | [**MapMatchWaypoint**](MapMatchWaypoint.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

