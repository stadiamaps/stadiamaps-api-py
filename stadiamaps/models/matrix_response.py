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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from stadiamaps.models.coordinate import Coordinate
from stadiamaps.models.matrix_distance import MatrixDistance
from stadiamaps.models.routing_long_units import RoutingLongUnits
from stadiamaps.models.warning import Warning
from typing import Optional, Set
from typing_extensions import Self

class MatrixResponse(BaseModel):
    """
    MatrixResponse
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="An identifier to disambiguate requests (echoed by the server).")
    sources: Annotated[List[Coordinate], Field(min_length=1)] = Field(description="The list of starting locations determined by snapping to the nearest appropriate point on the road network for the costing model. All locations appear in the same order as the input.")
    targets: Annotated[List[Coordinate], Field(min_length=1)] = Field(description="The list of ending locations determined by snapping to the nearest appropriate point on the road network for the costing model. All locations appear in the same order as the input.")
    sources_to_targets: Annotated[List[List[MatrixDistance]], Field(min_length=1)] = Field(description="The matrix of starting and ending locations, along with the computed distance and travel time. The array is row-ordered. This means that the time and distance from the first location to all others forms the first row of the array, followed by the time and distance from the second source location to all target locations, etc.")
    warnings: Optional[List[Warning]] = None
    units: RoutingLongUnits
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "sources", "targets", "sources_to_targets", "warnings", "units"]

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
        """Create an instance of MatrixResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in sources (list)
        _items = []
        if self.sources:
            for _item_sources in self.sources:
                if _item_sources:
                    _items.append(_item_sources.to_dict())
            _dict['sources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in targets (list)
        _items = []
        if self.targets:
            for _item_targets in self.targets:
                if _item_targets:
                    _items.append(_item_targets.to_dict())
            _dict['targets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in sources_to_targets (list of list)
        _items = []
        if self.sources_to_targets:
            for _item_sources_to_targets in self.sources_to_targets:
                if _item_sources_to_targets:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item_sources_to_targets if _inner_item is not None]
                    )
            _dict['sources_to_targets'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in warnings (list)
        _items = []
        if self.warnings:
            for _item_warnings in self.warnings:
                if _item_warnings:
                    _items.append(_item_warnings.to_dict())
            _dict['warnings'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatrixResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "sources": [Coordinate.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None,
            "targets": [Coordinate.from_dict(_item) for _item in obj["targets"]] if obj.get("targets") is not None else None,
            "sources_to_targets": [
                    [MatrixDistance.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["sources_to_targets"]
                ] if obj.get("sources_to_targets") is not None else None,
            "warnings": [Warning.from_dict(_item) for _item in obj["warnings"]] if obj.get("warnings") is not None else None,
            "units": obj.get("units") if obj.get("units") is not None else RoutingLongUnits.KILOMETERS
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


