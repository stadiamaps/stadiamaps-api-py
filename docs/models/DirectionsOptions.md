# stadiamaps.model.directions_options.DirectionsOptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**units** | [**DistanceUnit**](DistanceUnit.md) | [**DistanceUnit**](DistanceUnit.md) |  | [optional] 
**language** | [**ValhallaLanguages**](ValhallaLanguages.md) | [**ValhallaLanguages**](ValhallaLanguages.md) |  | [optional] 
**directions_type** | str,  | str,  | The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter. | [optional] must be one of ["none", "maneuvers", "instructions", ] if omitted the server will use the default value of "instructions"
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

