# SimpleRoutingWaypoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | The latitude of a point in the shape. | 
**lon** | **float** | The longitude of a point in the shape. | 
**type** | **str** | A &#x60;break&#x60; represents the start or end of a leg, and allows reversals. A &#x60;through&#x60; location is an intermediate waypoint that must be visited between &#x60;break&#x60;s, but at which reversals are not allowed. A &#x60;via&#x60; is similar to a &#x60;through&#x60; except that reversals are allowed. A &#x60;break_through&#x60; is similar to a &#x60;break&#x60; in that it can be the start/end of a leg, but does not allow reversals. | [optional] [default to 'break']

## Example

```python
from stadiamaps.models.simple_routing_waypoint import SimpleRoutingWaypoint

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleRoutingWaypoint from a JSON string
simple_routing_waypoint_instance = SimpleRoutingWaypoint.from_json(json)
# print the JSON string representation of the object
print(SimpleRoutingWaypoint.to_json())

# convert the object into a dict
simple_routing_waypoint_dict = simple_routing_waypoint_instance.to_dict()
# create an instance of SimpleRoutingWaypoint from a dict
simple_routing_waypoint_from_dict = SimpleRoutingWaypoint.from_dict(simple_routing_waypoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


