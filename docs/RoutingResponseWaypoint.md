# RoutingResponseWaypoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | The latitude of a point in the shape. | 
**lon** | **float** | The longitude of a point in the shape. | 
**type** | **str** | A &#x60;break&#x60; represents the start or end of a leg, and allows reversals. A &#x60;through&#x60; location is an intermediate waypoint that must be visited between &#x60;break&#x60;s, but at which reversals are not allowed. A &#x60;via&#x60; is similar to a &#x60;through&#x60; except that reversals are allowed. A &#x60;break_through&#x60; is similar to a &#x60;break&#x60; in that it can be the start/end of a leg, but does not allow reversals. Defaults to &#x60;break&#x60;. | [optional] 
**original_index** | **int** | The original index of the location (locations may be reordered for optimized routes) | [optional] 

## Example

```python
from stadiamaps.models.routing_response_waypoint import RoutingResponseWaypoint

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingResponseWaypoint from a JSON string
routing_response_waypoint_instance = RoutingResponseWaypoint.from_json(json)
# print the JSON string representation of the object
print(RoutingResponseWaypoint.to_json())

# convert the object into a dict
routing_response_waypoint_dict = routing_response_waypoint_instance.to_dict()
# create an instance of RoutingResponseWaypoint from a dict
routing_response_waypoint_from_dict = RoutingResponseWaypoint.from_dict(routing_response_waypoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


