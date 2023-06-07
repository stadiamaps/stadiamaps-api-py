# stadiamaps.model.pelias_geo_json_feature.PeliasGeoJSONFeature

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**geometry** | [**GeoJSONPoint**](GeoJSONPoint.md) | [**GeoJSONPoint**](GeoJSONPoint.md) |  | 
**type** | str,  | str,  |  | must be one of ["Feature", ] 
**properties** | [**PeliasGeoJSONProperties**](PeliasGeoJSONProperties.md) | [**PeliasGeoJSONProperties**](PeliasGeoJSONProperties.md) |  | [optional] 
**id** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

