# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.1
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from stadiamaps.models.distance_unit import DistanceUnit
from stadiamaps.models.valhalla_languages import ValhallaLanguages

class DirectionsOptions(BaseModel):
    """
    DirectionsOptions
    """
    units: Optional[DistanceUnit] = None
    language: Optional[ValhallaLanguages] = None
    directions_type: Optional[StrictStr] = Field('instructions', description="The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["units", "language", "directions_type"]

    @validator('directions_type')
    def directions_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('none', 'maneuvers', 'instructions'):
            raise ValueError("must be one of enum values ('none', 'maneuvers', 'instructions')")
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
    def from_json(cls, json_str: str) -> DirectionsOptions:
        """Create an instance of DirectionsOptions from a JSON string"""
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
    def from_dict(cls, obj: dict) -> DirectionsOptions:
        """Create an instance of DirectionsOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return DirectionsOptions.parse_obj(obj)

        _obj = DirectionsOptions.parse_obj({
            "units": obj.get("units"),
            "language": obj.get("language"),
            "directions_type": obj.get("directions_type") if obj.get("directions_type") is not None else 'instructions'
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

