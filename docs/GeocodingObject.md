# GeocodingObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribution** | **str** | A URL containing attribution information. If you are not using Stadia Maps and our standard attribution already for your basemaps, you must include this attribution link somewhere in your website/app. | [optional] 
**query** | **Dict[str, object]** | Technical details of the query. This is most useful for debugging during development. See the full example for the list of properties; these should be self-explanatory, so we don&#39;t enumerate them in the spec. | [optional] 
**warnings** | **List[str]** | An array of non-critical warnings. This is normally for informational/debugging purposes and not a serious problem. | [optional] 
**errors** | **List[str]** | An array of more serious errors (for example, omitting a required parameter). Don’t ignore these. | [optional] 

## Example

```python
from stadiamaps.models.geocoding_object import GeocodingObject

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodingObject from a JSON string
geocoding_object_instance = GeocodingObject.from_json(json)
# print the JSON string representation of the object
print(GeocodingObject.to_json())

# convert the object into a dict
geocoding_object_dict = geocoding_object_instance.to_dict()
# create an instance of GeocodingObject from a dict
geocoding_object_form_dict = geocoding_object.from_dict(geocoding_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


