# OsrmWaypoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**location** | **List[float]** | A (longitude, latitude) coordinate pair. | 
**distance** | **float** | The distance of the snapped point from the original location. | 
**hint** | **str** |  | [optional] 

## Example

```python
from stadiamaps.models.osrm_waypoint import OsrmWaypoint

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmWaypoint from a JSON string
osrm_waypoint_instance = OsrmWaypoint.from_json(json)
# print the JSON string representation of the object
print(OsrmWaypoint.to_json())

# convert the object into a dict
osrm_waypoint_dict = osrm_waypoint_instance.to_dict()
# create an instance of OsrmWaypoint from a dict
osrm_waypoint_from_dict = OsrmWaypoint.from_dict(osrm_waypoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


