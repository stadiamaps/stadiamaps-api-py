# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 6.6.2
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from stadiamaps.models.road_class import RoadClass
from typing import Optional, Set
from typing_extensions import Self

class RoutingWaypointAllOfSearchFilter(BaseModel):
    """
    RoutingWaypointAllOfSearchFilter
    """ # noqa: E501
    exclude_tunnel: Optional[StrictBool] = Field(default=False, description="Excludes roads marked as tunnels")
    exclude_bridge: Optional[StrictBool] = Field(default=False, description="Excludes roads marked as bridges")
    exclude_ramp: Optional[StrictBool] = Field(default=False, description="Excludes roads marked as ramps")
    exclude_closures: Optional[StrictBool] = Field(default=True, description="Excludes roads marked as closed")
    min_road_class: Optional[RoadClass] = Field(default=None, description="The lowest road class allowed")
    max_road_class: Optional[RoadClass] = Field(default=None, description="The highest road class allowed")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["exclude_tunnel", "exclude_bridge", "exclude_ramp", "exclude_closures", "min_road_class", "max_road_class"]

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
        """Create an instance of RoutingWaypointAllOfSearchFilter from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RoutingWaypointAllOfSearchFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "exclude_tunnel": obj.get("exclude_tunnel") if obj.get("exclude_tunnel") is not None else False,
            "exclude_bridge": obj.get("exclude_bridge") if obj.get("exclude_bridge") is not None else False,
            "exclude_ramp": obj.get("exclude_ramp") if obj.get("exclude_ramp") is not None else False,
            "exclude_closures": obj.get("exclude_closures") if obj.get("exclude_closures") is not None else True,
            "min_road_class": obj.get("min_road_class"),
            "max_road_class": obj.get("max_road_class")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


