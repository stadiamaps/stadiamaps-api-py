# RouteResponseTrip


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The response status code | 
**status_message** | **str** | The response status message | 
**units** | [**ValhallaLongUnits**](ValhallaLongUnits.md) |  | 
**language** | [**ValhallaLanguages**](ValhallaLanguages.md) |  | 
**locations** | [**List[RoutingResponseWaypoint]**](RoutingResponseWaypoint.md) |  | 
**legs** | [**List[RouteLeg]**](RouteLeg.md) |  | 
**summary** | [**RouteSummary**](RouteSummary.md) |  | 

## Example

```python
from stadiamaps.models.route_response_trip import RouteResponseTrip

# TODO update the JSON string below
json = "{}"
# create an instance of RouteResponseTrip from a JSON string
route_response_trip_instance = RouteResponseTrip.from_json(json)
# print the JSON string representation of the object
print RouteResponseTrip.to_json()

# convert the object into a dict
route_response_trip_dict = route_response_trip_instance.to_dict()
# create an instance of RouteResponseTrip from a dict
route_response_trip_form_dict = route_response_trip.from_dict(route_response_trip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


