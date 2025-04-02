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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from stadiamaps.models.osrm_admin import OsrmAdmin
from stadiamaps.models.osrm_annotation import OsrmAnnotation
from stadiamaps.models.osrm_route_step import OsrmRouteStep
from stadiamaps.models.osrm_via_waypoint import OsrmViaWaypoint
from typing import Optional, Set
from typing_extensions import Self

class OsrmRouteLeg(BaseModel):
    """
    OsrmRouteLeg
    """ # noqa: E501
    distance: Union[StrictFloat, StrictInt] = Field(description="The distance traveled by the route, in meters.")
    duration: Union[StrictFloat, StrictInt] = Field(description="The estimated travel time, in number of seconds.")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total cost of the leg computed by the routing engine.")
    summary: Optional[StrictStr] = None
    steps: List[OsrmRouteStep]
    annotation: Optional[OsrmAnnotation] = None
    via_waypoints: Optional[List[OsrmViaWaypoint]] = Field(default=None, description="Indicates which waypoints are passed through rather than creating a new leg.")
    admins: Optional[List[OsrmAdmin]] = Field(default=None, description="Administrative regions visited along the leg.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["distance", "duration", "weight", "summary", "steps", "annotation", "via_waypoints", "admins"]

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
        """Create an instance of OsrmRouteLeg from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in steps (list)
        _items = []
        if self.steps:
            for _item_steps in self.steps:
                if _item_steps:
                    _items.append(_item_steps.to_dict())
            _dict['steps'] = _items
        # override the default output from pydantic by calling `to_dict()` of annotation
        if self.annotation:
            _dict['annotation'] = self.annotation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in via_waypoints (list)
        _items = []
        if self.via_waypoints:
            for _item_via_waypoints in self.via_waypoints:
                if _item_via_waypoints:
                    _items.append(_item_via_waypoints.to_dict())
            _dict['via_waypoints'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in admins (list)
        _items = []
        if self.admins:
            for _item_admins in self.admins:
                if _item_admins:
                    _items.append(_item_admins.to_dict())
            _dict['admins'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if via_waypoints (nullable) is None
        # and model_fields_set contains the field
        if self.via_waypoints is None and "via_waypoints" in self.model_fields_set:
            _dict['via_waypoints'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OsrmRouteLeg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "distance": obj.get("distance"),
            "duration": obj.get("duration"),
            "weight": obj.get("weight"),
            "summary": obj.get("summary"),
            "steps": [OsrmRouteStep.from_dict(_item) for _item in obj["steps"]] if obj.get("steps") is not None else None,
            "annotation": OsrmAnnotation.from_dict(obj["annotation"]) if obj.get("annotation") is not None else None,
            "via_waypoints": [OsrmViaWaypoint.from_dict(_item) for _item in obj["via_waypoints"]] if obj.get("via_waypoints") is not None else None,
            "admins": [OsrmAdmin.from_dict(_item) for _item in obj["admins"]] if obj.get("admins") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


