# AdminRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code. | [optional] 
**country_text** | **str** | The country name | [optional] 
**state_code** | **str** | The abbreviation code for the state (varies by country). | [optional] 
**state_text** | **str** | The state name. | [optional] 

## Example

```python
from stadiamaps.models.admin_region import AdminRegion

# TODO update the JSON string below
json = "{}"
# create an instance of AdminRegion from a JSON string
admin_region_instance = AdminRegion.from_json(json)
# print the JSON string representation of the object
print(AdminRegion.to_json())

# convert the object into a dict
admin_region_dict = admin_region_instance.to_dict()
# create an instance of AdminRegion from a dict
admin_region_form_dict = admin_region.from_dict(admin_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


