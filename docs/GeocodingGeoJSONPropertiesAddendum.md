# GeocodingGeoJSONPropertiesAddendum

Optional additional information from the underlying data source (ex: OSM). This includes select fields. The most useful fields are mapped in the definition here, but others may be available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**osm** | [**GeocodingGeoJSONPropertiesAddendumOsm**](GeocodingGeoJSONPropertiesAddendumOsm.md) |  | [optional] 

## Example

```python
from stadiamaps.models.geocoding_geo_json_properties_addendum import GeocodingGeoJSONPropertiesAddendum

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodingGeoJSONPropertiesAddendum from a JSON string
geocoding_geo_json_properties_addendum_instance = GeocodingGeoJSONPropertiesAddendum.from_json(json)
# print the JSON string representation of the object
print(GeocodingGeoJSONPropertiesAddendum.to_json())

# convert the object into a dict
geocoding_geo_json_properties_addendum_dict = geocoding_geo_json_properties_addendum_instance.to_dict()
# create an instance of GeocodingGeoJSONPropertiesAddendum from a dict
geocoding_geo_json_properties_addendum_from_dict = GeocodingGeoJSONPropertiesAddendum.from_dict(geocoding_geo_json_properties_addendum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


