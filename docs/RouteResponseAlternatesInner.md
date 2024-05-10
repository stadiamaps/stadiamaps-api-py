# RouteResponseAlternatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trip** | [**RouteTrip**](RouteTrip.md) |  | [optional] 

## Example

```python
from stadiamaps.models.route_response_alternates_inner import RouteResponseAlternatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RouteResponseAlternatesInner from a JSON string
route_response_alternates_inner_instance = RouteResponseAlternatesInner.from_json(json)
# print the JSON string representation of the object
print(RouteResponseAlternatesInner.to_json())

# convert the object into a dict
route_response_alternates_inner_dict = route_response_alternates_inner_instance.to_dict()
# create an instance of RouteResponseAlternatesInner from a dict
route_response_alternates_inner_from_dict = RouteResponseAlternatesInner.from_dict(route_response_alternates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


