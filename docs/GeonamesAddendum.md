# GeonamesAddendum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_code** | **str** | The GeoNames feature code (for GeoNames results only). | 

## Example

```python
from stadiamaps.models.geonames_addendum import GeonamesAddendum

# TODO update the JSON string below
json = "{}"
# create an instance of GeonamesAddendum from a JSON string
geonames_addendum_instance = GeonamesAddendum.from_json(json)
# print the JSON string representation of the object
print(GeonamesAddendum.to_json())

# convert the object into a dict
geonames_addendum_dict = geonames_addendum_instance.to_dict()
# create an instance of GeonamesAddendum from a dict
geonames_addendum_from_dict = GeonamesAddendum.from_dict(geonames_addendum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


