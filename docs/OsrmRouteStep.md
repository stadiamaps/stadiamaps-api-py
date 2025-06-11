# OsrmRouteStep

A maneuver such as a turn or merge, followed by travel along a single road or path.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **float** | The distance traveled by the route, in meters. | 
**duration** | **float** | The estimated travel time, in number of seconds. | 
**geometry** | **str** | An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm) with 6 digits of decimal precision (NOTE: most implementations default to 5). | 
**weight** | **float** |  | [optional] 
**name** | **str** | The name of the segment (ex: road) being traversed | [optional] 
**ref** | **str** | A reference number of code for the segment being traversed. | [optional] 
**pronunciation** | **str** | Pronunciation of the name (if available). The format of this varies by implementation/vendor. | [optional] 
**destinations** | **str** |  | [optional] 
**exits** | **str** |  | [optional] 
**mode** | **str** | The mode of travel. | 
**maneuver** | [**OsrmStepManeuver**](OsrmStepManeuver.md) |  | 
**intersections** | [**List[OsrmIntersection]**](OsrmIntersection.md) |  | [optional] 
**rotary_name** | **str** | The name of the traffic circle. | [optional] 
**rotary_pronunciation** | **str** | Pronunciation of the rotary name (if available). The format of this varies by implementation/vendor. | [optional] 
**driving_side** | **str** | The side of the road on which driving is legal for this step. | [optional] 
**voice_instructions** | [**List[OsrmVoiceInstruction]**](OsrmVoiceInstruction.md) | A list of announcements which should be spoken at various points along the maneuver. | [optional] 
**banner_instructions** | [**List[OsrmBannerInstruction]**](OsrmBannerInstruction.md) | A list of announcements which should be displayed prominently on screen at various points along the maneuver. | [optional] 
**speed_limit_sign** | **str** | The style of speed limit signs used along the step. | [optional] 
**speed_limit_unit** | **str** | The unit of measure that is used locally along the step. This may be different from the unit used in maxspeed annotations, and is provided so that apps can localize their display. | [optional] 

## Example

```python
from stadiamaps.models.osrm_route_step import OsrmRouteStep

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmRouteStep from a JSON string
osrm_route_step_instance = OsrmRouteStep.from_json(json)
# print the JSON string representation of the object
print(OsrmRouteStep.to_json())

# convert the object into a dict
osrm_route_step_dict = osrm_route_step_instance.to_dict()
# create an instance of OsrmRouteStep from a dict
osrm_route_step_from_dict = OsrmRouteStep.from_dict(osrm_route_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


