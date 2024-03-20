# RouteSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | The estimated travel time, in seconds | 
**length** | **float** | The estimated travel distance, in &#x60;units&#x60; (km or mi) | 
**min_lat** | **float** | The minimum latitude of the bounding box containing the route. | 
**max_lat** | **float** | The maximum latitude of the bounding box containing the route. | 
**min_lon** | **float** | The minimum longitude of the bounding box containing the route. | 
**max_lon** | **float** | The maximum longitude of the bounding box containing the route. | 

## Example

```python
from stadiamaps.models.route_summary import RouteSummary

# TODO update the JSON string below
json = "{}"
# create an instance of RouteSummary from a JSON string
route_summary_instance = RouteSummary.from_json(json)
# print the JSON string representation of the object
print(RouteSummary.to_json())

# convert the object into a dict
route_summary_dict = route_summary_instance.to_dict()
# create an instance of RouteSummary from a dict
route_summary_form_dict = route_summary.from_dict(route_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


