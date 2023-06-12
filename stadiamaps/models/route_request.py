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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from stadiamaps.models.costing_model import CostingModel
from stadiamaps.models.costing_options import CostingOptions
from stadiamaps.models.directions_options import DirectionsOptions
from stadiamaps.models.routing_waypoint import RoutingWaypoint

class RouteRequest(BaseModel):
    """
    RouteRequest
    """
    id: Optional[StrictStr] = Field(None, description="An identifier to disambiguate requests (echoed by the server).")
    locations: conlist(RoutingWaypoint, min_items=2) = Field(...)
    costing: CostingModel = Field(...)
    costing_options: Optional[CostingOptions] = None
    avoid_locations: Optional[conlist(RoutingWaypoint)] = None
    avoid_polygons: Optional[conlist(conlist(conlist(Union[StrictFloat, StrictInt])))] = Field(None, description="One or multiple exterior rings of polygons in the form of nested JSON arrays. Roads intersecting these rings will be avoided during path finding. Open rings will be closed automatically.")
    directions_options: Optional[DirectionsOptions] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "locations", "costing", "costing_options", "avoid_locations", "avoid_polygons", "directions_options"]

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
    def from_json(cls, json_str: str) -> RouteRequest:
        """Create an instance of RouteRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of costing_options
        if self.costing_options:
            _dict['costing_options'] = self.costing_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in avoid_locations (list)
        _items = []
        if self.avoid_locations:
            for _item in self.avoid_locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['avoid_locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of directions_options
        if self.directions_options:
            _dict['directions_options'] = self.directions_options.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RouteRequest:
        """Create an instance of RouteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RouteRequest.parse_obj(obj)

        _obj = RouteRequest.parse_obj({
            "id": obj.get("id"),
            "locations": [RoutingWaypoint.from_dict(_item) for _item in obj.get("locations")] if obj.get("locations") is not None else None,
            "costing": obj.get("costing"),
            "costing_options": CostingOptions.from_dict(obj.get("costing_options")) if obj.get("costing_options") is not None else None,
            "avoid_locations": [RoutingWaypoint.from_dict(_item) for _item in obj.get("avoid_locations")] if obj.get("avoid_locations") is not None else None,
            "avoid_polygons": obj.get("avoid_polygons"),
            "directions_options": DirectionsOptions.from_dict(obj.get("directions_options")) if obj.get("directions_options") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

