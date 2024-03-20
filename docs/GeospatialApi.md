# stadiamaps.GeospatialApi

All URIs are relative to *https://api.stadiamaps.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**elevation**](GeospatialApi.md#elevation) | **POST** /elevation/v1 | Get the elevation profile along a polyline or at a point.
[**tz_lookup**](GeospatialApi.md#tz_lookup) | **GET** /tz/lookup/v1 | Get the current time zone information for any point on earth.


# **elevation**
> HeightResponse elevation(height_request=height_request)

Get the elevation profile along a polyline or at a point.

The Stadia elevation API allows you to get the elevation of any point on earth. You can pass either a simple set of points or a Google encoded polyline string. This pairs well with our routing APIs, so you can generate an elevation profile for your next bike or run.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.height_request import HeightRequest
from stadiamaps.models.height_response import HeightResponse
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
    api_instance = stadiamaps.GeospatialApi(api_client)
    height_request = stadiamaps.HeightRequest() # HeightRequest |  (optional)

    try:
        # Get the elevation profile along a polyline or at a point.
        api_response = api_instance.elevation(height_request=height_request)
        print("The response of GeospatialApi->elevation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeospatialApi->elevation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **height_request** | [**HeightRequest**](HeightRequest.md)|  | [optional] 

### Return type

[**HeightResponse**](HeightResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns a list of elevations along the polyline, in meters. |  -  |
**400** | Bad request; more details will be included |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tz_lookup**
> TzResponse tz_lookup(lat, lng, timestamp=timestamp)

Get the current time zone information for any point on earth.

The Stadia TZ API provides time zone information, as well as information about any special offset (such as DST) in effect based on the latest IANA TZDB. Note that this API may not be accurate for timestamps in the past and does not claim to report precise nautical times in the open ocean beyond territorial waters.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.tz_response import TzResponse
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
    api_instance = stadiamaps.GeospatialApi(api_client)
    lat = 3.4 # float | The latitude of the point you are interested in.
    lng = 3.4 # float | The longitude of the point you are interested in.
    timestamp = 56 # int | The UNIX timestamp at which the UTC and DST offsets will be calculated. This defaults to the present time. This endpoint is not necessarily guaranteed to be accurate for timestamps that occurred in the past. Time zone geographic boundaries change over time, so if the point you are querying for was previously in a different time zone, historical results will not be accurate. If, however, the point has been in the same geographic time zone for a very long time (ex: `America/New_York`), the historical data may be accurate for 100+ years in the past (depending on how far back the IANA TZDB rules have been specified). (optional)

    try:
        # Get the current time zone information for any point on earth.
        api_response = api_instance.tz_lookup(lat, lng, timestamp=timestamp)
        print("The response of GeospatialApi->tz_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GeospatialApi->tz_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| The latitude of the point you are interested in. | 
 **lng** | **float**| The longitude of the point you are interested in. | 
 **timestamp** | **int**| The UNIX timestamp at which the UTC and DST offsets will be calculated. This defaults to the present time. This endpoint is not necessarily guaranteed to be accurate for timestamps that occurred in the past. Time zone geographic boundaries change over time, so if the point you are querying for was previously in a different time zone, historical results will not be accurate. If, however, the point has been in the same geographic time zone for a very long time (ex: &#x60;America/New_York&#x60;), the historical data may be accurate for 100+ years in the past (depending on how far back the IANA TZDB rules have been specified). | [optional] 

### Return type

[**TzResponse**](TzResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the time zone metadata. |  -  |
**404** | Time zone not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

