# stadiamaps.model.trace_attributes_response.TraceAttributesResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TraceAttributesBaseResponse](TraceAttributesBaseResponse.md) | [**TraceAttributesBaseResponse**](TraceAttributesBaseResponse.md) | [**TraceAttributesBaseResponse**](TraceAttributesBaseResponse.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | An identifier to disambiguate requests (echoed by the server). | [optional] 
**units** | [**ValhallaLongUnits**](ValhallaLongUnits.md) | [**ValhallaLongUnits**](ValhallaLongUnits.md) |  | [optional] 
**[alternate_paths](#alternate_paths)** | list, tuple,  | tuple,  | Alternate paths, if any, that were not classified as the best match. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# alternate_paths

Alternate paths, if any, that were not classified as the best match.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Alternate paths, if any, that were not classified as the best match. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TraceAttributesBaseResponse**](TraceAttributesBaseResponse.md) | [**TraceAttributesBaseResponse**](TraceAttributesBaseResponse.md) | [**TraceAttributesBaseResponse**](TraceAttributesBaseResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

