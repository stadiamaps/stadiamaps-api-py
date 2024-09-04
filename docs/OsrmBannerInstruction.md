# OsrmBannerInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance_along_geometry** | **float** | How far (in meters) from the upcoming maneuver the instruction should start being displayed. | 
**primary** | [**OsrmBannerContent**](OsrmBannerContent.md) |  | 
**secondary** | [**OsrmBannerContent**](OsrmBannerContent.md) |  | [optional] 

## Example

```python
from stadiamaps.models.osrm_banner_instruction import OsrmBannerInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmBannerInstruction from a JSON string
osrm_banner_instruction_instance = OsrmBannerInstruction.from_json(json)
# print the JSON string representation of the object
print(OsrmBannerInstruction.to_json())

# convert the object into a dict
osrm_banner_instruction_dict = osrm_banner_instruction_instance.to_dict()
# create an instance of OsrmBannerInstruction from a dict
osrm_banner_instruction_from_dict = OsrmBannerInstruction.from_dict(osrm_banner_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


