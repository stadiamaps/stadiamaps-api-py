# BicycleCostingOptionsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bicycle_type** | **str** |  | [optional] [default to 'Hybrid']
**cycling_speed** | **int** | The average comfortable travel speed (in kph) along smooth, flat roads. The costing will vary the speed based on the surface, bicycle type, elevation change, etc. This value should be the average sustainable cruising speed the cyclist can maintain over the entire route. The default speeds are as follows based on bicycle type:   * Road - 25kph   * Cross - 20kph   * Hybrid - 18kph   * Mountain - 16kph | [optional] 
**use_roads** | **float** | A measure of willingness to use roads alongside other vehicles. Values near 0 attempt to avoid roads and stay on cycleways, and values near 1 indicate the cyclist is more comfortable on roads. | [optional] [default to 0.5]
**use_hills** | **float** | A measure of willingness to take tackle hills. Values near 0 attempt to avoid hills and steeper grades even if it means a longer route, and values near 1 indicates that the user does not fear them. Note that as some routes may be impossible without hills, 0 does not guarantee avoidance of them. | [optional] [default to 0.5]
**avoid_bad_surfaces** | **float** | A measure of how much the cyclist wants to avoid roads with poor surfaces relative to the type of bicycle being ridden. When 0, there is no penalization of roads with poorer surfaces, and only bicycle speed is taken into account. As the value approaches 1, roads with poor surfaces relative to the bicycle type receive a heaver penalty, so they will only be taken if they significantly reduce travel time. When the value is 1, all bad surfaces are completely avoided from the route, including the start and end points. | [optional] [default to 0.25]
**bss_return_cost** | **int** | The estimated cost (in seconds) to return a bicycle in &#x60;bikeshare&#x60; mode. | [optional] [default to 120]
**bss_return_penalty** | **int** | A penalty (in seconds) to return a bicycle in &#x60;bikeshare&#x60; mode. | [optional] [default to 0]

## Example

```python
from stadiamaps.models.bicycle_costing_options_all_of import BicycleCostingOptionsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of BicycleCostingOptionsAllOf from a JSON string
bicycle_costing_options_all_of_instance = BicycleCostingOptionsAllOf.from_json(json)
# print the JSON string representation of the object
print BicycleCostingOptionsAllOf.to_json()

# convert the object into a dict
bicycle_costing_options_all_of_dict = bicycle_costing_options_all_of_instance.to_dict()
# create an instance of BicycleCostingOptionsAllOf from a dict
bicycle_costing_options_all_of_form_dict = bicycle_costing_options_all_of.from_dict(bicycle_costing_options_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


