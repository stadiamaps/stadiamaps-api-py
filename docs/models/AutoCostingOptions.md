# stadiamaps.model.auto_costing_options.AutoCostingOptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[BaseCostingOptions](BaseCostingOptions.md) | [**BaseCostingOptions**](BaseCostingOptions.md) | [**BaseCostingOptions**](BaseCostingOptions.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**height** | decimal.Decimal, int, float,  | decimal.Decimal,  | The height of the automobile (in meters). | [optional] if omitted the server will use the default value of 1.9value must be a 64 bit float
**width** | decimal.Decimal, int, float,  | decimal.Decimal,  | The width of the automobile (in meters). | [optional] if omitted the server will use the default value of 1.6value must be a 64 bit float
**toll_booth_cost** | decimal.Decimal, int,  | decimal.Decimal,  | The estimated cost (in seconds) when a toll booth is encountered. | [optional] if omitted the server will use the default value of 15
**toll_booth_penalty** | decimal.Decimal, int,  | decimal.Decimal,  | A penalty (in seconds) applied to the route cost when a toll booth is encountered. This penalty can be used to reduce the likelihood of suggesting a route with toll booths unless absolutely necessary. | [optional] if omitted the server will use the default value of 0
**ferry_cost** | decimal.Decimal, int,  | decimal.Decimal,  | The estimated cost (in seconds) when a ferry is encountered. | [optional] if omitted the server will use the default value of 300
**use_highways** | decimal.Decimal, int, float,  | decimal.Decimal,  | A measure of willingness to take highways. Values near 0 attempt to avoid highways, and values near 1 will favour them. Note that as some routes may be impossible without highways, 0 does not guarantee avoidance of them. | [optional] if omitted the server will use the default value of 0.5value must be a 64 bit float
**use_tolls** | decimal.Decimal, int, float,  | decimal.Decimal,  | A measure of willingness to take toll roads. Values near 0 attempt to avoid tolls, and values near 1 will favour them. Note that as some routes may be impossible without tolls, 0 does not guarantee avoidance of them. | [optional] if omitted the server will use the default value of 0.5value must be a 64 bit float
**use_tracks** | [**UseTracksCostingOption**](UseTracksCostingOption.md) | [**UseTracksCostingOption**](UseTracksCostingOption.md) |  | [optional] 
**top_speed** | decimal.Decimal, int,  | decimal.Decimal,  | The top speed (in kph) that the vehicle is capable of travelling. | [optional] if omitted the server will use the default value of 140
**shortest** | bool,  | BoolClass,  | If true changes the cost metric to be quasi-shortest (pure distance-based) costing. This will disable ALL other costing factors. | [optional] if omitted the server will use the default value of False
**ignore_closures** | bool,  | BoolClass,  | If true, ignores all known closures. This option cannot be set if &#x60;location.search_filter.exclude_closures&#x60; is also specified. | [optional] if omitted the server will use the default value of False
**include_hov2** | bool,  | BoolClass,  | If true, indicates the desire to include HOV roads with a 2-occupant requirement in the route when advantageous. | [optional] if omitted the server will use the default value of False
**include_hov3** | bool,  | BoolClass,  | If true, indicates the desire to include HOV roads with a 3-occupant requirement in the route when advantageous. | [optional] if omitted the server will use the default value of False
**include_hot** | bool,  | BoolClass,  | If true, indicates the desire to include toll roads which require the driver to pay a toll if the occupant requirement isn&#x27;t met | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

