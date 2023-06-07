# IsochroneRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**locations** | [**List[Coordinate]**](Coordinate.md) |  | 
**costing** | [**IsochroneCostingModel**](IsochroneCostingModel.md) |  | 
**costing_options** | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**contours** | [**List[Contour]**](Contour.md) |  | 
**polygons** | **bool** | If true, the generated GeoJSON will use polygons. The default is to use LineStrings. Polygon output makes it easier to render overlapping areas in some visualization tools (such as MapLibre renderers). | [optional] [default to False]
**denoise** | **float** | A value in the range [0, 1] which will be used to smooth out or remove smaller contours. A value of 1 will only return the largest contour for a given time value. A value of 0.5 drops any contours that are less than half the area of the largest contour in the set of contours for that same time value. | [optional] [default to 1]
**generalize** | **float** | The value in meters to be used as a tolerance for Douglas-Peucker generalization. | [optional] [default to 200.0]
**show_locations** | **bool** | If true, then the output GeoJSON will include the input locations as two MultiPoint features: one for the exact input coordinates, and a second for the route network node location that the point was snapped to. | [optional] [default to False]

## Example

```python
from stadiamaps.models.isochrone_request import IsochroneRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IsochroneRequest from a JSON string
isochrone_request_instance = IsochroneRequest.from_json(json)
# print the JSON string representation of the object
print IsochroneRequest.to_json()

# convert the object into a dict
isochrone_request_dict = isochrone_request_instance.to_dict()
# create an instance of IsochroneRequest from a dict
isochrone_request_form_dict = isochrone_request.from_dict(isochrone_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


