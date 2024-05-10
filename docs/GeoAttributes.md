# GeoAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**curvature** | **int** | Curvature factor. | [optional] 
**max_down_slope** | **float** | The maximum downward slope. Uses 1 degree precision for slopes to -16 degrees, and 4 degree precision afterwards (up to a max of -76 degrees). | [optional] 
**max_up_slope** | **float** | The maximum upward slope. Uses 1 degree precision for slopes to 16 degrees, and 4 degree precision afterwards (up to a max of 76 degrees). | [optional] 
**weighted_grade** | **float** | The weighted estimate of the grade. | [optional] 
**length** | **int** | The length of the edge, in meters. | [optional] 

## Example

```python
from stadiamaps.models.geo_attributes import GeoAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of GeoAttributes from a JSON string
geo_attributes_instance = GeoAttributes.from_json(json)
# print the JSON string representation of the object
print(GeoAttributes.to_json())

# convert the object into a dict
geo_attributes_dict = geo_attributes_instance.to_dict()
# create an instance of GeoAttributes from a dict
geo_attributes_from_dict = GeoAttributes.from_dict(geo_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


