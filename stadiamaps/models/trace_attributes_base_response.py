# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 10.0.1
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from stadiamaps.models.admin_region import AdminRegion
from stadiamaps.models.matched_point import MatchedPoint
from stadiamaps.models.trace_edge import TraceEdge
from typing import Optional, Set
from typing_extensions import Self

class TraceAttributesBaseResponse(BaseModel):
    """
    TraceAttributesBaseResponse
    """ # noqa: E501
    edges: Optional[List[TraceEdge]] = Field(default=None, description="The list of edges matched along the path.")
    admins: Optional[List[AdminRegion]] = Field(default=None, description="The set of administrative regions matched along the path. Rather than repeating this information for every end node, the admins in this list are referenced by index.")
    matched_points: Optional[List[MatchedPoint]] = Field(default=None, description="List of match results when using the map_snap shape match algorithm. There is a one-to-one correspondence with the input set of latitude, longitude coordinates and this list of match results.")
    osm_changeset: Optional[StrictInt] = None
    shape: Optional[StrictStr] = Field(default=None, description="The encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm) of the matched path.")
    confidence_score: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["edges", "admins", "matched_points", "osm_changeset", "shape", "confidence_score"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TraceAttributesBaseResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in edges (list)
        _items = []
        if self.edges:
            for _item_edges in self.edges:
                if _item_edges:
                    _items.append(_item_edges.to_dict())
            _dict['edges'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in admins (list)
        _items = []
        if self.admins:
            for _item_admins in self.admins:
                if _item_admins:
                    _items.append(_item_admins.to_dict())
            _dict['admins'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in matched_points (list)
        _items = []
        if self.matched_points:
            for _item_matched_points in self.matched_points:
                if _item_matched_points:
                    _items.append(_item_matched_points.to_dict())
            _dict['matched_points'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if edges (nullable) is None
        # and model_fields_set contains the field
        if self.edges is None and "edges" in self.model_fields_set:
            _dict['edges'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TraceAttributesBaseResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "edges": [TraceEdge.from_dict(_item) for _item in obj["edges"]] if obj.get("edges") is not None else None,
            "admins": [AdminRegion.from_dict(_item) for _item in obj["admins"]] if obj.get("admins") is not None else None,
            "matched_points": [MatchedPoint.from_dict(_item) for _item in obj["matched_points"]] if obj.get("matched_points") is not None else None,
            "osm_changeset": obj.get("osm_changeset"),
            "shape": obj.get("shape"),
            "confidence_score": obj.get("confidence_score")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


