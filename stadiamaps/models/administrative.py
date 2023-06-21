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

class Administrative(BaseModel):
    """
    Administrative
    """
    iso_3166_1: Optional[StrictStr] = Field(None, alias="iso_3166-1", description="The ISO 3166-1 alpha-2 country code of the administrative region.")
    country: Optional[StrictStr] = Field(None, description="The full country name.")
    iso_3166_2: Optional[StrictStr] = Field(None, alias="iso_3166-2", description="The ISO 3166-2 code identifying the principal subdivision (ex: provinces or states) within a country.")
    state: Optional[StrictStr] = Field(None, description="The full state or province name.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["iso_3166-1", "country", "iso_3166-2", "state"]

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
    def from_json(cls, json_str: str) -> Administrative:
        """Create an instance of Administrative from a JSON string"""
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
    def from_dict(cls, obj: dict) -> Administrative:
        """Create an instance of Administrative from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Administrative.parse_obj(obj)

        _obj = Administrative.parse_obj({
            "iso_3166_1": obj.get("iso_3166-1"),
            "country": obj.get("country"),
            "iso_3166_2": obj.get("iso_3166-2"),
            "state": obj.get("state")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

