# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 8.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class GeoAttributes(BaseModel):
    """
    GeoAttributes
    """ # noqa: E501
    curvature: Optional[StrictInt] = Field(default=None, description="Curvature factor.")
    max_down_slope: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The maximum downward slope. Uses 1 degree precision for slopes to -16 degrees, and 4 degree precision afterwards (up to a max of -76 degrees).")
    max_up_slope: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The maximum upward slope. Uses 1 degree precision for slopes to 16 degrees, and 4 degree precision afterwards (up to a max of 76 degrees).")
    weighted_grade: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The weighted estimate of the grade.")
    length: Optional[StrictInt] = Field(default=None, description="The length of the edge, in meters.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["curvature", "max_down_slope", "max_up_slope", "weighted_grade", "length"]

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
        """Create an instance of GeoAttributes from a JSON string"""
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
        """Create an instance of GeoAttributes from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "curvature": obj.get("curvature"),
            "max_down_slope": obj.get("max_down_slope"),
            "max_up_slope": obj.get("max_up_slope"),
            "weighted_grade": obj.get("weighted_grade"),
            "length": obj.get("length")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


