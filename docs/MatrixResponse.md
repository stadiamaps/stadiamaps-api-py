# MatrixResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**sources** | [**List[Coordinate]**](Coordinate.md) | The list of starting locations determined by snapping to the nearest appropriate point on the road network for the costing model. All locations appear in the same order as the input. | 
**targets** | [**List[Coordinate]**](Coordinate.md) | The list of ending locations determined by snapping to the nearest appropriate point on the road network for the costing model. All locations appear in the same order as the input. | 
**sources_to_targets** | **List[List[MatrixDistance]]** | The matrix of starting and ending locations, along with the computed distance and travel time. The array is row-ordered. This means that the time and distance from the first location to all others forms the first row of the array, followed by the time and distance from the second source location to all target locations, etc. | 
**warnings** | [**List[Warning]**](Warning.md) |  | [optional] 
**units** | [**ValhallaLongUnits**](ValhallaLongUnits.md) |  | 

## Example

```python
from stadiamaps.models.matrix_response import MatrixResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MatrixResponse from a JSON string
matrix_response_instance = MatrixResponse.from_json(json)
# print the JSON string representation of the object
print(MatrixResponse.to_json())

# convert the object into a dict
matrix_response_dict = matrix_response_instance.to_dict()
# create an instance of MatrixResponse from a dict
matrix_response_from_dict = MatrixResponse.from_dict(matrix_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


