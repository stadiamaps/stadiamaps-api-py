# GeocodeResponseEnvelopePropertiesV2

The GeoJSON response envelope.  This is parameterized over the feature properties type to allow for changes between versions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | **List[float]** | The geographic bounding box covering all features in the result set.  This is empty for autocomplete results. | [optional] 
**features** | [**List[FeaturePropertiesV2]**](FeaturePropertiesV2.md) |  | 
**geocoding** | [**GeocodingMeta**](GeocodingMeta.md) |  | 
**type** | **str** | The GeoJSON object type as defined in RFC 7946.  NOTE: This is always FeatureCollection, as the response envelope is designed to hold multiple results. | 

## Example

```python
from stadiamaps.models.geocode_response_envelope_properties_v2 import GeocodeResponseEnvelopePropertiesV2

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodeResponseEnvelopePropertiesV2 from a JSON string
geocode_response_envelope_properties_v2_instance = GeocodeResponseEnvelopePropertiesV2.from_json(json)
# print the JSON string representation of the object
print(GeocodeResponseEnvelopePropertiesV2.to_json())

# convert the object into a dict
geocode_response_envelope_properties_v2_dict = geocode_response_envelope_properties_v2_instance.to_dict()
# create an instance of GeocodeResponseEnvelopePropertiesV2 from a dict
geocode_response_envelope_properties_v2_from_dict = GeocodeResponseEnvelopePropertiesV2.from_dict(geocode_response_envelope_properties_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


