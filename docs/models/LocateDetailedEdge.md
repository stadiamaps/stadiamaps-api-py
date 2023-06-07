# stadiamaps.model.locate_detailed_edge.LocateDetailedEdge

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**sidewalk_left** | bool,  | BoolClass,  | Is there a sidewalk to the left of the edge? | [optional] 
**sidewalk_right** | bool,  | BoolClass,  | Is there a sidewalk to the right of the edge? | [optional] 
**lane_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**stop_sign** | bool,  | BoolClass,  | Is there a stop sign at end of the directed edge? | [optional] 
**sac_scale** | str,  | str,  |  | [optional] must be one of ["none", "hiking", "mountain hiking", "demanding mountain hiking", "alpine hiking", "demanding alpine hiking", "difficult alpine hiking", ] 
**yield_sign** | bool,  | BoolClass,  | Is there a yield sign at end of the directed edge? | [optional] 
**not_thru** | bool,  | BoolClass,  | Does the edge lead to a \&quot;no-through\&quot; region? | [optional] 
**forward** | bool,  | BoolClass,  | Is the edge info forward? If false, then reverse is implied. | [optional] 
**end_node** | [**NodeId**](NodeId.md) | [**NodeId**](NodeId.md) |  | [optional] 
**truck_route** | bool,  | BoolClass,  | Is the edge part of a truck route/network? | [optional] 
**speeds** | [**Speeds**](Speeds.md) | [**Speeds**](Speeds.md) |  | [optional] 
**bike_network** | bool,  | BoolClass,  | Is the edge part of a bicycle network? | [optional] 
**round_about** | bool,  | BoolClass,  | Is the edge part of a roundabout? | [optional] 
**traffic_signal** | bool,  | BoolClass,  | Is there a traffic signal at the end of the directed edge? | [optional] 
**access_restriction** | bool,  | BoolClass,  | Is there a general restriction or access condition? | [optional] 
**destination_only** | bool,  | BoolClass,  | Is the edge destination only? If so, it will not be routed through. | [optional] 
**geo_attributes** | [**GeoAttributes**](GeoAttributes.md) | [**GeoAttributes**](GeoAttributes.md) |  | [optional] 
**start_restriction** | [**Restrictions**](Restrictions.md) | [**Restrictions**](Restrictions.md) |  | [optional] 
**cycle_lane** | str,  | str,  | Indication of the type of cycle lane (if any) present along an edge. | [optional] must be one of ["none", "shared", "dedicated", "separated", ] 
**end_restriction** | [**Restrictions**](Restrictions.md) | [**Restrictions**](Restrictions.md) |  | [optional] 
**seasonal** | bool,  | BoolClass,  | Is access seasonal (ex. no access in winter)? | [optional] 
**country_crossing** | bool,  | BoolClass,  | Does the edge cross into a new country? | [optional] 
**part_of_complex_restriction** | bool,  | BoolClass,  | Is the edge part of a complex restriction? | [optional] 
**has_sign** | bool,  | BoolClass,  | Do exit signs exist for the edge? | [optional] 
**access** | [**Restrictions**](Restrictions.md) | [**Restrictions**](Restrictions.md) |  | [optional] 
**bridge** | bool,  | BoolClass,  | Is the edge part of a bridge? | [optional] 
**classification** | [**HighwayClassification**](HighwayClassification.md) | [**HighwayClassification**](HighwayClassification.md) |  | [optional] 
**toll** | bool,  | BoolClass,  | Is the edge part of a toll road? | [optional] 
**tunnel** | bool,  | BoolClass,  | Is the edge part of a tunnel? | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

