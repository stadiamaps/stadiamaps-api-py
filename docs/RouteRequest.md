# RouteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**DistanceUnit**](DistanceUnit.md) |  | [optional] 
**language** | [**ValhallaLanguages**](ValhallaLanguages.md) |  | [optional] 
**directions_type** | **str** | The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter. | [optional] [default to 'instructions']
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**locations** | [**List[RoutingWaypoint]**](RoutingWaypoint.md) |  | 
**costing** | [**CostingModel**](CostingModel.md) |  | 
**costing_options** | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**exclude_locations** | [**List[RoutingWaypoint]**](RoutingWaypoint.md) | This has the same format as the locations list. Locations are mapped to the closed road(s), and these road(s) are excluded from the route path computation. | [optional] 
**exclude_polygons** | **List[List[List[float]]]** | One or multiple exterior rings of polygons in the form of nested JSON arrays. Roads intersecting these rings will be avoided during path finding. Open rings will be closed automatically. If you only need to avoid a few specific roads, it&#39;s much more efficient to use &#x60;exclude_locations&#x60;. | [optional] 
**alternates** | **int** | How many alternate routes are desired. Note that fewer or no alternates may be returned. Alternates are not yet supported on routes with more than 2 locations or on time-dependent routes. | [optional] 

## Example

```python
from stadiamaps.models.route_request import RouteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RouteRequest from a JSON string
route_request_instance = RouteRequest.from_json(json)
# print the JSON string representation of the object
print(RouteRequest.to_json())

# convert the object into a dict
route_request_dict = route_request_instance.to_dict()
# create an instance of RouteRequest from a dict
route_request_form_dict = route_request.from_dict(route_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


