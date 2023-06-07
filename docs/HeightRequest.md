# HeightRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**shape** | [**List[Coordinate]**](Coordinate.md) | REQUIRED if &#x60;encoded_polyline&#x60; is not present. | [optional] 
**encoded_polyline** | **str** | REQUIRED if &#x60;shape&#x60; is not present. An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm). | [optional] 
**shape_format** | **str** | Specifies whether the polyline is encoded with 6 digit precision (polyline6) or 5 digit precision (polyline5). | [optional] [default to 'polyline6']
**range** | **bool** | Controls whether or not the returned array is one-dimensional (height only) or two-dimensional (with a range and height). The range dimension can be used to generate a graph or steepness gradient along a route. | [optional] [default to False]
**height_precision** | **int** | The decimal precision (number of digits after the point) of the output. When 0, integer values are returned. Valid values are 0, 1, and 2. | [optional] [default to 0]

## Example

```python
from stadiamaps.models.height_request import HeightRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HeightRequest from a JSON string
height_request_instance = HeightRequest.from_json(json)
# print the JSON string representation of the object
print HeightRequest.to_json()

# convert the object into a dict
height_request_dict = height_request_instance.to_dict()
# create an instance of HeightRequest from a dict
height_request_form_dict = height_request.from_dict(height_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


