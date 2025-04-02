# WofContextComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abbreviation** | **str** |  | [optional] 
**gid** | **str** | A globally unique identifier for a feature. Note: these are not stable for all datasets! For example, OSM features may be deleted and re-added with a new ID. Others like Who&#39;s on First guarantee stability long term. | 
**name** | **str** |  | 

## Example

```python
from stadiamaps.models.wof_context_component import WofContextComponent

# TODO update the JSON string below
json = "{}"
# create an instance of WofContextComponent from a JSON string
wof_context_component_instance = WofContextComponent.from_json(json)
# print the JSON string representation of the object
print(WofContextComponent.to_json())

# convert the object into a dict
wof_context_component_dict = wof_context_component_instance.to_dict()
# create an instance of WofContextComponent from a dict
wof_context_component_from_dict = WofContextComponent.from_dict(wof_context_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


