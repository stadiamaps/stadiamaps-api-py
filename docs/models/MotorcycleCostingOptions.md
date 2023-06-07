# stadiamaps.model.motorcycle_costing_options.MotorcycleCostingOptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[AutoCostingOptions](AutoCostingOptions.md) | [**AutoCostingOptions**](AutoCostingOptions.md) | [**AutoCostingOptions**](AutoCostingOptions.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**use_highways** | decimal.Decimal, int, float,  | decimal.Decimal,  | A measure of willingness to use highways. Values near 0 attempt to avoid highways and stay on roads with lower speeds, and values near 1 indicate the rider is more comfortable on these roads. | [optional] if omitted the server will use the default value of 1.0value must be a 64 bit float
**use_trails** | decimal.Decimal, int, float,  | decimal.Decimal,  | A measure of the rider&#x27;s sense of adventure. Values near 0 attempt to avoid highways and stay on roads with potentially unsuitable terrain (trails, tracks, unclassified, or bad surfaces), and values near 1 will tend to avoid major roads and route on secondary roads. | [optional] if omitted the server will use the default value of 0.0value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

