# OsrmIntersection

Detailed information about intersections that the route traverses. For every step, the first intersection is at the location of the maneuver. Additional intersections will be provided for every road or path traversed until the next step.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **List[float]** | A (longitude, latitude) coordinate pair. | 
**bearings** | **List[int]** | A list of bearing values that are available for travel through the intersection. | 
**classes** | **List[str]** |  | [optional] 
**entry** | **List[bool]** | A list of entry flags, which map 1:1 to the bearings. A value of true indicates that the respective road could be entered on a valid route. False indicates that the turn onto the respective road would violate a restriction. | 
**var_in** | **int** | An index into bearings/entry array. Used to calculate the bearing just before the turn. Namely, the clockwise angle from true north to the direction of travel immediately before the maneuver/passing the intersection. Bearings are given relative to the intersection. To get the bearing in the direction of driving, the bearing has to be rotated by a value of 180. The value is not supplied for depart maneuvers. | [optional] 
**out** | **int** | An index into bearings/entry array. Used to calculate the bearing just after the turn. Namely, the clockwise angle from true north to the direction of travel immediately after the maneuver/passing the intersection. This is not supplied for arrive maneuvers. | [optional] 
**lanes** | [**List[OsrmLane]**](OsrmLane.md) | Available turn lanes at the intersection. May be omitted if no lane information is available for the intersection. | [optional] 
**admin_index** | **int** | The index into the admin boundaries list on the route leg. | [optional] 
**duration** | **float** | The estimated duration, in seconds, to traverse the intersection. | [optional] 
**turn_duration** | **float** | The estimated duration, in seconds, to complete the turn. | [optional] 
**turn_weight** | **float** |  | [optional] 
**geometry_index** | **int** | The index of the intersection in the leg geometry. | [optional] 
**weight** | **float** |  | [optional] 

## Example

```python
from stadiamaps.models.osrm_intersection import OsrmIntersection

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmIntersection from a JSON string
osrm_intersection_instance = OsrmIntersection.from_json(json)
# print the JSON string representation of the object
print(OsrmIntersection.to_json())

# convert the object into a dict
osrm_intersection_dict = osrm_intersection_instance.to_dict()
# create an instance of OsrmIntersection from a dict
osrm_intersection_from_dict = OsrmIntersection.from_dict(osrm_intersection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


