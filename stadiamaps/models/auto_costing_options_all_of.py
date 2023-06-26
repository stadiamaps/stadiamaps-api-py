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


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, confloat, conint

class AutoCostingOptionsAllOf(BaseModel):
    """
    AutoCostingOptionsAllOf
    """
    height: Optional[Union[StrictFloat, StrictInt]] = Field(1.9, description="The height of the automobile (in meters).")
    width: Optional[Union[StrictFloat, StrictInt]] = Field(1.6, description="The width of the automobile (in meters).")
    toll_booth_cost: Optional[StrictInt] = Field(15, description="The estimated cost (in seconds) when a toll booth is encountered.")
    toll_booth_penalty: Optional[StrictInt] = Field(0, description="A penalty (in seconds) applied to the route cost when a toll booth is encountered. This penalty can be used to reduce the likelihood of suggesting a route with toll booths unless absolutely necessary.")
    ferry_cost: Optional[StrictInt] = Field(300, description="The estimated cost (in seconds) when a ferry is encountered.")
    use_highways: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(0.5, description="A measure of willingness to take highways. Values near 0 attempt to avoid highways, and values near 1 will favour them. Note that as some routes may be impossible without highways, 0 does not guarantee avoidance of them.")
    use_tolls: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(0.5, description="A measure of willingness to take toll roads. Values near 0 attempt to avoid tolls, and values near 1 will favour them. Note that as some routes may be impossible without tolls, 0 does not guarantee avoidance of them.")
    use_tracks: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(None, description="A measure of willingness to take track roads. Values near 0 attempt to avoid them, and values near 1 will favour them. Note that as some routes may be impossible without track roads, 0 does not guarantee avoidance of them. The default value is 0 for automobiles, busses, and trucks; and 0.5 for all other costing modes.")
    top_speed: Optional[conint(strict=True, le=252, ge=10)] = Field(140, description="The top speed (in kph) that the vehicle is capable of travelling.")
    shortest: Optional[StrictBool] = Field(False, description="If true changes the cost metric to be quasi-shortest (pure distance-based) costing. This will disable ALL other costing factors.")
    ignore_closures: Optional[StrictBool] = Field(False, description="If true, ignores all known closures. This option cannot be set if `location.search_filter.exclude_closures` is also specified.")
    include_hov2: Optional[StrictBool] = Field(False, description="If true, indicates the desire to include HOV roads with a 2-occupant requirement in the route when advantageous.")
    include_hov3: Optional[StrictBool] = Field(False, description="If true, indicates the desire to include HOV roads with a 3-occupant requirement in the route when advantageous.")
    include_hot: Optional[StrictBool] = Field(False, description="If true, indicates the desire to include toll roads which require the driver to pay a toll if the occupant requirement isn't met")
    additional_properties: Dict[str, Any] = {}
    __properties = ["height", "width", "toll_booth_cost", "toll_booth_penalty", "ferry_cost", "use_highways", "use_tolls", "use_tracks", "top_speed", "shortest", "ignore_closures", "include_hov2", "include_hov3", "include_hot"]

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
    def from_json(cls, json_str: str) -> AutoCostingOptionsAllOf:
        """Create an instance of AutoCostingOptionsAllOf from a JSON string"""
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
    def from_dict(cls, obj: dict) -> AutoCostingOptionsAllOf:
        """Create an instance of AutoCostingOptionsAllOf from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return AutoCostingOptionsAllOf.parse_obj(obj)

        _obj = AutoCostingOptionsAllOf.parse_obj({
            "height": obj.get("height") if obj.get("height") is not None else 1.9,
            "width": obj.get("width") if obj.get("width") is not None else 1.6,
            "toll_booth_cost": obj.get("toll_booth_cost") if obj.get("toll_booth_cost") is not None else 15,
            "toll_booth_penalty": obj.get("toll_booth_penalty") if obj.get("toll_booth_penalty") is not None else 0,
            "ferry_cost": obj.get("ferry_cost") if obj.get("ferry_cost") is not None else 300,
            "use_highways": obj.get("use_highways") if obj.get("use_highways") is not None else 0.5,
            "use_tolls": obj.get("use_tolls") if obj.get("use_tolls") is not None else 0.5,
            "use_tracks": obj.get("use_tracks"),
            "top_speed": obj.get("top_speed") if obj.get("top_speed") is not None else 140,
            "shortest": obj.get("shortest") if obj.get("shortest") is not None else False,
            "ignore_closures": obj.get("ignore_closures") if obj.get("ignore_closures") is not None else False,
            "include_hov2": obj.get("include_hov2") if obj.get("include_hov2") is not None else False,
            "include_hov3": obj.get("include_hov3") if obj.get("include_hov3") is not None else False,
            "include_hot": obj.get("include_hot") if obj.get("include_hot") is not None else False
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

