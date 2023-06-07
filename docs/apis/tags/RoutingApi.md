<a id="__pageTop"></a>
# stadiamaps.apis.tags.routing_api.RoutingApi

All URIs are relative to *https://api.stadiamaps.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**isochrone**](#isochrone) | **post** /isochrone/v1 | Calculate areas of equal travel time from a location.
[**map_match**](#map_match) | **post** /map_match/v1 | Match a recorded route to the road network.
[**nearest_roads**](#nearest_roads) | **post** /nearest_roads/v1 | Find the nearest roads to the set of input locations.
[**optimized_route**](#optimized_route) | **post** /optimized_route/v1 | Calculate an optimized route between a known start and end point.
[**route**](#route) | **post** /route/v1 | Get turn by turn routing instructions between two or more locations.
[**time_distance_matrix**](#time_distance_matrix) | **post** /matrix/v1 | Calculate a time distance matrix for a grid of start and end points.
[**trace_attributes**](#trace_attributes) | **post** /trace_attributes/v1 | Trace the attributes of roads visited on a route.

# **isochrone**
<a id="isochrone"></a>
> IsochroneResponse isochrone()

Calculate areas of equal travel time from a location.

The isochrone API lets you compute or visualize areas of roughly equal travel time based on the routing graph. The resulting polygon can be rendered on a map and shaded much like elevation contours and used for exploring urban mobility.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import routing_api
from stadiamaps.model.isochrone_request import IsochroneRequest
from stadiamaps.model.isochrone_response import IsochroneResponse
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
    api_instance = routing_api.RoutingApi(api_client)

    # example passing only optional values
    body = IsochroneRequest(
        id="kesklinn",
        locations=[
            Coordinate(
                lat=59.436884,
                lon=24.742595,
            )
        ],
        costing=IsochroneCostingModel("auto"),
        costing_options=CostingOptions(
            auto=AutoCostingOptions(None),
,
,
            truck=TruckCostingOptions(None),
            bicycle=BicycleCostingOptions(None),
            motor_scooter=MotorScooterCostingOptions(None),
            motorcycle=MotorcycleCostingOptions(None),
            pedestrian=PedestrianCostingOptions(
                walking_speed=0.5,
                walkway_factor=1,
                sidewalk_factor=1,
                alley_factor=2,
                driveway_factor=5,
                step_penalty=30,
                use_ferry=UseFerryCostingOption(0.5),
                use_living_streets=UseLivingStreetsCostingOption(0),
                use_tracks=UseTracksCostingOption(0),
                use_hills=UseHillsCostingOption(0.5),
                use_lit=0,
                service_penalty=1,
                service_factor=1,
                max_hiking_difficulty=1,
                bss_rent_cost=120,
                bss_rent_penalty=0,
            ),
        ),
        contours=[
            Contour(
                time=15,
                distance=10.0,
                color="aabbcc",
            )
        ],
        polygons=False,
        denoise=1,
        generalize=200.0,
        show_locations=False,
    )
    try:
        # Calculate areas of equal travel time from a location.
        api_response = api_instance.isochrone(
            body=body,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling RoutingApi->isochrone: %s\n" % e)
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
[**IsochroneRequest**](../../models/IsochroneRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#isochrone.ApiResponseFor200) | Returns a GeoJSON object which can be integrated into your geospatial application.

#### isochrone.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IsochroneResponse**](../../models/IsochroneResponse.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **map_match**
<a id="map_match"></a>
> MapMatchRouteResponse map_match()

Match a recorded route to the road network.

The map matching API transforms a recorded route into navigation instructions like you would get from the `route` endpoint. The input can be in the form of either an encoded polyline, or (optionally) timestamped coordinates.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import routing_api
from stadiamaps.model.map_match_route_response import MapMatchRouteResponse
from stadiamaps.model.map_match_request import MapMatchRequest
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
    api_instance = routing_api.RoutingApi(api_client)

    # example passing only optional values
    body = MapMatchRequest(None)
    try:
        # Match a recorded route to the road network.
        api_response = api_instance.map_match(
            body=body,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling RoutingApi->map_match: %s\n" % e)
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
[**MapMatchRequest**](../../models/MapMatchRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#map_match.ApiResponseFor200) | Returns the matched route, which looks more or less like a normal route response, optionally with a &#x60;linear_references&#x60; key.
400 | [ApiResponseFor400](#map_match.ApiResponseFor400) | Bad request; more details will be included
500 | [ApiResponseFor500](#map_match.ApiResponseFor500) | An internal parse error occurred; more details will be included

#### map_match.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MapMatchRouteResponse**](../../models/MapMatchRouteResponse.md) |  | 


#### map_match.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### map_match.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **nearest_roads**
<a id="nearest_roads"></a>
> NearestRoadsResponse nearest_roads()

Find the nearest roads to the set of input locations.

The nearest roads API allows you query for detailed information about streets and intersections near the input locations.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import routing_api
from stadiamaps.model.nearest_roads_request import NearestRoadsRequest
from stadiamaps.model.nearest_roads_response import NearestRoadsResponse
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
    api_instance = routing_api.RoutingApi(api_client)

    # example passing only optional values
    body = NearestRoadsRequest(None)
    try:
        # Find the nearest roads to the set of input locations.
        api_response = api_instance.nearest_roads(
            body=body,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling RoutingApi->nearest_roads: %s\n" % e)
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
[**NearestRoadsRequest**](../../models/NearestRoadsRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#nearest_roads.ApiResponseFor200) | Returns a list of streets and intersections that match the query.

#### nearest_roads.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**NearestRoadsResponse**](../../models/NearestRoadsResponse.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **optimized_route**
<a id="optimized_route"></a>
> RouteResponse optimized_route()

Calculate an optimized route between a known start and end point.

The optimized route API is a mix of the matrix and normal route API. For an optimized route, the start and end point are fixed, but the intermediate points will be re-ordered to form an optimal route visiting all nodes once. Note that all matrix endpoints have a limit of 1000 elements, regardless of the costing/mode of travel. A matrix request with 3 inputs and 5 outputs has 3 x 5 = 15 elements. This means you could send a 100 x 10 or 20 x 50 matrix request (each having 1000 elements), but not 40 x 30 as it has 1200 elements.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import routing_api
from stadiamaps.model.optimized_route_request import OptimizedRouteRequest
from stadiamaps.model.route_response import RouteResponse
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
    api_instance = routing_api.RoutingApi(api_client)

    # example passing only optional values
    body = OptimizedRouteRequest(None)
    try:
        # Calculate an optimized route between a known start and end point.
        api_response = api_instance.optimized_route(
            body=body,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling RoutingApi->optimized_route: %s\n" % e)
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
[**OptimizedRouteRequest**](../../models/OptimizedRouteRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#optimized_route.ApiResponseFor200) | Returns the optimized route, which looks more or less like a normal route response. The only significant difference is that the &#x60;locations&#x60; may be re-ordered and annotated with an &#x60;original_index&#x60;.
400 | [ApiResponseFor400](#optimized_route.ApiResponseFor400) | Bad request; more details will be included
500 | [ApiResponseFor500](#optimized_route.ApiResponseFor500) | An internal parse error occurred; more details will be included

#### optimized_route.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RouteResponse**](../../models/RouteResponse.md) |  | 


#### optimized_route.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### optimized_route.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **route**
<a id="route"></a>
> RouteResponse route()

Get turn by turn routing instructions between two or more locations.

The route (turn-by-turn) API computes routes between two or more locations. It supports a variety of tunable costing methods, and supports routing through intermediate waypoints and discontinuous multi-leg routes.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import routing_api
from stadiamaps.model.route_request import RouteRequest
from stadiamaps.model.route_response import RouteResponse
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
    api_instance = routing_api.RoutingApi(api_client)

    # example passing only optional values
    body = RouteRequest(None)
    try:
        # Get turn by turn routing instructions between two or more locations.
        api_response = api_instance.route(
            body=body,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling RoutingApi->route: %s\n" % e)
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
[**RouteRequest**](../../models/RouteRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#route.ApiResponseFor200) | Returns the computed route
400 | [ApiResponseFor400](#route.ApiResponseFor400) | Bad request; more details will be included
500 | [ApiResponseFor500](#route.ApiResponseFor500) | An internal parse error occurred; more details will be included

#### route.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RouteResponse**](../../models/RouteResponse.md) |  | 


#### route.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### route.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **time_distance_matrix**
<a id="time_distance_matrix"></a>
> MatrixResponse time_distance_matrix()

Calculate a time distance matrix for a grid of start and end points.

The time distance matrix API lets you compare travel times between a set of possible start and end points. Note that all matrix endpoints have a limit of 1000 elements, regardless of the costing/mode of travel. A matrix request with 3 inputs and 5 outputs has 3 x 5 = 15 elements. This means you could send a 100 x 10 or 20 x 50 matrix request (each having 1000 elements), but not 40 x 30 as it has 1200 elements.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import routing_api
from stadiamaps.model.matrix_response import MatrixResponse
from stadiamaps.model.matrix_request import MatrixRequest
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
    api_instance = routing_api.RoutingApi(api_client)

    # example passing only optional values
    body = MatrixRequest(None)
    try:
        # Calculate a time distance matrix for a grid of start and end points.
        api_response = api_instance.time_distance_matrix(
            body=body,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling RoutingApi->time_distance_matrix: %s\n" % e)
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
[**MatrixRequest**](../../models/MatrixRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#time_distance_matrix.ApiResponseFor200) | Returns a matrix of times and distances between the start and end points.

#### time_distance_matrix.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MatrixResponse**](../../models/MatrixResponse.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **trace_attributes**
<a id="trace_attributes"></a>
> TraceAttributesResponse trace_attributes()

Trace the attributes of roads visited on a route.

The trace attributes endpoint retrieves detailed information along a route, returning details for each section along the path, as well as any intersections encountered. In addition to tracing a recording route, this is great for providing just-in-time info to navigation applications, enabling them to conserve resources by omitting info like speed limits upfront that may be irrelevant if the user goes off-route.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import stadiamaps
from stadiamaps.apis.tags import routing_api
from stadiamaps.model.trace_attributes_request import TraceAttributesRequest
from stadiamaps.model.trace_attributes_response import TraceAttributesResponse
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
    api_instance = routing_api.RoutingApi(api_client)

    # example passing only optional values
    body = TraceAttributesRequest(None)
    try:
        # Trace the attributes of roads visited on a route.
        api_response = api_instance.trace_attributes(
            body=body,
        )
        pprint(api_response)
    except stadiamaps.ApiException as e:
        print("Exception when calling RoutingApi->trace_attributes: %s\n" % e)
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
[**TraceAttributesRequest**](../../models/TraceAttributesRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#trace_attributes.ApiResponseFor200) | Returns the edges along the traced route with detailed info.

#### trace_attributes.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TraceAttributesResponse**](../../models/TraceAttributesResponse.md) |  | 


### Authorization

[ApiKeyAuth](../../../README.md#ApiKeyAuth)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

