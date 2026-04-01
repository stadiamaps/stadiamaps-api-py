# ReverseQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**point_lat** | **float** | The latitude of the point at which to perform the search. | [optional] 
**point_lon** | **float** | The longitude of the point at which to perform the search. | [optional] 
**boundary_circle_radius** | **float** | The radius of the circle (in kilometers) to limit the search to. Defaults to 50km if unspecified. | [optional] 
**boundary_country** | **List[str]** | A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. | [optional] 
**boundary_gid** | **str** | The GID of an area to limit the search to. | [optional] 
**layers** | [**List[GeocodingLayer]**](GeocodingLayer.md) | A list of layers to limit the search to. | [optional] 
**sources** | [**List[GeocodingSource]**](GeocodingSource.md) | A list of sources to limit the search to. | [optional] 
**size** | **int** | The maximum number of results to return. | [optional] 
**lang** | **str** | A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a &#x60;langtag&#x60; (in RFC 5646 terms) can contain script, region, etc., only the &#x60;language&#x60; portion, an ISO 639 code, will be considered. So &#x60;en-US&#x60; and &#x60;en-GB&#x60; will both be treated as English. | [optional] 

## Example

```python
from stadiamaps.models.reverse_query import ReverseQuery

# TODO update the JSON string below
json = "{}"
# create an instance of ReverseQuery from a JSON string
reverse_query_instance = ReverseQuery.from_json(json)
# print the JSON string representation of the object
print(ReverseQuery.to_json())

# convert the object into a dict
reverse_query_dict = reverse_query_instance.to_dict()
# create an instance of ReverseQuery from a dict
reverse_query_from_dict = ReverseQuery.from_dict(reverse_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


