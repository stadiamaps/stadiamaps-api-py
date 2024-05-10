# MatrixWaypoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | The latitude of a point in the shape. | 
**lon** | **float** | The longitude of a point in the shape. | 
**search_cutoff** | **int** | The cutoff (in meters) at which we will assume the input is too far away from civilisation to be worth correlating to the nearest graph elements. The default is 35 km. | [optional] 

## Example

```python
from stadiamaps.models.matrix_waypoint import MatrixWaypoint

# TODO update the JSON string below
json = "{}"
# create an instance of MatrixWaypoint from a JSON string
matrix_waypoint_instance = MatrixWaypoint.from_json(json)
# print the JSON string representation of the object
print(MatrixWaypoint.to_json())

# convert the object into a dict
matrix_waypoint_dict = matrix_waypoint_instance.to_dict()
# create an instance of MatrixWaypoint from a dict
matrix_waypoint_from_dict = MatrixWaypoint.from_dict(matrix_waypoint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


