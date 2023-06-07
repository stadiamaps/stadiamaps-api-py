# CostingOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto** | [**AutoCostingOptions**](AutoCostingOptions.md) |  | [optional] 
**bus** | [**AutoCostingOptions**](AutoCostingOptions.md) |  | [optional] 
**taxi** | [**AutoCostingOptions**](AutoCostingOptions.md) |  | [optional] 
**truck** | [**TruckCostingOptions**](TruckCostingOptions.md) |  | [optional] 
**bicycle** | [**BicycleCostingOptions**](BicycleCostingOptions.md) |  | [optional] 
**motor_scooter** | [**MotorScooterCostingOptions**](MotorScooterCostingOptions.md) |  | [optional] 
**motorcycle** | [**MotorcycleCostingOptions**](MotorcycleCostingOptions.md) |  | [optional] 
**pedestrian** | [**PedestrianCostingOptions**](PedestrianCostingOptions.md) |  | [optional] 

## Example

```python
from stadiamaps.models.costing_options import CostingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CostingOptions from a JSON string
costing_options_instance = CostingOptions.from_json(json)
# print the JSON string representation of the object
print CostingOptions.to_json()

# convert the object into a dict
costing_options_dict = costing_options_instance.to_dict()
# create an instance of CostingOptions from a dict
costing_options_form_dict = costing_options.from_dict(costing_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


