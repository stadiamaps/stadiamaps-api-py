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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist
from stadiamaps.models.trace_attributes_base_response import TraceAttributesBaseResponse
from stadiamaps.models.valhalla_long_units import ValhallaLongUnits

class TraceAttributesResponseAllOf(BaseModel):
    """
    TraceAttributesResponseAllOf
    """
    id: Optional[StrictStr] = Field(None, description="An identifier to disambiguate requests (echoed by the server).")
    units: Optional[ValhallaLongUnits] = None
    alternate_paths: Optional[conlist(TraceAttributesBaseResponse)] = Field(None, description="Alternate paths, if any, that were not classified as the best match.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "units", "alternate_paths"]

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
    def from_json(cls, json_str: str) -> TraceAttributesResponseAllOf:
        """Create an instance of TraceAttributesResponseAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in alternate_paths (list)
        _items = []
        if self.alternate_paths:
            for _item in self.alternate_paths:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alternate_paths'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TraceAttributesResponseAllOf:
        """Create an instance of TraceAttributesResponseAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TraceAttributesResponseAllOf.parse_obj(obj)

        _obj = TraceAttributesResponseAllOf.parse_obj({
            "id": obj.get("id"),
            "units": obj.get("units"),
            "alternate_paths": [TraceAttributesBaseResponse.from_dict(_item) for _item in obj.get("alternate_paths")] if obj.get("alternate_paths") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

