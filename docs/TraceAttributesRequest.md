# TraceAttributesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**shape** | [**List[MapMatchWaypoint]**](MapMatchWaypoint.md) | REQUIRED if &#x60;encoded_polyline&#x60; is not present. Note that &#x60;break&#x60; type locations are only supported when &#x60;shape_match&#x60; is set to &#x60;map_match&#x60;. | [optional] 
**encoded_polyline** | **str** | REQUIRED if &#x60;shape&#x60; is not present. An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm). Note that the polyline must be encoded with 6 digits of precision rather than the usual 5. | [optional] 
**costing** | [**MapMatchCostingModel**](MapMatchCostingModel.md) |  | 
**costing_options** | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**shape_match** | **str** | Three snapping modes provide some control over how the map matching occurs. &#x60;edge_walk&#x60; is fast, but requires extremely precise data that matches the route graph almost perfectly. &#x60;map_snap&#x60; can handle significantly noisier data, but is very expensive. &#x60;walk_or_snap&#x60;, the default, tries to use edge walking first and falls back to map matching if edge walking fails. In general, you should not need to change this parameter unless you want to trace a multi-leg route with multiple &#x60;break&#x60; locations in the &#x60;shape&#x60;. | [optional] 
**units** | [**DistanceUnit**](DistanceUnit.md) |  | [optional] [default to DistanceUnit.KM]
**language** | [**RoutingLanguages**](RoutingLanguages.md) |  | [optional] [default to RoutingLanguages.EN_MINUS_US]
**directions_type** | **str** | The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter. | [optional] [default to 'instructions']
**filters** | [**TraceAttributeFilterOptions**](TraceAttributeFilterOptions.md) | If present, provides either a whitelist or a blacklist of keys to include/exclude in the response. This key is optional, and if omitted from the request, all available info will be returned. | [optional] 
**elevation_interval** | **float** | If greater than zero, attempts to include elevation along the route at regular intervals. The \&quot;native\&quot; internal resolution is 30m, so we recommend you use this when possible. This number is interpreted as either meters or feet depending on the unit parameter. Elevation for route sections containing a bridge or tunnel is interpolated linearly. This doesn&#39;t always match the true elevation of the bridge/tunnel, but it prevents sharp artifacts from the surrounding terrain. This functionality is unique to the routing endpoints and is not available via the elevation API. NOTE: This has no effect on the OSRM response format. | [optional] [default to 0.0]

## Example

```python
from stadiamaps.models.trace_attributes_request import TraceAttributesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TraceAttributesRequest from a JSON string
trace_attributes_request_instance = TraceAttributesRequest.from_json(json)
# print the JSON string representation of the object
print(TraceAttributesRequest.to_json())

# convert the object into a dict
trace_attributes_request_dict = trace_attributes_request_instance.to_dict()
# create an instance of TraceAttributesRequest from a dict
trace_attributes_request_from_dict = TraceAttributesRequest.from_dict(trace_attributes_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


