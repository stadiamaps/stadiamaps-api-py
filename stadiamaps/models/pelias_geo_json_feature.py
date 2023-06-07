# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.1
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from stadiamaps.models.geo_json_point import GeoJSONPoint
from stadiamaps.models.pelias_geo_json_properties import PeliasGeoJSONProperties

class PeliasGeoJSONFeature(BaseModel):
    """
    PeliasGeoJSONFeature
    """
    type: StrictStr = Field(...)
    geometry: GeoJSONPoint = Field(...)
    properties: Optional[PeliasGeoJSONProperties] = None
    id: Optional[StrictStr] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["type", "geometry", "properties", "id"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('Feature'):
            raise ValueError("must be one of enum values ('Feature')")
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
    def from_json(cls, json_str: str) -> PeliasGeoJSONFeature:
        """Create an instance of PeliasGeoJSONFeature from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of geometry
        if self.geometry:
            _dict['geometry'] = self.geometry.to_dict()
        # override the default output from pydantic by calling `to_dict()` of properties
        if self.properties:
            _dict['properties'] = self.properties.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PeliasGeoJSONFeature:
        """Create an instance of PeliasGeoJSONFeature from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PeliasGeoJSONFeature.parse_obj(obj)

        _obj = PeliasGeoJSONFeature.parse_obj({
            "type": obj.get("type"),
            "geometry": GeoJSONPoint.from_dict(obj.get("geometry")) if obj.get("geometry") is not None else None,
            "properties": PeliasGeoJSONProperties.from_dict(obj.get("properties")) if obj.get("properties") is not None else None,
            "id": obj.get("id")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

