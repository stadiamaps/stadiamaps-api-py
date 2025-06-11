# MapMatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**shape** | [**List[MapMatchWaypoint]**](MapMatchWaypoint.md) | REQUIRED if &#x60;encoded_polyline&#x60; is not present. Note that &#x60;break&#x60; type locations are only supported when &#x60;shape_match&#x60; is set to &#x60;map_match&#x60;. | [optional] 
**encoded_polyline** | **str** | REQUIRED if &#x60;shape&#x60; is not present. An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm). Note that the polyline must be encoded with 6 digits of precision rather than the default 5! | [optional] 
**costing** | [**MapMatchCostingModel**](MapMatchCostingModel.md) |  | 
**costing_options** | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**shape_match** | **str** | Three snapping modes provide some control over how the map matching occurs. &#x60;edge_walk&#x60; is fast, but requires extremely precise data that matches the route graph almost perfectly. &#x60;map_snap&#x60; can handle significantly noisier data, but is very expensive. &#x60;walk_or_snap&#x60;, the default, tries to use edge walking first and falls back to map matching if edge walking fails. In general, you should not need to change this parameter unless you want to trace a multi-leg route with multiple &#x60;break&#x60; locations in the &#x60;shape&#x60;. | [optional] 
**units** | [**DistanceUnit**](DistanceUnit.md) |  | [optional] [default to DistanceUnit.KM]
**language** | [**RoutingLanguages**](RoutingLanguages.md) |  | [optional] [default to RoutingLanguages.EN_MINUS_US]
**directions_type** | **str** | The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter. | [optional] [default to 'instructions']
**format** | **str** | The output response format. The default JSON format is extremely compact and ideal for web or data-constrained use cases where you want to fetch additional attributes on demand in small chunks. The OSRM format is much richer and is configurable with significantly more info for turn-by-turn navigation use cases. | [optional] 
**banner_instructions** | **bool** | Optionally includes helpful banners with timing information for turn-by-turn navigation. This is only available in the OSRM format. | [optional] 
**voice_instructions** | **bool** | Optionally includes voice instructions with timing information for turn-by-turn navigation. This is only available in the OSRM format. | [optional] 
**filters** | [**AnnotationFilters**](AnnotationFilters.md) |  | [optional] 
**begin_time** | **int** | The timestamp at the start of the trace. Combined with &#x60;durations&#x60;, this provides a way to include timing information for an &#x60;encoded_polyline&#x60; trace. | [optional] 
**durations** | **int** | A list of durations (in seconds) between each successive pair of points in a polyline. | [optional] 
**use_timestamps** | **bool** | If true, the input timestamps or durations should be used when computing elapsed time for each edge along the matched path rather than the routing algorithm estimates. | [optional] [default to False]
**trace_options** | [**MapMatchTraceOptions**](MapMatchTraceOptions.md) |  | [optional] 
**linear_references** | **bool** | If true, the response will include a &#x60;linear_references&#x60; value that contains an array of base64-encoded [OpenLR location references](https://www.openlr-association.com/fileadmin/user_upload/openlr-whitepaper_v1.5.pdf), one for each graph edge of the road network matched by the trace. | [optional] [default to False]
**elevation_interval** | **float** | If greater than zero, attempts to include elevation along the route at regular intervals. The \&quot;native\&quot; internal resolution is 30m, so we recommend you use this when possible. This number is interpreted as either meters or feet depending on the unit parameter. Elevation for route sections containing a bridge or tunnel is interpolated linearly. This doesn&#39;t always match the true elevation of the bridge/tunnel, but it prevents sharp artifacts from the surrounding terrain. This functionality is unique to the routing endpoints and is not available via the elevation API. NOTE: This has no effect on the OSRM response format. | [optional] [default to 0.0]

## Example

```python
from stadiamaps.models.map_match_request import MapMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MapMatchRequest from a JSON string
map_match_request_instance = MapMatchRequest.from_json(json)
# print the JSON string representation of the object
print(MapMatchRequest.to_json())

# convert the object into a dict
map_match_request_dict = map_match_request_instance.to_dict()
# create an instance of MapMatchRequest from a dict
map_match_request_from_dict = MapMatchRequest.from_dict(map_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


