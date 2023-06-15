# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.3
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class RoadClass(str, Enum):
    """
    Class of road (ranked in descending order)
    """

    """
    allowed enum values
    """
    MOTORWAY = 'motorway'
    TRUNK = 'trunk'
    PRIMARY = 'primary'
    SECONDARY = 'secondary'
    TERTIARY = 'tertiary'
    UNCLASSIFIED = 'unclassified'
    RESIDENTIAL = 'residential'
    SERVICE_OTHER = 'service_other'

    @classmethod
    def from_json(cls, json_str: str) -> RoadClass:
        """Create an instance of RoadClass from a JSON string"""
        return RoadClass(json.loads(json_str))


