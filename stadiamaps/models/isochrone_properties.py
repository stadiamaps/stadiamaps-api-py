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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, validator

class IsochroneProperties(BaseModel):
    """
    IsochroneProperties
    """
    fill_color: Optional[StrictStr] = Field(None, alias="fillColor")
    opacity: Optional[Union[StrictFloat, StrictInt]] = None
    fill: Optional[StrictStr] = None
    fill_opacity: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="fillOpacity")
    color: Optional[StrictStr] = None
    contour: Optional[Union[StrictFloat, StrictInt]] = None
    metric: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["fillColor", "opacity", "fill", "fillOpacity", "color", "contour", "metric"]

    @validator('metric')
    def metric_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('time', 'distance'):
            raise ValueError("must be one of enum values ('time', 'distance')")
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
    def from_json(cls, json_str: str) -> IsochroneProperties:
        """Create an instance of IsochroneProperties from a JSON string"""
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
    def from_dict(cls, obj: dict) -> IsochroneProperties:
        """Create an instance of IsochroneProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return IsochroneProperties.parse_obj(obj)

        _obj = IsochroneProperties.parse_obj({
            "fill_color": obj.get("fillColor"),
            "opacity": obj.get("opacity"),
            "fill": obj.get("fill"),
            "fill_opacity": obj.get("fillOpacity"),
            "color": obj.get("color"),
            "contour": obj.get("contour"),
            "metric": obj.get("metric")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

