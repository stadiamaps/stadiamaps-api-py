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


class CostingModel(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Costing models for determining the most optimal route to take. Note that bikeshare and motorcycle are still in beta. While Valhalla supports multimodal routing, we do not currently process transit data and have excluded it from the list. See https://valhalla.readthedocs.io/en/latest/api/turn-by-turn/api-reference/#costing-models for detailed descriptions of each model.
    """
    
    @schemas.classproperty
    def AUTO(cls):
        return cls("auto")
    
    @schemas.classproperty
    def BUS(cls):
        return cls("bus")
    
    @schemas.classproperty
    def TAXI(cls):
        return cls("taxi")
    
    @schemas.classproperty
    def TRUCK(cls):
        return cls("truck")
    
    @schemas.classproperty
    def BICYCLE(cls):
        return cls("bicycle")
    
    @schemas.classproperty
    def BIKESHARE(cls):
        return cls("bikeshare")
    
    @schemas.classproperty
    def MOTOR_SCOOTER(cls):
        return cls("motor_scooter")
    
    @schemas.classproperty
    def MOTORCYCLE(cls):
        return cls("motorcycle")
    
    @schemas.classproperty
    def PEDESTRIAN(cls):
        return cls("pedestrian")
