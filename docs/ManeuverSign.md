# ManeuverSign


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exit_number_elements** | [**List[ManeuverSignElement]**](ManeuverSignElement.md) | A list of exit number elements. This is typically just a single value. | [optional] 
**exit_branch_elements** | [**List[ManeuverSignElement]**](ManeuverSignElement.md) | A list of exit branch elements. The text is a subsequent road name or route number after the sign. | [optional] 
**exit_toward_elements** | [**List[ManeuverSignElement]**](ManeuverSignElement.md) | A list of exit name elements. The text is the interchange identifier (used more frequently outside the US). | [optional] 
**exit_name_elements** | [**List[ManeuverSignElement]**](ManeuverSignElement.md) | A list of exit name elements. The text is the location where the road ahead goes (typically a city, but occasionally a road name or route number). | [optional] 

## Example

```python
from stadiamaps.models.maneuver_sign import ManeuverSign

# TODO update the JSON string below
json = "{}"
# create an instance of ManeuverSign from a JSON string
maneuver_sign_instance = ManeuverSign.from_json(json)
# print the JSON string representation of the object
print ManeuverSign.to_json()

# convert the object into a dict
maneuver_sign_dict = maneuver_sign_instance.to_dict()
# create an instance of ManeuverSign from a dict
maneuver_sign_form_dict = maneuver_sign.from_dict(maneuver_sign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


