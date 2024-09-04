# OsrmRouteLeg


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **float** | The distance traveled by the route, in meters. | 
**duration** | **float** | The estimated travel time, in number of seconds. | 
**weight** | **float** | The total cost of the leg computed by the routing engine. | [optional] 
**summary** | **str** |  | [optional] 
**steps** | [**List[OsrmRouteStep]**](OsrmRouteStep.md) |  | 
**annotation** | [**OsrmAnnotation**](OsrmAnnotation.md) |  | [optional] 
**via_waypoints** | [**List[OsrmViaWaypoint]**](OsrmViaWaypoint.md) | Indicates which waypoints are passed through rather than creating a new leg. | [optional] 
**admins** | [**List[OsrmAdmin]**](OsrmAdmin.md) | Administrative regions visited along the leg. | [optional] 

## Example

```python
from stadiamaps.models.osrm_route_leg import OsrmRouteLeg

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmRouteLeg from a JSON string
osrm_route_leg_instance = OsrmRouteLeg.from_json(json)
# print the JSON string representation of the object
print(OsrmRouteLeg.to_json())

# convert the object into a dict
osrm_route_leg_dict = osrm_route_leg_instance.to_dict()
# create an instance of OsrmRouteLeg from a dict
osrm_route_leg_from_dict = OsrmRouteLeg.from_dict(osrm_route_leg_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


