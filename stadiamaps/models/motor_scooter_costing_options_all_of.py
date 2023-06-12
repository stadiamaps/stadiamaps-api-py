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


from typing import Optional, Union
from pydantic import BaseModel, Field, confloat, conint

class MotorScooterCostingOptionsAllOf(BaseModel):
    """
    MotorScooterCostingOptionsAllOf
    """
    use_primary: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(0.5, description="A measure of willingness to use primary roads. Values near 0 attempt to avoid primary roads and stay on roads with lower speeds, and values near 1 indicate the rider is more comfortable on these roads.")
    use_hills: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(0.5, description="A measure of willingness to take tackle hills. Values near 0 attempt to avoid hills and steeper grades even if it means a longer route, and values near 1 indicates that the rider does not fear them. Note that as some routes may be impossible without hills, 0 does not guarantee avoidance of them.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["use_primary", "use_hills"]

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
    def from_json(cls, json_str: str) -> MotorScooterCostingOptionsAllOf:
        """Create an instance of MotorScooterCostingOptionsAllOf from a JSON string"""
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
    def from_dict(cls, obj: dict) -> MotorScooterCostingOptionsAllOf:
        """Create an instance of MotorScooterCostingOptionsAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MotorScooterCostingOptionsAllOf.parse_obj(obj)

        _obj = MotorScooterCostingOptionsAllOf.parse_obj({
            "use_primary": obj.get("use_primary") if obj.get("use_primary") is not None else 0.5,
            "use_hills": obj.get("use_hills") if obj.get("use_hills") is not None else 0.5
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

