# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.5
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class MapMatchCostingModel(str, Enum):
    """
    MapMatchCostingModel
    """

    """
    allowed enum values
    """
    AUTO = 'auto'
    BICYCLE = 'bicycle'
    BUS = 'bus'
    PEDESTRIAN = 'pedestrian'

    @classmethod
    def from_json(cls, json_str: str) -> MapMatchCostingModel:
        """Create an instance of MapMatchCostingModel from a JSON string"""
        return MapMatchCostingModel(json.loads(json_str))


