# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.5
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, validator

class Speeds(BaseModel):
    """
    Speeds
    """
    predicted: Optional[StrictBool] = Field(None, description="Does this edge have predicted (historical) speed records?")
    constrained_flow: Optional[StrictInt] = Field(None, description="Speed when there is no traffic, in kph.")
    free_flow: Optional[StrictInt] = Field(None, description="Speed when there is heavy traffic, in kph.")
    type: Optional[StrictStr] = Field(None, description="The type of speed which is used when setting default speeds. When `tagged`, the explicit `max_speed` tags from OpenStreetMap are being used. When `classified`, the values are being inferred from the highway classification.")
    default: Optional[StrictInt] = Field(None, description="The default speed used for calculations. NOTE: Values greater than 250 are used for special cases and should not be treated as literal.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["predicted", "constrained_flow", "free_flow", "type", "default"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('classified', 'tagged'):
            raise ValueError("must be one of enum values ('classified', 'tagged')")
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
    def from_json(cls, json_str: str) -> Speeds:
        """Create an instance of Speeds from a JSON string"""
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
    def from_dict(cls, obj: dict) -> Speeds:
        """Create an instance of Speeds from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Speeds.parse_obj(obj)

        _obj = Speeds.parse_obj({
            "predicted": obj.get("predicted"),
            "constrained_flow": obj.get("constrained_flow"),
            "free_flow": obj.get("free_flow"),
            "type": obj.get("type"),
            "default": obj.get("default")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

