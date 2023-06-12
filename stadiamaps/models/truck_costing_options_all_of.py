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
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt

class TruckCostingOptionsAllOf(BaseModel):
    """
    TruckCostingOptionsAllOf
    """
    height: Optional[Union[StrictFloat, StrictInt]] = Field(4.11, description="The height of the truck (in meters).")
    width: Optional[Union[StrictFloat, StrictInt]] = Field(2.6, description="The width of the truck (in meters).")
    length: Optional[Union[StrictFloat, StrictInt]] = Field(21.64, description="The length of the truck (in meters).")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(21.77, description="The weight of the truck (in tonnes).")
    axle_load: Optional[Union[StrictFloat, StrictInt]] = Field(9.07, description="The axle load of the truck (in tonnes).")
    hazmat: Optional[StrictBool] = Field(False, description="Whether or not the truck is carrying hazardous materials.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["height", "width", "length", "weight", "axle_load", "hazmat"]

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
    def from_json(cls, json_str: str) -> TruckCostingOptionsAllOf:
        """Create an instance of TruckCostingOptionsAllOf from a JSON string"""
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
    def from_dict(cls, obj: dict) -> TruckCostingOptionsAllOf:
        """Create an instance of TruckCostingOptionsAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TruckCostingOptionsAllOf.parse_obj(obj)

        _obj = TruckCostingOptionsAllOf.parse_obj({
            "height": obj.get("height") if obj.get("height") is not None else 4.11,
            "width": obj.get("width") if obj.get("width") is not None else 2.6,
            "length": obj.get("length") if obj.get("length") is not None else 21.64,
            "weight": obj.get("weight") if obj.get("weight") is not None else 21.77,
            "axle_load": obj.get("axle_load") if obj.get("axle_load") is not None else 9.07,
            "hazmat": obj.get("hazmat") if obj.get("hazmat") is not None else False
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

