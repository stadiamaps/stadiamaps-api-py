# GeocodeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geocoding** | [**GeocodingObject**](GeocodingObject.md) |  | 
**bbox** | **List[float]** | An array of 4 floating point numbers representing the (W, S, E, N) extremes of the features found. | [optional] 
**features** | [**List[GeocodingGeoJSONFeature]**](GeocodingGeoJSONFeature.md) |  | 

## Example

```python
from stadiamaps.models.geocode_response import GeocodeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodeResponse from a JSON string
geocode_response_instance = GeocodeResponse.from_json(json)
# print the JSON string representation of the object
print(GeocodeResponse.to_json())

# convert the object into a dict
geocode_response_dict = geocode_response_instance.to_dict()
# create an instance of GeocodeResponse from a dict
geocode_response_from_dict = GeocodeResponse.from_dict(geocode_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


