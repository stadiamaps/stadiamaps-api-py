# MapMatchWaypoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | The latitude of a point in the shape. | 
**lon** | **float** | The longitude of a point in the shape. | 
**type** | **str** | A &#x60;break&#x60; represents the start or end of a leg, and allows reversals. A &#x60;through&#x60; location is an intermediate waypoint that must be visited between &#x60;break&#x60;s, but at which reversals are not allowed. A &#x60;via&#x60; is similar to a &#x60;through&#x60; except that reversals are allowed. A &#x60;break_through&#x60; is similar to a &#x60;break&#x60; in that it can be the start/end of a leg, but does not allow reversals. Defaults to &#x60;break&#x60;. | [optional] 
**time** | **int** | The timestamp of the waypoint, in seconds. This can inform the map matching algorithm about when the point was measured. A UNIX timestamp, or any increasing integer sequence measuring seconds from some reference point can be used. | [optional] 

## Example

```python
from stadiamaps.models.map_match_waypoint import MapMatchWaypoint

# TODO update the JSON string below
json = "{}"
# create an instance of MapMatchWaypoint from a JSON string
map_match_waypoint_instance = MapMatchWaypoint.from_json(json)
# print the JSON string representation of the object
print(MapMatchWaypoint.to_json())

# convert the object into a dict
map_match_waypoint_dict = map_match_waypoint_instance.to_dict()
# create an instance of MapMatchWaypoint from a dict
map_match_waypoint_from_dict = MapMatchWaypoint.from_dict(map_match_waypoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


