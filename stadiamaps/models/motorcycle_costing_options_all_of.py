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


from typing import Optional, Union
from pydantic import BaseModel, Field, confloat, conint

class MotorcycleCostingOptionsAllOf(BaseModel):
    """
    MotorcycleCostingOptionsAllOf
    """
    use_highways: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(1.0, description="A measure of willingness to use highways. Values near 0 attempt to avoid highways and stay on roads with lower speeds, and values near 1 indicate the rider is more comfortable on these roads.")
    use_trails: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(0.0, description="A measure of the rider's sense of adventure. Values near 0 attempt to avoid highways and stay on roads with potentially unsuitable terrain (trails, tracks, unclassified, or bad surfaces), and values near 1 will tend to avoid major roads and route on secondary roads.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["use_highways", "use_trails"]

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
    def from_json(cls, json_str: str) -> MotorcycleCostingOptionsAllOf:
        """Create an instance of MotorcycleCostingOptionsAllOf from a JSON string"""
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
    def from_dict(cls, obj: dict) -> MotorcycleCostingOptionsAllOf:
        """Create an instance of MotorcycleCostingOptionsAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MotorcycleCostingOptionsAllOf.parse_obj(obj)

        _obj = MotorcycleCostingOptionsAllOf.parse_obj({
            "use_highways": obj.get("use_highways") if obj.get("use_highways") is not None else 1.0,
            "use_trails": obj.get("use_trails") if obj.get("use_trails") is not None else 0.0
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

