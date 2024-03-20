# RouteManeuver


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **int** | The type of route maneuver.  | Code | Type                                | |------|-------------------------------------| | 0    | None                                | | 1    | Start                               | | 2    | Start right                         | | 3    | Start left                          | | 4    | Destination                         | | 5    | Destination right                   | | 6    | Destination left                    | | 7    | Becomes                             | | 8    | Continue                            | | 9    | Slight right                        | | 10   | Right                               | | 11   | Sharp right                         | | 12   | U-turn right                        | | 13   | U-turn left                         | | 14   | Sharp left                          | | 15   | Left                                | | 16   | Slight left                         | | 17   | Ramp straight                       | | 18   | Ramp right                          | | 19   | Ramp left                           | | 20   | Exit right                          | | 21   | Exit left                           | | 22   | Stay straight                       | | 23   | Stay right                          | | 24   | Stay left                           | | 25   | Merge                               | | 26   | Enter roundabout                    | | 27   | Exit roundabout                     | | 28   | Enter ferry                         | | 29   | Exit ferry                          | | 30   | Transit                             | | 31   | Transit transfer                    | | 32   | Transit remain on                   | | 33   | Transit connection start            | | 34   | Transit connection transfer         | | 35   | Transit connection destination      | | 36   | Post-transit connection destination | | 37   | Merge right                         | | 38   | Merge left                          |  | 
**instruction** | **str** | The written maneuver instruction. | 
**verbal_transition_alert_instruction** | **str** | Text suitable for use as a verbal navigation alert. | [optional] 
**verbal_pre_transition_instruction** | **str** | Text suitable for use as a verbal navigation alert immediately prior to the maneuver transition. | [optional] 
**verbal_post_transition_instruction** | **str** | Text suitable for use as a verbal navigation alert immediately after to the maneuver transition. | [optional] 
**street_names** | **List[str]** | A list of street names that are consistent along the entire maneuver. | [optional] 
**begin_street_names** | **List[str]** | A list of street names at the beginning of the maneuver, if they are different from the names at the end. | [optional] 
**time** | **float** | The estimated time to complete the entire maneuver, in seconds. | 
**length** | **float** | The length of the maneuver, in &#x60;units&#x60;. | 
**begin_shape_index** | **int** | The index into the list of shape points for the start of the maneuver. | 
**end_shape_index** | **int** | The index into the list of shape points for the end of the maneuver. | 
**toll** | **bool** | True any portion of the maneuver is subject to a toll. | [optional] [default to False]
**rough** | **bool** | True any portion of the maneuver is unpaved or has portions of rough pavement. | [optional] [default to False]
**gate** | **bool** | True if a gate is encountered in the course of this maneuver. | [optional] [default to False]
**ferry** | **bool** | True if a ferry is encountered in the course of this maneuver. | [optional] [default to False]
**sign** | [**ManeuverSign**](ManeuverSign.md) |  | [optional] 
**roundabout_exit_count** | **int** | The exit number of the roundabout to take after entering. | [optional] 
**depart_instruction** | **int** | The written departure time instruction (typically used in a transit maneuver). | [optional] 
**verbal_depart_instruction** | **int** | Text suitable for use as a verbal departure time instruction (typically used in a transit maneuver). | [optional] 
**arrive_instruction** | **int** | The written arrival time instruction (typically used in a transit maneuver). | [optional] 
**verbal_arrive_instruction** | **int** | Text suitable for use as a verbal departure time instruction (typically used in a transit maneuver). | [optional] 
**transit_info** | **Dict[str, object]** | Public transit info (not currently supported). | [optional] 
**verbal_multi_cue** | **bool** | True if the &#x60;verbal_pre_transition_instruction&#x60; has been appended with the verbal instruction of the next maneuver. | [optional] [default to False]
**travel_mode** | [**TravelMode**](TravelMode.md) |  | 
**travel_type** | **str** | The type of travel over the maneuver. This can be thought of as a specialization of the travel mode. For example, vehicular travel may be via car, motorcycle, etc.; and travel via bicycle may be via a road bike, mountain bike, etc. | 
**bss_maneuver_type** | **str** | Describes a bike share action when using bikeshare routing. | [optional] 

## Example

```python
from stadiamaps.models.route_maneuver import RouteManeuver

# TODO update the JSON string below
json = "{}"
# create an instance of RouteManeuver from a JSON string
route_maneuver_instance = RouteManeuver.from_json(json)
# print the JSON string representation of the object
print(RouteManeuver.to_json())

# convert the object into a dict
route_maneuver_dict = route_maneuver_instance.to_dict()
# create an instance of RouteManeuver from a dict
route_maneuver_form_dict = route_maneuver.from_dict(route_maneuver_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


