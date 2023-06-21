# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.4
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class MapMatchTraceOptions(BaseModel):
    """
    MapMatchTraceOptions
    """
    search_radius: Optional[StrictInt] = Field(None, description="The search radius, in meters, when trying to match each trace point.")
    gps_accuracy: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The accuracy of the GPS, in meters.")
    breakage_distance: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The breaking distance, in meters, between trace points.")
    interpolation_distance: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The interpolation distance, in meters, beyond which trace points are merged together.")
    turn_penalty_factor: Optional[StrictInt] = Field(None, description="Penalizes turns from one road segment to next. For a pedestrian trace, you may see a back-and-forth motion along the streets of your path with the default settings. Try increasing the turn penalty factor to 500 to reduce jitter in the output. Note that if GPS accuracy is already good, increasing this above the default will usually negatively affect the quality of map matching.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["search_radius", "gps_accuracy", "breakage_distance", "interpolation_distance", "turn_penalty_factor"]

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
    def from_json(cls, json_str: str) -> MapMatchTraceOptions:
        """Create an instance of MapMatchTraceOptions from a JSON string"""
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
    def from_dict(cls, obj: dict) -> MapMatchTraceOptions:
        """Create an instance of MapMatchTraceOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MapMatchTraceOptions.parse_obj(obj)

        _obj = MapMatchTraceOptions.parse_obj({
            "search_radius": obj.get("search_radius"),
            "gps_accuracy": obj.get("gps_accuracy"),
            "breakage_distance": obj.get("breakage_distance"),
            "interpolation_distance": obj.get("interpolation_distance"),
            "turn_penalty_factor": obj.get("turn_penalty_factor")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

