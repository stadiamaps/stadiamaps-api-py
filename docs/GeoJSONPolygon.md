# GeoJSONPolygon


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[List[float]]]** |  | 

## Example

```python
from stadiamaps.models.geo_json_polygon import GeoJSONPolygon

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJSONPolygon from a JSON string
geo_json_polygon_instance = GeoJSONPolygon.from_json(json)
# print the JSON string representation of the object
print GeoJSONPolygon.to_json()

# convert the object into a dict
geo_json_polygon_dict = geo_json_polygon_instance.to_dict()
# create an instance of GeoJSONPolygon from a dict
geo_json_polygon_form_dict = geo_json_polygon.from_dict(geo_json_polygon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


