# stadiamaps.model.matched_point.MatchedPoint

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**lon** | decimal.Decimal, int, float,  | decimal.Decimal,  | The longitude of the matched point. | value must be a 64 bit float
**type** | str,  | str,  |  | must be one of ["unmatched", "interpolated", "matched", ] 
**lat** | decimal.Decimal, int, float,  | decimal.Decimal,  | The latitude of the matched point. | value must be a 64 bit float
**edge_index** | decimal.Decimal, int,  | decimal.Decimal,  | The index of the edge in the list of &#x60;edges&#x60;. This key will be missing if the point is unmatched. | [optional] 
**begin_route_discontinuity** | bool,  | BoolClass,  | If true, this match result is the begin location of a route discontinuity. | [optional] if omitted the server will use the default value of False
**end_route_discontinuity** | bool,  | BoolClass,  | If true, this match result is the end location of a route discontinuity. | [optional] if omitted the server will use the default value of False
**distance_along_edge** | decimal.Decimal, int, float,  | decimal.Decimal,  | The distance along the associated edge for this matched point, expressed as a value between 0 and 1. For example, if the matched point is halfway along the edge, then the value will be 0.5. This key will be absent if the point is unmatched. | [optional] value must be a 64 bit float
**distance_from_trace_point** | decimal.Decimal, int, float,  | decimal.Decimal,  | The distance in meters from the trace point to the matched point. This key will be absent if the point is unmatched. | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

