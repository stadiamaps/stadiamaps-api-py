# stadiamaps.model.map_match_trace_options.MapMatchTraceOptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**search_radius** | decimal.Decimal, int,  | decimal.Decimal,  | The search radius, in meters, when trying to match each trace point. | [optional] 
**gps_accuracy** | decimal.Decimal, int, float,  | decimal.Decimal,  | The accuracy of the GPS, in meters. | [optional] value must be a 64 bit float
**breakage_distance** | decimal.Decimal, int, float,  | decimal.Decimal,  | The breaking distance, in meters, between trace points. | [optional] value must be a 64 bit float
**interpolation_distance** | decimal.Decimal, int, float,  | decimal.Decimal,  | The interpolation distance, in meters, beyond which trace points are merged together. | [optional] value must be a 64 bit float
**turn_penalty_factor** | decimal.Decimal, int,  | decimal.Decimal,  | Penalizes turns from one road segment to next. For a pedestrian trace, you may see a back-and-forth motion along the streets of your path with the default settings. Try increasing the turn penalty factor to 500 to reduce jitter in the output. Note that if GPS accuracy is already good, increasing this above the default will usually negatively affect the quality of map matching. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

