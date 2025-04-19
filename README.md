# Stadia Maps Python API Client

The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

For more information about the API, please visit [https://docs.stadiamaps.com](https://docs.stadiamaps.com)

## Requirements.

Python 3.8+

## Installation & Usage

You can install via your favorite package manager.
For example:

### pip

```shell
pip install stadiamaps
```

### poetry

```shell
poetry add stadiamaps
```

### Tests

Execute `pytest` to run the tests. These are run automatically via CI.

## Getting Started

After following the [installation procedure](#installation--usage), you'll need a Stadia Maps API key.

You can create an API key for free
[here](https://client.stadiamaps.com/signup/?utm_source=github&utm_campaign=sdk_readme&utm_content=python_readme)
(no credit card required).

```python
import os
import stadiamaps
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# You can also use our EU endpoint to keep traffic within the EU like so:
# configuration = stadiamaps.Configuration(host="https://api-eu.stadiamaps.com")
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration()

# Configure API key authorization. This example assumes it is injected via an environment
# variable.
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    text = "Kursi 3" # str | The place name (address, venue name, etc.) to search for.

    try:
        # Search and geocode quickly based on partial input.
        api_response = api_instance.autocomplete_v2(text, lang="en")
        print("The response of GeocodingApi->autocomplete:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GeocodingApi->autocomplete_v2: %s\n" % e)
```

## Documentation

Official documentation lives at [docs.stadiamaps.com](https://docs.stadiamaps.com/?utm_source=github&utm_campaign=sdk_readme&utm_content=python_readme),
where we have both long-form prose explanations of each endpoint and an interactive [API reference](https://docs.stadiamaps.com/api-reference/?utm_source=github&utm_campaign=sdk_readme&utm_content=python_readme).

You can also find auto-generated class references below.

### API Endpoints

All URIs are relative to *https://api.stadiamaps.com*

Class | Method                                                              | HTTP request                            | Description
------------ |---------------------------------------------------------------------|-----------------------------------------| -------------
*GeocodingApi* | [**autocomplete**](docs/GeocodingApi.md#autocomplete)               | **GET** /geocoding/v1/autocomplete      | Search and geocode quickly based on partial input.
*GeocodingApi* | [**place**](docs/GeocodingApi.md#place)                             | **GET** /geocoding/v1/place             | Retrieve details of a place using its GID.
*GeocodingApi* | [**reverse**](docs/GeocodingApi.md#reverse)                         | **GET** /geocoding/v1/reverse           | Find places and addresses near geographic coordinates (reverse geocoding).
*GeocodingApi* | [**search**](docs/GeocodingApi.md#search)                           | **GET** /geocoding/v1/search            | Search for location and other info using a place name or address (forward geocoding).
*GeocodingApi* | [**search_structured**](docs/GeocodingApi.md#search_structured)     | **GET** /geocoding/v1/search/structured | Find locations matching components (structured forward geocoding).
*GeocodingApi* | [**search_bulk**](docs/GeocodingApi.md#search_bulk)                 | **GET** /geocoding/v1/search/bulk       | Bulk geocoding.
*GeospatialApi* | [**elevation**](docs/GeospatialApi.md#elevation)                    | **POST** /elevation/v1                  | Get the elevation profile along a polyline or at a point.
*GeospatialApi* | [**tz_lookup**](docs/GeospatialApi.md#tz_lookup)                    | **GET** /tz/lookup/v1                   | Get the current time zone information for any point on earth.
*RoutingApi* | [**isochrone**](docs/RoutingApi.md#isochrone)                       | **POST** /isochrone/v1                  | Calculate areas of equal travel time from a location.
*RoutingApi* | [**map_match**](docs/RoutingApi.md#map_match)                       | **POST** /map_match/v1                  | Match a recorded route to the road network.
*RoutingApi* | [**nearest_roads**](docs/RoutingApi.md#nearest_roads)               | **POST** /nearest_roads/v1              | Find the nearest roads to the set of input locations.
*RoutingApi* | [**optimized_route**](docs/RoutingApi.md#optimized_route)           | **POST** /optimized_route/v1            | Calculate an optimized route between a known start and end point.
*RoutingApi* | [**route**](docs/RoutingApi.md#route)                               | **POST** /route/v1                      | Get turn by turn routing instructions between two or more locations.
*RoutingApi* | [**time_distance_matrix**](docs/RoutingApi.md#time_distance_matrix) | **POST** /matrix/v1                     | Calculate a time distance matrix for use in an optimizer.
*RoutingApi* | [**trace_attributes**](docs/RoutingApi.md#trace_attributes)         | **POST** /trace_attributes/v1           | Trace the attributes of roads visited on a route.

