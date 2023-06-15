# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.3
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List
from pydantic import BaseModel, Field, StrictStr, conlist, validator
from stadiamaps.models.trace_attribute_key import TraceAttributeKey

class TraceAttributeFilterOptions(BaseModel):
    """
    TraceAttributeFilterOptions
    """
    attributes: conlist(TraceAttributeKey, min_items=1) = Field(...)
    action: StrictStr = Field(..., description="Determines whether the list of attributes will be used as a whitelist or a blacklist.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["attributes", "action"]

    @validator('action')
    def action_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('include', 'exclude'):
            raise ValueError("must be one of enum values ('include', 'exclude')")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> TraceAttributeFilterOptions:
        """Create an instance of TraceAttributeFilterOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TraceAttributeFilterOptions:
        """Create an instance of TraceAttributeFilterOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TraceAttributeFilterOptions.parse_obj(obj)

        _obj = TraceAttributeFilterOptions.parse_obj({
            "attributes": obj.get("attributes"),
            "action": obj.get("action")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

