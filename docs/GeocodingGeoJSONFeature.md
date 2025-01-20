# GeocodingGeoJSONFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**geometry** | [**GeoJSONPoint**](GeoJSONPoint.md) |  | 
**properties** | [**GeocodingGeoJSONProperties**](GeocodingGeoJSONProperties.md) |  | [optional] 
**bbox** | **List[float]** | An array of 4 floating point numbers representing the (W, S, E, N) extremes of the features found. | [optional] 

## Example

```python
from stadiamaps.models.geocoding_geo_json_feature import GeocodingGeoJSONFeature

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodingGeoJSONFeature from a JSON string
geocoding_geo_json_feature_instance = GeocodingGeoJSONFeature.from_json(json)
# print the JSON string representation of the object
print(GeocodingGeoJSONFeature.to_json())

# convert the object into a dict
geocoding_geo_json_feature_dict = geocoding_geo_json_feature_instance.to_dict()
# create an instance of GeocodingGeoJSONFeature from a dict
geocoding_geo_json_feature_from_dict = GeocodingGeoJSONFeature.from_dict(geocoding_geo_json_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


