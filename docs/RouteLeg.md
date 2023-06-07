# RouteLeg


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maneuvers** | [**List[RouteManeuver]**](RouteManeuver.md) |  | 
**shape** | **str** | An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm) with 6 digits of decimal precision. | 
**summary** | [**RouteSummary**](RouteSummary.md) |  | 

## Example

```python
from stadiamaps.models.route_leg import RouteLeg

# TODO update the JSON string below
json = "{}"
# create an instance of RouteLeg from a JSON string
route_leg_instance = RouteLeg.from_json(json)
# print the JSON string representation of the object
print RouteLeg.to_json()

# convert the object into a dict
route_leg_dict = route_leg_instance.to_dict()
# create an instance of RouteLeg from a dict
route_leg_form_dict = route_leg.from_dict(route_leg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


