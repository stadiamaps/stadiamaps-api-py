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


from typing import List, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, validator

class GeoJSONPolygon(BaseModel):
    """
    GeoJSONPolygon
    """
    type: StrictStr = Field(...)
    coordinates: conlist(conlist(conlist(Union[StrictFloat, StrictInt], max_items=3, min_items=2))) = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["type", "coordinates"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Point', 'MultiPoint', 'LineString', 'MultiLineString', 'Polygon', 'MultiPolygon'):
            raise ValueError("must be one of enum values ('Point', 'MultiPoint', 'LineString', 'MultiLineString', 'Polygon', 'MultiPolygon')")
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
    def from_json(cls, json_str: str) -> GeoJSONPolygon:
        """Create an instance of GeoJSONPolygon from a JSON string"""
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
    def from_dict(cls, obj: dict) -> GeoJSONPolygon:
        """Create an instance of GeoJSONPolygon from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GeoJSONPolygon.parse_obj(obj)

        _obj = GeoJSONPolygon.parse_obj({
            "type": obj.get("type"),
            "coordinates": obj.get("coordinates")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

