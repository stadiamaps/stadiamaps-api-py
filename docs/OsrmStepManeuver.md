# OsrmStepManeuver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **List[float]** | A (longitude, latitude) coordinate pair. | 
**instruction** | **str** | A human-readable instruction for the maneuver. | [optional] 
**bearing_before** | **int** | The clockwise angle from true north to the direction of travel immediately before the maneuver. | 
**bearing_after** | **int** | The clockwise angle from true north to the direction of travel immediately after the maneuver. | 
**type** | **str** |  | 
**modifier** | [**OsrmGuidanceModifier**](OsrmGuidanceModifier.md) |  | [optional] 
**exit** | **int** | The exit number to take (for roundabouts, rotaries, and number of intersections). | [optional] 

## Example

```python
from stadiamaps.models.osrm_step_maneuver import OsrmStepManeuver

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmStepManeuver from a JSON string
osrm_step_maneuver_instance = OsrmStepManeuver.from_json(json)
# print the JSON string representation of the object
print(OsrmStepManeuver.to_json())

# convert the object into a dict
osrm_step_maneuver_dict = osrm_step_maneuver_instance.to_dict()
# create an instance of OsrmStepManeuver from a dict
osrm_step_maneuver_from_dict = OsrmStepManeuver.from_dict(osrm_step_maneuver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


