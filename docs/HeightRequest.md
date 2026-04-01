# HeightRequest

Request body for the elevation endpoint.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**shape** | [**List[Coordinate]**](Coordinate.md) | The path to get the height along, expressed as a sequence of coordinates.  REQUIRED if &#x60;encoded_polyline&#x60; is not present. | [optional] 
**encoded_polyline** | **str** | An [encoded polyline string](https://developers.google.com/maps/documentation/utilities/polylinealgorithm).  REQUIRED if &#x60;shape&#x60; is not present. | [optional] 
**shape_format** | [**ShapeFormat**](ShapeFormat.md) | Specifies whether the polyline is encoded with 6 digit precision (polyline6) or 5 digit precision (polyline5). | [optional] 
**range** | **bool** | Controls whether the returned array is one-dimensional (height only) or two-dimensional (with a range and height). The range dimension can be used to generate a graph or steepness gradient along a route. | [optional] 
**height_precision** | **int** | The decimal precision (number of digits after the point) of the output. | [optional] 
**resample_distance** | **int** | The distance at which the input polyline should be sampled to provide uniform distances between points. If not set, the input shape will be used as-is. | [optional] 

## Example

```python
from stadiamaps.models.height_request import HeightRequest

# TODO update the JSON string below
json = "{}"
# create an instance of HeightRequest from a JSON string
height_request_instance = HeightRequest.from_json(json)
# print the JSON string representation of the object
print(HeightRequest.to_json())

# convert the object into a dict
height_request_dict = height_request_instance.to_dict()
# create an instance of HeightRequest from a dict
height_request_from_dict = HeightRequest.from_dict(height_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


