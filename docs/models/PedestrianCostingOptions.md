# stadiamaps.model.pedestrian_costing_options.PedestrianCostingOptions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**walking_speed** | decimal.Decimal, int,  | decimal.Decimal,  | Walking speed in kph. | [optional] 
**walkway_factor** | decimal.Decimal, int, float,  | decimal.Decimal,  | A factor that multiplies the cost when walkways are encountered. | [optional] if omitted the server will use the default value of 1value must be a 64 bit float
**sidewalk_factor** | decimal.Decimal, int, float,  | decimal.Decimal,  | A factor that multiplies the cost when sidewalks are encountered. | [optional] if omitted the server will use the default value of 1value must be a 64 bit float
**alley_factor** | decimal.Decimal, int, float,  | decimal.Decimal,  | A factor that multiplies the cost when alleys are encountered. | [optional] if omitted the server will use the default value of 2value must be a 64 bit float
**driveway_factor** | decimal.Decimal, int, float,  | decimal.Decimal,  | A factor that multiplies the cost when driveways are encountered. | [optional] if omitted the server will use the default value of 5value must be a 64 bit float
**step_penalty** | decimal.Decimal, int,  | decimal.Decimal,  | A penalty (in seconds) added to each transition onto a path with steps or stairs. | [optional] if omitted the server will use the default value of 30
**use_ferry** | [**UseFerryCostingOption**](UseFerryCostingOption.md) | [**UseFerryCostingOption**](UseFerryCostingOption.md) |  | [optional] 
**use_living_streets** | [**UseLivingStreetsCostingOption**](UseLivingStreetsCostingOption.md) | [**UseLivingStreetsCostingOption**](UseLivingStreetsCostingOption.md) |  | [optional] 
**use_tracks** | [**UseTracksCostingOption**](UseTracksCostingOption.md) | [**UseTracksCostingOption**](UseTracksCostingOption.md) |  | [optional] 
**use_hills** | [**UseHillsCostingOption**](UseHillsCostingOption.md) | [**UseHillsCostingOption**](UseHillsCostingOption.md) |  | [optional] 
**use_lit** | decimal.Decimal, int, float,  | decimal.Decimal,  | A measure of preference for streets that are lit. 0 indicates indifference toward lit streets, and 1 indicates that unlit streets should be avoided. Note that even with values near 1, there is no guarantee that the returned route will include lit segments. | [optional] if omitted the server will use the default value of 0value must be a 64 bit float
**service_penalty** | decimal.Decimal, int,  | decimal.Decimal,  | A penalty applied to transitions to service roads. This penalty can be used to reduce the likelihood of suggesting a route with service roads unless absolutely necessary. The default penalty is 15 for cars, busses, motor scooters, and motorcycles; and zero for others. | [optional] 
**service_factor** | decimal.Decimal, int, float,  | decimal.Decimal,  | A factor that multiplies the cost when service roads are encountered. The default is 1.2 for cars and busses, and 1 for trucks, motor scooters, and motorcycles. | [optional] if omitted the server will use the default value of 1value must be a 64 bit float
**max_hiking_difficulty** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum difficulty of hiking trails allowed. This corresponds to the OSM &#x60;sac_scale&#x60;. | [optional] if omitted the server will use the default value of 1
**bss_rent_cost** | decimal.Decimal, int,  | decimal.Decimal,  | The estimated cost (in seconds) to rent a bicycle from a sharing station in &#x60;bikeshare&#x60; mode. | [optional] if omitted the server will use the default value of 120
**bss_rent_penalty** | decimal.Decimal, int,  | decimal.Decimal,  | A penalty (in seconds) to rent a bicycle in &#x60;bikeshare&#x60; mode. | [optional] if omitted the server will use the default value of 0
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

