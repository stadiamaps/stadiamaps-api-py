# stadiamaps.model.geo_attributes.GeoAttributes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**curvature** | decimal.Decimal, int,  | decimal.Decimal,  | Curvature factor. | [optional] 
**max_down_slope** | decimal.Decimal, int, float,  | decimal.Decimal,  | The maximum downward slope. Uses 1 degree precision for slopes to -16 degrees, and 4 degree precision afterwards (up to a max of -76 degrees). | [optional] value must be a 32 bit float
**max_up_slope** | decimal.Decimal, int, float,  | decimal.Decimal,  | The maximum upward slope. Uses 1 degree precision for slopes to 16 degrees, and 4 degree precision afterwards (up to a max of 76 degrees). | [optional] value must be a 32 bit float
**weighted_grade** | decimal.Decimal, int, float,  | decimal.Decimal,  | The weighted estimate of the grade. | [optional] value must be a 32 bit float
**length** | decimal.Decimal, int,  | decimal.Decimal,  | The length of the edge, in meters. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

