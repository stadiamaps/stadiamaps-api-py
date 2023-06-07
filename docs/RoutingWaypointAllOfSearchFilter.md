# RoutingWaypointAllOfSearchFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_tunnel** | **bool** | Excludes roads marked as tunnels | [optional] [default to False]
**exclude_bridge** | **bool** | Excludes roads marked as bridges | [optional] [default to False]
**exclude_ramp** | **bool** | Excludes roads marked as ramps | [optional] [default to False]
**exclude_closures** | **bool** | Excludes roads marked as closed | [optional] [default to True]
**min_road_class** | [**RoadClass**](RoadClass.md) |  | [optional] 
**max_road_class** | [**RoadClass**](RoadClass.md) |  | [optional] 

## Example

```python
from stadiamaps.models.routing_waypoint_all_of_search_filter import RoutingWaypointAllOfSearchFilter

# TODO update the JSON string below
json = "{}"
# create an instance of RoutingWaypointAllOfSearchFilter from a JSON string
routing_waypoint_all_of_search_filter_instance = RoutingWaypointAllOfSearchFilter.from_json(json)
# print the JSON string representation of the object
print RoutingWaypointAllOfSearchFilter.to_json()

# convert the object into a dict
routing_waypoint_all_of_search_filter_dict = routing_waypoint_all_of_search_filter_instance.to_dict()
# create an instance of RoutingWaypointAllOfSearchFilter from a dict
routing_waypoint_all_of_search_filter_form_dict = routing_waypoint_all_of_search_filter.from_dict(routing_waypoint_all_of_search_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


