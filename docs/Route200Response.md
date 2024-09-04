# Route200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**trip** | [**RouteTrip**](RouteTrip.md) |  | 
**alternates** | [**List[RouteResponseAlternatesInner]**](RouteResponseAlternatesInner.md) |  | [optional] 
**code** | **str** |  | 
**message** | **str** |  | [optional] 
**data_version** | **str** |  | [optional] 
**waypoints** | [**List[OsrmWaypoint]**](OsrmWaypoint.md) |  | [optional] 
**routes** | [**List[OsrmRoute]**](OsrmRoute.md) |  | [optional] 

## Example

```python
from stadiamaps.models.route200_response import Route200Response

# TODO update the JSON string below
json = "{}"
# create an instance of Route200Response from a JSON string
route200_response_instance = Route200Response.from_json(json)
# print the JSON string representation of the object
print(Route200Response.to_json())

# convert the object into a dict
route200_response_dict = route200_response_instance.to_dict()
# create an instance of Route200Response from a dict
route200_response_from_dict = Route200Response.from_dict(route200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


