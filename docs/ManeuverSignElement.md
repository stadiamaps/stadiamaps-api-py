# ManeuverSignElement


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The interchange sign text (varies based on the context; see the &#x60;maneuverSign&#x60; schema). | 
**is_route_number** | **bool** | True if the sign is a route number. | [optional] 
**consecutive_count** | **int** | The frequency of this sign element within a set a consecutive signs. | [optional] 

## Example

```python
from stadiamaps.models.maneuver_sign_element import ManeuverSignElement

# TODO update the JSON string below
json = "{}"
# create an instance of ManeuverSignElement from a JSON string
maneuver_sign_element_instance = ManeuverSignElement.from_json(json)
# print the JSON string representation of the object
print ManeuverSignElement.to_json()

# convert the object into a dict
maneuver_sign_element_dict = maneuver_sign_element_instance.to_dict()
# create an instance of ManeuverSignElement from a dict
maneuver_sign_element_form_dict = maneuver_sign_element.from_dict(maneuver_sign_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


