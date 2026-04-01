# TzResponseV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tz_id** | **str** | The canonical time zone ID.  In the event that multiple time zones could be returned, the first one from the Unicode CLDR timezone.xml is returned. | 
**utc_offset** | **int** | The total offset, in seconds, from UTC that is currently in effect for this time zone.  This accounts for both the standard offset and any seasonal adjustments (e.g. DST). | 
**is_dst** | **bool** | Whether Daylight Saving Time (or a similar seasonal offset) is in effect at the queried timestamp. | 
**timestamp** | **int** | Integer non-leap seconds since January 1, 1970 (UNIX timestamp).  If present, offsets will be calculated as of this time. Otherwise, offsets will be effective as of the time of the query. | 
**local_rfc_2822_timestamp** | **str** | The local time expressed as an RFC 2822 timestamp (e.g. Tue, 1 Jun 2003 10:52:37 -0500).  If a timestamp is included in the request, it will be localized here. Otherwise, this will reflect the time of the request.  NOTE: RFC 2822 is more restrictive than other formats and cannot represent all dates. | [optional] 
**local_rfc_3339_timestamp** | **str** | The local time expressed as an RFC 3339 (ISO 8601) timestamp (e.g. 2003-06-01T10:52:37+02:00).  If a timestamp is included in the request, it will be localized here. Otherwise, this will reflect the time of the request. | 

## Example

```python
from stadiamaps.models.tz_response_v2 import TzResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of TzResponseV2 from a JSON string
tz_response_v2_instance = TzResponseV2.from_json(json)
# print the JSON string representation of the object
print(TzResponseV2.to_json())

# convert the object into a dict
tz_response_v2_dict = tz_response_v2_instance.to_dict()
# create an instance of TzResponseV2 from a dict
tz_response_v2_from_dict = TzResponseV2.from_dict(tz_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


