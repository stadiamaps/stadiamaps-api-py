# GeoJSONLineString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**coordinates** | **List[List[float]]** |  | 

## Example

```python
from stadiamaps.models.geo_json_line_string import GeoJSONLineString

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJSONLineString from a JSON string
geo_json_line_string_instance = GeoJSONLineString.from_json(json)
# print the JSON string representation of the object
print(GeoJSONLineString.to_json())

# convert the object into a dict
geo_json_line_string_dict = geo_json_line_string_instance.to_dict()
# create an instance of GeoJSONLineString from a dict
geo_json_line_string_from_dict = GeoJSONLineString.from_dict(geo_json_line_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


