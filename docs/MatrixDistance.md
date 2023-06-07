# MatrixDistance


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **float** | The distance (in &#x60;units&#x60;) between the location in &#x60;sources&#x60; at &#x60;from_index&#x60; and the location in &#x60;targets&#x60; at &#x60;to_index&#x60;. | 
**time** | **int** | The travel time (in seconds) between the location in &#x60;sources&#x60; at &#x60;from_index&#x60; and the location in &#x60;targets&#x60; at &#x60;to_index&#x60;. | 
**from_index** | **int** | The index of the start location in the &#x60;sources&#x60; array. | 
**to_index** | **int** | The index of the end location in the &#x60;targets&#x60; array. | 

## Example

```python
from stadiamaps.models.matrix_distance import MatrixDistance

# TODO update the JSON string below
json = "{}"
# create an instance of MatrixDistance from a JSON string
matrix_distance_instance = MatrixDistance.from_json(json)
# print the JSON string representation of the object
print MatrixDistance.to_json()

# convert the object into a dict
matrix_distance_dict = matrix_distance_instance.to_dict()
# create an instance of MatrixDistance from a dict
matrix_distance_form_dict = matrix_distance.from_dict(matrix_distance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


