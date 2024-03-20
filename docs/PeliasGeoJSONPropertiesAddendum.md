# PeliasGeoJSONPropertiesAddendum

Optional additional information from the underlying data source (ex: OSM). This includes select fields. The most useful fields are mapped in the definition here, but others may be available.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**osm** | [**PeliasGeoJSONPropertiesAddendumOsm**](PeliasGeoJSONPropertiesAddendumOsm.md) |  | [optional] 

## Example

```python
from stadiamaps.models.pelias_geo_json_properties_addendum import PeliasGeoJSONPropertiesAddendum

# TODO update the JSON string below
json = "{}"
# create an instance of PeliasGeoJSONPropertiesAddendum from a JSON string
pelias_geo_json_properties_addendum_instance = PeliasGeoJSONPropertiesAddendum.from_json(json)
# print the JSON string representation of the object
print(PeliasGeoJSONPropertiesAddendum.to_json())

# convert the object into a dict
pelias_geo_json_properties_addendum_dict = pelias_geo_json_properties_addendum_instance.to_dict()
# create an instance of PeliasGeoJSONPropertiesAddendum from a dict
pelias_geo_json_properties_addendum_form_dict = pelias_geo_json_properties_addendum.from_dict(pelias_geo_json_properties_addendum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


