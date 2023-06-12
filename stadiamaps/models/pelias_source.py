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





class PeliasSource(str, Enum):
    """
    Our database contains info from multiple sources. These identifiers can be used to either limit search results or to determine the relevance of a result.
    """

    """
    allowed enum values
    """
    OPENSTREETMAP = 'openstreetmap'
    OPENADDRESSES = 'openaddresses'
    WHOSONFIRST = 'whosonfirst'
    GEONAMES = 'geonames'

    @classmethod
    def from_json(cls, json_str: str) -> PeliasSource:
        """Create an instance of PeliasSource from a JSON string"""
        return PeliasSource(json.loads(json_str))


