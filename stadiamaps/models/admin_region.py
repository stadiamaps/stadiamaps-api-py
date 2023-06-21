# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.4
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr

class AdminRegion(BaseModel):
    """
    AdminRegion
    """
    country_code: Optional[StrictStr] = Field(None, description="The [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code.")
    country_text: Optional[StrictStr] = Field(None, description="The country name")
    state_code: Optional[StrictStr] = Field(None, description="The abbreviation code for the state (varies by country).")
    state_text: Optional[StrictStr] = Field(None, description="The state name.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["country_code", "country_text", "state_code", "state_text"]

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
    def from_json(cls, json_str: str) -> AdminRegion:
        """Create an instance of AdminRegion from a JSON string"""
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
    def from_dict(cls, obj: dict) -> AdminRegion:
        """Create an instance of AdminRegion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AdminRegion.parse_obj(obj)

        _obj = AdminRegion.parse_obj({
            "country_code": obj.get("country_code"),
            "country_text": obj.get("country_text"),
            "state_code": obj.get("state_code"),
            "state_text": obj.get("state_text")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

