# FoursquareAddendum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tel** | **str** |  | [optional] 
**website** | **str** |  | [optional] 

## Example

```python
from stadiamaps.models.foursquare_addendum import FoursquareAddendum

# TODO update the JSON string below
json = "{}"
# create an instance of FoursquareAddendum from a JSON string
foursquare_addendum_instance = FoursquareAddendum.from_json(json)
# print the JSON string representation of the object
print(FoursquareAddendum.to_json())

# convert the object into a dict
foursquare_addendum_dict = foursquare_addendum_instance.to_dict()
# create an instance of FoursquareAddendum from a dict
foursquare_addendum_from_dict = FoursquareAddendum.from_dict(foursquare_addendum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


