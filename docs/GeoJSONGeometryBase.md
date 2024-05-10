# GeoJSONGeometryBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 

## Example

```python
from stadiamaps.models.geo_json_geometry_base import GeoJSONGeometryBase

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJSONGeometryBase from a JSON string
geo_json_geometry_base_instance = GeoJSONGeometryBase.from_json(json)
# print the JSON string representation of the object
print(GeoJSONGeometryBase.to_json())

# convert the object into a dict
geo_json_geometry_base_dict = geo_json_geometry_base_instance.to_dict()
# create an instance of GeoJSONGeometryBase from a dict
geo_json_geometry_base_from_dict = GeoJSONGeometryBase.from_dict(geo_json_geometry_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


