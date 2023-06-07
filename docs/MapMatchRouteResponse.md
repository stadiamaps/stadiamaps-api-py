# MapMatchRouteResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**trip** | [**RouteResponseTrip**](RouteResponseTrip.md) |  | 
**linear_references** | **List[str]** |  | [optional] 

## Example

```python
from stadiamaps.models.map_match_route_response import MapMatchRouteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MapMatchRouteResponse from a JSON string
map_match_route_response_instance = MapMatchRouteResponse.from_json(json)
# print the JSON string representation of the object
print MapMatchRouteResponse.to_json()

# convert the object into a dict
map_match_route_response_dict = map_match_route_response_instance.to_dict()
# create an instance of MapMatchRouteResponse from a dict
map_match_route_response_form_dict = map_match_route_response.from_dict(map_match_route_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


