# RouteTrip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The response status code | 
**status_message** | **str** | The response status message | 
**units** | [**RoutingLongUnits**](RoutingLongUnits.md) |  | [default to RoutingLongUnits.KILOMETERS]
**language** | [**RoutingLanguages**](RoutingLanguages.md) |  | [default to RoutingLanguages.EN_MINUS_US]
**locations** | [**List[RoutingResponseWaypoint]**](RoutingResponseWaypoint.md) |  | 
**legs** | [**List[RouteLeg]**](RouteLeg.md) |  | 
**summary** | [**RouteSummary**](RouteSummary.md) |  | 

## Example

```python
from stadiamaps.models.route_trip import RouteTrip

# TODO update the JSON string below
json = "{}"
# create an instance of RouteTrip from a JSON string
route_trip_instance = RouteTrip.from_json(json)
# print the JSON string representation of the object
print(RouteTrip.to_json())

# convert the object into a dict
route_trip_dict = route_trip_instance.to_dict()
# create an instance of RouteTrip from a dict
route_trip_from_dict = RouteTrip.from_dict(route_trip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


