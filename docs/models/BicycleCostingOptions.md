# stadiamaps.model.bicycle_costing_options.BicycleCostingOptions

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
**bicycle_type** | str,  | str,  |  | [optional] must be one of ["Road", "Hybrid", "Cross", "Mountain", ] if omitted the server will use the default value of "Hybrid"
**cycling_speed** | decimal.Decimal, int,  | decimal.Decimal,  | The average comfortable travel speed (in kph) along smooth, flat roads. The costing will vary the speed based on the surface, bicycle type, elevation change, etc. This value should be the average sustainable cruising speed the cyclist can maintain over the entire route. The default speeds are as follows based on bicycle type:   * Road - 25kph   * Cross - 20kph   * Hybrid - 18kph   * Mountain - 16kph | [optional] 
**use_roads** | decimal.Decimal, int, float,  | decimal.Decimal,  | A measure of willingness to use roads alongside other vehicles. Values near 0 attempt to avoid roads and stay on cycleways, and values near 1 indicate the cyclist is more comfortable on roads. | [optional] if omitted the server will use the default value of 0.5value must be a 64 bit float
**use_hills** | [**UseHillsCostingOption**](UseHillsCostingOption.md) | [**UseHillsCostingOption**](UseHillsCostingOption.md) |  | [optional] 
**avoid_bad_surfaces** | decimal.Decimal, int, float,  | decimal.Decimal,  | A measure of how much the cyclist wants to avoid roads with poor surfaces relative to the type of bicycle being ridden. When 0, there is no penalization of roads with poorer surfaces, and only bicycle speed is taken into account. As the value approaches 1, roads with poor surfaces relative to the bicycle type receive a heaver penalty, so they will only be taken if they significantly reduce travel time. When the value is 1, all bad surfaces are completely avoided from the route, including the start and end points. | [optional] if omitted the server will use the default value of 0.25value must be a 64 bit float
**bss_return_cost** | decimal.Decimal, int,  | decimal.Decimal,  | The estimated cost (in seconds) to return a bicycle in &#x60;bikeshare&#x60; mode. | [optional] if omitted the server will use the default value of 120
**bss_return_penalty** | decimal.Decimal, int,  | decimal.Decimal,  | A penalty (in seconds) to return a bicycle in &#x60;bikeshare&#x60; mode. | [optional] if omitted the server will use the default value of 0
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

