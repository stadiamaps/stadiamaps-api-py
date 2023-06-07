# stadiamaps.model.truck_costing_options.TruckCostingOptions

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
**height** | decimal.Decimal, int, float,  | decimal.Decimal,  | The height of the truck (in meters). | [optional] if omitted the server will use the default value of 4.11value must be a 64 bit float
**width** | decimal.Decimal, int, float,  | decimal.Decimal,  | The width of the truck (in meters). | [optional] if omitted the server will use the default value of 2.6value must be a 64 bit float
**length** | decimal.Decimal, int, float,  | decimal.Decimal,  | The length of the truck (in meters). | [optional] if omitted the server will use the default value of 21.64value must be a 64 bit float
**weight** | decimal.Decimal, int, float,  | decimal.Decimal,  | The weight of the truck (in tonnes). | [optional] if omitted the server will use the default value of 21.77value must be a 64 bit float
**axle_load** | decimal.Decimal, int, float,  | decimal.Decimal,  | The axle load of the truck (in tonnes). | [optional] if omitted the server will use the default value of 9.07value must be a 64 bit float
**hazmat** | bool,  | BoolClass,  | Whether or not the truck is carrying hazardous materials. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

