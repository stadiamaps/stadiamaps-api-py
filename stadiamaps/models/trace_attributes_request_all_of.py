# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.5
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel
from stadiamaps.models.trace_attributes_request_all_of_filters import TraceAttributesRequestAllOfFilters

class TraceAttributesRequestAllOf(BaseModel):
    """
    TraceAttributesRequestAllOf
    """
    filters: Optional[TraceAttributesRequestAllOfFilters] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["filters"]

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
    def from_json(cls, json_str: str) -> TraceAttributesRequestAllOf:
        """Create an instance of TraceAttributesRequestAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TraceAttributesRequestAllOf:
        """Create an instance of TraceAttributesRequestAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TraceAttributesRequestAllOf.parse_obj(obj)

        _obj = TraceAttributesRequestAllOf.parse_obj({
            "filters": TraceAttributesRequestAllOfFilters.from_dict(obj.get("filters")) if obj.get("filters") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

