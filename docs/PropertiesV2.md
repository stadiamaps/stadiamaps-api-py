# PropertiesV2

The GeoJSON properties object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addendum** | [**AddendumV2**](AddendumV2.md) |  | [optional] 
**address_components** | [**AddressComponentsV2**](AddressComponentsV2.md) |  | [optional] 
**coarse_location** | **str** | The coarse-grained location of the place (e.g. Seoul, South Korea).  In search experiences, this is typically the second line of a result cell. | [optional] 
**confidence** | **float** | The level of confidence (0.0 - 1.0) that the result is what you actually searched for.  This is not necessarily the same as relevance (results are returned sorted by relevance already), but rather how closely the explicit or inferred components match the result. This is only present for forward geocoding responses (not autocomplete or place details). | [optional] 
**context** | [**Context**](Context.md) |  | [optional] 
**distance** | **float** | The distance from the search focus point, in kilometers. | [optional] 
**formatted_address_line** | **str** | The address formatted as a single line, following local postal conventions for ordering and separators. | [optional] 
**formatted_address_lines** | **List[str]** | Address components split up into lines, following local postal conventions for ordering and separators. | [optional] 
**gid** | **str** | The globally unique identifier for this result.  You can use this to uniquely identify a place, and to get the full details from the place details endpoint.  NOTE: While GIDs are unique, they may not necessarily be stable in all datasets. | 
**layer** | **str** | The data layer containing the place (e.g. \&quot;address\&quot; or \&quot;poi\&quot;). | 
**match_type** | [**MatchType**](MatchType.md) | The type of match (forward geocoding endpoints only). | [optional] 
**name** | **str** | The best name for the place, accounting for request language preferences.  When building an autocomplete search experience, this is the primary display string. | 
**precision** | [**Precision**](Precision.md) |  | 
**sources** | [**List[SourceAttribution]**](SourceAttribution.md) | A list of sources from which the result is derived. | [optional] 

## Example

```python
from stadiamaps.models.properties_v2 import PropertiesV2

# TODO update the JSON string below
json = "{}"
# create an instance of PropertiesV2 from a JSON string
properties_v2_instance = PropertiesV2.from_json(json)
# print the JSON string representation of the object
print(PropertiesV2.to_json())

# convert the object into a dict
properties_v2_dict = properties_v2_instance.to_dict()
# create an instance of PropertiesV2 from a dict
properties_v2_from_dict = PropertiesV2.from_dict(properties_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


