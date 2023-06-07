# SimpleRoutingWaypointAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A &#x60;break&#x60; represents the start or end of a leg, and allows reversals. A &#x60;through&#x60; location is an intermediate waypoint that must be visited between &#x60;break&#x60;s, but at which reversals are not allowed. A &#x60;via&#x60; is similar to a &#x60;through&#x60; except that reversals are allowed. A &#x60;break_through&#x60; is similar to a &#x60;break&#x60; in that it can be the start/end of a leg, but does not allow reversals. | [optional] [default to 'break']

## Example

```python
from stadiamaps.models.simple_routing_waypoint_all_of import SimpleRoutingWaypointAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SimpleRoutingWaypointAllOf from a JSON string
simple_routing_waypoint_all_of_instance = SimpleRoutingWaypointAllOf.from_json(json)
# print the JSON string representation of the object
print SimpleRoutingWaypointAllOf.to_json()

# convert the object into a dict
simple_routing_waypoint_all_of_dict = simple_routing_waypoint_all_of_instance.to_dict()
# create an instance of SimpleRoutingWaypointAllOf from a dict
simple_routing_waypoint_all_of_form_dict = simple_routing_waypoint_all_of.from_dict(simple_routing_waypoint_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


