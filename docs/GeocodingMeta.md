# GeocodingMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution** | **str** |  | 
**error** | **str** | Errors encountered serving the request (if any). | [optional] 

## Example

```python
from stadiamaps.models.geocoding_meta import GeocodingMeta

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodingMeta from a JSON string
geocoding_meta_instance = GeocodingMeta.from_json(json)
# print the JSON string representation of the object
print(GeocodingMeta.to_json())

# convert the object into a dict
geocoding_meta_dict = geocoding_meta_instance.to_dict()
# create an instance of GeocodingMeta from a dict
geocoding_meta_from_dict = GeocodingMeta.from_dict(geocoding_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


