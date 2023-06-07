<a id="__pageTop"></a>
# stadiamaps.apis.tags.geocoding_api.GeocodingApi

All URIs are relative to *https://api.stadiamaps.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](#autocomplete) | **get** /geocoding/v1/autocomplete | Search and geocode quickly based on partial input.
[**place**](#place) | **get** /geocoding/v1/place | Retrieve details of a place using its GID.
[**reverse**](#reverse) | **get** /geocoding/v1/reverse | Find places and addresses near geographic coordinates (reverse geocoding).
[**search**](#search) | **get** /geocoding/v1/search | Search for location and other info using a place name or address (forward geocoding).
[**search_structured**](#search_structured) | **get** /geocoding/v1/search/structured | Find locations matching components (structured forward geocoding).

# **autocomplete**
<a id="autocomplete"></a>
> PeliasResponse autocomplete(text)

Search and geocode quickly based on partial input.

Autocomplete enables interactive search-as-you-type user experiences, suggesting places as you type, along with information that will help your users find the correct place quickly.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import geocoding_api
from stadiamaps.model.pelias_response import PeliasResponse
from stadiamaps.model.pelias_layer import PeliasLayer
from stadiamaps.model.pelias_source import PeliasSource
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geocoding_api.GeocodingApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'text': "1600 Pennsylvania Ave NW",
    }
    try:
        # Search and geocode quickly based on partial input.
        api_response = api_instance.autocomplete(
            query_params=query_params,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeocodingApi->autocomplete: %s\n" % e)

    # example passing only optional values
    query_params = {
        'text': "1600 Pennsylvania Ave NW",
        'focus.point.lat': 3.14,
        'focus.point.lon': 3.14,
        'boundary.rect.min_lat': 3.14,
        'boundary.rect.max_lat': 3.14,
        'boundary.rect.min_lon': 3.14,
        'boundary.rect.max_lon': 3.14,
        'boundary.circle.lat': 3.14,
        'boundary.circle.lon': 3.14,
        'boundary.circle.radius': 3.14,
        'boundary.country': [
        "boundary.country_example"
    ],
        'boundary.gid': "boundary.gid_example",
        'layers': [
        PeliasLayer("venue")
    ],
        'sources': [
        PeliasSource("openstreetmap")
    ],
        'size': 1,
        'lang': "lang_example",
    }
    try:
        # Search and geocode quickly based on partial input.
        api_response = api_instance.autocomplete(
            query_params=query_params,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeocodingApi->autocomplete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
text | TextSchema | | 
focus.point.lat | FocusPointLatSchema | | optional
focus.point.lon | FocusPointLonSchema | | optional
boundary.rect.min_lat | BoundaryRectMinLatSchema | | optional
boundary.rect.max_lat | BoundaryRectMaxLatSchema | | optional
boundary.rect.min_lon | BoundaryRectMinLonSchema | | optional
boundary.rect.max_lon | BoundaryRectMaxLonSchema | | optional
boundary.circle.lat | BoundaryCircleLatSchema | | optional
boundary.circle.lon | BoundaryCircleLonSchema | | optional
boundary.circle.radius | BoundaryCircleRadiusSchema | | optional
boundary.country | BoundaryCountrySchema | | optional
boundary.gid | BoundaryGidSchema | | optional
layers | LayersSchema | | optional
sources | SourcesSchema | | optional
size | SizeSchema | | optional
lang | LangSchema | | optional


# TextSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FocusPointLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# FocusPointLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMinLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMaxLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMinLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMaxLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCircleLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCircleLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCircleRadiusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCountrySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# BoundaryGidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LayersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) | [**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) | [**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) |  | 

# SourcesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) | [**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) | [**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) |  | 

# SizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#autocomplete.ApiResponseFor200) | Returns the collection of autocomplete results.
400 | [ApiResponseFor400](#autocomplete.ApiResponseFor400) | Bad request

#### autocomplete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PeliasResponse**](../../models/PeliasResponse.md) |  | 


#### autocomplete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **place**
<a id="place"></a>
> PeliasResponse place(ids)

Retrieve details of a place using its GID.

Many search result components include an associated GID field (for example, an address may have a `localadmin_gid`). The place endpoint lets you look up these places directly by ID. Note that these IDs are not stable for all sources. See the [online documentation](https://docs.stadiamaps.com/geocoding-search-autocomplete/place-lookup/) for details.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import geocoding_api
from stadiamaps.model.pelias_response import PeliasResponse
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geocoding_api.GeocodingApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'ids': [
        "ids_example"
    ],
    }
    try:
        # Retrieve details of a place using its GID.
        api_response = api_instance.place(
            query_params=query_params,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeocodingApi->place: %s\n" % e)

    # example passing only optional values
    query_params = {
        'ids': [
        "ids_example"
    ],
        'lang': "lang_example",
    }
    try:
        # Retrieve details of a place using its GID.
        api_response = api_instance.place(
            query_params=query_params,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeocodingApi->place: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
ids | IdsSchema | | 
lang | LangSchema | | optional


# IdsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# LangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#place.ApiResponseFor200) | Returns the collection of search results.
400 | [ApiResponseFor400](#place.ApiResponseFor400) | Bad request

#### place.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PeliasResponse**](../../models/PeliasResponse.md) |  | 


#### place.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **reverse**
<a id="reverse"></a>
> PeliasResponse reverse(point_latpoint_lon)

Find places and addresses near geographic coordinates (reverse geocoding).

Reverse geocoding and search finds places and addresses near any geographic coordinates.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import geocoding_api
from stadiamaps.model.pelias_response import PeliasResponse
from stadiamaps.model.pelias_layer import PeliasLayer
from stadiamaps.model.pelias_source import PeliasSource
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geocoding_api.GeocodingApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'point.lat': 48.848268,
        'point.lon': 2.294471,
    }
    try:
        # Find places and addresses near geographic coordinates (reverse geocoding).
        api_response = api_instance.reverse(
            query_params=query_params,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeocodingApi->reverse: %s\n" % e)

    # example passing only optional values
    query_params = {
        'point.lat': 48.848268,
        'point.lon': 2.294471,
        'boundary.circle.radius': 3.14,
        'layers': [
        PeliasLayer("venue")
    ],
        'sources': [
        PeliasSource("openstreetmap")
    ],
        'boundary.country': [
        "boundary.country_example"
    ],
        'boundary.gid': "boundary.gid_example",
        'size': 1,
        'lang': "lang_example",
    }
    try:
        # Find places and addresses near geographic coordinates (reverse geocoding).
        api_response = api_instance.reverse(
            query_params=query_params,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeocodingApi->reverse: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
point.lat | PointLatSchema | | 
point.lon | PointLonSchema | | 
boundary.circle.radius | BoundaryCircleRadiusSchema | | optional
layers | LayersSchema | | optional
sources | SourcesSchema | | optional
boundary.country | BoundaryCountrySchema | | optional
boundary.gid | BoundaryGidSchema | | optional
size | SizeSchema | | optional
lang | LangSchema | | optional


# PointLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# PointLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCircleRadiusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# LayersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) | [**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) | [**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) |  | 

# SourcesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) | [**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) | [**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) |  | 

# BoundaryCountrySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# BoundaryGidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#reverse.ApiResponseFor200) | Returns the collection of search results.
400 | [ApiResponseFor400](#reverse.ApiResponseFor400) | Bad request

#### reverse.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PeliasResponse**](../../models/PeliasResponse.md) |  | 


#### reverse.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search**
<a id="search"></a>
> PeliasResponse search(text)

Search for location and other info using a place name or address (forward geocoding).

The search endpoint lets you search for addresses, points of interest, and administrative areas. This is most commonly used for forward geocoding applications where you need to find the geographic coordinates of an address.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import geocoding_api
from stadiamaps.model.pelias_response import PeliasResponse
from stadiamaps.model.pelias_layer import PeliasLayer
from stadiamaps.model.pelias_source import PeliasSource
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geocoding_api.GeocodingApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'text': "1600 Pennsylvania Ave NW",
    }
    try:
        # Search for location and other info using a place name or address (forward geocoding).
        api_response = api_instance.search(
            query_params=query_params,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeocodingApi->search: %s\n" % e)

    # example passing only optional values
    query_params = {
        'text': "1600 Pennsylvania Ave NW",
        'focus.point.lat': 3.14,
        'focus.point.lon': 3.14,
        'boundary.rect.min_lat': 3.14,
        'boundary.rect.max_lat': 3.14,
        'boundary.rect.min_lon': 3.14,
        'boundary.rect.max_lon': 3.14,
        'boundary.circle.lat': 3.14,
        'boundary.circle.lon': 3.14,
        'boundary.circle.radius': 3.14,
        'boundary.country': [
        "boundary.country_example"
    ],
        'boundary.gid': "boundary.gid_example",
        'layers': [
        PeliasLayer("venue")
    ],
        'sources': [
        PeliasSource("openstreetmap")
    ],
        'size': 1,
        'lang': "lang_example",
    }
    try:
        # Search for location and other info using a place name or address (forward geocoding).
        api_response = api_instance.search(
            query_params=query_params,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeocodingApi->search: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
text | TextSchema | | 
focus.point.lat | FocusPointLatSchema | | optional
focus.point.lon | FocusPointLonSchema | | optional
boundary.rect.min_lat | BoundaryRectMinLatSchema | | optional
boundary.rect.max_lat | BoundaryRectMaxLatSchema | | optional
boundary.rect.min_lon | BoundaryRectMinLonSchema | | optional
boundary.rect.max_lon | BoundaryRectMaxLonSchema | | optional
boundary.circle.lat | BoundaryCircleLatSchema | | optional
boundary.circle.lon | BoundaryCircleLonSchema | | optional
boundary.circle.radius | BoundaryCircleRadiusSchema | | optional
boundary.country | BoundaryCountrySchema | | optional
boundary.gid | BoundaryGidSchema | | optional
layers | LayersSchema | | optional
sources | SourcesSchema | | optional
size | SizeSchema | | optional
lang | LangSchema | | optional


# TextSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FocusPointLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# FocusPointLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMinLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMaxLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMinLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMaxLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCircleLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCircleLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCircleRadiusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCountrySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# BoundaryGidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LayersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) | [**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) | [**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) |  | 

# SourcesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) | [**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) | [**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) |  | 

# SizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search.ApiResponseFor200) | Returns the collection of search results.
400 | [ApiResponseFor400](#search.ApiResponseFor400) | Bad request

#### search.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PeliasResponse**](../../models/PeliasResponse.md) |  | 


#### search.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_structured**
<a id="search_structured"></a>
> PeliasResponse search_structured()

Find locations matching components (structured forward geocoding).

The structured search endpoint lets you search for addresses, points of interest, and administrative areas. Rather than a single string which the API must infer meaning from, the structured search endpoint allows you to specify the known components upfront, which is useful in many forward geocoding workflows.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import geocoding_api
from stadiamaps.model.pelias_response import PeliasResponse
from stadiamaps.model.pelias_layer import PeliasLayer
from stadiamaps.model.pelias_source import PeliasSource
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
configuration.api_key['ApiKeyAuth'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'
# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = geocoding_api.GeocodingApi(api_client)

    # example passing only optional values
    query_params = {
        'address': "11 Wall Street",
        'neighbourhood': "Financial District",
        'borough': "Manhattan",
        'locality': "New York",
        'county': "New York County",
        'region': "New York",
        'postalcode': "10005",
        'country': "USA",
        'focus.point.lat': 3.14,
        'focus.point.lon': 3.14,
        'boundary.rect.min_lat': 3.14,
        'boundary.rect.max_lat': 3.14,
        'boundary.rect.min_lon': 3.14,
        'boundary.rect.max_lon': 3.14,
        'boundary.circle.lat': 3.14,
        'boundary.circle.lon': 3.14,
        'boundary.circle.radius': 3.14,
        'boundary.country': [
        "boundary.country_example"
    ],
        'boundary.gid': "boundary.gid_example",
        'layers': [
        PeliasLayer("venue")
    ],
        'sources': [
        PeliasSource("openstreetmap")
    ],
        'size': 1,
        'lang': "lang_example",
    }
    try:
        # Find locations matching components (structured forward geocoding).
        api_response = api_instance.search_structured(
            query_params=query_params,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeocodingApi->search_structured: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
address | AddressSchema | | optional
neighbourhood | NeighbourhoodSchema | | optional
borough | BoroughSchema | | optional
locality | LocalitySchema | | optional
county | CountySchema | | optional
region | RegionSchema | | optional
postalcode | PostalcodeSchema | | optional
country | CountrySchema | | optional
focus.point.lat | FocusPointLatSchema | | optional
focus.point.lon | FocusPointLonSchema | | optional
boundary.rect.min_lat | BoundaryRectMinLatSchema | | optional
boundary.rect.max_lat | BoundaryRectMaxLatSchema | | optional
boundary.rect.min_lon | BoundaryRectMinLonSchema | | optional
boundary.rect.max_lon | BoundaryRectMaxLonSchema | | optional
boundary.circle.lat | BoundaryCircleLatSchema | | optional
boundary.circle.lon | BoundaryCircleLonSchema | | optional
boundary.circle.radius | BoundaryCircleRadiusSchema | | optional
boundary.country | BoundaryCountrySchema | | optional
boundary.gid | BoundaryGidSchema | | optional
layers | LayersSchema | | optional
sources | SourcesSchema | | optional
size | SizeSchema | | optional
lang | LangSchema | | optional


# AddressSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# NeighbourhoodSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# BoroughSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LocalitySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CountySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# RegionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# PostalcodeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CountrySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# FocusPointLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# FocusPointLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMinLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMaxLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMinLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryRectMaxLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCircleLatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCircleLonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCircleRadiusSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# BoundaryCountrySchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# BoundaryGidSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LayersSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) | [**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) | [**PeliasLayer**]({{complexTypePrefix}}PeliasLayer.md) |  | 

# SourcesSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) | [**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) | [**PeliasSource**]({{complexTypePrefix}}PeliasSource.md) |  | 

# SizeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# LangSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_structured.ApiResponseFor200) | Returns the collection of search results.
400 | [ApiResponseFor400](#search_structured.ApiResponseFor400) | Bad request

#### search_structured.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PeliasResponse**](../../models/PeliasResponse.md) |  | 


#### search_structured.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

