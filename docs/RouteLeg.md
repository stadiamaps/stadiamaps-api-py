# RouteLeg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maneuvers** | [**List[RouteManeuver]**](RouteManeuver.md) |  | 
**shape** | **str** | An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm) with 6 digits of decimal precision. | 
**summary** | [**RouteSummary**](RouteSummary.md) |  | 
**elevation_interval** | **float** | The sampling distance between elevation values along the route. This echoes the request parameter having the same name. | [optional] 
**elevation** | **List[float]** | An array of elevation values sampled every &#x60;elevation_interval&#x60;. Units are either metric or imperial depending on the value of &#x60;units&#x60;. | [optional] 

## Example

```python
from stadiamaps.models.route_leg import RouteLeg

# TODO update the JSON string below
json = "{}"
# create an instance of RouteLeg from a JSON string
route_leg_instance = RouteLeg.from_json(json)
# print the JSON string representation of the object
print(RouteLeg.to_json())

# convert the object into a dict
route_leg_dict = route_leg_instance.to_dict()
# create an instance of RouteLeg from a dict
route_leg_from_dict = RouteLeg.from_dict(route_leg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


