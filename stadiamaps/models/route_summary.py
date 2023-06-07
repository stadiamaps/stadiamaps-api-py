# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.1
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class RouteSummary(BaseModel):
    """
    RouteSummary
    """
    time: Union[StrictFloat, StrictInt] = Field(..., description="The estimated travel time, in seconds")
    length: Union[StrictFloat, StrictInt] = Field(..., description="The estimated travel distance, in `units` (km or mi)")
    min_lat: Union[StrictFloat, StrictInt] = Field(..., description="The minimum latitude of the bounding box containing the route.")
    max_lat: Union[StrictFloat, StrictInt] = Field(..., description="The maximum latitude of the bounding box containing the route.")
    min_lon: Union[StrictFloat, StrictInt] = Field(..., description="The minimum longitude of the bounding box containing the route.")
    max_lon: Union[StrictFloat, StrictInt] = Field(..., description="The maximum longitude of the bounding box containing the route.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["time", "length", "min_lat", "max_lat", "min_lon", "max_lon"]

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
    def from_json(cls, json_str: str) -> RouteSummary:
        """Create an instance of RouteSummary from a JSON string"""
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
    def from_dict(cls, obj: dict) -> RouteSummary:
        """Create an instance of RouteSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RouteSummary.parse_obj(obj)

        _obj = RouteSummary.parse_obj({
            "time": obj.get("time"),
            "length": obj.get("length"),
            "min_lat": obj.get("min_lat"),
            "max_lat": obj.get("max_lat"),
            "min_lon": obj.get("min_lon"),
            "max_lon": obj.get("max_lon")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

