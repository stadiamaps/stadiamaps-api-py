# stadiamaps.model.base_costing_options.BaseCostingOptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**maneuver_penalty** | decimal.Decimal, int,  | decimal.Decimal,  | A penalty (in seconds) applied when transitioning between roads (determined by name). | [optional] if omitted the server will use the default value of 5
**gate_cost** | decimal.Decimal, int,  | decimal.Decimal,  | The estimated cost (in seconds) when a gate is encountered. | [optional] if omitted the server will use the default value of 15
**gate_penalty** | decimal.Decimal, int,  | decimal.Decimal,  | A penalty (in seconds) applied to the route cost when a gate is encountered. This penalty can be used to reduce the likelihood of suggesting a route with gates unless absolutely necessary. | [optional] if omitted the server will use the default value of 300
**country_crossing_cost** | decimal.Decimal, int,  | decimal.Decimal,  | The estimated cost (in seconds) when encountering an international border. | [optional] if omitted the server will use the default value of 600
**country_crossing_penalty** | decimal.Decimal, int,  | decimal.Decimal,  | A penalty applied to transitions to international border crossings. This penalty can be used to reduce the likelihood of suggesting a route with border crossings unless absolutely necessary. | [optional] if omitted the server will use the default value of 0
**service_penalty** | decimal.Decimal, int,  | decimal.Decimal,  | A penalty applied to transitions to service roads. This penalty can be used to reduce the likelihood of suggesting a route with service roads unless absolutely necessary. The default penalty is 15 for cars, busses, motor scooters, and motorcycles; and zero for others. | [optional] 
**service_factor** | decimal.Decimal, int, float,  | decimal.Decimal,  | A factor that multiplies the cost when service roads are encountered. The default is 1.2 for cars and busses, and 1 for trucks, motor scooters, and motorcycles. | [optional] if omitted the server will use the default value of 1value must be a 64 bit float
**use_living_streets** | [**UseLivingStreetsCostingOption**](UseLivingStreetsCostingOption.md) | [**UseLivingStreetsCostingOption**](UseLivingStreetsCostingOption.md) |  | [optional] 
**use_ferry** | [**UseFerryCostingOption**](UseFerryCostingOption.md) | [**UseFerryCostingOption**](UseFerryCostingOption.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

