# MotorScooterCostingOptionsAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_primary** | **float** | A measure of willingness to use primary roads. Values near 0 attempt to avoid primary roads and stay on roads with lower speeds, and values near 1 indicate the rider is more comfortable on these roads. | [optional] [default to 0.5]
**use_hills** | **float** | A measure of willingness to take tackle hills. Values near 0 attempt to avoid hills and steeper grades even if it means a longer route, and values near 1 indicates that the rider does not fear them. Note that as some routes may be impossible without hills, 0 does not guarantee avoidance of them. | [optional] [default to 0.5]

## Example

```python
from stadiamaps.models.motor_scooter_costing_options_all_of import MotorScooterCostingOptionsAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of MotorScooterCostingOptionsAllOf from a JSON string
motor_scooter_costing_options_all_of_instance = MotorScooterCostingOptionsAllOf.from_json(json)
# print the JSON string representation of the object
print MotorScooterCostingOptionsAllOf.to_json()

# convert the object into a dict
motor_scooter_costing_options_all_of_dict = motor_scooter_costing_options_all_of_instance.to_dict()
# create an instance of MotorScooterCostingOptionsAllOf from a dict
motor_scooter_costing_options_all_of_form_dict = motor_scooter_costing_options_all_of.from_dict(motor_scooter_costing_options_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


