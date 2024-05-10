# OptimizedRouteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**DistanceUnit**](DistanceUnit.md) |  | [optional] 
**language** | [**ValhallaLanguages**](ValhallaLanguages.md) |  | [optional] 
**directions_type** | **str** | The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter. | [optional] [default to 'instructions']
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**locations** | [**List[Coordinate]**](Coordinate.md) | The list of locations. The first and last are assumed to be the start and end points, and all intermediate points are locations that you want to visit along the way. | 
**costing** | [**MatrixCostingModel**](MatrixCostingModel.md) |  | 
**costing_options** | [**CostingOptions**](CostingOptions.md) |  | [optional] 

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


