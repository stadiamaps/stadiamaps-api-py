# RouteRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**locations** | [**List[RoutingWaypoint]**](RoutingWaypoint.md) |  | 
**costing** | [**CostingModel**](CostingModel.md) |  | 
**costing_options** | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**avoid_locations** | [**List[RoutingWaypoint]**](RoutingWaypoint.md) |  | [optional] 
**avoid_polygons** | **List[List[List[float]]]** | One or multiple exterior rings of polygons in the form of nested JSON arrays. Roads intersecting these rings will be avoided during path finding. Open rings will be closed automatically. | [optional] 
**directions_options** | [**DirectionsOptions**](DirectionsOptions.md) |  | [optional] 

## Example

```python
from stadiamaps.models.route_request import RouteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RouteRequest from a JSON string
route_request_instance = RouteRequest.from_json(json)
# print the JSON string representation of the object
print RouteRequest.to_json()

# convert the object into a dict
route_request_dict = route_request_instance.to_dict()
# create an instance of RouteRequest from a dict
route_request_form_dict = route_request.from_dict(route_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


