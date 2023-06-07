# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications. All endpoints are versioned individually to allow for granular upgrades. We follow the [Semantic Versioning scheme](https://semver.org/).  # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Contact: support@stadiamaps.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from stadiamaps import schemas  # noqa: F401


class TraceAttributeKey(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "edge.names": "EDGE_NAMES",
            "edge.length": "EDGE_LENGTH",
            "edge.speed": "EDGE_SPEED",
            "edge.road_class": "EDGE_ROAD_CLASS",
            "edge.begin_heading": "EDGE_BEGIN_HEADING",
            "edge.end_heading": "EDGE_END_HEADING",
            "edge.begin_shape_index": "EDGE_BEGIN_SHAPE_INDEX",
            "edge.end_shape_index": "EDGE_END_SHAPE_INDEX",
            "edge.traversability": "EDGE_TRAVERSABILITY",
            "edge.use": "EDGE_USE",
            "edge.toll": "EDGE_TOLL",
            "edge.unpaved": "EDGE_UNPAVED",
            "edge.tunnel": "EDGE_TUNNEL",
            "edge.bridge": "EDGE_BRIDGE",
            "edge.roundabout": "EDGE_ROUNDABOUT",
            "edge.internal_intersection": "EDGE_INTERNAL_INTERSECTION",
            "edge.drive_on_right": "EDGE_DRIVE_ON_RIGHT",
            "edge.surface": "EDGE_SURFACE",
            "edge.sign.exit_number": "EDGE_SIGN_EXIT_NUMBER",
            "edge.sign.exit_branch": "EDGE_SIGN_EXIT_BRANCH",
            "edge.sign.exit_toward": "EDGE_SIGN_EXIT_TOWARD",
            "edge.sign.exit_name": "EDGE_SIGN_EXIT_NAME",
            "edge.travel_mode": "EDGE_TRAVEL_MODE",
            "edge.vehicle_type": "EDGE_VEHICLE_TYPE",
            "edge.pedestrian_type": "EDGE_PEDESTRIAN_TYPE",
            "edge.bicycle_type": "EDGE_BICYCLE_TYPE",
            "edge.transit_type": "EDGE_TRANSIT_TYPE",
            "edge.id": "EDGE_ID",
            "edge.way_id": "EDGE_WAY_ID",
            "edge.weighted_grade": "EDGE_WEIGHTED_GRADE",
            "edge.max_upward_grade": "EDGE_MAX_UPWARD_GRADE",
            "edge.max_downward_grade": "EDGE_MAX_DOWNWARD_GRADE",
            "edge.mean_elevation": "EDGE_MEAN_ELEVATION",
            "edge.lane_count": "EDGE_LANE_COUNT",
            "edge.cycle_lane": "EDGE_CYCLE_LANE",
            "edge.bicycle_network": "EDGE_BICYCLE_NETWORK",
            "edge.sac_scale": "EDGE_SAC_SCALE",
            "edge.sidewalk": "EDGE_SIDEWALK",
            "edge.density": "EDGE_DENSITY",
            "edge.speed_limit": "EDGE_SPEED_LIMIT",
            "edge.truck_speed": "EDGE_TRUCK_SPEED",
            "edge.truck_route": "EDGE_TRUCK_ROUTE",
            "node.intersecting_edge.begin_heading": "NODE_INTERSECTING_EDGE_BEGIN_HEADING",
            "node.intersecting_edge.from_edge_name_consistency": "NODE_INTERSECTING_EDGE_FROM_EDGE_NAME_CONSISTENCY",
            "node.intersecting_edge.to_edge_name_consistency": "NODE_INTERSECTING_EDGE_TO_EDGE_NAME_CONSISTENCY",
            "node.intersecting_edge.driveability": "NODE_INTERSECTING_EDGE_DRIVEABILITY",
            "node.intersecting_edge.cyclability": "NODE_INTERSECTING_EDGE_CYCLABILITY",
            "node.intersecting_edge.walkability": "NODE_INTERSECTING_EDGE_WALKABILITY",
            "node.intersecting_edge.use": "NODE_INTERSECTING_EDGE_USE",
            "node.intersecting_edge.road_class": "NODE_INTERSECTING_EDGE_ROAD_CLASS",
            "node.elapsed_time": "NODE_ELAPSED_TIME",
            "node.admin_index": "NODE_ADMIN_INDEX",
            "node.type": "NODE_TYPE",
            "node.fork": "NODE_FORK",
            "node.time_zone": "NODE_TIME_ZONE",
            "osm_changeset": "OSM_CHANGESET",
            "shape": "SHAPE",
            "admin.country_code": "ADMIN_COUNTRY_CODE",
            "admin.country_text": "ADMIN_COUNTRY_TEXT",
            "admin.state_code": "ADMIN_STATE_CODE",
            "admin.state_text": "ADMIN_STATE_TEXT",
            "matched.point": "MATCHED_POINT",
            "matched.type": "MATCHED_TYPE",
            "matched.edge_index": "MATCHED_EDGE_INDEX",
            "matched.begin_route_discontinuity": "MATCHED_BEGIN_ROUTE_DISCONTINUITY",
            "matched.end_route_discontinuity": "MATCHED_END_ROUTE_DISCONTINUITY",
            "matched.distance_along_edge": "MATCHED_DISTANCE_ALONG_EDGE",
            "matched.distance_from_trace_point": "MATCHED_DISTANCE_FROM_TRACE_POINT",
        }
    
    @schemas.classproperty
    def EDGE_NAMES(cls):
        return cls("edge.names")
    
    @schemas.classproperty
    def EDGE_LENGTH(cls):
        return cls("edge.length")
    
    @schemas.classproperty
    def EDGE_SPEED(cls):
        return cls("edge.speed")
    
    @schemas.classproperty
    def EDGE_ROAD_CLASS(cls):
        return cls("edge.road_class")
    
    @schemas.classproperty
    def EDGE_BEGIN_HEADING(cls):
        return cls("edge.begin_heading")
    
    @schemas.classproperty
    def EDGE_END_HEADING(cls):
        return cls("edge.end_heading")
    
    @schemas.classproperty
    def EDGE_BEGIN_SHAPE_INDEX(cls):
        return cls("edge.begin_shape_index")
    
    @schemas.classproperty
    def EDGE_END_SHAPE_INDEX(cls):
        return cls("edge.end_shape_index")
    
    @schemas.classproperty
    def EDGE_TRAVERSABILITY(cls):
        return cls("edge.traversability")
    
    @schemas.classproperty
    def EDGE_USE(cls):
        return cls("edge.use")
    
    @schemas.classproperty
    def EDGE_TOLL(cls):
        return cls("edge.toll")
    
    @schemas.classproperty
    def EDGE_UNPAVED(cls):
        return cls("edge.unpaved")
    
    @schemas.classproperty
    def EDGE_TUNNEL(cls):
        return cls("edge.tunnel")
    
    @schemas.classproperty
    def EDGE_BRIDGE(cls):
        return cls("edge.bridge")
    
    @schemas.classproperty
    def EDGE_ROUNDABOUT(cls):
        return cls("edge.roundabout")
    
    @schemas.classproperty
    def EDGE_INTERNAL_INTERSECTION(cls):
        return cls("edge.internal_intersection")
    
    @schemas.classproperty
    def EDGE_DRIVE_ON_RIGHT(cls):
        return cls("edge.drive_on_right")
    
    @schemas.classproperty
    def EDGE_SURFACE(cls):
        return cls("edge.surface")
    
    @schemas.classproperty
    def EDGE_SIGN_EXIT_NUMBER(cls):
        return cls("edge.sign.exit_number")
    
    @schemas.classproperty
    def EDGE_SIGN_EXIT_BRANCH(cls):
        return cls("edge.sign.exit_branch")
    
    @schemas.classproperty
    def EDGE_SIGN_EXIT_TOWARD(cls):
        return cls("edge.sign.exit_toward")
    
    @schemas.classproperty
    def EDGE_SIGN_EXIT_NAME(cls):
        return cls("edge.sign.exit_name")
    
    @schemas.classproperty
    def EDGE_TRAVEL_MODE(cls):
        return cls("edge.travel_mode")
    
    @schemas.classproperty
    def EDGE_VEHICLE_TYPE(cls):
        return cls("edge.vehicle_type")
    
    @schemas.classproperty
    def EDGE_PEDESTRIAN_TYPE(cls):
        return cls("edge.pedestrian_type")
    
    @schemas.classproperty
    def EDGE_BICYCLE_TYPE(cls):
        return cls("edge.bicycle_type")
    
    @schemas.classproperty
    def EDGE_TRANSIT_TYPE(cls):
        return cls("edge.transit_type")
    
    @schemas.classproperty
    def EDGE_ID(cls):
        return cls("edge.id")
    
    @schemas.classproperty
    def EDGE_WAY_ID(cls):
        return cls("edge.way_id")
    
    @schemas.classproperty
    def EDGE_WEIGHTED_GRADE(cls):
        return cls("edge.weighted_grade")
    
    @schemas.classproperty
    def EDGE_MAX_UPWARD_GRADE(cls):
        return cls("edge.max_upward_grade")
    
    @schemas.classproperty
    def EDGE_MAX_DOWNWARD_GRADE(cls):
        return cls("edge.max_downward_grade")
    
    @schemas.classproperty
    def EDGE_MEAN_ELEVATION(cls):
        return cls("edge.mean_elevation")
    
    @schemas.classproperty
    def EDGE_LANE_COUNT(cls):
        return cls("edge.lane_count")
    
    @schemas.classproperty
    def EDGE_CYCLE_LANE(cls):
        return cls("edge.cycle_lane")
    
    @schemas.classproperty
    def EDGE_BICYCLE_NETWORK(cls):
        return cls("edge.bicycle_network")
    
    @schemas.classproperty
    def EDGE_SAC_SCALE(cls):
        return cls("edge.sac_scale")
    
    @schemas.classproperty
    def EDGE_SIDEWALK(cls):
        return cls("edge.sidewalk")
    
    @schemas.classproperty
    def EDGE_DENSITY(cls):
        return cls("edge.density")
    
    @schemas.classproperty
    def EDGE_SPEED_LIMIT(cls):
        return cls("edge.speed_limit")
    
    @schemas.classproperty
    def EDGE_TRUCK_SPEED(cls):
        return cls("edge.truck_speed")
    
    @schemas.classproperty
    def EDGE_TRUCK_ROUTE(cls):
        return cls("edge.truck_route")
    
    @schemas.classproperty
    def NODE_INTERSECTING_EDGE_BEGIN_HEADING(cls):
        return cls("node.intersecting_edge.begin_heading")
    
    @schemas.classproperty
    def NODE_INTERSECTING_EDGE_FROM_EDGE_NAME_CONSISTENCY(cls):
        return cls("node.intersecting_edge.from_edge_name_consistency")
    
    @schemas.classproperty
    def NODE_INTERSECTING_EDGE_TO_EDGE_NAME_CONSISTENCY(cls):
        return cls("node.intersecting_edge.to_edge_name_consistency")
    
    @schemas.classproperty
    def NODE_INTERSECTING_EDGE_DRIVEABILITY(cls):
        return cls("node.intersecting_edge.driveability")
    
    @schemas.classproperty
    def NODE_INTERSECTING_EDGE_CYCLABILITY(cls):
        return cls("node.intersecting_edge.cyclability")
    
    @schemas.classproperty
    def NODE_INTERSECTING_EDGE_WALKABILITY(cls):
        return cls("node.intersecting_edge.walkability")
    
    @schemas.classproperty
    def NODE_INTERSECTING_EDGE_USE(cls):
        return cls("node.intersecting_edge.use")
    
    @schemas.classproperty
    def NODE_INTERSECTING_EDGE_ROAD_CLASS(cls):
        return cls("node.intersecting_edge.road_class")
    
    @schemas.classproperty
    def NODE_ELAPSED_TIME(cls):
        return cls("node.elapsed_time")
    
    @schemas.classproperty
    def NODE_ADMIN_INDEX(cls):
        return cls("node.admin_index")
    
    @schemas.classproperty
    def NODE_TYPE(cls):
        return cls("node.type")
    
    @schemas.classproperty
    def NODE_FORK(cls):
        return cls("node.fork")
    
    @schemas.classproperty
    def NODE_TIME_ZONE(cls):
        return cls("node.time_zone")
    
    @schemas.classproperty
    def OSM_CHANGESET(cls):
        return cls("osm_changeset")
    
    @schemas.classproperty
    def SHAPE(cls):
        return cls("shape")
    
    @schemas.classproperty
    def ADMIN_COUNTRY_CODE(cls):
        return cls("admin.country_code")
    
    @schemas.classproperty
    def ADMIN_COUNTRY_TEXT(cls):
        return cls("admin.country_text")
    
    @schemas.classproperty
    def ADMIN_STATE_CODE(cls):
        return cls("admin.state_code")
    
    @schemas.classproperty
    def ADMIN_STATE_TEXT(cls):
        return cls("admin.state_text")
    
    @schemas.classproperty
    def MATCHED_POINT(cls):
        return cls("matched.point")
    
    @schemas.classproperty
    def MATCHED_TYPE(cls):
        return cls("matched.type")
    
    @schemas.classproperty
    def MATCHED_EDGE_INDEX(cls):
        return cls("matched.edge_index")
    
    @schemas.classproperty
    def MATCHED_BEGIN_ROUTE_DISCONTINUITY(cls):
        return cls("matched.begin_route_discontinuity")
    
    @schemas.classproperty
    def MATCHED_END_ROUTE_DISCONTINUITY(cls):
        return cls("matched.end_route_discontinuity")
    
    @schemas.classproperty
    def MATCHED_DISTANCE_ALONG_EDGE(cls):
        return cls("matched.distance_along_edge")
    
    @schemas.classproperty
    def MATCHED_DISTANCE_FROM_TRACE_POINT(cls):
        return cls("matched.distance_from_trace_point")
