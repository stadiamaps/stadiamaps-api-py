# NearestRoadsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**DistanceUnit**](DistanceUnit.md) |  | [optional] [default to DistanceUnit.KM]
**language** | [**ValhallaLanguages**](ValhallaLanguages.md) |  | [optional] [default to ValhallaLanguages.EN_MINUS_US]
**directions_type** | **str** | The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter. | [optional] [default to 'instructions']
**locations** | [**List[Coordinate]**](Coordinate.md) |  | 
**costing** | [**CostingModel**](CostingModel.md) |  | [optional] 
**costing_options** | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**verbose** | **bool** |  | [optional] [default to False]

## Example

```python
from stadiamaps.models.nearest_roads_request import NearestRoadsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NearestRoadsRequest from a JSON string
nearest_roads_request_instance = NearestRoadsRequest.from_json(json)
# print the JSON string representation of the object
print(NearestRoadsRequest.to_json())

# convert the object into a dict
nearest_roads_request_dict = nearest_roads_request_instance.to_dict()
# create an instance of NearestRoadsRequest from a dict
nearest_roads_request_from_dict = NearestRoadsRequest.from_dict(nearest_roads_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


