# BaseCostingOptions


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

## Example

```python
from stadiamaps.models.base_costing_options import BaseCostingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of BaseCostingOptions from a JSON string
base_costing_options_instance = BaseCostingOptions.from_json(json)
# print the JSON string representation of the object
print(BaseCostingOptions.to_json())

# convert the object into a dict
base_costing_options_dict = base_costing_options_instance.to_dict()
# create an instance of BaseCostingOptions from a dict
base_costing_options_form_dict = base_costing_options.from_dict(base_costing_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


