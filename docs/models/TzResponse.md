# stadiamaps.model.tz_response.TzResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**dst_offset** | decimal.Decimal, int,  | decimal.Decimal,  | The special offset, in seconds, from UTC that is in effect for this time zone as of the queried timestamp (defaults to now). If no additional offsets are in effect, this value is zero. This typically reflects Daylight Saving Time, but may indicate other special offsets. To get the total offset in effect, add &#x60;dst_offset&#x60; and &#x60;utc_offset&#x60; together. | 
**base_utc_offset** | decimal.Decimal, int,  | decimal.Decimal,  | The base offset, in seconds, from UTC that is normally in effect for this time zone. | 
**tz_id** | str,  | str,  | The canonical time zone ID. In the event that multiple time zones could be returned, the first one from the Unicode CLDR timezone.xml is returned. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

