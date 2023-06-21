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



from pydantic import BaseModel, Field, StrictInt, StrictStr

class TzResponse(BaseModel):
    """
    TzResponse
    """
    tz_id: StrictStr = Field(..., description="The canonical time zone ID. In the event that multiple time zones could be returned, the first one from the Unicode CLDR timezone.xml is returned.")
    base_utc_offset: StrictInt = Field(..., description="The base offset, in seconds, from UTC that is normally in effect for this time zone.")
    dst_offset: StrictInt = Field(..., description="The special offset, in seconds, from UTC that is in effect for this time zone as of the queried timestamp (defaults to now). If no additional offsets are in effect, this value is zero. This typically reflects Daylight Saving Time, but may indicate other special offsets. To get the total offset in effect, add `dst_offset` and `utc_offset` together.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["tz_id", "base_utc_offset", "dst_offset"]

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
    def from_json(cls, json_str: str) -> TzResponse:
        """Create an instance of TzResponse from a JSON string"""
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
    def from_dict(cls, obj: dict) -> TzResponse:
        """Create an instance of TzResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TzResponse.parse_obj(obj)

        _obj = TzResponse.parse_obj({
            "tz_id": obj.get("tz_id"),
            "base_utc_offset": obj.get("base_utc_offset"),
            "dst_offset": obj.get("dst_offset")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

