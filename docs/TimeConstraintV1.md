# TimeConstraintV1

Specifies the time context for time-dependent routing (e.g., to account for traffic patterns or time-based access restrictions). Defaults \"now\" for traffic-influenced routing profiles like `auto_traffic`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | The type of time constraint: 0 &#x3D; current time (depart now), 1 &#x3D; depart at the specified time, 2 &#x3D; arrive by the specified time. | 
**value** | **str** | The date and time in &#x60;YYYY-MM-DDTHH:MM&#x60; format (seconds are accepted, but will be ignored). The date and time are local (civil) time as observed at the location. Required for types 1 and 2. Must not be provided for type 0. | [optional] 

## Example

```python
from stadiamaps.models.time_constraint_v1 import TimeConstraintV1

# TODO update the JSON string below
json = "{}"
# create an instance of TimeConstraintV1 from a JSON string
time_constraint_v1_instance = TimeConstraintV1.from_json(json)
# print the JSON string representation of the object
print(TimeConstraintV1.to_json())

# convert the object into a dict
time_constraint_v1_dict = time_constraint_v1_instance.to_dict()
# create an instance of TimeConstraintV1 from a dict
time_constraint_v1_from_dict = TimeConstraintV1.from_dict(time_constraint_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


