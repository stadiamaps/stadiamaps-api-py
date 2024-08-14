# PeliasGeoJSONFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**geometry** | [**GeoJSONPoint**](GeoJSONPoint.md) |  | 
**properties** | [**PeliasGeoJSONProperties**](PeliasGeoJSONProperties.md) |  | [optional] 
**bbox** | **List[float]** | An array of 4 floating point numbers representing the (W, S, E, N) extremes of the features found. | [optional] 

## Example

```python
from stadiamaps.models.pelias_geo_json_feature import PeliasGeoJSONFeature

# TODO update the JSON string below
json = "{}"
# create an instance of PeliasGeoJSONFeature from a JSON string
pelias_geo_json_feature_instance = PeliasGeoJSONFeature.from_json(json)
# print the JSON string representation of the object
print(PeliasGeoJSONFeature.to_json())

# convert the object into a dict
pelias_geo_json_feature_dict = pelias_geo_json_feature_instance.to_dict()
# create an instance of PeliasGeoJSONFeature from a dict
pelias_geo_json_feature_from_dict = PeliasGeoJSONFeature.from_dict(pelias_geo_json_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


