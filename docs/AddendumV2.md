# AddendumV2

Miscellaneous data that doesn't quite fit anywhere else in the record.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**foursquare** | [**FoursquareAddendum**](FoursquareAddendum.md) |  | [optional] 
**geonames** | [**GeonamesAddendum**](GeonamesAddendum.md) |  | [optional] 
**osm** | [**OpenStreetMapAddendum**](OpenStreetMapAddendum.md) |  | [optional] 
**whosonfirst_concordances** | [**WhosOnFirstConcordances**](WhosOnFirstConcordances.md) |  | [optional] 

## Example

```python
from stadiamaps.models.addendum_v2 import AddendumV2

# TODO update the JSON string below
json = "{}"
# create an instance of AddendumV2 from a JSON string
addendum_v2_instance = AddendumV2.from_json(json)
# print the JSON string representation of the object
print(AddendumV2.to_json())

# convert the object into a dict
addendum_v2_dict = addendum_v2_instance.to_dict()
# create an instance of AddendumV2 from a dict
addendum_v2_from_dict = AddendumV2.from_dict(addendum_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


