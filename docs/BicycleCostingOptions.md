# BicycleCostingOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maneuver_penalty** | **int** | A penalty (in seconds) applied when transitioning between roads (determined by name). | [optional] [default to 5]
**gate_cost** | **int** | The estimated cost (in seconds) when a gate is encountered. | [optional] [default to 15]
**gate_penalty** | **int** | A penalty (in seconds) applied to the route cost when a gate is encountered. This penalty can be used to reduce the likelihood of suggesting a route with gates unless absolutely necessary. | [optional] [default to 300]
**country_crossing_cost** | **int** | The estimated cost (in seconds) when encountering an international border. | [optional] [default to 600]
**country_crossing_penalty** | **int** | A penalty applied to transitions to international border crossings. This penalty can be used to reduce the likelihood of suggesting a route with border crossings unless absolutely necessary. | [optional] [default to 0]
**service_penalty** | **int** | A penalty applied to transitions to service roads. This penalty can be used to reduce the likelihood of suggesting a route with service roads unless absolutely necessary. The default penalty is 15 for cars, busses, motor scooters, and motorcycles; and zero for others. | [optional] 
**service_factor** | **float** | A factor that multiplies the cost when service roads are encountered. The default is 1.2 for cars and busses, and 1 for trucks, motor scooters, and motorcycles. | [optional] [default to 1]
**use_living_streets** | **float** | A measure of willingness to take living streets. Values near 0 attempt to avoid them, and values near 1 will favour them. Note that as some routes may be impossible without living streets, 0 does not guarantee avoidance of them. The default value is 0 for trucks; 0.1 for other motor vehicles; 0.5 for bicycles; and 0.6 for pedestrians. | [optional] 
**use_ferry** | **float** | A measure of willingness to take ferries. Values near 0 attempt to avoid ferries, and values near 1 will favour them. Note that as some routes may be impossible without ferries, 0 does not guarantee avoidance of them. | [optional] [default to 0.5]
**ignore_restrictions** | **bool** | If set to true, ignores any restrictions (eg: turn and conditional restrictions). Useful for matching GPS traces to the road network regardless of restrictions. | [optional] 
**ignore_non_vehicular_restrictions** | **bool** | If set to true, ignores most restrictions (eg: turn and conditional restrictions), but still respects restrictions that impact vehicle safety such as weight and size. | [optional] 
**ignore_oneways** | **bool** | If set to true, ignores directional restrictions on roads. Useful for matching GPS traces to the road network regardless of restrictions. | [optional] 
**bicycle_type** | **str** | The type of bicycle: * Road: has narrow tires and is generally lightweight and designed for speed on paved surfaces * Hybrid or City: designed for city riding or casual riding on roads and paths with good surfaces * Cross: similar to a road bike, but has wider tires so it can handle rougher surfaces * Mountain: able to handle most surfaces, but generally heavier and slower on paved surfaces | [optional] [default to 'Hybrid']
**cycling_speed** | **int** | The average comfortable travel speed (in kph) along smooth, flat roads. The costing will vary the speed based on the surface, bicycle type, elevation change, etc. This value should be the average sustainable cruising speed the cyclist can maintain over the entire route. The default speeds are as follows based on bicycle type:   * Road - 25kph   * Cross - 20kph   * Hybrid - 18kph   * Mountain - 16kph | [optional] 
**use_roads** | **float** | A measure of willingness to use roads alongside other vehicles. Values near 0 attempt to avoid roads and stay on cycleways, and values near 1 indicate the cyclist is more comfortable on roads. | [optional] [default to 0.5]
**use_hills** | **float** | A measure of willingness to take tackle hills. Values near 0 attempt to avoid hills and steeper grades even if it means a longer route, and values near 1 indicates that the user does not fear them. Note that as some routes may be impossible without hills, 0 does not guarantee avoidance of them. | [optional] [default to 0.5]
**avoid_bad_surfaces** | **float** | A measure of how much the cyclist wants to avoid roads with poor surfaces relative to the type of bicycle being ridden. When 0, there is no penalization of roads with poorer surfaces, and only bicycle speed is taken into account. As the value approaches 1, roads with poor surfaces relative to the bicycle type receive a heaver penalty, so they will only be taken if they significantly reduce travel time. When the value is 1, all bad surfaces are completely avoided from the route, including the start and end points. | [optional] [default to 0.25]
**bss_return_cost** | **int** | The estimated cost (in seconds) to return a bicycle in &#x60;bikeshare&#x60; mode. | [optional] [default to 120]
**bss_return_penalty** | **int** | A penalty (in seconds) to return a bicycle in &#x60;bikeshare&#x60; mode. | [optional] [default to 0]

## Example

```python
from stadiamaps.models.bicycle_costing_options import BicycleCostingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BicycleCostingOptions from a JSON string
bicycle_costing_options_instance = BicycleCostingOptions.from_json(json)
# print the JSON string representation of the object
print(BicycleCostingOptions.to_json())

# convert the object into a dict
bicycle_costing_options_dict = bicycle_costing_options_instance.to_dict()
# create an instance of BicycleCostingOptions from a dict
bicycle_costing_options_form_dict = bicycle_costing_options.from_dict(bicycle_costing_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


