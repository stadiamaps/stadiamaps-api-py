# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.6
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class PeliasResponseGeocoding(BaseModel):
    """
    PeliasResponseGeocoding
    """
    attribution: Optional[StrictStr] = Field(None, description="A URL containing attribution information. If you are not using Stadia Maps and our standard attribution already for your basemaps, you must include this attribution link somewhere in your website/app.")
    query: Optional[Dict[str, Any]] = Field(None, description="Technical details of the query. This is most useful for debugging during development. See the full example for the list of properties; these should be self-explanatory, so we don't enumerate them in the spec.")
    warnings: Optional[conlist(StrictStr)] = Field(None, description="An array of non-critical warnings. This is normally for informational/debugging purposes and not a serious problem.")
    errors: Optional[conlist(StrictStr)] = Field(None, description="An array of more serious errors (for example, omitting a required parameter). Don’t ignore these.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["attribution", "query", "warnings", "errors"]

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
    def from_json(cls, json_str: str) -> PeliasResponseGeocoding:
        """Create an instance of PeliasResponseGeocoding from a JSON string"""
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
    def from_dict(cls, obj: dict) -> PeliasResponseGeocoding:
        """Create an instance of PeliasResponseGeocoding from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PeliasResponseGeocoding.parse_obj(obj)

        _obj = PeliasResponseGeocoding.parse_obj({
            "attribution": obj.get("attribution"),
            "query": obj.get("query"),
            "warnings": obj.get("warnings"),
            "errors": obj.get("errors")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

