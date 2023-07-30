# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.6
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool

class Access(BaseModel):
    """
    Access
    """
    golf_cart: Optional[StrictBool] = None
    wheelchair: Optional[StrictBool] = None
    taxi: Optional[StrictBool] = None
    hov: Optional[StrictBool] = Field(None, alias="HOV")
    truck: Optional[StrictBool] = None
    emergency: Optional[StrictBool] = None
    pedestrian: Optional[StrictBool] = None
    car: Optional[StrictBool] = None
    bus: Optional[StrictBool] = None
    bicycle: Optional[StrictBool] = None
    motorcycle: Optional[StrictBool] = None
    moped: Optional[StrictBool] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["golf_cart", "wheelchair", "taxi", "HOV", "truck", "emergency", "pedestrian", "car", "bus", "bicycle", "motorcycle", "moped"]

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
    def from_json(cls, json_str: str) -> Access:
        """Create an instance of Access from a JSON string"""
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
    def from_dict(cls, obj: dict) -> Access:
        """Create an instance of Access from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Access.parse_obj(obj)

        _obj = Access.parse_obj({
            "golf_cart": obj.get("golf_cart"),
            "wheelchair": obj.get("wheelchair"),
            "taxi": obj.get("taxi"),
            "hov": obj.get("HOV"),
            "truck": obj.get("truck"),
            "emergency": obj.get("emergency"),
            "pedestrian": obj.get("pedestrian"),
            "car": obj.get("car"),
            "bus": obj.get("bus"),
            "bicycle": obj.get("bicycle"),
            "motorcycle": obj.get("motorcycle"),
            "moped": obj.get("moped")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

