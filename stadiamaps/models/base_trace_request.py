# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 9.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from stadiamaps.models.costing_options import CostingOptions
from stadiamaps.models.distance_unit import DistanceUnit
from stadiamaps.models.map_match_costing_model import MapMatchCostingModel
from stadiamaps.models.map_match_waypoint import MapMatchWaypoint
from stadiamaps.models.routing_languages import RoutingLanguages
from typing import Optional, Set
from typing_extensions import Self

class BaseTraceRequest(BaseModel):
    """
    BaseTraceRequest
    """ # noqa: E501
    units: Optional[DistanceUnit] = DistanceUnit.KM
    language: Optional[RoutingLanguages] = RoutingLanguages.EN_MINUS_US
    directions_type: Optional[StrictStr] = Field(default='instructions', description="The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter.")
    id: Optional[StrictStr] = Field(default=None, description="An identifier to disambiguate requests (echoed by the server).")
    shape: Optional[List[MapMatchWaypoint]] = Field(default=None, description="REQUIRED if `encoded_polyline` is not present. Note that `break` type locations are only supported when `shape_match` is set to `map_match`.")
    encoded_polyline: Optional[StrictStr] = Field(default=None, description="REQUIRED if `shape` is not present. An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm). Note that the polyline must be encoded with 6 digits of precision rather than the usual 5.")
    costing: MapMatchCostingModel
    costing_options: Optional[CostingOptions] = None
    shape_match: Optional[StrictStr] = Field(default=None, description="Three snapping modes provide some control over how the map matching occurs. `edge_walk` is fast, but requires extremely precise data that matches the route graph almost perfectly. `map_snap` can handle significantly noisier data, but is very expensive. `walk_or_snap`, the default, tries to use edge walking first and falls back to map matching if edge walking fails. In general, you should not need to change this parameter unless you want to trace a multi-leg route with multiple `break` locations in the `shape`.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["units", "language", "directions_type", "id", "shape", "encoded_polyline", "costing", "costing_options", "shape_match"]

    @field_validator('directions_type')
    def directions_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'maneuvers', 'instructions']):
            raise ValueError("must be one of enum values ('none', 'maneuvers', 'instructions')")
        return value

    @field_validator('shape_match')
    def shape_match_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['edge_walk', 'map_snap', 'walk_or_snap']):
            raise ValueError("must be one of enum values ('edge_walk', 'map_snap', 'walk_or_snap')")
        return value

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
        """Create an instance of BaseTraceRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in shape (list)
        _items = []
        if self.shape:
            for _item_shape in self.shape:
                if _item_shape:
                    _items.append(_item_shape.to_dict())
            _dict['shape'] = _items
        # override the default output from pydantic by calling `to_dict()` of costing_options
        if self.costing_options:
            _dict['costing_options'] = self.costing_options.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BaseTraceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "units": obj.get("units") if obj.get("units") is not None else DistanceUnit.KM,
            "language": obj.get("language") if obj.get("language") is not None else RoutingLanguages.EN_MINUS_US,
            "directions_type": obj.get("directions_type") if obj.get("directions_type") is not None else 'instructions',
            "id": obj.get("id"),
            "shape": [MapMatchWaypoint.from_dict(_item) for _item in obj["shape"]] if obj.get("shape") is not None else None,
            "encoded_polyline": obj.get("encoded_polyline"),
            "costing": obj.get("costing"),
            "costing_options": CostingOptions.from_dict(obj["costing_options"]) if obj.get("costing_options") is not None else None,
            "shape_match": obj.get("shape_match")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


