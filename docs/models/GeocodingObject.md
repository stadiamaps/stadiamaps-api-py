# stadiamaps.model.geocoding_object.GeocodingObject

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**attribution** | str,  | str,  | A URL containing attribution information. If you are not using Stadia Maps and our standard attribution already for your basemaps, you must include this attribution link somewhere in your website/app. | [optional] 
**[query](#query)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Technical details of the query. This is most useful for debugging during development. See the full example for the list of properties; these should be self-explanatory, so we don&#x27;t enumerate them in the spec. | [optional] 
**[warnings](#warnings)** | list, tuple,  | tuple,  | An array of non-critical warnings. This is normally for informational/debugging purposes and not a serious problem. | [optional] 
**[errors](#errors)** | list, tuple,  | tuple,  | An array of more serious errors (for example, omitting a required parameter). Don’t ignore these. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# query

Technical details of the query. This is most useful for debugging during development. See the full example for the list of properties; these should be self-explanatory, so we don't enumerate them in the spec.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Technical details of the query. This is most useful for debugging during development. See the full example for the list of properties; these should be self-explanatory, so we don&#x27;t enumerate them in the spec. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# warnings

An array of non-critical warnings. This is normally for informational/debugging purposes and not a serious problem.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of non-critical warnings. This is normally for informational/debugging purposes and not a serious problem. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# errors

An array of more serious errors (for example, omitting a required parameter). Don’t ignore these.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of more serious errors (for example, omitting a required parameter). Don’t ignore these. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

