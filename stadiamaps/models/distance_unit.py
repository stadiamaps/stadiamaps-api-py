# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.2
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class DistanceUnit(str, Enum):
    """
    DistanceUnit
    """

    """
    allowed enum values
    """
    KM = 'km'
    MI = 'mi'

    @classmethod
    def from_json(cls, json_str: str) -> DistanceUnit:
        """Create an instance of DistanceUnit from a JSON string"""
        return DistanceUnit(json.loads(json_str))


