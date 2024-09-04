# OsrmAdmin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** | The ISO 3166-1 two-character code for the admin region. | [optional] 
**iso_3166_1_alpha3** | **str** | The ISO 3166-1 three-character code for the admin region. | [optional] 

## Example

```python
from stadiamaps.models.osrm_admin import OsrmAdmin

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmAdmin from a JSON string
osrm_admin_instance = OsrmAdmin.from_json(json)
# print the JSON string representation of the object
print(OsrmAdmin.to_json())

# convert the object into a dict
osrm_admin_dict = osrm_admin_instance.to_dict()
# create an instance of OsrmAdmin from a dict
osrm_admin_from_dict = OsrmAdmin.from_dict(osrm_admin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


