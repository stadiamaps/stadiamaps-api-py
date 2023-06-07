# MapMatchRequestAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**begin_time** | **int** | The timestamp at the start of the trace. Combined with &#x60;durations&#x60;, this provides a way to include timing information for an &#x60;encoded_polyline&#x60; trace. | [optional] 
**durations** | **int** | A list of durations (in seconds) between each successive pair of points in a polyline. | [optional] 
**use_timestamps** | **bool** | If true, the input timestamps or durations should be used when computing elapsed time for each edge along the matched path rather than the routing algorithm estimates. | [optional] [default to False]
**trace_options** | [**MapMatchTraceOptions**](MapMatchTraceOptions.md) |  | [optional] 
**linear_references** | **bool** | If true, the response will include a &#x60;linear_references&#x60; value that contains an array of base64-encoded [OpenLR location references](https://www.openlr-association.com/fileadmin/user_upload/openlr-whitepaper_v1.5.pdf), one for each graph edge of the road network matched by the trace. | [optional] [default to False]

## Example

```python
from stadiamaps.models.map_match_request_all_of import MapMatchRequestAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of MapMatchRequestAllOf from a JSON string
map_match_request_all_of_instance = MapMatchRequestAllOf.from_json(json)
# print the JSON string representation of the object
print MapMatchRequestAllOf.to_json()

# convert the object into a dict
map_match_request_all_of_dict = map_match_request_all_of_instance.to_dict()
# create an instance of MapMatchRequestAllOf from a dict
map_match_request_all_of_form_dict = map_match_request_all_of.from_dict(map_match_request_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


