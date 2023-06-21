# coding: utf-8

# flake8: noqa

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.4
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "1.0.5"

# import apis into sdk package
from stadiamaps.api.geocoding_api import GeocodingApi
from stadiamaps.api.geospatial_api import GeospatialApi
from stadiamaps.api.routing_api import RoutingApi

# import ApiClient
from stadiamaps.api_response import ApiResponse
from stadiamaps.api_client import ApiClient
from stadiamaps.configuration import Configuration
from stadiamaps.exceptions import OpenApiException
from stadiamaps.exceptions import ApiTypeError
from stadiamaps.exceptions import ApiValueError
from stadiamaps.exceptions import ApiKeyError
from stadiamaps.exceptions import ApiAttributeError
from stadiamaps.exceptions import ApiException

# import models into sdk package
from stadiamaps.models.access import Access
from stadiamaps.models.admin_region import AdminRegion
from stadiamaps.models.administrative import Administrative
from stadiamaps.models.auto_costing_options import AutoCostingOptions
from stadiamaps.models.auto_costing_options_all_of import AutoCostingOptionsAllOf
from stadiamaps.models.base_costing_options import BaseCostingOptions
from stadiamaps.models.base_trace_request import BaseTraceRequest
from stadiamaps.models.bicycle_costing_options import BicycleCostingOptions
from stadiamaps.models.bicycle_costing_options_all_of import BicycleCostingOptionsAllOf
from stadiamaps.models.bike_network import BikeNetwork
from stadiamaps.models.contour import Contour
from stadiamaps.models.coordinate import Coordinate
from stadiamaps.models.costing_model import CostingModel
from stadiamaps.models.costing_options import CostingOptions
from stadiamaps.models.directions_options import DirectionsOptions
from stadiamaps.models.distance_unit import DistanceUnit
from stadiamaps.models.edge_sign import EdgeSign
from stadiamaps.models.edge_use import EdgeUse
from stadiamaps.models.end_node import EndNode
from stadiamaps.models.geo_attributes import GeoAttributes
from stadiamaps.models.geo_json_geometry import GeoJSONGeometry
from stadiamaps.models.geo_json_geometry_base import GeoJSONGeometryBase
from stadiamaps.models.geo_json_line_string import GeoJSONLineString
from stadiamaps.models.geo_json_line_string_all_of import GeoJSONLineStringAllOf
from stadiamaps.models.geo_json_point import GeoJSONPoint
from stadiamaps.models.geo_json_point_all_of import GeoJSONPointAllOf
from stadiamaps.models.geo_json_polygon import GeoJSONPolygon
from stadiamaps.models.geo_json_polygon_all_of import GeoJSONPolygonAllOf
from stadiamaps.models.geocoding_object import GeocodingObject
from stadiamaps.models.height_request import HeightRequest
from stadiamaps.models.height_response import HeightResponse
from stadiamaps.models.highway_classification import HighwayClassification
from stadiamaps.models.intersecting_edge import IntersectingEdge
from stadiamaps.models.isochrone_costing_model import IsochroneCostingModel
from stadiamaps.models.isochrone_feature import IsochroneFeature
from stadiamaps.models.isochrone_properties import IsochroneProperties
from stadiamaps.models.isochrone_request import IsochroneRequest
from stadiamaps.models.isochrone_response import IsochroneResponse
from stadiamaps.models.locate_detailed_edge import LocateDetailedEdge
from stadiamaps.models.locate_edge import LocateEdge
from stadiamaps.models.locate_edge_info import LocateEdgeInfo
from stadiamaps.models.locate_node import LocateNode
from stadiamaps.models.locate_node_all_of import LocateNodeAllOf
from stadiamaps.models.locate_object import LocateObject
from stadiamaps.models.maneuver_sign import ManeuverSign
from stadiamaps.models.maneuver_sign_element import ManeuverSignElement
from stadiamaps.models.map_match_costing_model import MapMatchCostingModel
from stadiamaps.models.map_match_request import MapMatchRequest
from stadiamaps.models.map_match_request_all_of import MapMatchRequestAllOf
from stadiamaps.models.map_match_route_response import MapMatchRouteResponse
from stadiamaps.models.map_match_route_response_all_of import MapMatchRouteResponseAllOf
from stadiamaps.models.map_match_trace_options import MapMatchTraceOptions
from stadiamaps.models.map_match_waypoint import MapMatchWaypoint
from stadiamaps.models.map_match_waypoint_all_of import MapMatchWaypointAllOf
from stadiamaps.models.matched_point import MatchedPoint
from stadiamaps.models.matrix_costing_model import MatrixCostingModel
from stadiamaps.models.matrix_distance import MatrixDistance
from stadiamaps.models.matrix_request import MatrixRequest
from stadiamaps.models.matrix_response import MatrixResponse
from stadiamaps.models.motor_scooter_costing_options import MotorScooterCostingOptions
from stadiamaps.models.motor_scooter_costing_options_all_of import MotorScooterCostingOptionsAllOf
from stadiamaps.models.motorcycle_costing_options import MotorcycleCostingOptions
from stadiamaps.models.motorcycle_costing_options_all_of import MotorcycleCostingOptionsAllOf
from stadiamaps.models.nearest_roads_request import NearestRoadsRequest
from stadiamaps.models.node_id import NodeId
from stadiamaps.models.node_type import NodeType
from stadiamaps.models.optimized_route_request import OptimizedRouteRequest
from stadiamaps.models.pedestrian_costing_options import PedestrianCostingOptions
from stadiamaps.models.pelias_geo_json_feature import PeliasGeoJSONFeature
from stadiamaps.models.pelias_geo_json_properties import PeliasGeoJSONProperties
from stadiamaps.models.pelias_geo_json_properties_addendum import PeliasGeoJSONPropertiesAddendum
from stadiamaps.models.pelias_geo_json_properties_addendum_osm import PeliasGeoJSONPropertiesAddendumOsm
from stadiamaps.models.pelias_layer import PeliasLayer
from stadiamaps.models.pelias_response import PeliasResponse
from stadiamaps.models.pelias_response_geocoding import PeliasResponseGeocoding
from stadiamaps.models.pelias_source import PeliasSource
from stadiamaps.models.restrictions import Restrictions
from stadiamaps.models.road_class import RoadClass
from stadiamaps.models.route_leg import RouteLeg
from stadiamaps.models.route_maneuver import RouteManeuver
from stadiamaps.models.route_request import RouteRequest
from stadiamaps.models.route_response import RouteResponse
from stadiamaps.models.route_response_trip import RouteResponseTrip
from stadiamaps.models.route_summary import RouteSummary
from stadiamaps.models.routing_response_waypoint import RoutingResponseWaypoint
from stadiamaps.models.routing_response_waypoint_all_of import RoutingResponseWaypointAllOf
from stadiamaps.models.routing_waypoint import RoutingWaypoint
from stadiamaps.models.routing_waypoint_all_of import RoutingWaypointAllOf
from stadiamaps.models.routing_waypoint_all_of_search_filter import RoutingWaypointAllOfSearchFilter
from stadiamaps.models.simple_routing_waypoint import SimpleRoutingWaypoint
from stadiamaps.models.simple_routing_waypoint_all_of import SimpleRoutingWaypointAllOf
from stadiamaps.models.speeds import Speeds
from stadiamaps.models.trace_attribute_filter_options import TraceAttributeFilterOptions
from stadiamaps.models.trace_attribute_key import TraceAttributeKey
from stadiamaps.models.trace_attributes_base_response import TraceAttributesBaseResponse
from stadiamaps.models.trace_attributes_request import TraceAttributesRequest
from stadiamaps.models.trace_attributes_request_all_of import TraceAttributesRequestAllOf
from stadiamaps.models.trace_attributes_request_all_of_filters import TraceAttributesRequestAllOfFilters
from stadiamaps.models.trace_attributes_response import TraceAttributesResponse
from stadiamaps.models.trace_attributes_response_all_of import TraceAttributesResponseAllOf
from stadiamaps.models.trace_edge import TraceEdge
from stadiamaps.models.travel_mode import TravelMode
from stadiamaps.models.traversability import Traversability
from stadiamaps.models.truck_costing_options import TruckCostingOptions
from stadiamaps.models.truck_costing_options_all_of import TruckCostingOptionsAllOf
from stadiamaps.models.tz_response import TzResponse
from stadiamaps.models.valhalla_languages import ValhallaLanguages
from stadiamaps.models.valhalla_long_units import ValhallaLongUnits
from stadiamaps.models.warning import Warning
