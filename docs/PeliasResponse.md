# PeliasResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**geocoding** | [**GeocodingObject**](GeocodingObject.md) |  | 
**bbox** | **List[float]** | An array of 4 floating point numbers representing the (W, S, E, N) extremes of the features found. | [optional] 
**features** | [**List[PeliasGeoJSONFeature]**](PeliasGeoJSONFeature.md) |  | 

## Example

```python
from stadiamaps.models.pelias_response import PeliasResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PeliasResponse from a JSON string
pelias_response_instance = PeliasResponse.from_json(json)
# print the JSON string representation of the object
print(PeliasResponse.to_json())

# convert the object into a dict
pelias_response_dict = pelias_response_instance.to_dict()
# create an instance of PeliasResponse from a dict
pelias_response_form_dict = pelias_response.from_dict(pelias_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


