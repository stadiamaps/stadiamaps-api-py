# stadiamaps.model.route_maneuver.RouteManeuver

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**begin_shape_index** | decimal.Decimal, int,  | decimal.Decimal,  | The index into the list of shape points for the start of the maneuver. | 
**cost** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 
**travel_mode** | [**TravelMode**](TravelMode.md) | [**TravelMode**](TravelMode.md) |  | 
**instruction** | str,  | str,  | The written maneuver instruction. | 
**length** | decimal.Decimal, int, float,  | decimal.Decimal,  | The length of the maneuver, in &#x60;units&#x60;. | value must be a 64 bit float
**end_shape_index** | decimal.Decimal, int,  | decimal.Decimal,  | The index into the list of shape points for the end of the maneuver. | 
**time** | decimal.Decimal, int, float,  | decimal.Decimal,  | The estimated time to complete the entire maneuver, in seconds. | value must be a 64 bit float
**type** | decimal.Decimal, int,  | decimal.Decimal,  | The type of route maneuver.  | Code | Type                                | |------|-------------------------------------| | 0    | None                                | | 1    | Start                               | | 2    | Start right                         | | 3    | Start left                          | | 4    | Destination                         | | 5    | Destination right                   | | 6    | Destination left                    | | 7    | Becomes                             | | 8    | Continue                            | | 9    | Slight right                        | | 10   | Right                               | | 11   | Sharp right                         | | 12   | U-turn right                        | | 13   | U-turn left                         | | 14   | Sharp left                          | | 15   | Left                                | | 16   | Slight left                         | | 17   | Ramp straight                       | | 18   | Ramp right                          | | 19   | Ramp left                           | | 20   | Exit right                          | | 21   | Exit left                           | | 22   | Stay straight                       | | 23   | Stay right                          | | 24   | Stay left                           | | 25   | Merge                               | | 26   | Enter roundabout                    | | 27   | Exit roundabout                     | | 28   | Enter ferry                         | | 29   | Exit ferry                          | | 30   | Transit                             | | 31   | Transit transfer                    | | 32   | Transit remain on                   | | 33   | Transit connection start            | | 34   | Transit connection transfer         | | 35   | Transit connection destination      | | 36   | Post-transit connection destination | | 37   | Merge right                         | | 38   | Merge left                          |  | 
**travel_type** | str,  | str,  |  | must be one of ["car", "foot", "road", "tram", "metro", "rail", "bus", "ferry", "cable_car", "gondola", "funicular", ] 
**verbal_transition_alert_instruction** | str,  | str,  | Text suitable for use as a verbal navigation alert. | [optional] 
**verbal_pre_transition_instruction** | str,  | str,  | Text suitable for use as a verbal navigation alert immediately prior to the maneuver transition. | [optional] 
**verbal_post_transition_instruction** | str,  | str,  | Text suitable for use as a verbal navigation alert immediately after to the maneuver transition. | [optional] 
**[street_names](#street_names)** | list, tuple,  | tuple,  | A list of street names that are consistent along the entire maneuver. | [optional] 
**[begin_street_names](#begin_street_names)** | list, tuple,  | tuple,  | A list of street names at the beginning of the maneuver, if they are different from the names at the end. | [optional] 
**toll** | bool,  | BoolClass,  | True any portion of the maneuver is subject to a toll. | [optional] if omitted the server will use the default value of False
**rough** | bool,  | BoolClass,  | True any portion of the maneuver is unpaved or has portions of rough pavement. | [optional] if omitted the server will use the default value of False
**gate** | bool,  | BoolClass,  | True if a gate is encountered in the course of this maneuver. | [optional] if omitted the server will use the default value of False
**ferry** | bool,  | BoolClass,  | True if a ferry is encountered in the course of this maneuver. | [optional] if omitted the server will use the default value of False
**sign** | [**ManeuverSign**](ManeuverSign.md) | [**ManeuverSign**](ManeuverSign.md) |  | [optional] 
**roundabout_exit_count** | decimal.Decimal, int,  | decimal.Decimal,  | The exit number of the roundabout to take after entering. | [optional] 
**depart_instruction** | decimal.Decimal, int,  | decimal.Decimal,  | The written departure time instruction (typically used in a transit maneuver). | [optional] 
**verbal_depart_instruction** | decimal.Decimal, int,  | decimal.Decimal,  | Text suitable for use as a verbal departure time instruction (typically used in a transit maneuver). | [optional] 
**arrive_instruction** | decimal.Decimal, int,  | decimal.Decimal,  | The written arrival time instruction (typically used in a transit maneuver). | [optional] 
**verbal_arrive_instruction** | decimal.Decimal, int,  | decimal.Decimal,  | Text suitable for use as a verbal departure time instruction (typically used in a transit maneuver). | [optional] 
**transit_info** | [**TransitInfo**](TransitInfo.md) | [**TransitInfo**](TransitInfo.md) |  | [optional] 
**verbal_multi_cue** | bool,  | BoolClass,  | True if the &#x60;verbal_pre_transition_instruction&#x60; has been appended with the verbal instruction of the next maneuver. | [optional] if omitted the server will use the default value of False
**bss_maneuver_type** | str,  | str,  | Describes a bike share action when using bikeshare routing. | [optional] must be one of ["NoneAction", "RentBikeAtBikeShare", "ReturnBikeAtBikeShare", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# street_names

A list of street names that are consistent along the entire maneuver.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of street names that are consistent along the entire maneuver. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# begin_street_names

A list of street names at the beginning of the maneuver, if they are different from the names at the end.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of street names at the beginning of the maneuver, if they are different from the names at the end. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

