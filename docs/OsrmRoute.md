# OsrmRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **float** | The distance traveled by the route, in meters. | 
**duration** | **float** | The estimated travel time, in number of seconds. | 
**geometry** | **str** | An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm). Note that the polyline is encoded with 6 digits of precision rather than the default 5! | 
**weight** | **float** | The total cost of the route computed by the routing engine. | [optional] 
**weight_name** | **str** | The costing model used for the route. | [optional] 
**legs** | [**List[OsrmRouteLeg]**](OsrmRouteLeg.md) |  | 

## Example

```python
from stadiamaps.models.osrm_route import OsrmRoute

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmRoute from a JSON string
osrm_route_instance = OsrmRoute.from_json(json)
# print the JSON string representation of the object
print(OsrmRoute.to_json())

# convert the object into a dict
osrm_route_dict = osrm_route_instance.to_dict()
# create an instance of OsrmRoute from a dict
osrm_route_from_dict = OsrmRoute.from_dict(osrm_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


