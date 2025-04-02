# SourceAttribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixit_url** | **str** |  | [optional] 
**source** | **str** |  | 
**source_id** | **str** |  | 

## Example

```python
from stadiamaps.models.source_attribution import SourceAttribution

# TODO update the JSON string below
json = "{}"
# create an instance of SourceAttribution from a JSON string
source_attribution_instance = SourceAttribution.from_json(json)
# print the JSON string representation of the object
print(SourceAttribution.to_json())

# convert the object into a dict
source_attribution_dict = source_attribution_instance.to_dict()
# create an instance of SourceAttribution from a dict
source_attribution_from_dict = SourceAttribution.from_dict(source_attribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


