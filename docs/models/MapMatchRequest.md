# stadiamaps.model.map_match_request.MapMatchRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[BaseTraceRequest](BaseTraceRequest.md) | [**BaseTraceRequest**](BaseTraceRequest.md) | [**BaseTraceRequest**](BaseTraceRequest.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**begin_time** | decimal.Decimal, int,  | decimal.Decimal,  | The timestamp at the start of the trace. Combined with &#x60;durations&#x60;, this provides a way to include timing information for an &#x60;encoded_polyline&#x60; trace. | [optional] 
**durations** | decimal.Decimal, int,  | decimal.Decimal,  | A list of durations (in seconds) between each successive pair of points in a polyline. | [optional] 
**use_timestamps** | bool,  | BoolClass,  | If true, the input timestamps or durations should be used when computing elapsed time for each edge along the matched path rather than the routing algorithm estimates. | [optional] if omitted the server will use the default value of False
**trace_options** | [**MapMatchTraceOptions**](MapMatchTraceOptions.md) | [**MapMatchTraceOptions**](MapMatchTraceOptions.md) |  | [optional] 
**linear_references** | bool,  | BoolClass,  | If true, the response will include a &#x60;linear_references&#x60; value that contains an array of base64-encoded [OpenLR location references](https://www.openlr-association.com/fileadmin/user_upload/openlr-whitepaper_v1.5.pdf), one for each graph edge of the road network matched by the trace. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

