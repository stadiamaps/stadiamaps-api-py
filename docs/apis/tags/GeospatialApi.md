<a id="__pageTop"></a>
# stadiamaps.apis.tags.geospatial_api.GeospatialApi

All URIs are relative to *https://api.stadiamaps.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elevation**](#elevation) | **post** /elevation/v1 | Get the elevation profile along a polyline or at a point.
[**tz_lookup**](#tz_lookup) | **get** /tz/lookup/v1 | Get the current time zone information for any point on earth.

# **elevation**
<a id="elevation"></a>
> HeightResponse elevation()

Get the elevation profile along a polyline or at a point.

The Stadia elevation API allows you to get the elevation of any point on earth. You can pass either a simple set of points or a Google encoded polyline string. This pairs well with our routing APIs, so you can generate an elevation profile for your next bike or run.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import geospatial_api
from stadiamaps.model.height_request import HeightRequest
from stadiamaps.model.height_response import HeightResponse
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
    api_instance = geospatial_api.GeospatialApi(api_client)

    # example passing only optional values
    body = HeightRequest(
        id="kesklinn",
        shape=[
            Coordinate(
                lat=59.436884,
                lon=24.742595,
            )
        ],
        encoded_polyline="encoded_polyline_example",
        shape_format="polyline6",
        range=False,
        height_precision=0,
    )
    try:
        # Get the elevation profile along a polyline or at a point.
        api_response = api_instance.elevation(
            body=body,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeospatialApi->elevation: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HeightRequest**](../../models/HeightRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#elevation.ApiResponseFor200) | Returns a list of elevations along the polyline, in meters.

#### elevation.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HeightResponse**](../../models/HeightResponse.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **tz_lookup**
<a id="tz_lookup"></a>
> TzResponse tz_lookup(latlng)

Get the current time zone information for any point on earth.

The Stadia TZ API provides time zone information, as well as information about any special offset (such as DST) in effect based on the latest IANA TZDB. Note that this API may not be accurate for timestamps in the past and does not claim to report precise nautical times in the open ocean beyond territorial waters.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import geospatial_api
from stadiamaps.model.tz_response import TzResponse
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
    api_instance = geospatial_api.GeospatialApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'lat': -90,
        'lng': -180,
    }
    try:
        # Get the current time zone information for any point on earth.
        api_response = api_instance.tz_lookup(
            query_params=query_params,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeospatialApi->tz_lookup: %s\n" % e)

    # example passing only optional values
    query_params = {
        'lat': -90,
        'lng': -180,
        'timestamp': 0,
    }
    try:
        # Get the current time zone information for any point on earth.
        api_response = api_instance.tz_lookup(
            query_params=query_params,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling GeospatialApi->tz_lookup: %s\n" % e)
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
lat | LatSchema | | 
lng | LngSchema | | 
timestamp | TimestampSchema | | optional


# LatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# LngSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | value must be a 64 bit float

# TimestampSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 64 bit integer

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#tz_lookup.ApiResponseFor200) | Returns the time zone metadata.
404 | [ApiResponseFor404](#tz_lookup.ApiResponseFor404) | Time zone not found

#### tz_lookup.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TzResponse**](../../models/TzResponse.md) |  | 


#### tz_lookup.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

