# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.3
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conint, validator

class RoutingResponseWaypoint(BaseModel):
    """
    RoutingResponseWaypoint
    """
    lat: Union[StrictFloat, StrictInt] = Field(..., description="The latitude of a point in the shape.")
    lon: Union[StrictFloat, StrictInt] = Field(..., description="The longitude of a point in the shape.")
    type: Optional[StrictStr] = Field('break', description="A `break` represents the start or end of a leg, and allows reversals. A `through` location is an intermediate waypoint that must be visited between `break`s, but at which reversals are not allowed. A `via` is similar to a `through` except that reversals are allowed. A `break_through` is similar to a `break` in that it can be the start/end of a leg, but does not allow reversals.")
    original_index: Optional[conint(strict=True, ge=0)] = Field(None, description="The original index of the location (locations may be reordered for optimized routes)")
    additional_properties: Dict[str, Any] = {}
    __properties = ["lat", "lon", "type", "original_index"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('break', 'through', 'via', 'break_through'):
            raise ValueError("must be one of enum values ('break', 'through', 'via', 'break_through')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> RoutingResponseWaypoint:
        """Create an instance of RoutingResponseWaypoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoutingResponseWaypoint:
        """Create an instance of RoutingResponseWaypoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoutingResponseWaypoint.parse_obj(obj)

        _obj = RoutingResponseWaypoint.parse_obj({
            "lat": obj.get("lat"),
            "lon": obj.get("lon"),
            "type": obj.get("type") if obj.get("type") is not None else 'break',
            "original_index": obj.get("original_index")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

