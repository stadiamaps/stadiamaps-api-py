# TraceAttributesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edges** | [**List[TraceEdge]**](TraceEdge.md) | The list of edges matched along the path. | [optional] 
**admins** | [**List[AdminRegion]**](AdminRegion.md) | The set of administrative regions matched along the path. Rather than repeating this information for every end node, the admins in this list are referenced by index. | [optional] 
**matched_points** | [**List[MatchedPoint]**](MatchedPoint.md) | List of match results when using the map_snap shape match algorithm. There is a one-to-one correspondence with the input set of latitude, longitude coordinates and this list of match results. | [optional] 
**osm_changeset** | **int** |  | [optional] 
**shape** | **str** | The encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm) of the matched path. | [optional] 
**confidence_score** | **float** |  | [optional] 
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**units** | [**RoutingLongUnits**](RoutingLongUnits.md) |  | [optional] [default to RoutingLongUnits.KILOMETERS]
**alternate_paths** | [**List[TraceAttributesBaseResponse]**](TraceAttributesBaseResponse.md) | Alternate paths, if any, that were not classified as the best match. | [optional] 

## Example

```python
from stadiamaps.models.trace_attributes_response import TraceAttributesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TraceAttributesResponse from a JSON string
trace_attributes_response_instance = TraceAttributesResponse.from_json(json)
# print the JSON string representation of the object
print(TraceAttributesResponse.to_json())

# convert the object into a dict
trace_attributes_response_dict = trace_attributes_response_instance.to_dict()
# create an instance of TraceAttributesResponse from a dict
trace_attributes_response_from_dict = TraceAttributesResponse.from_dict(trace_attributes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


