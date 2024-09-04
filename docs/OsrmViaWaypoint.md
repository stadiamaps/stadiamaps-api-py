# OsrmViaWaypoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance_from_start** | **float** | The distance from the start of the leg, in meters. | 
**geometry_index** | **int** | The index of the waypoint&#39;s location in the route geometry. | 
**waypoint_index** | **int** | The index of the associated waypoint. | 

## Example

```python
from stadiamaps.models.osrm_via_waypoint import OsrmViaWaypoint

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmViaWaypoint from a JSON string
osrm_via_waypoint_instance = OsrmViaWaypoint.from_json(json)
# print the JSON string representation of the object
print(OsrmViaWaypoint.to_json())

# convert the object into a dict
osrm_via_waypoint_dict = osrm_via_waypoint_instance.to_dict()
# create an instance of OsrmViaWaypoint from a dict
osrm_via_waypoint_from_dict = OsrmViaWaypoint.from_dict(osrm_via_waypoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


