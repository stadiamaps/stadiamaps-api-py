# Context

The geographic context for a feature.  Note that while data sources and country codes are listed, this does not *necessarily* mean that the view is a specific hierarchy endorsed by that source. We generally attempt to present the same view as OpenStreetMap. Contact us if your use case requires a specific political view of the world.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_a2** | **str** | The ISO 3166-1 alpha-2 country code in which the feature is located. | [optional] 
**iso_3166_a3** | **str** | The ISO 3166-1 alpha-3 country code in which the feature is located. | [optional] 
**whosonfirst** | [**WofContext**](WofContext.md) | The geographic context, with administrative hierarchy modeled using the Who&#39;s on First taxonomy. | 

## Example

```python
from stadiamaps.models.context import Context

# TODO update the JSON string below
json = "{}"
# create an instance of Context from a JSON string
context_instance = Context.from_json(json)
# print the JSON string representation of the object
print(Context.to_json())

# convert the object into a dict
context_dict = context_instance.to_dict()
# create an instance of Context from a dict
context_from_dict = Context.from_dict(context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


