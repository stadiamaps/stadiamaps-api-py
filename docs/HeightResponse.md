# HeightResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**shape** | [**List[Coordinate]**](Coordinate.md) |  | [optional] 
**encoded_polyline** | **str** | The input polyline. | [optional] 
**height** | **List[int]** | The list of heights for each point, in meters. Present if &#x60;range&#x60; is &#x60;false&#x60;. | [optional] 
**range_height** | **List[List[int]]** | The list of horizontal distances and heights (respectively) for each point, in meters. Present if &#x60;range&#x60; is &#x60;true&#x60;. | [optional] 

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


