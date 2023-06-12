# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.2
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr

class ManeuverSignElement(BaseModel):
    """
    ManeuverSignElement
    """
    text: StrictStr = Field(..., description="The interchange sign text (varies based on the context; see the `maneuverSign` schema).")
    is_route_number: Optional[StrictBool] = Field(None, description="True if the sign is a route number.")
    consecutive_count: Optional[StrictInt] = Field(None, description="The frequency of this sign element within a set a consecutive signs.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["text", "is_route_number", "consecutive_count"]

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
    def from_json(cls, json_str: str) -> ManeuverSignElement:
        """Create an instance of ManeuverSignElement from a JSON string"""
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
    def from_dict(cls, obj: dict) -> ManeuverSignElement:
        """Create an instance of ManeuverSignElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ManeuverSignElement.parse_obj(obj)

        _obj = ManeuverSignElement.parse_obj({
            "text": obj.get("text"),
            "is_route_number": obj.get("is_route_number"),
            "consecutive_count": obj.get("consecutive_count")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

