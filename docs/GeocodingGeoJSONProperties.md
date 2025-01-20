# GeocodingGeoJSONProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gid** | **str** | A scoped GID for this result. This can be passed to the place endpoint. Note that these are not always stable long-term. | [optional] 
**source_id** | **str** | An ID referencing the original data source (specified via source) for the result. These IDs are specific to the source that they originated from. For example, in the case of OSM, these typically look like way/123 or point/123. | [optional] 
**label** | **str** | A full, human-readable label. However, you may not necessarily want to use this; be sure to read the docs for name, locality, and region before making a decision. This field is mostly localized. The order of components is generally locally correct (ex: for an address in South Korea, the house number appears after the street name). However, components will use a request language equivalent if one exists (ex: Seoul instead of 서울 if lang&#x3D;en). | [optional] 
**layer** | [**GeocodingLayer**](GeocodingLayer.md) |  | [optional] 
**source** | **str** | The ID of the data source that the result came from. | [optional] 
**name** | **str** | The name of the place, the street address including house number, or label of similar relevance. If your app is localized to a specific region, you may get better display results by combining name, locality OR region (or neither?), and postal code together in the local format. Experiment with what works best for your use case. | [optional] 
**accuracy** | **str** | The accuracy of the geographic coordinates in the result. This value is a property of the result itself and won&#39;t change based on the query. A point result means that the record can reasonably be represented by a single geographic point. Addresses, venues, or interpolated addresses usually have point accuracy. Larger areas, such as a city or country, cannot be represented by a single point, so a centroid is given instead. | [optional] 
**addendum** | [**GeocodingGeoJSONPropertiesAddendum**](GeocodingGeoJSONPropertiesAddendum.md) |  | [optional] 
**continent** | **str** |  | [optional] 
**continent_gid** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**country_a** | **str** | The ISO 3166-1 alpha-3 code for the country the place is located in. | [optional] 
**country_code** | **str** | The ISO 3166-1 alpha-2 code for the country the place is located in. | [optional] 
**country_gid** | **str** |  | [optional] 
**neighbourhood** | **str** |  | [optional] 
**neighbourhood_gid** | **str** |  | [optional] 
**borough** | **str** |  | [optional] 
**borough_gid** | **str** |  | [optional] 
**postalcode** | **str** |  | [optional] 
**street** | **str** |  | [optional] 
**housenumber** | **str** |  | [optional] 
**locality** | **str** | The city, village, town, etc. that the place / address is part of. Note that values may not always match postal or local conventions perfectly. | [optional] 
**locality_gid** | **str** |  | [optional] 
**county** | **str** | Administrative divisions between localities and regions. Useful for disambiguating nearby results with similar names. | [optional] 
**county_gid** | **str** |  | [optional] 
**region** | **str** | Typically the first administrative division within a country. For example, a US state or a Canadian province. | [optional] 
**region_a** | **str** | The abbreviation for the region (e.g. PA for the US state of Pennsylvania). | [optional] 
**region_gid** | **str** |  | [optional] 
**localadmin** | **str** | In many countries, this is the lowest level of government. Sometimes interchangeable with locality. | [optional] 
**localadmin_gid** | **str** |  | [optional] 
**match_type** | **str** | For search and structured search results, the type of match. | [optional] 

## Example

```python
from stadiamaps.models.geocoding_geo_json_properties import GeocodingGeoJSONProperties

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodingGeoJSONProperties from a JSON string
geocoding_geo_json_properties_instance = GeocodingGeoJSONProperties.from_json(json)
# print the JSON string representation of the object
print(GeocodingGeoJSONProperties.to_json())

# convert the object into a dict
geocoding_geo_json_properties_dict = geocoding_geo_json_properties_instance.to_dict()
# create an instance of GeocodingGeoJSONProperties from a dict
geocoding_geo_json_properties_from_dict = GeocodingGeoJSONProperties.from_dict(geocoding_geo_json_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


