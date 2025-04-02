# SearchQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The place name (address, venue name, etc.) to search for. | [optional] 
**focus_point_lat** | **float** | The latitude of the point to focus the search on. This will bias results toward the focus point. Requires &#x60;focus.point.lon&#x60;. | [optional] 
**focus_point_lon** | **float** | The longitude of the point to focus the search on. This will bias results toward the focus point. Requires &#x60;focus.point.lat&#x60;. | [optional] 
**boundary_rect_min_lat** | **float** | Defines the min latitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
**boundary_rect_max_lat** | **float** | Defines the max latitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
**boundary_rect_min_lon** | **float** | Defines the min longitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
**boundary_rect_max_lon** | **float** | Defines the max longitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
**boundary_circle_lat** | **float** | The latitude of the center of a circle to limit the search to. Requires &#x60;boundary.circle.lon&#x60;. | [optional] 
**boundary_circle_lon** | **float** | The longitude of the center of a circle to limit the search to. Requires &#x60;boundary.circle.lat&#x60;. | [optional] 
**boundary_circle_radius** | **float** | The radius of the circle (in kilometers) to limit the search to. Defaults to 50km if unspecified. | [optional] 
**boundary_country** | **List[str]** | A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. | [optional] 
**boundary_gid** | **str** | The GID of an area to limit the search to. | [optional] 
**layers** | [**List[GeocodingLayer]**](GeocodingLayer.md) | A list of layers to limit the search to. | [optional] 
**sources** | [**List[GeocodingSource]**](GeocodingSource.md) | A list of sources to limit the search to. | [optional] 
**size** | **int** | The maximum number of results to return. | [optional] 
**lang** | **str** | A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a &#x60;langtag&#x60; (in RFC 5646 terms) can contain script, region, etc., only the &#x60;language&#x60; portion, an ISO 639 code, will be considered. So &#x60;en-US&#x60; and &#x60;en-GB&#x60; will both be treated as English. | [optional] 

## Example

```python
from stadiamaps.models.search_query import SearchQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SearchQuery from a JSON string
search_query_instance = SearchQuery.from_json(json)
# print the JSON string representation of the object
print(SearchQuery.to_json())

# convert the object into a dict
search_query_dict = search_query_instance.to_dict()
# create an instance of SearchQuery from a dict
search_query_from_dict = SearchQuery.from_dict(search_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


