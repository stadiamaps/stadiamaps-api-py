# MapMatchWaypointAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **int** | The timestamp of the waypoint, in seconds. This can inform the map matching algorithm about when the point was measured. A UNIX timestamp, or any increasing integer sequence measuring seconds from some reference point can be used. | [optional] 

## Example

```python
from stadiamaps.models.map_match_waypoint_all_of import MapMatchWaypointAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of MapMatchWaypointAllOf from a JSON string
map_match_waypoint_all_of_instance = MapMatchWaypointAllOf.from_json(json)
# print the JSON string representation of the object
print MapMatchWaypointAllOf.to_json()

# convert the object into a dict
map_match_waypoint_all_of_dict = map_match_waypoint_all_of_instance.to_dict()
# create an instance of MapMatchWaypointAllOf from a dict
map_match_waypoint_all_of_form_dict = map_match_waypoint_all_of.from_dict(map_match_waypoint_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


