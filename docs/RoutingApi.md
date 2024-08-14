# stadiamaps.RoutingApi

All URIs are relative to *https://api.stadiamaps.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**isochrone**](RoutingApi.md#isochrone) | **POST** /isochrone/v1 | Calculate areas of equal travel time from a location.
[**map_match**](RoutingApi.md#map_match) | **POST** /map_match/v1 | Match a recorded route to the road network.
[**nearest_roads**](RoutingApi.md#nearest_roads) | **POST** /nearest_roads/v1 | Find the nearest roads to the set of input locations.
[**optimized_route**](RoutingApi.md#optimized_route) | **POST** /optimized_route/v1 | Calculate an optimized route between a known start and end point.
[**route**](RoutingApi.md#route) | **POST** /route/v1 | Get turn by turn routing instructions between two or more locations.
[**time_distance_matrix**](RoutingApi.md#time_distance_matrix) | **POST** /matrix/v1 | Calculate a time distance matrix for use in an optimizer.
[**trace_attributes**](RoutingApi.md#trace_attributes) | **POST** /trace_attributes/v1 | Trace the attributes of roads visited on a route.


# **isochrone**
> IsochroneResponse isochrone(isochrone_request=isochrone_request)

Calculate areas of equal travel time from a location.

The isochrone API computes reachable areas within a time or distance constraint. The resulting polygon can be rendered on a map and used for assessing urban mobility, planning, or as a search filter of places within a constrained range.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.isochrone_request import IsochroneRequest
from stadiamaps.models.isochrone_response import IsochroneResponse
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
    api_instance = stadiamaps.RoutingApi(api_client)
    isochrone_request = stadiamaps.IsochroneRequest() # IsochroneRequest |  (optional)

    try:
        # Calculate areas of equal travel time from a location.
        api_response = api_instance.isochrone(isochrone_request=isochrone_request)
        print("The response of RoutingApi->isochrone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->isochrone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **isochrone_request** | [**IsochroneRequest**](IsochroneRequest.md)|  | [optional] 

### Return type

[**IsochroneResponse**](IsochroneResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A GeoJSON object which can be integrated into your geospatial application. |  -  |
**400** | Bad request; more details will be included |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **map_match**
> MapMatchRouteResponse map_match(map_match_request=map_match_request)

Match a recorded route to the road network.

The map matching API transforms a recorded route into navigation instructions like you would get from the `route` endpoint. The input can be in the form of either an encoded polyline, or (optionally) timestamped coordinates.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.map_match_request import MapMatchRequest
from stadiamaps.models.map_match_route_response import MapMatchRouteResponse
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
    api_instance = stadiamaps.RoutingApi(api_client)
    map_match_request = stadiamaps.MapMatchRequest() # MapMatchRequest |  (optional)

    try:
        # Match a recorded route to the road network.
        api_response = api_instance.map_match(map_match_request=map_match_request)
        print("The response of RoutingApi->map_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->map_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **map_match_request** | [**MapMatchRequest**](MapMatchRequest.md)|  | [optional] 

### Return type

[**MapMatchRouteResponse**](MapMatchRouteResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The matched route(s), which looks more or less like a normal route response, optionally with a &#x60;linear_references&#x60; key. |  -  |
**400** | Bad request; more details will be included |  -  |
**500** | An internal parse error occurred; more details will be included |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **nearest_roads**
> List[LocateObject] nearest_roads(nearest_roads_request=nearest_roads_request)

Find the nearest roads to the set of input locations.

The nearest roads API allows you query for detailed information about streets and intersections near the input locations.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.locate_object import LocateObject
from stadiamaps.models.nearest_roads_request import NearestRoadsRequest
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
    api_instance = stadiamaps.RoutingApi(api_client)
    nearest_roads_request = stadiamaps.NearestRoadsRequest() # NearestRoadsRequest |  (optional)

    try:
        # Find the nearest roads to the set of input locations.
        api_response = api_instance.nearest_roads(nearest_roads_request=nearest_roads_request)
        print("The response of RoutingApi->nearest_roads:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->nearest_roads: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nearest_roads_request** | [**NearestRoadsRequest**](NearestRoadsRequest.md)|  | [optional] 

### Return type

[**List[LocateObject]**](LocateObject.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of streets and intersections that match the query. |  -  |
**400** | Bad request; more details will be included |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **optimized_route**
> RouteResponse optimized_route(optimized_route_request=optimized_route_request)

Calculate an optimized route between a known start and end point.

The optimized route API is a mix of the matrix and normal route API. For an optimized route, the start and end point are fixed, but the intermediate points will be re-ordered to form an optimal route visiting all nodes once.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.optimized_route_request import OptimizedRouteRequest
from stadiamaps.models.route_response import RouteResponse
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
    api_instance = stadiamaps.RoutingApi(api_client)
    optimized_route_request = stadiamaps.OptimizedRouteRequest() # OptimizedRouteRequest |  (optional)

    try:
        # Calculate an optimized route between a known start and end point.
        api_response = api_instance.optimized_route(optimized_route_request=optimized_route_request)
        print("The response of RoutingApi->optimized_route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->optimized_route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optimized_route_request** | [**OptimizedRouteRequest**](OptimizedRouteRequest.md)|  | [optional] 

### Return type

[**RouteResponse**](RouteResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The optimized route, which looks more or less like a normal route response. The only significant difference is that the &#x60;locations&#x60; may be re-ordered and annotated with an &#x60;original_index&#x60;. |  -  |
**400** | Bad request; more details will be included |  -  |
**500** | An internal parse error occurred; more details will be included |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **route**
> RouteResponse route(route_request=route_request)

Get turn by turn routing instructions between two or more locations.

The route (turn-by-turn) API computes routes between two or more locations. It supports a variety of tunable costing methods, and supports routing through intermediate waypoints and discontinuous multi-leg routes.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.route_request import RouteRequest
from stadiamaps.models.route_response import RouteResponse
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
    api_instance = stadiamaps.RoutingApi(api_client)
    route_request = stadiamaps.RouteRequest() # RouteRequest |  (optional)

    try:
        # Get turn by turn routing instructions between two or more locations.
        api_response = api_instance.route(route_request=route_request)
        print("The response of RoutingApi->route:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->route: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **route_request** | [**RouteRequest**](RouteRequest.md)|  | [optional] 

### Return type

[**RouteResponse**](RouteResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The computed route(s). |  -  |
**400** | Bad request; more details will be included |  -  |
**500** | An internal parse error occurred; more details will be included |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **time_distance_matrix**
> MatrixResponse time_distance_matrix(matrix_request=matrix_request)

Calculate a time distance matrix for use in an optimizer.

The time distance matrix API lets you compare travel times between a set of possible start and end points. See https://docs.stadiamaps.com/limits/ for documentation of our latest limits.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.matrix_request import MatrixRequest
from stadiamaps.models.matrix_response import MatrixResponse
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
    api_instance = stadiamaps.RoutingApi(api_client)
    matrix_request = stadiamaps.MatrixRequest() # MatrixRequest |  (optional)

    try:
        # Calculate a time distance matrix for use in an optimizer.
        api_response = api_instance.time_distance_matrix(matrix_request=matrix_request)
        print("The response of RoutingApi->time_distance_matrix:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->time_distance_matrix: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matrix_request** | [**MatrixRequest**](MatrixRequest.md)|  | [optional] 

### Return type

[**MatrixResponse**](MatrixResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A matrix of times and distances between the start and end points. |  -  |
**400** | Bad request; more details will be included. NOTE: failure to find suitable edges near a location will result in a 400. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trace_attributes**
> TraceAttributesResponse trace_attributes(trace_attributes_request=trace_attributes_request)

Trace the attributes of roads visited on a route.

The trace attributes endpoint retrieves detailed information along a route, returning details for each section along the path, as well as any intersections encountered. In addition to tracing a recording route, this is great for providing just-in-time info to navigation applications, enabling them to conserve resources by omitting info like speed limits upfront that may be irrelevant if the user goes off-route.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import stadiamaps
from stadiamaps.models.trace_attributes_request import TraceAttributesRequest
from stadiamaps.models.trace_attributes_response import TraceAttributesResponse
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
    api_instance = stadiamaps.RoutingApi(api_client)
    trace_attributes_request = stadiamaps.TraceAttributesRequest() # TraceAttributesRequest |  (optional)

    try:
        # Trace the attributes of roads visited on a route.
        api_response = api_instance.trace_attributes(trace_attributes_request=trace_attributes_request)
        print("The response of RoutingApi->trace_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->trace_attributes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trace_attributes_request** | [**TraceAttributesRequest**](TraceAttributesRequest.md)|  | [optional] 

### Return type

[**TraceAttributesResponse**](TraceAttributesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The edges along the traced route with detailed info. |  -  |
**400** | Bad request; more details will be included |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

