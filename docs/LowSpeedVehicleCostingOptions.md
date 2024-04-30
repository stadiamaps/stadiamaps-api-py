# LowSpeedVehicleCostingOptions


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
**vehicle_type** | **str** | The type of vehicle: * low_speed_vehicle (BETA): a low-speed vehicle which falls under a different regulatory and licensing regime than automobiles (ex: LSV in the US and Canada, Quadricycles in the EU, etc.) * golf_cart: a street legal golf cart that is under a similar regulator regime as the generic LSV laws, but may need to follow special paths when available or abide by restrictions specific to golf carts. | [optional] [default to 'low_speed_vehicle']
**top_speed** | **int** | The top speed (in kph) that the vehicle is capable of travelling. This impacts travel time calculations as well as which roads are preferred. A very low speed vehicle will tend to prefer lower speed roads even in the presence of other legal routes. | [optional] [default to 35]
**max_allowed_speed_limit** | **int** | The maximum speed limit for highways on which it is legal for the vehicle to travel. Defaults to 57 (kph; around 35 mph). Acceptable values range from 20 to 80. Highways with *tagged* speed limits higher than this value will not be routed over (some caveats apply; this feature is still BETA). | [optional] [default to 57]

## Example

```python
from stadiamaps.models.low_speed_vehicle_costing_options import LowSpeedVehicleCostingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LowSpeedVehicleCostingOptions from a JSON string
low_speed_vehicle_costing_options_instance = LowSpeedVehicleCostingOptions.from_json(json)
# print the JSON string representation of the object
print(LowSpeedVehicleCostingOptions.to_json())

# convert the object into a dict
low_speed_vehicle_costing_options_dict = low_speed_vehicle_costing_options_instance.to_dict()
# create an instance of LowSpeedVehicleCostingOptions from a dict
low_speed_vehicle_costing_options_form_dict = low_speed_vehicle_costing_options.from_dict(low_speed_vehicle_costing_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


