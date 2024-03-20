# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 6.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class HighwayClassification(BaseModel):
    """
    HighwayClassification
    """ # noqa: E501
    internal: Optional[StrictBool] = Field(default=None, description="Is the edge internal to an intersection?")
    link: Optional[StrictBool] = Field(default=None, description="Is the edge a ramp or turn channel?")
    surface: Optional[StrictStr] = Field(default=None, description="A representation of the smoothness of the highway. This is used for costing and access checks based on the vehicle type.")
    use: Optional[StrictStr] = None
    classification: Optional[StrictStr] = Field(default=None, description="The classification/importance of the road/path. Used for a variety of purposes including fallback speed estimation and access for certain vehicle types.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["internal", "link", "surface", "use", "classification"]

    @field_validator('surface')
    def surface_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['paved_smooth', 'paved', 'paved_rough', 'compacted', 'dirt', 'gravel', 'path', 'impassable']):
            raise ValueError("must be one of enum values ('paved_smooth', 'paved', 'paved_rough', 'compacted', 'dirt', 'gravel', 'path', 'impassable')")
        return value

    @field_validator('use')
    def use_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['road', 'ramp', 'turn_channel', 'track', 'driveway', 'alley', 'parking_aisle', 'emergency_access', 'drive_through', 'culdesac', 'living_street', 'service_road', 'cycleway', 'mountain_bike', 'sidewalk', 'footway', 'elevator', 'steps', 'escalator', 'path', 'pedestrian', 'bridleway', 'pedestrian_crossing', 'rest_area', 'service_area', 'other', 'rail', 'ferry', 'rail-ferry', 'bus', 'egress_connection', 'platform_connnection', 'transit_connection', 'construction']):
            raise ValueError("must be one of enum values ('road', 'ramp', 'turn_channel', 'track', 'driveway', 'alley', 'parking_aisle', 'emergency_access', 'drive_through', 'culdesac', 'living_street', 'service_road', 'cycleway', 'mountain_bike', 'sidewalk', 'footway', 'elevator', 'steps', 'escalator', 'path', 'pedestrian', 'bridleway', 'pedestrian_crossing', 'rest_area', 'service_area', 'other', 'rail', 'ferry', 'rail-ferry', 'bus', 'egress_connection', 'platform_connnection', 'transit_connection', 'construction')")
        return value

    @field_validator('classification')
    def classification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['motorway', 'trunk', 'primary', 'secondary', 'tertiary', 'unclassified', 'residential', 'service_other']):
            raise ValueError("must be one of enum values ('motorway', 'trunk', 'primary', 'secondary', 'tertiary', 'unclassified', 'residential', 'service_other')")
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
        """Create an instance of HighwayClassification from a JSON string"""
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
        """Create an instance of HighwayClassification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "internal": obj.get("internal"),
            "link": obj.get("link"),
            "surface": obj.get("surface"),
            "use": obj.get("use"),
            "classification": obj.get("classification")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


