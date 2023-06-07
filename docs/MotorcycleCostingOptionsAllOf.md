# MotorcycleCostingOptionsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_highways** | **float** | A measure of willingness to use highways. Values near 0 attempt to avoid highways and stay on roads with lower speeds, and values near 1 indicate the rider is more comfortable on these roads. | [optional] [default to 1.0]
**use_trails** | **float** | A measure of the rider&#39;s sense of adventure. Values near 0 attempt to avoid highways and stay on roads with potentially unsuitable terrain (trails, tracks, unclassified, or bad surfaces), and values near 1 will tend to avoid major roads and route on secondary roads. | [optional] [default to 0.0]

## Example

```python
from stadiamaps.models.motorcycle_costing_options_all_of import MotorcycleCostingOptionsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of MotorcycleCostingOptionsAllOf from a JSON string
motorcycle_costing_options_all_of_instance = MotorcycleCostingOptionsAllOf.from_json(json)
# print the JSON string representation of the object
print MotorcycleCostingOptionsAllOf.to_json()

# convert the object into a dict
motorcycle_costing_options_all_of_dict = motorcycle_costing_options_all_of_instance.to_dict()
# create an instance of MotorcycleCostingOptionsAllOf from a dict
motorcycle_costing_options_all_of_form_dict = motorcycle_costing_options_all_of.from_dict(motorcycle_costing_options_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


