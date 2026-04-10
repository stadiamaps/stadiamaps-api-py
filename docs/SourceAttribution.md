# SourceAttribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fixit_url** | **str** | A URL where you can submit changes to the source data for a place (e.g. edit on OpenStreetMap, Foursquare Placemaker, etc.). | [optional] 
**source** | **str** | The source identifier. | 
**source_id** | **str** | The ID of the record as it appears in the original source. | 

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


