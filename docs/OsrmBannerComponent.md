# OsrmBannerComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from stadiamaps.models.osrm_banner_component import OsrmBannerComponent

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmBannerComponent from a JSON string
osrm_banner_component_instance = OsrmBannerComponent.from_json(json)
# print the JSON string representation of the object
print(OsrmBannerComponent.to_json())

# convert the object into a dict
osrm_banner_component_dict = osrm_banner_component_instance.to_dict()
# create an instance of OsrmBannerComponent from a dict
osrm_banner_component_from_dict = OsrmBannerComponent.from_dict(osrm_banner_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


