# TraceEdge


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**names** | **List[str]** | The name(s) of the road at this edge, if any. | [optional] 
**length** | **float** | The length of this edge in &#x60;units&#x60;. | [optional] 
**speed** | **int** | The speed of this edge in &#x60;units&#x60;/hr, in terms of average/free-flow speed for routing purposes. This is affected by any number of factors such as the road service, vehicle type, etc. and not just the posted speed limits. | [optional] 
**road_class** | [**RoadClass**](RoadClass.md) |  | [optional] 
**begin_heading** | **int** | The direction at the beginning of an edge. The units are degrees clockwise from north. | [optional] 
**end_heading** | **int** | The direction at the end of an edge. The units are degrees clockwise from north. | [optional] 
**begin_shape_index** | **int** | Index into the list of shape points for the start of the edge. | [optional] 
**end_shape_index** | **int** | Index into the list of shape points for the end of the edge. | [optional] 
**traversability** | [**Traversability**](Traversability.md) |  | [optional] 
**use** | [**EdgeUse**](EdgeUse.md) |  | [optional] 
**toll** | **bool** | True if the edge has a toll. | [optional] 
**unpaved** | **bool** | True if the edge has rough payment. | [optional] 
**tunnel** | **bool** | True if the edge has a tunnel. | [optional] 
**bridge** | **bool** | True if the edge has a bridge. | [optional] 
**roundabout** | **bool** | True if the edge has a roundabout. | [optional] 
**internal_intersection** | **bool** | True if the edge has an internal intersection. | [optional] 
**drive_on_right** | **bool** | True if the edge is in an area where you must drive on the right side of the road. | [optional] 
**surface** | **str** | The type of surface for the edge. | [optional] 
**sign** | [**EdgeSign**](EdgeSign.md) |  | [optional] 
**travel_mode** | [**TravelMode**](TravelMode.md) |  | [optional] 
**vehicle_type** | **str** |  | [optional] 
**pedestrian_type** | **str** |  | [optional] 
**bicycle_type** | **str** |  | [optional] 
**transit_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**way_id** | **int** | The way identifier of the edge in OSM. | [optional] 
**weighted_grade** | **float** | The weighted grade factor. Valhalla manufactures a weighted grade from elevation data. It is a measure used for hill avoidance in routing - sort of a relative energy use along an edge. But since an edge in Valhalla can possibly go up and down over several hills it might not equate to what you would normally think of as grade. | [optional] 
**max_upward_grade** | **int** | The maximum upward slope. A value of 32768 indicates no elevation data is available for this edge. | [optional] 
**max_downward_grade** | **int** | The maximum downward slope. A value of 32768 indicates no elevation data is available for this edge. | [optional] 
**mean_elevation** | **int** | The mean elevation along the edge. Units are meters by default. If the &#x60;units&#x60; are specified as miles, then the mean elevation is returned in feet. A value of 32768 indicates no elevation data is available for this edge. | [optional] 
**lane_count** | **int** | The number of lanes for this edge. | [optional] 
**cycle_lane** | **str** | The type of cycle lane (if any) along this edge. | [optional] 
**bicycle_network** | **int** | The type of bicycle network, if any. This is an integer comprised of constants bitwise or&#39;d together. For example, a route that&#39;s part of both a local and mountain network would have a value of 12. 1 - National 2 - Regional 4 - Local 8 - Mountain | [optional] 
**sac_scale** | **int** | The difficulty of the hiking trail according to the SAC scale. 0 - No Sac Scale 1 - Hiking 2 - Mountain hiking 3 - Demanding mountain hiking 4 - Alpine hiking 5 - Demanding alpine hiking 6 - Difficult alpine hiking | [optional] 
**sidewalk** | **str** |  | [optional] 
**density** | **int** |  | [optional] 
**speed_limit** | **object** | The speed limit along the edge measured in &#x60;units&#x60;/hr. This may be either an integer or the string \&quot;unlimited\&quot; if speed limit data is available. If absent, there is no speed limit data available. | [optional] 
**truck_speed** | **int** | The truck speed of this edge in &#x60;units&#x60;/hr, in terms of average/free-flow speed for routing purposes. This is affected by any number of factors such as the road service, vehicle type, etc. and not just the posted speed limits. | [optional] 
**truck_route** | **bool** | True if the edge is part of a truck route/network. | [optional] 
**end_node** | [**EndNode**](EndNode.md) |  | [optional] 

## Example

```python
from stadiamaps.models.trace_edge import TraceEdge

# TODO update the JSON string below
json = "{}"
# create an instance of TraceEdge from a JSON string
trace_edge_instance = TraceEdge.from_json(json)
# print the JSON string representation of the object
print TraceEdge.to_json()

# convert the object into a dict
trace_edge_dict = trace_edge_instance.to_dict()
# create an instance of TraceEdge from a dict
trace_edge_form_dict = trace_edge.from_dict(trace_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


