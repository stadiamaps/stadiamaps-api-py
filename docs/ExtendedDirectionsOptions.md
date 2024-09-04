# ExtendedDirectionsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The output response format. The default JSON format is extremely compact and ideal for web or data-constrained use cases where you want to fetch additional attributes on demand in small chunks. The OSRM format is much richer and is configurable with significantly more info for turn-by-turn navigation use cases. | [optional] 
**banner_instructions** | **bool** | Optionally includes helpful banners with timing information for turn-by-turn navigation. This is only available in the OSRM format. | [optional] 
**voice_instructions** | **bool** | Optionally includes voice instructions with timing information for turn-by-turn navigation. This is only available in the OSRM format. | [optional] 
**filters** | [**AnnotationFilters**](AnnotationFilters.md) |  | [optional] 

## Example

```python
from stadiamaps.models.extended_directions_options import ExtendedDirectionsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ExtendedDirectionsOptions from a JSON string
extended_directions_options_instance = ExtendedDirectionsOptions.from_json(json)
# print the JSON string representation of the object
print(ExtendedDirectionsOptions.to_json())

# convert the object into a dict
extended_directions_options_dict = extended_directions_options_instance.to_dict()
# create an instance of ExtendedDirectionsOptions from a dict
extended_directions_options_from_dict = ExtendedDirectionsOptions.from_dict(extended_directions_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


