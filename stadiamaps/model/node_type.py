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


class NodeType(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        enum_value_to_name = {
            "street_intersection": "STREET_INTERSECTION",
            "gate": "GATE",
            "bollard": "BOLLARD",
            "toll_booth": "TOLL_BOOTH",
            "multi_use_transit_stop": "MULTI_USE_TRANSIT_STOP",
            "bike_share": "BIKE_SHARE",
            "parking": "PARKING",
            "motor_way_junction": "MOTOR_WAY_JUNCTION",
            "border_control": "BORDER_CONTROL",
        }
    
    @schemas.classproperty
    def STREET_INTERSECTION(cls):
        return cls("street_intersection")
    
    @schemas.classproperty
    def GATE(cls):
        return cls("gate")
    
    @schemas.classproperty
    def BOLLARD(cls):
        return cls("bollard")
    
    @schemas.classproperty
    def TOLL_BOOTH(cls):
        return cls("toll_booth")
    
    @schemas.classproperty
    def MULTI_USE_TRANSIT_STOP(cls):
        return cls("multi_use_transit_stop")
    
    @schemas.classproperty
    def BIKE_SHARE(cls):
        return cls("bike_share")
    
    @schemas.classproperty
    def PARKING(cls):
        return cls("parking")
    
    @schemas.classproperty
    def MOTOR_WAY_JUNCTION(cls):
        return cls("motor_way_junction")
    
    @schemas.classproperty
    def BORDER_CONTROL(cls):
        return cls("border_control")
