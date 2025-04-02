# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 9.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class RoutingLongUnits(str, Enum):
    """
    RoutingLongUnits
    """

    """
    allowed enum values
    """
    MILES = 'miles'
    KILOMETERS = 'kilometers'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RoutingLongUnits from a JSON string"""
        return cls(json.loads(json_str))


