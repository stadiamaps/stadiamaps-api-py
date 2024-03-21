# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 6.1.0
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
from typing import Optional, Set
from typing_extensions import Self

class Access(BaseModel):
    """
    Access
    """ # noqa: E501
    golf_cart: Optional[StrictBool] = None
    wheelchair: Optional[StrictBool] = None
    taxi: Optional[StrictBool] = None
    hov: Optional[StrictBool] = Field(default=None, alias="HOV")
    truck: Optional[StrictBool] = None
    emergency: Optional[StrictBool] = None
    pedestrian: Optional[StrictBool] = None
    car: Optional[StrictBool] = None
    bus: Optional[StrictBool] = None
    bicycle: Optional[StrictBool] = None
    motorcycle: Optional[StrictBool] = None
    moped: Optional[StrictBool] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["golf_cart", "wheelchair", "taxi", "HOV", "truck", "emergency", "pedestrian", "car", "bus", "bicycle", "motorcycle", "moped"]

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
        """Create an instance of Access from a JSON string"""
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
        """Create an instance of Access from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "golf_cart": obj.get("golf_cart"),
            "wheelchair": obj.get("wheelchair"),
            "taxi": obj.get("taxi"),
            "HOV": obj.get("HOV"),
            "truck": obj.get("truck"),
            "emergency": obj.get("emergency"),
            "pedestrian": obj.get("pedestrian"),
            "car": obj.get("car"),
            "bus": obj.get("bus"),
            "bicycle": obj.get("bicycle"),
            "motorcycle": obj.get("motorcycle"),
            "moped": obj.get("moped")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


