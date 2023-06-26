# HeightResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**shape** | [**List[Coordinate]**](Coordinate.md) |  | [optional] 
**encoded_polyline** | **str** | The input polyline. | [optional] 
**height** | **List[int]** | The list of heights for each point, in meters. Present only if &#x60;range&#x60; is &#x60;false&#x60;. Null values indicate missing data. | [optional] 
**range_height** | **List[List[int]]** | The list of ranges and heights for each point in the shape, where each entry is an array of length 2. Present only if &#x60;range&#x60; is &#x60;true&#x60;. In each pair, the first element represents the range or distance along the input locations. It is the cumulative distance along the previous coordinates in the shape up to the current coordinate. This value for the first coordinate in the shape will always be 0. The second element in the pair represents the height or elevation at the associated coordinate. The height is null if no height data exists for a given location. Both values are expressed in meters. | [optional] 

## Example

```python
from stadiamaps.models.height_response import HeightResponse

# TODO update the JSON string below
json = "{}"
# create an instance of HeightResponse from a JSON string
height_response_instance = HeightResponse.from_json(json)
# print the JSON string representation of the object
print HeightResponse.to_json()

# convert the object into a dict
height_response_dict = height_response_instance.to_dict()
# create an instance of HeightResponse from a dict
height_response_form_dict = height_response.from_dict(height_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


