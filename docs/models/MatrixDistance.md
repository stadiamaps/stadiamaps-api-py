# stadiamaps.model.matrix_distance.MatrixDistance

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**from_index** | decimal.Decimal, int,  | decimal.Decimal,  | The index of the start location in the &#x60;sources&#x60; array. | 
**distance** | decimal.Decimal, int, float,  | decimal.Decimal,  | The distance (in &#x60;units&#x60;) between the location in &#x60;sources&#x60; at &#x60;from_index&#x60; and the location in &#x60;targets&#x60; at &#x60;to_index&#x60;. | value must be a 64 bit float
**time** | decimal.Decimal, int,  | decimal.Decimal,  | The travel time (in seconds) between the location in &#x60;sources&#x60; at &#x60;from_index&#x60; and the location in &#x60;targets&#x60; at &#x60;to_index&#x60;. | 
**to_index** | decimal.Decimal, int,  | decimal.Decimal,  | The index of the end location in the &#x60;targets&#x60; array. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

