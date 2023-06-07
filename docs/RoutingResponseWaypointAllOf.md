# RoutingResponseWaypointAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_index** | **int** | The original index of the location (locations may be reordered for optimized routes) | [optional] 

## Example

```python
from stadiamaps.models.routing_response_waypoint_all_of import RoutingResponseWaypointAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingResponseWaypointAllOf from a JSON string
routing_response_waypoint_all_of_instance = RoutingResponseWaypointAllOf.from_json(json)
# print the JSON string representation of the object
print RoutingResponseWaypointAllOf.to_json()

# convert the object into a dict
routing_response_waypoint_all_of_dict = routing_response_waypoint_all_of_instance.to_dict()
# create an instance of RoutingResponseWaypointAllOf from a dict
routing_response_waypoint_all_of_form_dict = routing_response_waypoint_all_of.from_dict(routing_response_waypoint_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


