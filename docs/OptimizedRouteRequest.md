# OptimizedRouteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**DistanceUnit**](DistanceUnit.md) |  | [optional] [default to DistanceUnit.KM]
**language** | [**RoutingLanguages**](RoutingLanguages.md) |  | [optional] [default to RoutingLanguages.EN_MINUS_US]
**directions_type** | **str** | The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter. | [optional] [default to 'instructions']
**format** | **str** | The output response format. The default JSON format is extremely compact and ideal for web or data-constrained use cases where you want to fetch additional attributes on demand in small chunks. The OSRM format is much richer and is configurable with significantly more info for turn-by-turn navigation use cases. | [optional] 
**banner_instructions** | **bool** | Optionally includes helpful banners with timing information for turn-by-turn navigation. This is only available in the OSRM format. | [optional] 
**voice_instructions** | **bool** | Optionally includes voice instructions with timing information for turn-by-turn navigation. This is only available in the OSRM format. | [optional] 
**filters** | [**AnnotationFilters**](AnnotationFilters.md) |  | [optional] 
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**locations** | [**List[Coordinate]**](Coordinate.md) | The list of locations. The first and last are assumed to be the start and end points, and all intermediate points are locations that you want to visit along the way. | 
**costing** | [**MatrixCostingModel**](MatrixCostingModel.md) |  | 
**costing_options** | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**elevation_interval** | **float** | If greater than zero, attempts to include elevation along the route at regular intervals. The \&quot;native\&quot; internal resolution is 30m, so we recommend you use this when possible. This number is interpreted as either meters or feet depending on the unit parameter. Elevation for route sections containing a bridge or tunnel is interpolated linearly. This doesn&#39;t always match the true elevation of the bridge/tunnel, but it prevents sharp artifacts from the surrounding terrain. This functionality is unique to the routing endpoints and is not available via the elevation API. NOTE: This has no effect on the OSRM response format. | [optional] [default to 0.0]

## Example

```python
from stadiamaps.models.optimized_route_request import OptimizedRouteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OptimizedRouteRequest from a JSON string
optimized_route_request_instance = OptimizedRouteRequest.from_json(json)
# print the JSON string representation of the object
print(OptimizedRouteRequest.to_json())

# convert the object into a dict
optimized_route_request_dict = optimized_route_request_instance.to_dict()
# create an instance of OptimizedRouteRequest from a dict
optimized_route_request_from_dict = OptimizedRouteRequest.from_dict(optimized_route_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


