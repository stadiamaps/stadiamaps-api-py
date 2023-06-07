# RoutingWaypoint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | The latitude of a point in the shape. | 
**lon** | **float** | The longitude of a point in the shape. | 
**type** | **str** | A &#x60;break&#x60; represents the start or end of a leg, and allows reversals. A &#x60;through&#x60; location is an intermediate waypoint that must be visited between &#x60;break&#x60;s, but at which reversals are not allowed. A &#x60;via&#x60; is similar to a &#x60;through&#x60; except that reversals are allowed. A &#x60;break_through&#x60; is similar to a &#x60;break&#x60; in that it can be the start/end of a leg, but does not allow reversals. | [optional] [default to 'break']
**heading** | **int** | The preferred direction of travel when starting the route, in integer clockwise degrees from north. North is 0, south is 180, east is 90, and west is 270. | [optional] 
**heading_tolerance** | **int** | The tolerance (in degrees) determining whether a street is considered the same direction. | [optional] [default to 60]
**minimum_reachability** | **int** | The minimum number of nodes that must be reachable for a given edge to consider that edge as belonging to a connected region. If a candidate edge has fewer connections, it will be considered a disconnected island. | [optional] [default to 50]
**radius** | **int** | The distance (in meters) to look for candidate edges around the location for purposes of snapping locations to the route graph. If there are no candidates within this distance, the closest candidate within a reasonable search distance will be used. This is subject to clamping by internal limits. | [optional] [default to 0]
**rank_candidates** | **bool** | If true, candidates will be ranked according to their distance from the target location as well as other factors. If false, candidates will only be ranked using their distance from the target. | [optional] [default to True]
**preferred_side** | **str** | If the location is not offset from the road centerline or is closest to an intersection, this option has no effect. Otherwise, the preferred side of street is used to determine whether or not the location should be visited from the same, opposite or either side of the road with respect to the side of the road the given locale drives on. | [optional] 
**node_snap_tolerance** | **int** | During edge correlation this is the tolerance (in meters) used to determine whether or not to snap to the intersection rather than along the street, if the snap location is within this distance from the intersection, the intersection is used instead. | [optional] [default to 5]
**street_side_tolerance** | **int** | A tolerance in meters from the edge centerline used for determining the side of the street that the location is on. If the distance to the centerline is less than this tolerance, no side will be inferred. Otherwise, the left or right side will be selected depending on the direction of travel. | [optional] [default to 5]
**street_side_max_distance** | **int** | A tolerance in meters from the edge centerline used for determining the side of the street that the location is on. If the distance to the centerline is greater than this tolerance, no side will be inferred. Otherwise, the left or right side will be selected depending on the direction of travel. | [optional] [default to 1000]
**search_filter** | [**RoutingWaypointAllOfSearchFilter**](RoutingWaypointAllOfSearchFilter.md) |  | [optional] 

## Example

```python
from stadiamaps.models.routing_waypoint import RoutingWaypoint

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingWaypoint from a JSON string
routing_waypoint_instance = RoutingWaypoint.from_json(json)
# print the JSON string representation of the object
print RoutingWaypoint.to_json()

# convert the object into a dict
routing_waypoint_dict = routing_waypoint_instance.to_dict()
# create an instance of RoutingWaypoint from a dict
routing_waypoint_form_dict = routing_waypoint.from_dict(routing_waypoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


