# stadiamaps.model.route_summary.RouteSummary

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**min_lon** | decimal.Decimal, int, float,  | decimal.Decimal,  | The minimum longitude of the bounding box containing the route. | value must be a 64 bit float
**max_lat** | decimal.Decimal, int, float,  | decimal.Decimal,  | The maximum latitude of the bounding box containing the route. | value must be a 64 bit float
**max_lon** | decimal.Decimal, int, float,  | decimal.Decimal,  | The maximum longitude of the bounding box containing the route. | value must be a 64 bit float
**length** | decimal.Decimal, int, float,  | decimal.Decimal,  | The estimated travel distance, in &#x60;units&#x60; (km or mi) | value must be a 64 bit float
**time** | decimal.Decimal, int, float,  | decimal.Decimal,  | The estimated travel time, in seconds | value must be a 64 bit float
**min_lat** | decimal.Decimal, int, float,  | decimal.Decimal,  | The minimum latitude of the bounding box containing the route. | value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

