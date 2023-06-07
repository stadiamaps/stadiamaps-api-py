# stadiamaps.model.pelias_geo_json_properties.PeliasGeoJSONProperties

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**gid** | str,  | str,  | A scoped GID for this result. This can be passed to the place endpoint. Note that these are not always stable. For OSM, Geonames, and Who&#x27;s on First, these are usually stable, but for other sources like OSM, no stability is guaranteed. | [optional] 
**source_id** | str,  | str,  | An ID referencing the original data source (specified via source) for the result. These IDs are specific to the source that they originated from. For example, in the case of OSM, these typically look like way/123 or point/123. | [optional] 
**label** | str,  | str,  | A full, human-readable label. However, you may not necessarily want to use this; be sure to read the docs for name, locality, and region before making a decision. This field is mostly localized. The order of components is generally locally correct (ex: for an address in South Korea, the house number appears after the street name). However, components will use a request language equivalent if one exists (ex: Seoul instead of 서울 if lang&#x3D;en). | [optional] 
**layer** | [**PeliasLayer**](PeliasLayer.md) | [**PeliasLayer**](PeliasLayer.md) |  | [optional] 
**name** | str,  | str,  | The name of the place, the street address including house number, or label of similar relevance. If your app is localized to a specific region, you may get better display results by combining name, locality OR region (or neither?), and postal code together in the local format. Experiment with what works best for your use case. | [optional] 
**accuracy** | str,  | str,  | The accuracy of the geographic coordinates in the result. This value is a property of the result itself and won&#x27;t change based on the query. A point result means that the record can reasonably be represented by a single geographic point. Addresses, venues, or interpolated addresses usually have point accuracy. Larger areas, such as a city or country, cannot be represented by a single point, so a centroid is given instead. | [optional] must be one of ["point", "centroid", ] 
**[addendum](#addendum)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Optional additional information from the underlying data source (ex: OSM). This includes select fields. The most useful fields are mapped in the definition here, but others may be available. | [optional] 
**continent** | str,  | str,  |  | [optional] 
**continent_gid** | str,  | str,  |  | [optional] 
**country** | str,  | str,  |  | [optional] 
**country_gid** | str,  | str,  |  | [optional] 
**neighbourhood** | str,  | str,  |  | [optional] 
**neighbourhood_gid** | str,  | str,  |  | [optional] 
**borough** | str,  | str,  |  | [optional] 
**borough_gid** | str,  | str,  |  | [optional] 
**postalcode** | str,  | str,  |  | [optional] 
**street** | str,  | str,  |  | [optional] 
**housenumber** | str,  | str,  |  | [optional] 
**locality** | str,  | str,  | The city, village, town, etc. that the place / address is part of. Note that values may not always match postal or local conventions perfectly. | [optional] 
**lecality_gid** | str,  | str,  |  | [optional] 
**county** | str,  | str,  | Administrative divisions between localities and regions. Useful for disambiguating nearby results with similar names. | [optional] 
**region** | str,  | str,  | Typically the first administrative division within a country. For example, a US state or a Canadian province. | [optional] 
**region_a** | str,  | str,  | The abbreviation for the region. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# addendum

Optional additional information from the underlying data source (ex: OSM). This includes select fields. The most useful fields are mapped in the definition here, but others may be available.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Optional additional information from the underlying data source (ex: OSM). This includes select fields. The most useful fields are mapped in the definition here, but others may be available. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[osm](#osm)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# osm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**website** | str,  | str,  |  | [optional] 
**wikipedia** | str,  | str,  |  | [optional] 
**wikidata** | str,  | str,  |  | [optional] 
**phone** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

