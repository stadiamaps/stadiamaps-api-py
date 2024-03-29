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


from typing import List
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from stadiamaps.models.route_leg import RouteLeg
from stadiamaps.models.route_summary import RouteSummary
from stadiamaps.models.routing_response_waypoint import RoutingResponseWaypoint
from stadiamaps.models.valhalla_languages import ValhallaLanguages
from stadiamaps.models.valhalla_long_units import ValhallaLongUnits

class RouteResponseTrip(BaseModel):
    """
    RouteResponseTrip
    """
    status: StrictInt = Field(..., description="The response status code")
    status_message: StrictStr = Field(..., description="The response status message")
    units: ValhallaLongUnits = Field(...)
    language: ValhallaLanguages = Field(...)
    locations: conlist(RoutingResponseWaypoint) = Field(...)
    legs: conlist(RouteLeg) = Field(...)
    summary: RouteSummary = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["status", "status_message", "units", "language", "locations", "legs", "summary"]

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
    def from_json(cls, json_str: str) -> RouteResponseTrip:
        """Create an instance of RouteResponseTrip from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item in self.locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in legs (list)
        _items = []
        if self.legs:
            for _item in self.legs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['legs'] = _items
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RouteResponseTrip:
        """Create an instance of RouteResponseTrip from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RouteResponseTrip.parse_obj(obj)

        _obj = RouteResponseTrip.parse_obj({
            "status": obj.get("status"),
            "status_message": obj.get("status_message"),
            "units": obj.get("units"),
            "language": obj.get("language"),
            "locations": [RoutingResponseWaypoint.from_dict(_item) for _item in obj.get("locations")] if obj.get("locations") is not None else None,
            "legs": [RouteLeg.from_dict(_item) for _item in obj.get("legs")] if obj.get("legs") is not None else None,
            "summary": RouteSummary.from_dict(obj.get("summary")) if obj.get("summary") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

