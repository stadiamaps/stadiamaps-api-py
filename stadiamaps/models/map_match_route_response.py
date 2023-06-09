# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.5
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from stadiamaps.models.route_response_trip import RouteResponseTrip

class MapMatchRouteResponse(BaseModel):
    """
    MapMatchRouteResponse
    """
    id: Optional[StrictStr] = Field(None, description="An identifier to disambiguate requests (echoed by the server).")
    trip: RouteResponseTrip = Field(...)
    linear_references: Optional[conlist(StrictStr)] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "trip", "linear_references"]

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
    def from_json(cls, json_str: str) -> MapMatchRouteResponse:
        """Create an instance of MapMatchRouteResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of trip
        if self.trip:
            _dict['trip'] = self.trip.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MapMatchRouteResponse:
        """Create an instance of MapMatchRouteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MapMatchRouteResponse.parse_obj(obj)

        _obj = MapMatchRouteResponse.parse_obj({
            "id": obj.get("id"),
            "trip": RouteResponseTrip.from_dict(obj.get("trip")) if obj.get("trip") is not None else None,
            "linear_references": obj.get("linear_references")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

