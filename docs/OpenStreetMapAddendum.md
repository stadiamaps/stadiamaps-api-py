# OpenStreetMapAddendum

OpenStreetMap-specific additional fields.  These values are exactly as they appear in the associated OSM tag.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**brand** | **str** | The principal brand of goods/services sold at a place, or the common identity for individually owned and operated stores. | [optional] 
**iata** | **str** | IATA airport code. | [optional] 
**icao** | **str** | ICAO airport code. | [optional] 
**opening_hours** | **str** | The opening hours of the place, in the OSM Opening Hours specification.  See https://wiki.openstreetmap.org/wiki/Key:opening_hours/specification for details. | [optional] 
**operator** | **str** | THe company, corp, person, or other entity directly in charge of operating something.  This is often used for public transport, hotels, restaurants, and postal services. See https://wiki.openstreetmap.org/wiki/Key:operator for details | [optional] 
**phone** | **str** |  | [optional] 
**website** | **str** |  | [optional] 
**wheelchair** | **str** | Is this place wheelchair accessible? | [optional] 
**wikidata** | **str** | Wikidata concordance ID. | [optional] 
**wikipedia** | **str** | Wikipedia concordance ID. | [optional] 

## Example

```python
from stadiamaps.models.open_street_map_addendum import OpenStreetMapAddendum

# TODO update the JSON string below
json = "{}"
# create an instance of OpenStreetMapAddendum from a JSON string
open_street_map_addendum_instance = OpenStreetMapAddendum.from_json(json)
# print the JSON string representation of the object
print(OpenStreetMapAddendum.to_json())

# convert the object into a dict
open_street_map_addendum_dict = open_street_map_addendum_instance.to_dict()
# create an instance of OpenStreetMapAddendum from a dict
open_street_map_addendum_from_dict = OpenStreetMapAddendum.from_dict(open_street_map_addendum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


