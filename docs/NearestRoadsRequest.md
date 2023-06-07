# NearestRoadsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locations** | [**List[Coordinate]**](Coordinate.md) |  | 
**costing** | [**CostingModel**](CostingModel.md) |  | [optional] 
**costing_options** | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**verbose** | **bool** |  | [optional] [default to False]
**directions_options** | [**DirectionsOptions**](DirectionsOptions.md) |  | [optional] 

## Example

```python
from stadiamaps.models.nearest_roads_request import NearestRoadsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NearestRoadsRequest from a JSON string
nearest_roads_request_instance = NearestRoadsRequest.from_json(json)
# print the JSON string representation of the object
print NearestRoadsRequest.to_json()

# convert the object into a dict
nearest_roads_request_dict = nearest_roads_request_instance.to_dict()
# create an instance of NearestRoadsRequest from a dict
nearest_roads_request_form_dict = nearest_roads_request.from_dict(nearest_roads_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


