# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 6.6.2
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class MatrixCostingModel(str, Enum):
    """
    MatrixCostingModel
    """

    """
    allowed enum values
    """
    AUTO = 'auto'
    BUS = 'bus'
    TAXI = 'taxi'
    TRUCK = 'truck'
    BICYCLE = 'bicycle'
    BIKESHARE = 'bikeshare'
    MOTOR_SCOOTER = 'motor_scooter'
    MOTORCYCLE = 'motorcycle'
    PEDESTRIAN = 'pedestrian'
    LOW_SPEED_VEHICLE = 'low_speed_vehicle'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MatrixCostingModel from a JSON string"""
        return cls(json.loads(json_str))


