# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 6.3.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from stadiamaps.models.route_leg import RouteLeg
from stadiamaps.models.route_summary import RouteSummary
from stadiamaps.models.routing_response_waypoint import RoutingResponseWaypoint
from stadiamaps.models.valhalla_languages import ValhallaLanguages
from stadiamaps.models.valhalla_long_units import ValhallaLongUnits
from typing import Optional, Set
from typing_extensions import Self

class RouteTrip(BaseModel):
    """
    RouteTrip
    """ # noqa: E501
    status: StrictInt = Field(description="The response status code")
    status_message: StrictStr = Field(description="The response status message")
    units: ValhallaLongUnits
    language: ValhallaLanguages
    locations: List[RoutingResponseWaypoint]
    legs: List[RouteLeg]
    summary: RouteSummary
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["status", "status_message", "units", "language", "locations", "legs", "summary"]

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
        """Create an instance of RouteTrip from a JSON string"""
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
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RouteTrip from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "status": obj.get("status"),
            "status_message": obj.get("status_message"),
            "units": obj.get("units"),
            "language": obj.get("language"),
            "locations": [RoutingResponseWaypoint.from_dict(_item) for _item in obj["locations"]] if obj.get("locations") is not None else None,
            "legs": [RouteLeg.from_dict(_item) for _item in obj["legs"]] if obj.get("legs") is not None else None,
            "summary": RouteSummary.from_dict(obj["summary"]) if obj.get("summary") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


