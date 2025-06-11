# stadiamaps.GeocodingApi

All URIs are relative to *https://api.stadiamaps.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](GeocodingApi.md#autocomplete) | **GET** /geocoding/v1/autocomplete | Search and geocode quickly based on partial input.
[**autocomplete_v2**](GeocodingApi.md#autocomplete_v2) | **GET** /geocoding/v2/autocomplete | 
[**place_details**](GeocodingApi.md#place_details) | **GET** /geocoding/v1/place | Retrieve details of a place using its GID.
[**place_details_v2**](GeocodingApi.md#place_details_v2) | **GET** /geocoding/v2/place_details | 
[**reverse**](GeocodingApi.md#reverse) | **GET** /geocoding/v1/reverse | Find places and addresses near geographic coordinates (reverse geocoding).
[**reverse_v2**](GeocodingApi.md#reverse_v2) | **GET** /geocoding/v2/reverse | 
[**search**](GeocodingApi.md#search) | **GET** /geocoding/v1/search | Search for location and other info using a place name or address (forward geocoding).
[**search_bulk**](GeocodingApi.md#search_bulk) | **POST** /geocoding/v1/search/bulk | Quickly run a batch of geocoding queries against the search or structured search endpoints.
[**search_structured**](GeocodingApi.md#search_structured) | **GET** /geocoding/v1/search/structured | Find locations matching components (structured forward geocoding).
[**search_v2**](GeocodingApi.md#search_v2) | **GET** /geocoding/v2/search | 


# **autocomplete**
> GeocodeResponse autocomplete(text, focus_point_lat=focus_point_lat, focus_point_lon=focus_point_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lat=boundary_rect_max_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_max_lon=boundary_rect_max_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_radius=boundary_circle_radius, boundary_country=boundary_country, boundary_gid=boundary_gid, layers=layers, sources=sources, size=size, lang=lang)

Search and geocode quickly based on partial input.

Autocomplete enables interactive search-as-you-type user experiences, suggesting places as you type, along with information that will help your users find the correct place quickly.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.geocode_response import GeocodeResponse
from stadiamaps.models.geocoding_layer import GeocodingLayer
from stadiamaps.models.geocoding_source import GeocodingSource
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration(
    host = "https://api.stadiamaps.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    text = 'text_example' # str | The place name (address, venue name, etc.) to search for.
    focus_point_lat = 3.4 # float | The latitude of the point to focus the search on. This will bias results toward the focus point. Requires `focus.point.lon`. (optional)
    focus_point_lon = 3.4 # float | The longitude of the point to focus the search on. This will bias results toward the focus point. Requires `focus.point.lat`. (optional)
    boundary_rect_min_lat = 3.4 # float | Defines the min latitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_rect_max_lat = 3.4 # float | Defines the max latitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_rect_min_lon = 3.4 # float | Defines the min longitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_rect_max_lon = 3.4 # float | Defines the max longitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_circle_lat = 3.4 # float | The latitude of the center of a circle to limit the search to. Requires `boundary.circle.lon`. (optional)
    boundary_circle_lon = 3.4 # float | The longitude of the center of a circle to limit the search to. Requires `boundary.circle.lat`. (optional)
    boundary_circle_radius = 3.4 # float | The radius of the circle (in kilometers) to limit the search to. Defaults to 50km (search) or 1km (reverse) if unspecified. (optional)
    boundary_country = ['boundary_country_example'] # List[str] | A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. (optional)
    boundary_gid = 'boundary_gid_example' # str | The GID of an area to limit the search to. (optional)
    layers = [stadiamaps.GeocodingLayer()] # List[GeocodingLayer] | A list of layers to limit the search to. (optional)
    sources = [stadiamaps.GeocodingSource()] # List[GeocodingSource] | A list of sources to limit the search to. (optional)
    size = 56 # int | The maximum number of results to return. (optional)
    lang = 'lang_example' # str | A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a `langtag` (in RFC 5646 terms) can contain script, region, etc., only the `language` portion, an ISO 639 code, will be considered. So `en-US` and `en-GB` will both be treated as English. (optional)

    try:
        # Search and geocode quickly based on partial input.
        api_response = api_instance.autocomplete(text, focus_point_lat=focus_point_lat, focus_point_lon=focus_point_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lat=boundary_rect_max_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_max_lon=boundary_rect_max_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_radius=boundary_circle_radius, boundary_country=boundary_country, boundary_gid=boundary_gid, layers=layers, sources=sources, size=size, lang=lang)
        print("The response of GeocodingApi->autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| The place name (address, venue name, etc.) to search for. | 
 **focus_point_lat** | **float**| The latitude of the point to focus the search on. This will bias results toward the focus point. Requires &#x60;focus.point.lon&#x60;. | [optional] 
 **focus_point_lon** | **float**| The longitude of the point to focus the search on. This will bias results toward the focus point. Requires &#x60;focus.point.lat&#x60;. | [optional] 
 **boundary_rect_min_lat** | **float**| Defines the min latitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_rect_max_lat** | **float**| Defines the max latitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_rect_min_lon** | **float**| Defines the min longitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_rect_max_lon** | **float**| Defines the max longitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_circle_lat** | **float**| The latitude of the center of a circle to limit the search to. Requires &#x60;boundary.circle.lon&#x60;. | [optional] 
 **boundary_circle_lon** | **float**| The longitude of the center of a circle to limit the search to. Requires &#x60;boundary.circle.lat&#x60;. | [optional] 
 **boundary_circle_radius** | **float**| The radius of the circle (in kilometers) to limit the search to. Defaults to 50km (search) or 1km (reverse) if unspecified. | [optional] 
 **boundary_country** | [**List[str]**](str.md)| A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. | [optional] 
 **boundary_gid** | **str**| The GID of an area to limit the search to. | [optional] 
 **layers** | [**List[GeocodingLayer]**](GeocodingLayer.md)| A list of layers to limit the search to. | [optional] 
 **sources** | [**List[GeocodingSource]**](GeocodingSource.md)| A list of sources to limit the search to. | [optional] 
 **size** | **int**| The maximum number of results to return. | [optional] 
 **lang** | **str**| A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a &#x60;langtag&#x60; (in RFC 5646 terms) can contain script, region, etc., only the &#x60;language&#x60; portion, an ISO 639 code, will be considered. So &#x60;en-US&#x60; and &#x60;en-GB&#x60; will both be treated as English. | [optional] 

### Return type

[**GeocodeResponse**](GeocodeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A GeoJSON collection of autocomplete search results. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **autocomplete_v2**
> GeocodeResponseEnvelopePropertiesV2 autocomplete_v2(text, focus_point_lat=focus_point_lat, focus_point_lon=focus_point_lon, layers=layers, sources=sources, boundary_gid=boundary_gid, boundary_country=boundary_country, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_max_lat=boundary_rect_max_lat, boundary_rect_max_lon=boundary_rect_max_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_radius=boundary_circle_radius, size=size, lang=lang)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.geocode_response_envelope_properties_v2 import GeocodeResponseEnvelopePropertiesV2
from stadiamaps.models.layer_id import LayerId
from stadiamaps.models.source_id import SourceId
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration(
    host = "https://api.stadiamaps.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    text = '1600 Pennsylvania Ave NW' # str | The text to search for (the start of an address, place name, etc.).
    focus_point_lat = 3.4 # float | The latitude of a focus point.  If provided (along with longitude), the search results should be more locally relevant. (optional)
    focus_point_lon = 3.4 # float | The longitude of a focus point.  If provided (along with longitude), the search results should be more locally relevant. (optional)
    layers = [stadiamaps.LayerId()] # List[LayerId] | A list of layers to limit the search to. (optional)
    sources = [stadiamaps.SourceId()] # List[SourceId] | A list of sources to limit the search to. (optional)
    boundary_gid = 'boundary_gid_example' # str | The GID of a region to limit the search to.  Note: these are not stable for all datasets! For example, OSM features may be deleted and re-added with a new ID. (optional)
    boundary_country = ['boundary_country_example'] # List[str] | A list of comma-separated country codes in ISO 3116-1 alpha-2 or alpha-3 format. The search will be limited to these countries. (optional)
    boundary_rect_min_lat = 3.4 # float | The minimum latitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. (optional)
    boundary_rect_min_lon = 3.4 # float | The minimum longitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. (optional)
    boundary_rect_max_lat = 3.4 # float | The maximum latitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. (optional)
    boundary_rect_max_lon = 3.4 # float | The maximum longitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. (optional)
    boundary_circle_lat = 3.4 # float | The latitude of the center of a circle to limit the search to.  NOTE: Requires boundary.circle.lon. (optional)
    boundary_circle_lon = 3.4 # float | The longitude of the center of a circle to limit the search to.  NOTE: Requires boundary.circle.lat. (optional)
    boundary_circle_radius = 56 # int | The radius of the circle (in kilometers) to limit the search to.  NOTE: Requires the other boundary.circle parameters to take effect. Defaults to 50km if unspecified. (optional)
    size = 56 # int | The maximum number of items to return from a query. (optional)
    lang = 'lang_example' # str | A BCP47 language tag which specifies a preference for localization of results. There is no default value, so place names will be returned as-is, which is usually in the local language. NOTE: The Accept-Language header is also respected, and many user agents will set it automatically. (optional)

    try:
        api_response = api_instance.autocomplete_v2(text, focus_point_lat=focus_point_lat, focus_point_lon=focus_point_lon, layers=layers, sources=sources, boundary_gid=boundary_gid, boundary_country=boundary_country, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_max_lat=boundary_rect_max_lat, boundary_rect_max_lon=boundary_rect_max_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_radius=boundary_circle_radius, size=size, lang=lang)
        print("The response of GeocodingApi->autocomplete_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->autocomplete_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| The text to search for (the start of an address, place name, etc.). | 
 **focus_point_lat** | **float**| The latitude of a focus point.  If provided (along with longitude), the search results should be more locally relevant. | [optional] 
 **focus_point_lon** | **float**| The longitude of a focus point.  If provided (along with longitude), the search results should be more locally relevant. | [optional] 
 **layers** | [**List[LayerId]**](LayerId.md)| A list of layers to limit the search to. | [optional] 
 **sources** | [**List[SourceId]**](SourceId.md)| A list of sources to limit the search to. | [optional] 
 **boundary_gid** | **str**| The GID of a region to limit the search to.  Note: these are not stable for all datasets! For example, OSM features may be deleted and re-added with a new ID. | [optional] 
 **boundary_country** | [**List[str]**](str.md)| A list of comma-separated country codes in ISO 3116-1 alpha-2 or alpha-3 format. The search will be limited to these countries. | [optional] 
 **boundary_rect_min_lat** | **float**| The minimum latitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. | [optional] 
 **boundary_rect_min_lon** | **float**| The minimum longitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. | [optional] 
 **boundary_rect_max_lat** | **float**| The maximum latitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. | [optional] 
 **boundary_rect_max_lon** | **float**| The maximum longitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. | [optional] 
 **boundary_circle_lat** | **float**| The latitude of the center of a circle to limit the search to.  NOTE: Requires boundary.circle.lon. | [optional] 
 **boundary_circle_lon** | **float**| The longitude of the center of a circle to limit the search to.  NOTE: Requires boundary.circle.lat. | [optional] 
 **boundary_circle_radius** | **int**| The radius of the circle (in kilometers) to limit the search to.  NOTE: Requires the other boundary.circle parameters to take effect. Defaults to 50km if unspecified. | [optional] 
 **size** | **int**| The maximum number of items to return from a query. | [optional] 
 **lang** | **str**| A BCP47 language tag which specifies a preference for localization of results. There is no default value, so place names will be returned as-is, which is usually in the local language. NOTE: The Accept-Language header is also respected, and many user agents will set it automatically. | [optional] 

### Return type

[**GeocodeResponseEnvelopePropertiesV2**](GeocodeResponseEnvelopePropertiesV2.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A GeoJSON FeatureCollection with the results |  -  |
**400** | A response with a description of why the request is malformed |  -  |
**500** | A response with a description of what went wrong internally |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_details**
> GeocodeResponse place_details(ids, lang=lang)

Retrieve details of a place using its GID.

Many search result components include an associated GID field (for example, an address may have a `localadmin_gid`). The place endpoint lets you look up these places directly by ID. Note that GIDs are not stable for all sources. See the [online documentation](https://docs.stadiamaps.com/geocoding-search-autocomplete/place-lookup/) for details.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.geocode_response import GeocodeResponse
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration(
    host = "https://api.stadiamaps.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    ids = ['ids_example'] # List[str] | A list of GIDs to search for.
    lang = 'lang_example' # str | A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a `langtag` (in RFC 5646 terms) can contain script, region, etc., only the `language` portion, an ISO 639 code, will be considered. So `en-US` and `en-GB` will both be treated as English. (optional)

    try:
        # Retrieve details of a place using its GID.
        api_response = api_instance.place_details(ids, lang=lang)
        print("The response of GeocodingApi->place_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->place_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| A list of GIDs to search for. | 
 **lang** | **str**| A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a &#x60;langtag&#x60; (in RFC 5646 terms) can contain script, region, etc., only the &#x60;language&#x60; portion, an ISO 639 code, will be considered. So &#x60;en-US&#x60; and &#x60;en-GB&#x60; will both be treated as English. | [optional] 

### Return type

[**GeocodeResponse**](GeocodeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A GeoJSON collection of search results. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_details_v2**
> GeocodeResponseEnvelopePropertiesV2 place_details_v2(ids, lang=lang)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.geocode_response_envelope_properties_v2 import GeocodeResponseEnvelopePropertiesV2
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration(
    host = "https://api.stadiamaps.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    ids = ['[\"whosonfirst:locality:102026327\"]'] # List[str] | 
    lang = 'lang_example' # str | A BCP47 language tag which specifies a preference for localization of results. There is no default value, so place names will be returned as-is, which is usually in the local language. NOTE: The Accept-Language header is also respected, and many user agents will set it automatically. (optional)

    try:
        api_response = api_instance.place_details_v2(ids, lang=lang)
        print("The response of GeocodingApi->place_details_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->place_details_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)|  | 
 **lang** | **str**| A BCP47 language tag which specifies a preference for localization of results. There is no default value, so place names will be returned as-is, which is usually in the local language. NOTE: The Accept-Language header is also respected, and many user agents will set it automatically. | [optional] 

### Return type

[**GeocodeResponseEnvelopePropertiesV2**](GeocodeResponseEnvelopePropertiesV2.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A GeoJSON FeatureCollection with the results |  -  |
**400** | A response with a description of why the request is malformed |  -  |
**500** | A response with a description of what went wrong internally |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverse**
> GeocodeResponse reverse(point_lat, point_lon, boundary_circle_radius=boundary_circle_radius, layers=layers, sources=sources, boundary_country=boundary_country, boundary_gid=boundary_gid, size=size, lang=lang)

Find places and addresses near geographic coordinates (reverse geocoding).

Reverse geocoding and search finds places and addresses near any geographic coordinates.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.geocode_response import GeocodeResponse
from stadiamaps.models.geocoding_layer import GeocodingLayer
from stadiamaps.models.geocoding_source import GeocodingSource
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration(
    host = "https://api.stadiamaps.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    point_lat = 3.4 # float | The latitude of the point at which to perform the search.
    point_lon = 3.4 # float | The longitude of the point at which to perform the search.
    boundary_circle_radius = 3.4 # float | The radius of the circle (in kilometers) to limit the search to. Defaults to 50km (search) or 1km (reverse) if unspecified. (optional)
    layers = [stadiamaps.GeocodingLayer()] # List[GeocodingLayer] | A list of layers to limit the search to. (optional)
    sources = [stadiamaps.GeocodingSource()] # List[GeocodingSource] | A list of sources to limit the search to. (optional)
    boundary_country = ['boundary_country_example'] # List[str] | A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. (optional)
    boundary_gid = 'boundary_gid_example' # str | The GID of an area to limit the search to. (optional)
    size = 56 # int | The maximum number of results to return. (optional)
    lang = 'lang_example' # str | A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a `langtag` (in RFC 5646 terms) can contain script, region, etc., only the `language` portion, an ISO 639 code, will be considered. So `en-US` and `en-GB` will both be treated as English. (optional)

    try:
        # Find places and addresses near geographic coordinates (reverse geocoding).
        api_response = api_instance.reverse(point_lat, point_lon, boundary_circle_radius=boundary_circle_radius, layers=layers, sources=sources, boundary_country=boundary_country, boundary_gid=boundary_gid, size=size, lang=lang)
        print("The response of GeocodingApi->reverse:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->reverse: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point_lat** | **float**| The latitude of the point at which to perform the search. | 
 **point_lon** | **float**| The longitude of the point at which to perform the search. | 
 **boundary_circle_radius** | **float**| The radius of the circle (in kilometers) to limit the search to. Defaults to 50km (search) or 1km (reverse) if unspecified. | [optional] 
 **layers** | [**List[GeocodingLayer]**](GeocodingLayer.md)| A list of layers to limit the search to. | [optional] 
 **sources** | [**List[GeocodingSource]**](GeocodingSource.md)| A list of sources to limit the search to. | [optional] 
 **boundary_country** | [**List[str]**](str.md)| A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. | [optional] 
 **boundary_gid** | **str**| The GID of an area to limit the search to. | [optional] 
 **size** | **int**| The maximum number of results to return. | [optional] 
 **lang** | **str**| A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a &#x60;langtag&#x60; (in RFC 5646 terms) can contain script, region, etc., only the &#x60;language&#x60; portion, an ISO 639 code, will be considered. So &#x60;en-US&#x60; and &#x60;en-GB&#x60; will both be treated as English. | [optional] 

### Return type

[**GeocodeResponse**](GeocodeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A GeoJSON collection of search results. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reverse_v2**
> GeocodeResponseEnvelopePropertiesV2 reverse_v2(point_lat, point_lon, layers=layers, sources=sources, boundary_gid=boundary_gid, boundary_country=boundary_country, boundary_circle_radius=boundary_circle_radius, size=size, lang=lang)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.geocode_response_envelope_properties_v2 import GeocodeResponseEnvelopePropertiesV2
from stadiamaps.models.layer_id import LayerId
from stadiamaps.models.source_id import SourceId
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration(
    host = "https://api.stadiamaps.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    point_lat = 48.848268 # float | The latitude of the point at which to perform the search.
    point_lon = 2.294471 # float | The longitude of the point at which to perform the search.
    layers = [stadiamaps.LayerId()] # List[LayerId] | A list of layers to limit the search to. (optional)
    sources = [stadiamaps.SourceId()] # List[SourceId] | A list of sources to limit the search to. (optional)
    boundary_gid = 'boundary_gid_example' # str | The GID of a region to limit the search to.  Note: these are not stable for all datasets! For example, OSM features may be deleted and re-added with a new ID. (optional)
    boundary_country = ['boundary_country_example'] # List[str] | A list of comma-separated country codes in ISO 3116-1 alpha-2 or alpha-3 format. The search will be limited to these countries. (optional)
    boundary_circle_radius = 56 # int | The radius of the circle (in kilometers) to limit the search to.  Defaults to 1km if unspecified. (optional)
    size = 56 # int | The maximum number of items to return from a query. (optional)
    lang = 'lang_example' # str | A BCP47 language tag which specifies a preference for localization of results. There is no default value, so place names will be returned as-is, which is usually in the local language. NOTE: The Accept-Language header is also respected, and many user agents will set it automatically. (optional)

    try:
        api_response = api_instance.reverse_v2(point_lat, point_lon, layers=layers, sources=sources, boundary_gid=boundary_gid, boundary_country=boundary_country, boundary_circle_radius=boundary_circle_radius, size=size, lang=lang)
        print("The response of GeocodingApi->reverse_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->reverse_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **point_lat** | **float**| The latitude of the point at which to perform the search. | 
 **point_lon** | **float**| The longitude of the point at which to perform the search. | 
 **layers** | [**List[LayerId]**](LayerId.md)| A list of layers to limit the search to. | [optional] 
 **sources** | [**List[SourceId]**](SourceId.md)| A list of sources to limit the search to. | [optional] 
 **boundary_gid** | **str**| The GID of a region to limit the search to.  Note: these are not stable for all datasets! For example, OSM features may be deleted and re-added with a new ID. | [optional] 
 **boundary_country** | [**List[str]**](str.md)| A list of comma-separated country codes in ISO 3116-1 alpha-2 or alpha-3 format. The search will be limited to these countries. | [optional] 
 **boundary_circle_radius** | **int**| The radius of the circle (in kilometers) to limit the search to.  Defaults to 1km if unspecified. | [optional] 
 **size** | **int**| The maximum number of items to return from a query. | [optional] 
 **lang** | **str**| A BCP47 language tag which specifies a preference for localization of results. There is no default value, so place names will be returned as-is, which is usually in the local language. NOTE: The Accept-Language header is also respected, and many user agents will set it automatically. | [optional] 

### Return type

[**GeocodeResponseEnvelopePropertiesV2**](GeocodeResponseEnvelopePropertiesV2.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A GeoJSON FeatureCollection with the results |  -  |
**400** | A response with a description of why the request is malformed |  -  |
**500** | A response with a description of what went wrong internally |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> GeocodeResponse search(text, focus_point_lat=focus_point_lat, focus_point_lon=focus_point_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lat=boundary_rect_max_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_max_lon=boundary_rect_max_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_radius=boundary_circle_radius, boundary_country=boundary_country, boundary_gid=boundary_gid, layers=layers, sources=sources, size=size, lang=lang)

Search for location and other info using a place name or address (forward geocoding).

The search endpoint lets you search for addresses, points of interest, and administrative areas. This is most commonly used for forward geocoding applications where you need to find the geographic coordinates of an address.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.geocode_response import GeocodeResponse
from stadiamaps.models.geocoding_layer import GeocodingLayer
from stadiamaps.models.geocoding_source import GeocodingSource
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration(
    host = "https://api.stadiamaps.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    text = 'text_example' # str | The place name (address, venue name, etc.) to search for.
    focus_point_lat = 3.4 # float | The latitude of the point to focus the search on. This will bias results toward the focus point. Requires `focus.point.lon`. (optional)
    focus_point_lon = 3.4 # float | The longitude of the point to focus the search on. This will bias results toward the focus point. Requires `focus.point.lat`. (optional)
    boundary_rect_min_lat = 3.4 # float | Defines the min latitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_rect_max_lat = 3.4 # float | Defines the max latitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_rect_min_lon = 3.4 # float | Defines the min longitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_rect_max_lon = 3.4 # float | Defines the max longitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_circle_lat = 3.4 # float | The latitude of the center of a circle to limit the search to. Requires `boundary.circle.lon`. (optional)
    boundary_circle_lon = 3.4 # float | The longitude of the center of a circle to limit the search to. Requires `boundary.circle.lat`. (optional)
    boundary_circle_radius = 3.4 # float | The radius of the circle (in kilometers) to limit the search to. Defaults to 50km (search) or 1km (reverse) if unspecified. (optional)
    boundary_country = ['boundary_country_example'] # List[str] | A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. (optional)
    boundary_gid = 'boundary_gid_example' # str | The GID of an area to limit the search to. (optional)
    layers = [stadiamaps.GeocodingLayer()] # List[GeocodingLayer] | A list of layers to limit the search to. (optional)
    sources = [stadiamaps.GeocodingSource()] # List[GeocodingSource] | A list of sources to limit the search to. (optional)
    size = 56 # int | The maximum number of results to return. (optional)
    lang = 'lang_example' # str | A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a `langtag` (in RFC 5646 terms) can contain script, region, etc., only the `language` portion, an ISO 639 code, will be considered. So `en-US` and `en-GB` will both be treated as English. (optional)

    try:
        # Search for location and other info using a place name or address (forward geocoding).
        api_response = api_instance.search(text, focus_point_lat=focus_point_lat, focus_point_lon=focus_point_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lat=boundary_rect_max_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_max_lon=boundary_rect_max_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_radius=boundary_circle_radius, boundary_country=boundary_country, boundary_gid=boundary_gid, layers=layers, sources=sources, size=size, lang=lang)
        print("The response of GeocodingApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| The place name (address, venue name, etc.) to search for. | 
 **focus_point_lat** | **float**| The latitude of the point to focus the search on. This will bias results toward the focus point. Requires &#x60;focus.point.lon&#x60;. | [optional] 
 **focus_point_lon** | **float**| The longitude of the point to focus the search on. This will bias results toward the focus point. Requires &#x60;focus.point.lat&#x60;. | [optional] 
 **boundary_rect_min_lat** | **float**| Defines the min latitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_rect_max_lat** | **float**| Defines the max latitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_rect_min_lon** | **float**| Defines the min longitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_rect_max_lon** | **float**| Defines the max longitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_circle_lat** | **float**| The latitude of the center of a circle to limit the search to. Requires &#x60;boundary.circle.lon&#x60;. | [optional] 
 **boundary_circle_lon** | **float**| The longitude of the center of a circle to limit the search to. Requires &#x60;boundary.circle.lat&#x60;. | [optional] 
 **boundary_circle_radius** | **float**| The radius of the circle (in kilometers) to limit the search to. Defaults to 50km (search) or 1km (reverse) if unspecified. | [optional] 
 **boundary_country** | [**List[str]**](str.md)| A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. | [optional] 
 **boundary_gid** | **str**| The GID of an area to limit the search to. | [optional] 
 **layers** | [**List[GeocodingLayer]**](GeocodingLayer.md)| A list of layers to limit the search to. | [optional] 
 **sources** | [**List[GeocodingSource]**](GeocodingSource.md)| A list of sources to limit the search to. | [optional] 
 **size** | **int**| The maximum number of results to return. | [optional] 
 **lang** | **str**| A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a &#x60;langtag&#x60; (in RFC 5646 terms) can contain script, region, etc., only the &#x60;language&#x60; portion, an ISO 639 code, will be considered. So &#x60;en-US&#x60; and &#x60;en-GB&#x60; will both be treated as English. | [optional] 

### Return type

[**GeocodeResponse**](GeocodeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A GeoJSON collection of search results. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_bulk**
> List[BulkSearchResponse] search_bulk(bulk_request=bulk_request)

Quickly run a batch of geocoding queries against the search or structured search endpoints.

The batch endpoint lets you specify many search or structured search requests at once. Once received, all requests will be processed internally on our infrastructure, improving throughput when you need to do a lot of queries.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.bulk_request import BulkRequest
from stadiamaps.models.bulk_search_response import BulkSearchResponse
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration(
    host = "https://api.stadiamaps.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    bulk_request = [stadiamaps.BulkRequest()] # List[BulkRequest] |  (optional)

    try:
        # Quickly run a batch of geocoding queries against the search or structured search endpoints.
        api_response = api_instance.search_bulk(bulk_request=bulk_request)
        print("The response of GeocodingApi->search_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->search_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_request** | [**List[BulkRequest]**](BulkRequest.md)|  | [optional] 

### Return type

[**List[BulkSearchResponse]**](BulkSearchResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of the individual query responses, each annotated with a status code. Individual requests may fail but this endpoint will still return all results. Responses will be in the same order as the input. |  -  |
**400** | Bad request; more details will be included |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_structured**
> GeocodeResponse search_structured(address=address, neighbourhood=neighbourhood, borough=borough, locality=locality, county=county, region=region, postalcode=postalcode, country=country, focus_point_lat=focus_point_lat, focus_point_lon=focus_point_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lat=boundary_rect_max_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_max_lon=boundary_rect_max_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_radius=boundary_circle_radius, boundary_country=boundary_country, boundary_gid=boundary_gid, layers=layers, sources=sources, size=size, lang=lang)

Find locations matching components (structured forward geocoding).

The structured search endpoint lets you search for addresses, points of interest, and administrative areas. Rather than a single string which the API must infer meaning from, the structured search endpoint allows you to specify the known components upfront, which is useful in many forward geocoding workflows.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.geocode_response import GeocodeResponse
from stadiamaps.models.geocoding_layer import GeocodingLayer
from stadiamaps.models.geocoding_source import GeocodingSource
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration(
    host = "https://api.stadiamaps.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    address = 'address_example' # str | A street name, optionally with a house number. (optional)
    neighbourhood = 'neighbourhood_example' # str | Varies by area, but has a locally specific meaning (NOT always an official administrative unit). (optional)
    borough = 'borough_example' # str | A unit within a city (not widely used, but present in places like NYC and Mexico City). (optional)
    locality = 'locality_example' # str | The city, village, town, etc. that the place/address is part of. (optional)
    county = 'county_example' # str | Administrative divisions between localities and regions. Not commonly used as input to structured geocoding. (optional)
    region = 'region_example' # str | Typically the first administrative division within a country. For example, a US state or a Canadian province. (optional)
    postalcode = 'postalcode_example' # str | A mail sorting code. (optional)
    country = 'country_example' # str | A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. (optional)
    focus_point_lat = 3.4 # float | The latitude of the point to focus the search on. This will bias results toward the focus point. Requires `focus.point.lon`. (optional)
    focus_point_lon = 3.4 # float | The longitude of the point to focus the search on. This will bias results toward the focus point. Requires `focus.point.lat`. (optional)
    boundary_rect_min_lat = 3.4 # float | Defines the min latitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_rect_max_lat = 3.4 # float | Defines the max latitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_rect_min_lon = 3.4 # float | Defines the min longitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_rect_max_lon = 3.4 # float | Defines the max longitude component of a bounding box to limit the search to. Requires all other `boundary.rect` parameters to be specified. (optional)
    boundary_circle_lat = 3.4 # float | The latitude of the center of a circle to limit the search to. Requires `boundary.circle.lon`. (optional)
    boundary_circle_lon = 3.4 # float | The longitude of the center of a circle to limit the search to. Requires `boundary.circle.lat`. (optional)
    boundary_circle_radius = 3.4 # float | The radius of the circle (in kilometers) to limit the search to. Defaults to 50km (search) or 1km (reverse) if unspecified. (optional)
    boundary_country = ['boundary_country_example'] # List[str] | A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. (optional)
    boundary_gid = 'boundary_gid_example' # str | The GID of an area to limit the search to. (optional)
    layers = [stadiamaps.GeocodingLayer()] # List[GeocodingLayer] | A list of layers to limit the search to. (optional)
    sources = [stadiamaps.GeocodingSource()] # List[GeocodingSource] | A list of sources to limit the search to. (optional)
    size = 56 # int | The maximum number of results to return. (optional)
    lang = 'lang_example' # str | A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a `langtag` (in RFC 5646 terms) can contain script, region, etc., only the `language` portion, an ISO 639 code, will be considered. So `en-US` and `en-GB` will both be treated as English. (optional)

    try:
        # Find locations matching components (structured forward geocoding).
        api_response = api_instance.search_structured(address=address, neighbourhood=neighbourhood, borough=borough, locality=locality, county=county, region=region, postalcode=postalcode, country=country, focus_point_lat=focus_point_lat, focus_point_lon=focus_point_lon, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_max_lat=boundary_rect_max_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_max_lon=boundary_rect_max_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_radius=boundary_circle_radius, boundary_country=boundary_country, boundary_gid=boundary_gid, layers=layers, sources=sources, size=size, lang=lang)
        print("The response of GeocodingApi->search_structured:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->search_structured: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **address** | **str**| A street name, optionally with a house number. | [optional] 
 **neighbourhood** | **str**| Varies by area, but has a locally specific meaning (NOT always an official administrative unit). | [optional] 
 **borough** | **str**| A unit within a city (not widely used, but present in places like NYC and Mexico City). | [optional] 
 **locality** | **str**| The city, village, town, etc. that the place/address is part of. | [optional] 
 **county** | **str**| Administrative divisions between localities and regions. Not commonly used as input to structured geocoding. | [optional] 
 **region** | **str**| Typically the first administrative division within a country. For example, a US state or a Canadian province. | [optional] 
 **postalcode** | **str**| A mail sorting code. | [optional] 
 **country** | **str**| A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. | [optional] 
 **focus_point_lat** | **float**| The latitude of the point to focus the search on. This will bias results toward the focus point. Requires &#x60;focus.point.lon&#x60;. | [optional] 
 **focus_point_lon** | **float**| The longitude of the point to focus the search on. This will bias results toward the focus point. Requires &#x60;focus.point.lat&#x60;. | [optional] 
 **boundary_rect_min_lat** | **float**| Defines the min latitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_rect_max_lat** | **float**| Defines the max latitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_rect_min_lon** | **float**| Defines the min longitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_rect_max_lon** | **float**| Defines the max longitude component of a bounding box to limit the search to. Requires all other &#x60;boundary.rect&#x60; parameters to be specified. | [optional] 
 **boundary_circle_lat** | **float**| The latitude of the center of a circle to limit the search to. Requires &#x60;boundary.circle.lon&#x60;. | [optional] 
 **boundary_circle_lon** | **float**| The longitude of the center of a circle to limit the search to. Requires &#x60;boundary.circle.lat&#x60;. | [optional] 
 **boundary_circle_radius** | **float**| The radius of the circle (in kilometers) to limit the search to. Defaults to 50km (search) or 1km (reverse) if unspecified. | [optional] 
 **boundary_country** | [**List[str]**](str.md)| A list of country codes in ISO 3116-1 alpha-2 or alpha-3 format. | [optional] 
 **boundary_gid** | **str**| The GID of an area to limit the search to. | [optional] 
 **layers** | [**List[GeocodingLayer]**](GeocodingLayer.md)| A list of layers to limit the search to. | [optional] 
 **sources** | [**List[GeocodingSource]**](GeocodingSource.md)| A list of sources to limit the search to. | [optional] 
 **size** | **int**| The maximum number of results to return. | [optional] 
 **lang** | **str**| A BCP47 language tag which specifies a preference for localization of results. By default, results are in the default locale of the source data, but specifying a language will attempt to localize the results. Note that while a &#x60;langtag&#x60; (in RFC 5646 terms) can contain script, region, etc., only the &#x60;language&#x60; portion, an ISO 639 code, will be considered. So &#x60;en-US&#x60; and &#x60;en-GB&#x60; will both be treated as English. | [optional] 

### Return type

[**GeocodeResponse**](GeocodeResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A GeoJSON collection of search results. |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_v2**
> GeocodeResponseEnvelopePropertiesV2 search_v2(text, focus_point_lat=focus_point_lat, focus_point_lon=focus_point_lon, layers=layers, sources=sources, boundary_gid=boundary_gid, boundary_country=boundary_country, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_max_lat=boundary_rect_max_lat, boundary_rect_max_lon=boundary_rect_max_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_radius=boundary_circle_radius, size=size, lang=lang)

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.geocode_response_envelope_properties_v2 import GeocodeResponseEnvelopePropertiesV2
from stadiamaps.models.layer_id import LayerId
from stadiamaps.models.source_id import SourceId
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration(
    host = "https://api.stadiamaps.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    text = '1600 Pennsylvania Ave NW' # str | The text to search for (the start of an address, place name, etc.).
    focus_point_lat = 3.4 # float | The latitude of a focus point.  If provided (along with longitude), the search results should be more locally relevant. (optional)
    focus_point_lon = 3.4 # float | The longitude of a focus point.  If provided (along with longitude), the search results should be more locally relevant. (optional)
    layers = [stadiamaps.LayerId()] # List[LayerId] | A list of layers to limit the search to. (optional)
    sources = [stadiamaps.SourceId()] # List[SourceId] | A list of sources to limit the search to. (optional)
    boundary_gid = 'boundary_gid_example' # str | The GID of a region to limit the search to.  Note: these are not stable for all datasets! For example, OSM features may be deleted and re-added with a new ID. (optional)
    boundary_country = ['boundary_country_example'] # List[str] | A list of comma-separated country codes in ISO 3116-1 alpha-2 or alpha-3 format. The search will be limited to these countries. (optional)
    boundary_rect_min_lat = 3.4 # float | The minimum latitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. (optional)
    boundary_rect_min_lon = 3.4 # float | The minimum longitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. (optional)
    boundary_rect_max_lat = 3.4 # float | The maximum latitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. (optional)
    boundary_rect_max_lon = 3.4 # float | The maximum longitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. (optional)
    boundary_circle_lat = 3.4 # float | The latitude of the center of a circle to limit the search to.  NOTE: Requires boundary.circle.lon. (optional)
    boundary_circle_lon = 3.4 # float | The longitude of the center of a circle to limit the search to.  NOTE: Requires boundary.circle.lat. (optional)
    boundary_circle_radius = 56 # int | The radius of the circle (in kilometers) to limit the search to.  NOTE: Requires the other boundary.circle parameters to take effect. Defaults to 50km if unspecified. (optional)
    size = 56 # int | The maximum number of items to return from a query. (optional)
    lang = 'lang_example' # str | A BCP47 language tag which specifies a preference for localization of results. There is no default value, so place names will be returned as-is, which is usually in the local language. NOTE: The Accept-Language header is also respected, and many user agents will set it automatically. (optional)

    try:
        api_response = api_instance.search_v2(text, focus_point_lat=focus_point_lat, focus_point_lon=focus_point_lon, layers=layers, sources=sources, boundary_gid=boundary_gid, boundary_country=boundary_country, boundary_rect_min_lat=boundary_rect_min_lat, boundary_rect_min_lon=boundary_rect_min_lon, boundary_rect_max_lat=boundary_rect_max_lat, boundary_rect_max_lon=boundary_rect_max_lon, boundary_circle_lat=boundary_circle_lat, boundary_circle_lon=boundary_circle_lon, boundary_circle_radius=boundary_circle_radius, size=size, lang=lang)
        print("The response of GeocodingApi->search_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeocodingApi->search_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **text** | **str**| The text to search for (the start of an address, place name, etc.). | 
 **focus_point_lat** | **float**| The latitude of a focus point.  If provided (along with longitude), the search results should be more locally relevant. | [optional] 
 **focus_point_lon** | **float**| The longitude of a focus point.  If provided (along with longitude), the search results should be more locally relevant. | [optional] 
 **layers** | [**List[LayerId]**](LayerId.md)| A list of layers to limit the search to. | [optional] 
 **sources** | [**List[SourceId]**](SourceId.md)| A list of sources to limit the search to. | [optional] 
 **boundary_gid** | **str**| The GID of a region to limit the search to.  Note: these are not stable for all datasets! For example, OSM features may be deleted and re-added with a new ID. | [optional] 
 **boundary_country** | [**List[str]**](str.md)| A list of comma-separated country codes in ISO 3116-1 alpha-2 or alpha-3 format. The search will be limited to these countries. | [optional] 
 **boundary_rect_min_lat** | **float**| The minimum latitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. | [optional] 
 **boundary_rect_min_lon** | **float**| The minimum longitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. | [optional] 
 **boundary_rect_max_lat** | **float**| The maximum latitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. | [optional] 
 **boundary_rect_max_lon** | **float**| The maximum longitude component of a search bounding box.  NOTE: Requires all other boundary.rect parameters to be specified. | [optional] 
 **boundary_circle_lat** | **float**| The latitude of the center of a circle to limit the search to.  NOTE: Requires boundary.circle.lon. | [optional] 
 **boundary_circle_lon** | **float**| The longitude of the center of a circle to limit the search to.  NOTE: Requires boundary.circle.lat. | [optional] 
 **boundary_circle_radius** | **int**| The radius of the circle (in kilometers) to limit the search to.  NOTE: Requires the other boundary.circle parameters to take effect. Defaults to 50km if unspecified. | [optional] 
 **size** | **int**| The maximum number of items to return from a query. | [optional] 
 **lang** | **str**| A BCP47 language tag which specifies a preference for localization of results. There is no default value, so place names will be returned as-is, which is usually in the local language. NOTE: The Accept-Language header is also respected, and many user agents will set it automatically. | [optional] 

### Return type

[**GeocodeResponseEnvelopePropertiesV2**](GeocodeResponseEnvelopePropertiesV2.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A GeoJSON FeatureCollection with the results |  -  |
**400** | A response with a description of why the request is malformed |  -  |
**500** | A response with a description of what went wrong internally |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

