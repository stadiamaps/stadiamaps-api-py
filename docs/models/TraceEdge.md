# stadiamaps.model.trace_edge.TraceEdge

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[names](#names)** | list, tuple,  | tuple,  | The name(s) of the road at this edge, if any. | [optional] 
**length** | decimal.Decimal, int, float,  | decimal.Decimal,  | The length of this edge in &#x60;units&#x60;. | [optional] value must be a 64 bit float
**speed** | decimal.Decimal, int,  | decimal.Decimal,  | The speed of this edge in &#x60;units&#x60;/hr, in terms of average/free-flow speed for routing purposes. This is affected by any number of factors such as the road service, vehicle type, etc. and not just the posted speed limits. | [optional] 
**road_class** | [**RoadClass**](RoadClass.md) | [**RoadClass**](RoadClass.md) |  | [optional] 
**begin_heading** | decimal.Decimal, int,  | decimal.Decimal,  | The direction at the beginning of an edge. The units are degrees clockwise from north. | [optional] 
**end_heading** | decimal.Decimal, int,  | decimal.Decimal,  | The direction at the end of an edge. The units are degrees clockwise from north. | [optional] 
**begin_shape_index** | decimal.Decimal, int,  | decimal.Decimal,  | Index into the list of shape points for the start of the edge. | [optional] 
**end_shape_index** | decimal.Decimal, int,  | decimal.Decimal,  | Index into the list of shape points for the end of the edge. | [optional] 
**traversability** | [**Traversability**](Traversability.md) | [**Traversability**](Traversability.md) |  | [optional] 
**use** | [**EdgeUse**](EdgeUse.md) | [**EdgeUse**](EdgeUse.md) |  | [optional] 
**toll** | bool,  | BoolClass,  | True if the edge has a toll. | [optional] 
**unpaved** | bool,  | BoolClass,  | True if the edge has rough payment. | [optional] 
**tunnel** | bool,  | BoolClass,  | True if the edge has a tunnel. | [optional] 
**bridge** | bool,  | BoolClass,  | True if the edge has a bridge. | [optional] 
**roundabout** | bool,  | BoolClass,  | True if the edge has a roundabout. | [optional] 
**internal_intersection** | bool,  | BoolClass,  | True if the edge has an internal intersection. | [optional] 
**drive_on_right** | bool,  | BoolClass,  | True if the edge is in an area where you must drive on the right side of the road. | [optional] 
**surface** | str,  | str,  | The type of surface for the edge. | [optional] must be one of ["paved_smooth", "paved", "paved_rough", "compacted", "dirt", "gravel", "path", "impassable", ] 
**sign** | [**EdgeSign**](EdgeSign.md) | [**EdgeSign**](EdgeSign.md) |  | [optional] 
**travel_mode** | [**TravelMode**](TravelMode.md) | [**TravelMode**](TravelMode.md) |  | [optional] 
**vehicle_type** | str,  | str,  |  | [optional] must be one of ["car", "motorcycle", "bus", "tractor_trailer", ] 
**pedestrian_type** | str,  | str,  |  | [optional] must be one of ["foot", "wheelchair", "segway", ] 
**bicycle_type** | str,  | str,  |  | [optional] must be one of ["road", "cross", "hybrid", "mountain", ] 
**transit_type** | str,  | str,  |  | [optional] must be one of ["tram", "metro", "rail", "bus", "ferry", "cable_car", "gondola", "funicular", ] 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] value must be a 64 bit integer
**way_id** | decimal.Decimal, int,  | decimal.Decimal,  | The way identifier of the edge in OSM. | [optional] value must be a 64 bit integer
**weighted_grade** | decimal.Decimal, int, float,  | decimal.Decimal,  | The weighted grade factor. Valhalla manufactures a weighted grade from elevation data. It is a measure used for hill avoidance in routing - sort of a relative energy use along an edge. But since an edge in Valhalla can possibly go up and down over several hills it might not equate to what you would normally think of as grade. | [optional] value must be a 64 bit float
**max_upward_grade** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum upward slope. A value of 32768 indicates no elevation data is available for this edge. | [optional] 
**max_downward_grade** | decimal.Decimal, int,  | decimal.Decimal,  | The maximum downward slope. A value of 32768 indicates no elevation data is available for this edge. | [optional] 
**mean_elevation** | decimal.Decimal, int,  | decimal.Decimal,  | The mean elevation along the edge. Units are meters by default. If the &#x60;units&#x60; are specified as miles, then the mean elevation is returned in feet. A value of 32768 indicates no elevation data is available for this edge. | [optional] 
**lane_count** | decimal.Decimal, int,  | decimal.Decimal,  | The number of lanes for this edge. | [optional] 
**cycle_lane** | str,  | str,  | The type of cycle lane (if any) along this edge. | [optional] must be one of ["none", "shared", "dedicated", "separated", ] 
**bicycle_network** | decimal.Decimal, int,  | decimal.Decimal,  | The type of bicycle network, if any. This is an integer comprised of constants bitwise or&#x27;d together. For example, a route that&#x27;s part of both a local and mountain network would have a value of 12. 1 - National 2 - Regional 4 - Local 8 - Mountain | [optional] 
**sac_scale** | decimal.Decimal, int,  | decimal.Decimal,  | The difficulty of the hiking trail according to the SAC scale. 0 - No Sac Scale 1 - Hiking 2 - Mountain hiking 3 - Demanding mountain hiking 4 - Alpine hiking 5 - Demanding alpine hiking 6 - Difficult alpine hiking | [optional] 
**sidewalk** | str,  | str,  |  | [optional] must be one of ["left", "right", "both", "none", ] 
**density** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**speed_limit** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The speed limit along the edge measured in &#x60;units&#x60;/hr. This may be either an integer or the string \&quot;unlimited\&quot; if speed limit data is available. If absent, there is no speed limit data available. | [optional] 
**truck_speed** | decimal.Decimal, int,  | decimal.Decimal,  | The truck speed of this edge in &#x60;units&#x60;/hr, in terms of average/free-flow speed for routing purposes. This is affected by any number of factors such as the road service, vehicle type, etc. and not just the posted speed limits. | [optional] 
**truck_route** | bool,  | BoolClass,  | True if the edge is part of a truck route/network. | [optional] 
**end_node** | [**EndNode**](EndNode.md) | [**EndNode**](EndNode.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# names

The name(s) of the road at this edge, if any.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The name(s) of the road at this edge, if any. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

