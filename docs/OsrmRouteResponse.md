# OsrmRouteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | [optional] 
**data_version** | **str** |  | [optional] 
**waypoints** | [**List[OsrmWaypoint]**](OsrmWaypoint.md) |  | [optional] 
**routes** | [**List[OsrmRoute]**](OsrmRoute.md) |  | [optional] 

## Example

```python
from stadiamaps.models.osrm_route_response import OsrmRouteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmRouteResponse from a JSON string
osrm_route_response_instance = OsrmRouteResponse.from_json(json)
# print the JSON string representation of the object
print(OsrmRouteResponse.to_json())

# convert the object into a dict
osrm_route_response_dict = osrm_route_response_instance.to_dict()
# create an instance of OsrmRouteResponse from a dict
osrm_route_response_from_dict = OsrmRouteResponse.from_dict(osrm_route_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


