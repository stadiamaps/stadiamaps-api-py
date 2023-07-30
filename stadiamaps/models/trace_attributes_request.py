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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from stadiamaps.models.costing_options import CostingOptions
from stadiamaps.models.directions_options import DirectionsOptions
from stadiamaps.models.map_match_costing_model import MapMatchCostingModel
from stadiamaps.models.map_match_waypoint import MapMatchWaypoint
from stadiamaps.models.trace_attributes_request_all_of_filters import TraceAttributesRequestAllOfFilters

class TraceAttributesRequest(BaseModel):
    """
    TraceAttributesRequest
    """
    id: Optional[StrictStr] = Field(None, description="An identifier to disambiguate requests (echoed by the server).")
    shape: Optional[conlist(MapMatchWaypoint)] = Field(None, description="REQUIRED if `encoded_polyline` is not present. Note that `break` type locations are only supported when `shape_match` is set to `map_match`.")
    encoded_polyline: Optional[StrictStr] = Field(None, description="REQUIRED if `shape` is not present. An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm). Note that the polyline must be encoded with 6 digits of precision rather than the usual 5.")
    costing: MapMatchCostingModel = Field(...)
    costing_options: Optional[CostingOptions] = None
    shape_match: Optional[StrictStr] = Field(None, description="Three snapping modes provide some control over how the map matching occurs. `edge_walk` is fast, but requires extremely precise data that matches the route graph almost perfectly. `map_snap` can handle significantly noisier data, but is very expensive. `walk_or_snap`, the default, tries to use edge walking first and falls back to map matching if edge walking fails. In general, you should not need to change this parameter unless you want to trace a multi-leg route with multiple `break` locations in the `shape`.")
    directions_options: Optional[DirectionsOptions] = None
    filters: Optional[TraceAttributesRequestAllOfFilters] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "shape", "encoded_polyline", "costing", "costing_options", "shape_match", "directions_options", "filters"]

    @validator('shape_match')
    def shape_match_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('edge_walk', 'map_snap', 'walk_or_snap'):
            raise ValueError("must be one of enum values ('edge_walk', 'map_snap', 'walk_or_snap')")
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
    def from_json(cls, json_str: str) -> TraceAttributesRequest:
        """Create an instance of TraceAttributesRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in shape (list)
        _items = []
        if self.shape:
            for _item in self.shape:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shape'] = _items
        # override the default output from pydantic by calling `to_dict()` of costing_options
        if self.costing_options:
            _dict['costing_options'] = self.costing_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of directions_options
        if self.directions_options:
            _dict['directions_options'] = self.directions_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TraceAttributesRequest:
        """Create an instance of TraceAttributesRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TraceAttributesRequest.parse_obj(obj)

        _obj = TraceAttributesRequest.parse_obj({
            "id": obj.get("id"),
            "shape": [MapMatchWaypoint.from_dict(_item) for _item in obj.get("shape")] if obj.get("shape") is not None else None,
            "encoded_polyline": obj.get("encoded_polyline"),
            "costing": obj.get("costing"),
            "costing_options": CostingOptions.from_dict(obj.get("costing_options")) if obj.get("costing_options") is not None else None,
            "shape_match": obj.get("shape_match"),
            "directions_options": DirectionsOptions.from_dict(obj.get("directions_options")) if obj.get("directions_options") is not None else None,
            "filters": TraceAttributesRequestAllOfFilters.from_dict(obj.get("filters")) if obj.get("filters") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

