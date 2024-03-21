# AutoCostingOptions


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
**height** | **float** | The height of the automobile (in meters). | [optional] [default to 1.9]
**width** | **float** | The width of the automobile (in meters). | [optional] [default to 1.6]
**toll_booth_cost** | **int** | The estimated cost (in seconds) when a toll booth is encountered. | [optional] [default to 15]
**toll_booth_penalty** | **int** | A penalty (in seconds) applied to the route cost when a toll booth is encountered. This penalty can be used to reduce the likelihood of suggesting a route with toll booths unless absolutely necessary. | [optional] [default to 0]
**ferry_cost** | **int** | The estimated cost (in seconds) when a ferry is encountered. | [optional] [default to 300]
**use_highways** | **float** | A measure of willingness to take highways. Values near 0 attempt to avoid highways, and values near 1 will favour them. Note that as some routes may be impossible without highways, 0 does not guarantee avoidance of them. | [optional] [default to 0.5]
**use_tolls** | **float** | A measure of willingness to take toll roads. Values near 0 attempt to avoid tolls, and values near 1 will favour them. Note that as some routes may be impossible without tolls, 0 does not guarantee avoidance of them. | [optional] [default to 0.5]
**use_tracks** | **float** | A measure of willingness to take track roads. Values near 0 attempt to avoid them, and values near 1 will favour them. Note that as some routes may be impossible without track roads, 0 does not guarantee avoidance of them. The default value is 0 for automobiles, busses, and trucks; and 0.5 for all other costing modes. | [optional] 
**top_speed** | **int** | The top speed (in kph) that the vehicle is capable of travelling. | [optional] [default to 140]
**shortest** | **bool** | If true changes the cost metric to be quasi-shortest (pure distance-based) costing. This will disable ALL other costing factors. | [optional] [default to False]
**ignore_closures** | **bool** | If true, ignores all known closures. This option cannot be set if &#x60;location.search_filter.exclude_closures&#x60; is also specified. | [optional] [default to False]
**include_hov2** | **bool** | If true, indicates the desire to include HOV roads with a 2-occupant requirement in the route when advantageous. | [optional] [default to False]
**include_hov3** | **bool** | If true, indicates the desire to include HOV roads with a 3-occupant requirement in the route when advantageous. | [optional] [default to False]
**include_hot** | **bool** | If true, indicates the desire to include toll roads which require the driver to pay a toll if the occupant requirement isn&#39;t met | [optional] [default to False]
**alley_factor** | **float** | A factor that multiplies the cost when alleys are encountered. | [optional] [default to 1]

## Example

```python
from stadiamaps.models.auto_costing_options import AutoCostingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of AutoCostingOptions from a JSON string
auto_costing_options_instance = AutoCostingOptions.from_json(json)
# print the JSON string representation of the object
print(AutoCostingOptions.to_json())

# convert the object into a dict
auto_costing_options_dict = auto_costing_options_instance.to_dict()
# create an instance of AutoCostingOptions from a dict
auto_costing_options_form_dict = auto_costing_options.from_dict(auto_costing_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


