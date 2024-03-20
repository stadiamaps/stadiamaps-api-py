# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 6.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class TraceAttributeKey(str, Enum):
    """
    TraceAttributeKey
    """

    """
    allowed enum values
    """
    EDGE_DOT_NAMES = 'edge.names'
    EDGE_DOT_LENGTH = 'edge.length'
    EDGE_DOT_SPEED = 'edge.speed'
    EDGE_DOT_ROAD_CLASS = 'edge.road_class'
    EDGE_DOT_BEGIN_HEADING = 'edge.begin_heading'
    EDGE_DOT_END_HEADING = 'edge.end_heading'
    EDGE_DOT_BEGIN_SHAPE_INDEX = 'edge.begin_shape_index'
    EDGE_DOT_END_SHAPE_INDEX = 'edge.end_shape_index'
    EDGE_DOT_TRAVERSABILITY = 'edge.traversability'
    EDGE_DOT_USE = 'edge.use'
    EDGE_DOT_TOLL = 'edge.toll'
    EDGE_DOT_UNPAVED = 'edge.unpaved'
    EDGE_DOT_TUNNEL = 'edge.tunnel'
    EDGE_DOT_BRIDGE = 'edge.bridge'
    EDGE_DOT_ROUNDABOUT = 'edge.roundabout'
    EDGE_DOT_INTERNAL_INTERSECTION = 'edge.internal_intersection'
    EDGE_DOT_DRIVE_ON_RIGHT = 'edge.drive_on_right'
    EDGE_DOT_SURFACE = 'edge.surface'
    EDGE_DOT_SIGN_DOT_EXIT_NUMBER = 'edge.sign.exit_number'
    EDGE_DOT_SIGN_DOT_EXIT_BRANCH = 'edge.sign.exit_branch'
    EDGE_DOT_SIGN_DOT_EXIT_TOWARD = 'edge.sign.exit_toward'
    EDGE_DOT_SIGN_DOT_EXIT_NAME = 'edge.sign.exit_name'
    EDGE_DOT_TRAVEL_MODE = 'edge.travel_mode'
    EDGE_DOT_VEHICLE_TYPE = 'edge.vehicle_type'
    EDGE_DOT_PEDESTRIAN_TYPE = 'edge.pedestrian_type'
    EDGE_DOT_BICYCLE_TYPE = 'edge.bicycle_type'
    EDGE_DOT_TRANSIT_TYPE = 'edge.transit_type'
    EDGE_DOT_ID = 'edge.id'
    EDGE_DOT_WAY_ID = 'edge.way_id'
    EDGE_DOT_WEIGHTED_GRADE = 'edge.weighted_grade'
    EDGE_DOT_MAX_UPWARD_GRADE = 'edge.max_upward_grade'
    EDGE_DOT_MAX_DOWNWARD_GRADE = 'edge.max_downward_grade'
    EDGE_DOT_MEAN_ELEVATION = 'edge.mean_elevation'
    EDGE_DOT_LANE_COUNT = 'edge.lane_count'
    EDGE_DOT_CYCLE_LANE = 'edge.cycle_lane'
    EDGE_DOT_BICYCLE_NETWORK = 'edge.bicycle_network'
    EDGE_DOT_SAC_SCALE = 'edge.sac_scale'
    EDGE_DOT_SIDEWALK = 'edge.sidewalk'
    EDGE_DOT_DENSITY = 'edge.density'
    EDGE_DOT_SPEED_LIMIT = 'edge.speed_limit'
    EDGE_DOT_TRUCK_SPEED = 'edge.truck_speed'
    EDGE_DOT_TRUCK_ROUTE = 'edge.truck_route'
    NODE_DOT_INTERSECTING_EDGE_DOT_BEGIN_HEADING = 'node.intersecting_edge.begin_heading'
    NODE_DOT_INTERSECTING_EDGE_DOT_FROM_EDGE_NAME_CONSISTENCY = 'node.intersecting_edge.from_edge_name_consistency'
    NODE_DOT_INTERSECTING_EDGE_DOT_TO_EDGE_NAME_CONSISTENCY = 'node.intersecting_edge.to_edge_name_consistency'
    NODE_DOT_INTERSECTING_EDGE_DOT_DRIVEABILITY = 'node.intersecting_edge.driveability'
    NODE_DOT_INTERSECTING_EDGE_DOT_CYCLABILITY = 'node.intersecting_edge.cyclability'
    NODE_DOT_INTERSECTING_EDGE_DOT_WALKABILITY = 'node.intersecting_edge.walkability'
    NODE_DOT_INTERSECTING_EDGE_DOT_USE = 'node.intersecting_edge.use'
    NODE_DOT_INTERSECTING_EDGE_DOT_ROAD_CLASS = 'node.intersecting_edge.road_class'
    NODE_DOT_ELAPSED_TIME = 'node.elapsed_time'
    NODE_DOT_ADMIN_INDEX = 'node.admin_index'
    NODE_DOT_TYPE = 'node.type'
    NODE_DOT_FORK = 'node.fork'
    NODE_DOT_TIME_ZONE = 'node.time_zone'
    OSM_CHANGESET = 'osm_changeset'
    SHAPE = 'shape'
    ADMIN_DOT_COUNTRY_CODE = 'admin.country_code'
    ADMIN_DOT_COUNTRY_TEXT = 'admin.country_text'
    ADMIN_DOT_STATE_CODE = 'admin.state_code'
    ADMIN_DOT_STATE_TEXT = 'admin.state_text'
    MATCHED_DOT_POINT = 'matched.point'
    MATCHED_DOT_TYPE = 'matched.type'
    MATCHED_DOT_EDGE_INDEX = 'matched.edge_index'
    MATCHED_DOT_BEGIN_ROUTE_DISCONTINUITY = 'matched.begin_route_discontinuity'
    MATCHED_DOT_END_ROUTE_DISCONTINUITY = 'matched.end_route_discontinuity'
    MATCHED_DOT_DISTANCE_ALONG_EDGE = 'matched.distance_along_edge'
    MATCHED_DOT_DISTANCE_FROM_TRACE_POINT = 'matched.distance_from_trace_point'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TraceAttributeKey from a JSON string"""
        return cls(json.loads(json_str))


