# stadiamaps.model.contour.Contour

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**time** | decimal.Decimal, int, float,  | decimal.Decimal,  | The time in minutes for the contour. Mutually exclusive of distance. | [optional] value must be a 64 bit float
**distance** | decimal.Decimal, int, float,  | decimal.Decimal,  | The distance in km for the contour. Mutually exclusive of time. | [optional] value must be a 64 bit float
**color** | str,  | str,  | The color for the output contour, specified as a hex value (without a leading &#x60;#&#x60;). If no color is specified, one will be assigned automatically. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

