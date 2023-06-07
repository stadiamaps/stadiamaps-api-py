# stadiamaps.model.speeds.Speeds

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**predicted** | bool,  | BoolClass,  | Does this edge have predicted (historical) speed records? | [optional] 
**constrained_flow** | decimal.Decimal, int,  | decimal.Decimal,  | Speed when there is no traffic, in kph. | [optional] 
**free_flow** | decimal.Decimal, int,  | decimal.Decimal,  | Speed when there is heavy traffic, in kph. | [optional] 
**type** | str,  | str,  | The type of speed which is used when setting default speeds. When &#x60;tagged&#x60;, the explicit &#x60;max_speed&#x60; tags from OpenStreetMap are being used. When &#x60;classified&#x60;, the values are being inferred from the highway classification. | [optional] must be one of ["classified", "tagged", ] 
**default** | decimal.Decimal, int,  | decimal.Decimal,  | The default speed used for calculations. NOTE: Values greater than 250 are used for special cases and should not be treated as literal. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

