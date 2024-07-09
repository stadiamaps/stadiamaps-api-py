# Stadia Maps Python API Client

The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

For more information about the API, please visit [https://docs.stadiamaps.com](https://docs.stadiamaps.com)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

```shell
pip install stadiamaps
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import stadiamaps
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
    text = "Põhja pst 27a" # str | The place name (address, venue name, etc.) to search for.

    try:
        # Search and geocode quickly based on partial input.
        api_response = api_instance.autocomplete(text)
        print("The response of GeocodingApi->autocomplete:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GeocodingApi->autocomplete: %s\n" % e)
```

## Documentation

Official documentation lives at [docs.stadiamaps.com](https://docs.stadiamaps.com/?utm_source=github&utm_campaign=sdk_readme&utm_content=python_readme),
where we have both long-form prose explanations of each endpoint and an interactive [API reference](https://docs.stadiamaps.com/api-reference/?utm_source=github&utm_campaign=sdk_readme&utm_content=python_readme).

You can also find auto-generated class references below.

### API Endpoints

All URIs are relative to *https://api.stadiamaps.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*GeocodingApi* | [**autocomplete**](docs/GeocodingApi.md#autocomplete) | **GET** /geocoding/v1/autocomplete | Search and geocode quickly based on partial input.
*GeocodingApi* | [**place**](docs/GeocodingApi.md#place) | **GET** /geocoding/v1/place | Retrieve details of a place using its GID.
*GeocodingApi* | [**reverse**](docs/GeocodingApi.md#reverse) | **GET** /geocoding/v1/reverse | Find places and addresses near geographic coordinates (reverse geocoding).
*GeocodingApi* | [**search**](docs/GeocodingApi.md#search) | **GET** /geocoding/v1/search | Search for location and other info using a place name or address (forward geocoding).
*GeocodingApi* | [**search_structured**](docs/GeocodingApi.md#search_structured) | **GET** /geocoding/v1/search/structured | Find locations matching components (structured forward geocoding).
*GeospatialApi* | [**elevation**](docs/GeospatialApi.md#elevation) | **POST** /elevation/v1 | Get the elevation profile along a polyline or at a point.
*GeospatialApi* | [**tz_lookup**](docs/GeospatialApi.md#tz_lookup) | **GET** /tz/lookup/v1 | Get the current time zone information for any point on earth.
*RoutingApi* | [**isochrone**](docs/RoutingApi.md#isochrone) | **POST** /isochrone/v1 | Calculate areas of equal travel time from a location.
*RoutingApi* | [**map_match**](docs/RoutingApi.md#map_match) | **POST** /map_match/v1 | Match a recorded route to the road network.
*RoutingApi* | [**nearest_roads**](docs/RoutingApi.md#nearest_roads) | **POST** /nearest_roads/v1 | Find the nearest roads to the set of input locations.
*RoutingApi* | [**optimized_route**](docs/RoutingApi.md#optimized_route) | **POST** /optimized_route/v1 | Calculate an optimized route between a known start and end point.
*RoutingApi* | [**route**](docs/RoutingApi.md#route) | **POST** /route/v1 | Get turn by turn routing instructions between two or more locations.
*RoutingApi* | [**time_distance_matrix**](docs/RoutingApi.md#time_distance_matrix) | **POST** /matrix/v1 | Calculate a time distance matrix for use in an optimizer.
*RoutingApi* | [**trace_attributes**](docs/RoutingApi.md#trace_attributes) | **POST** /trace_attributes/v1 | Trace the attributes of roads visited on a route.


### Models

 - [Access](docs/Access.md)
 - [AdminRegion](docs/AdminRegion.md)
 - [Administrative](docs/Administrative.md)
 - [AutoCostingOptions](docs/AutoCostingOptions.md)
 - [BaseCostingOptions](docs/BaseCostingOptions.md)
 - [BaseTraceRequest](docs/BaseTraceRequest.md)
 - [BicycleCostingOptions](docs/BicycleCostingOptions.md)
 - [BikeNetwork](docs/BikeNetwork.md)
 - [Contour](docs/Contour.md)
 - [Coordinate](docs/Coordinate.md)
 - [CostingModel](docs/CostingModel.md)
 - [CostingOptions](docs/CostingOptions.md)
 - [DirectionsOptions](docs/DirectionsOptions.md)
 - [DistanceUnit](docs/DistanceUnit.md)
 - [EdgeSign](docs/EdgeSign.md)
 - [EdgeUse](docs/EdgeUse.md)
 - [EndNode](docs/EndNode.md)
 - [GeoAttributes](docs/GeoAttributes.md)
 - [GeoJSONGeometry](docs/GeoJSONGeometry.md)
 - [GeoJSONGeometryBase](docs/GeoJSONGeometryBase.md)
 - [GeoJSONLineString](docs/GeoJSONLineString.md)
 - [GeoJSONPoint](docs/GeoJSONPoint.md)
 - [GeoJSONPolygon](docs/GeoJSONPolygon.md)
 - [GeocodingObject](docs/GeocodingObject.md)
 - [HeightRequest](docs/HeightRequest.md)
 - [HeightResponse](docs/HeightResponse.md)
 - [HighwayClassification](docs/HighwayClassification.md)
 - [IntersectingEdge](docs/IntersectingEdge.md)
 - [IsochroneCostingModel](docs/IsochroneCostingModel.md)
 - [IsochroneFeature](docs/IsochroneFeature.md)
 - [IsochroneProperties](docs/IsochroneProperties.md)
 - [IsochroneRequest](docs/IsochroneRequest.md)
 - [IsochroneResponse](docs/IsochroneResponse.md)
 - [LocateDetailedEdge](docs/LocateDetailedEdge.md)
 - [LocateEdge](docs/LocateEdge.md)
 - [LocateEdgeInfo](docs/LocateEdgeInfo.md)
 - [LocateNode](docs/LocateNode.md)
 - [LocateObject](docs/LocateObject.md)
 - [ManeuverSign](docs/ManeuverSign.md)
 - [ManeuverSignElement](docs/ManeuverSignElement.md)
 - [MapMatchCostingModel](docs/MapMatchCostingModel.md)
 - [MapMatchRequest](docs/MapMatchRequest.md)
 - [MapMatchRouteResponse](docs/MapMatchRouteResponse.md)
 - [MapMatchTraceOptions](docs/MapMatchTraceOptions.md)
 - [MapMatchWaypoint](docs/MapMatchWaypoint.md)
 - [MatchedPoint](docs/MatchedPoint.md)
 - [MatrixCostingModel](docs/MatrixCostingModel.md)
 - [MatrixDistance](docs/MatrixDistance.md)
 - [MatrixRequest](docs/MatrixRequest.md)
 - [MatrixResponse](docs/MatrixResponse.md)
 - [MotorScooterCostingOptions](docs/MotorScooterCostingOptions.md)
 - [MotorcycleCostingOptions](docs/MotorcycleCostingOptions.md)
 - [NearestRoadsRequest](docs/NearestRoadsRequest.md)
 - [NodeId](docs/NodeId.md)
 - [NodeType](docs/NodeType.md)
 - [OptimizedRouteRequest](docs/OptimizedRouteRequest.md)
 - [PedestrianCostingOptions](docs/PedestrianCostingOptions.md)
 - [PeliasGeoJSONFeature](docs/PeliasGeoJSONFeature.md)
 - [PeliasGeoJSONProperties](docs/PeliasGeoJSONProperties.md)
 - [PeliasGeoJSONPropertiesAddendum](docs/PeliasGeoJSONPropertiesAddendum.md)
 - [PeliasGeoJSONPropertiesAddendumOsm](docs/PeliasGeoJSONPropertiesAddendumOsm.md)
 - [PeliasLayer](docs/PeliasLayer.md)
 - [PeliasResponse](docs/PeliasResponse.md)
 - [PeliasSource](docs/PeliasSource.md)
 - [Restrictions](docs/Restrictions.md)
 - [RoadClass](docs/RoadClass.md)
 - [RouteLeg](docs/RouteLeg.md)
 - [RouteManeuver](docs/RouteManeuver.md)
 - [RouteRequest](docs/RouteRequest.md)
 - [RouteResponse](docs/RouteResponse.md)
 - [RouteResponseAlternatesInner](docs/RouteResponseAlternatesInner.md)
 - [RouteSummary](docs/RouteSummary.md)
 - [RouteTrip](docs/RouteTrip.md)
 - [RoutingResponseWaypoint](docs/RoutingResponseWaypoint.md)
 - [RoutingWaypoint](docs/RoutingWaypoint.md)
 - [RoutingWaypointAllOfSearchFilter](docs/RoutingWaypointAllOfSearchFilter.md)
 - [SimpleRoutingWaypoint](docs/SimpleRoutingWaypoint.md)
 - [Speeds](docs/Speeds.md)
 - [TraceAttributeFilterOptions](docs/TraceAttributeFilterOptions.md)
 - [TraceAttributeKey](docs/TraceAttributeKey.md)
 - [TraceAttributesBaseResponse](docs/TraceAttributesBaseResponse.md)
 - [TraceAttributesRequest](docs/TraceAttributesRequest.md)
 - [TraceAttributesResponse](docs/TraceAttributesResponse.md)
 - [TraceEdge](docs/TraceEdge.md)
 - [TravelMode](docs/TravelMode.md)
 - [Traversability](docs/Traversability.md)
 - [TruckCostingOptions](docs/TruckCostingOptions.md)
 - [TzResponse](docs/TzResponse.md)
 - [ValhallaLanguages](docs/ValhallaLanguages.md)
 - [ValhallaLongUnits](docs/ValhallaLongUnits.md)
 - [Warning](docs/Warning.md)
