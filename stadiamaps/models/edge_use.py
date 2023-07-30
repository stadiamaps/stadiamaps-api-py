# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.6
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class EdgeUse(str, Enum):
    """
    The use for the edge.
    """

    """
    allowed enum values
    """
    ROAD = 'road'
    RAMP = 'ramp'
    TURN_CHANNEL = 'turn_channel'
    TRACK = 'track'
    DRIVEWAY = 'driveway'
    ALLEY = 'alley'
    PARKING_AISLE = 'parking_aisle'
    EMERGENCY_ACCESS = 'emergency_access'
    DRIVE_THROUGH = 'drive_through'
    CULDESAC = 'culdesac'
    LIVING_STREET = 'living_street'
    SERVICE_ROAD = 'service_road'
    CYCLEWAY = 'cycleway'
    MOUNTAIN_BIKE = 'mountain_bike'
    SIDEWALK = 'sidewalk'
    FOOTWAY = 'footway'
    STEPS = 'steps'
    PATH = 'path'
    PEDESTRIAN = 'pedestrian'
    PEDESTRIAN_CROSSING = 'pedestrian_crossing'
    BRIDLEWAY = 'bridleway'
    REST_AREA = 'rest_area'
    SERVICE_AREA = 'service_area'
    OTHER = 'other'
    FERRY = 'ferry'
    RAIL_MINUS_FERRY = 'rail-ferry'
    RAIL = 'rail'
    BUS = 'bus'
    EGRESS_CONNECTION = 'egress_connection'
    PLATFORM_CONNECTION = 'platform_connection'
    TRANSIT_CONNECTION = 'transit_connection'

    @classmethod
    def from_json(cls, json_str: str) -> EdgeUse:
        """Create an instance of EdgeUse from a JSON string"""
        return EdgeUse(json.loads(json_str))


