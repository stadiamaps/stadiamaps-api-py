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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictInt, StrictStr, confloat, conint, conlist
from stadiamaps.models.admin_region import AdminRegion
from stadiamaps.models.matched_point import MatchedPoint
from stadiamaps.models.trace_edge import TraceEdge

class TraceAttributesBaseResponse(BaseModel):
    """
    TraceAttributesBaseResponse
    """
    edges: Optional[conlist(TraceEdge)] = Field(None, description="The list of edges matched along the path.")
    admins: Optional[conlist(AdminRegion)] = Field(None, description="The set of administrative regions matched along the path. Rather than repeating this information for every end node, the admins in this list are referenced by index.")
    matched_points: Optional[conlist(MatchedPoint)] = Field(None, description="List of match results when using the map_snap shape match algorithm. There is a one-to-one correspondence with the input set of latitude, longitude coordinates and this list of match results.")
    osm_changeset: Optional[StrictInt] = None
    shape: Optional[StrictStr] = Field(None, description="The encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm) of the matched path.")
    confidence_score: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["edges", "admins", "matched_points", "osm_changeset", "shape", "confidence_score"]

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
    def from_json(cls, json_str: str) -> TraceAttributesBaseResponse:
        """Create an instance of TraceAttributesBaseResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in edges (list)
        _items = []
        if self.edges:
            for _item in self.edges:
                if _item:
                    _items.append(_item.to_dict())
            _dict['edges'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in admins (list)
        _items = []
        if self.admins:
            for _item in self.admins:
                if _item:
                    _items.append(_item.to_dict())
            _dict['admins'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in matched_points (list)
        _items = []
        if self.matched_points:
            for _item in self.matched_points:
                if _item:
                    _items.append(_item.to_dict())
            _dict['matched_points'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TraceAttributesBaseResponse:
        """Create an instance of TraceAttributesBaseResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TraceAttributesBaseResponse.parse_obj(obj)

        _obj = TraceAttributesBaseResponse.parse_obj({
            "edges": [TraceEdge.from_dict(_item) for _item in obj.get("edges")] if obj.get("edges") is not None else None,
            "admins": [AdminRegion.from_dict(_item) for _item in obj.get("admins")] if obj.get("admins") is not None else None,
            "matched_points": [MatchedPoint.from_dict(_item) for _item in obj.get("matched_points")] if obj.get("matched_points") is not None else None,
            "osm_changeset": obj.get("osm_changeset"),
            "shape": obj.get("shape"),
            "confidence_score": obj.get("confidence_score")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

