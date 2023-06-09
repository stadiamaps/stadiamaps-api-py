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





class ValhallaLongUnits(str, Enum):
    """
    ValhallaLongUnits
    """

    """
    allowed enum values
    """
    MILES = 'miles'
    KILOMETERS = 'kilometers'

    @classmethod
    def from_json(cls, json_str: str) -> ValhallaLongUnits:
        """Create an instance of ValhallaLongUnits from a JSON string"""
        return ValhallaLongUnits(json.loads(json_str))


