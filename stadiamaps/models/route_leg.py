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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from stadiamaps.models.route_maneuver import RouteManeuver
from stadiamaps.models.route_summary import RouteSummary
from typing import Optional, Set
from typing_extensions import Self

class RouteLeg(BaseModel):
    """
    RouteLeg
    """ # noqa: E501
    maneuvers: Annotated[List[RouteManeuver], Field(min_length=1)]
    shape: StrictStr = Field(description="An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm) with 6 digits of decimal precision.")
    summary: RouteSummary
    elevation_interval: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The sampling distance between elevation values along the route. This echoes the request parameter having the same name (converted to `units` if necessary).")
    elevation: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="An array of elevation values sampled every `elevation_interval`. Units are either metric or imperial depending on the value of `units`.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["maneuvers", "shape", "summary", "elevation_interval", "elevation"]

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
        """Create an instance of RouteLeg from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in maneuvers (list)
        _items = []
        if self.maneuvers:
            for _item in self.maneuvers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['maneuvers'] = _items
        # override the default output from pydantic by calling `to_dict()` of summary
        if self.summary:
            _dict['summary'] = self.summary.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RouteLeg from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maneuvers": [RouteManeuver.from_dict(_item) for _item in obj["maneuvers"]] if obj.get("maneuvers") is not None else None,
            "shape": obj.get("shape"),
            "summary": RouteSummary.from_dict(obj["summary"]) if obj.get("summary") is not None else None,
            "elevation_interval": obj.get("elevation_interval"),
            "elevation": obj.get("elevation")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


