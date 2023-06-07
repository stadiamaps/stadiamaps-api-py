# TruckCostingOptionsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **float** | The height of the truck (in meters). | [optional] [default to 4.11]
**width** | **float** | The width of the truck (in meters). | [optional] [default to 2.6]
**length** | **float** | The length of the truck (in meters). | [optional] [default to 21.64]
**weight** | **float** | The weight of the truck (in tonnes). | [optional] [default to 21.77]
**axle_load** | **float** | The axle load of the truck (in tonnes). | [optional] [default to 9.07]
**hazmat** | **bool** | Whether or not the truck is carrying hazardous materials. | [optional] [default to False]

## Example

```python
from stadiamaps.models.truck_costing_options_all_of import TruckCostingOptionsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of TruckCostingOptionsAllOf from a JSON string
truck_costing_options_all_of_instance = TruckCostingOptionsAllOf.from_json(json)
# print the JSON string representation of the object
print TruckCostingOptionsAllOf.to_json()

# convert the object into a dict
truck_costing_options_all_of_dict = truck_costing_options_all_of_instance.to_dict()
# create an instance of TruckCostingOptionsAllOf from a dict
truck_costing_options_all_of_form_dict = truck_costing_options_all_of.from_dict(truck_costing_options_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


