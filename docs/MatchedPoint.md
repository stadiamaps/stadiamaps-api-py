# MatchedPoint


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | The latitude of the matched point. | 
**lon** | **float** | The longitude of the matched point. | 
**type** | **str** |  | 
**edge_index** | **int** | The index of the edge in the list of &#x60;edges&#x60;. This key will be missing if the point is unmatched. | [optional] 
**begin_route_discontinuity** | **bool** | If true, this match result is the begin location of a route discontinuity. | [optional] [default to False]
**end_route_discontinuity** | **bool** | If true, this match result is the end location of a route discontinuity. | [optional] [default to False]
**distance_along_edge** | **float** | The distance along the associated edge for this matched point, expressed as a value between 0 and 1. For example, if the matched point is halfway along the edge, then the value will be 0.5. This key will be absent if the point is unmatched. | [optional] 
**distance_from_trace_point** | **float** | The distance in meters from the trace point to the matched point. This key will be absent if the point is unmatched. | [optional] 

## Example

```python
from stadiamaps.models.matched_point import MatchedPoint

# TODO update the JSON string below
json = "{}"
# create an instance of MatchedPoint from a JSON string
matched_point_instance = MatchedPoint.from_json(json)
# print the JSON string representation of the object
print MatchedPoint.to_json()

# convert the object into a dict
matched_point_dict = matched_point_instance.to_dict()
# create an instance of MatchedPoint from a dict
matched_point_form_dict = matched_point.from_dict(matched_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


