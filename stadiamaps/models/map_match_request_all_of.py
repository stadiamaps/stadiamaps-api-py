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
from pydantic import BaseModel, Field, StrictBool, StrictInt
from stadiamaps.models.map_match_trace_options import MapMatchTraceOptions

class MapMatchRequestAllOf(BaseModel):
    """
    MapMatchRequestAllOf
    """
    begin_time: Optional[StrictInt] = Field(None, description="The timestamp at the start of the trace. Combined with `durations`, this provides a way to include timing information for an `encoded_polyline` trace.")
    durations: Optional[StrictInt] = Field(None, description="A list of durations (in seconds) between each successive pair of points in a polyline.")
    use_timestamps: Optional[StrictBool] = Field(False, description="If true, the input timestamps or durations should be used when computing elapsed time for each edge along the matched path rather than the routing algorithm estimates.")
    trace_options: Optional[MapMatchTraceOptions] = None
    linear_references: Optional[StrictBool] = Field(False, description="If true, the response will include a `linear_references` value that contains an array of base64-encoded [OpenLR location references](https://www.openlr-association.com/fileadmin/user_upload/openlr-whitepaper_v1.5.pdf), one for each graph edge of the road network matched by the trace.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["begin_time", "durations", "use_timestamps", "trace_options", "linear_references"]

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
    def from_json(cls, json_str: str) -> MapMatchRequestAllOf:
        """Create an instance of MapMatchRequestAllOf from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of trace_options
        if self.trace_options:
            _dict['trace_options'] = self.trace_options.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MapMatchRequestAllOf:
        """Create an instance of MapMatchRequestAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MapMatchRequestAllOf.parse_obj(obj)

        _obj = MapMatchRequestAllOf.parse_obj({
            "begin_time": obj.get("begin_time"),
            "durations": obj.get("durations"),
            "use_timestamps": obj.get("use_timestamps") if obj.get("use_timestamps") is not None else False,
            "trace_options": MapMatchTraceOptions.from_dict(obj.get("trace_options")) if obj.get("trace_options") is not None else None,
            "linear_references": obj.get("linear_references") if obj.get("linear_references") is not None else False
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

