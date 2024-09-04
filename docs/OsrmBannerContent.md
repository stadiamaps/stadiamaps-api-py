# OsrmBannerContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** |  | 
**type** | **str** |  | [optional] 
**modifier** | [**OsrmGuidanceModifier**](OsrmGuidanceModifier.md) |  | [optional] 
**components** | [**List[OsrmBannerComponent]**](OsrmBannerComponent.md) | A list of objects with additional context that allow for visual layout improvements beyond what&#39;s possible with plain text. | [optional] 

## Example

```python
from stadiamaps.models.osrm_banner_content import OsrmBannerContent

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmBannerContent from a JSON string
osrm_banner_content_instance = OsrmBannerContent.from_json(json)
# print the JSON string representation of the object
print(OsrmBannerContent.to_json())

# convert the object into a dict
osrm_banner_content_dict = osrm_banner_content_instance.to_dict()
# create an instance of OsrmBannerContent from a dict
osrm_banner_content_from_dict = OsrmBannerContent.from_dict(osrm_banner_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


