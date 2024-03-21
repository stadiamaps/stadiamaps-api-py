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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from stadiamaps.models.maneuver_sign import ManeuverSign
from stadiamaps.models.travel_mode import TravelMode
from typing import Optional, Set
from typing_extensions import Self

class RouteManeuver(BaseModel):
    """
    RouteManeuver
    """ # noqa: E501
    type: StrictInt = Field(description="The type of route maneuver.  | Code | Type                                | |------|-------------------------------------| | 0    | None                                | | 1    | Start                               | | 2    | Start right                         | | 3    | Start left                          | | 4    | Destination                         | | 5    | Destination right                   | | 6    | Destination left                    | | 7    | Becomes                             | | 8    | Continue                            | | 9    | Slight right                        | | 10   | Right                               | | 11   | Sharp right                         | | 12   | U-turn right                        | | 13   | U-turn left                         | | 14   | Sharp left                          | | 15   | Left                                | | 16   | Slight left                         | | 17   | Ramp straight                       | | 18   | Ramp right                          | | 19   | Ramp left                           | | 20   | Exit right                          | | 21   | Exit left                           | | 22   | Stay straight                       | | 23   | Stay right                          | | 24   | Stay left                           | | 25   | Merge                               | | 26   | Enter roundabout                    | | 27   | Exit roundabout                     | | 28   | Enter ferry                         | | 29   | Exit ferry                          | | 30   | Transit                             | | 31   | Transit transfer                    | | 32   | Transit remain on                   | | 33   | Transit connection start            | | 34   | Transit connection transfer         | | 35   | Transit connection destination      | | 36   | Post-transit connection destination | | 37   | Merge right                         | | 38   | Merge left                          | ")
    instruction: StrictStr = Field(description="The written maneuver instruction.")
    verbal_transition_alert_instruction: Optional[StrictStr] = Field(default=None, description="Text suitable for use as a verbal navigation alert.")
    verbal_pre_transition_instruction: Optional[StrictStr] = Field(default=None, description="Text suitable for use as a verbal navigation alert immediately prior to the maneuver transition.")
    verbal_post_transition_instruction: Optional[StrictStr] = Field(default=None, description="Text suitable for use as a verbal navigation alert immediately after to the maneuver transition.")
    street_names: Optional[List[StrictStr]] = Field(default=None, description="A list of street names that are consistent along the entire maneuver.")
    begin_street_names: Optional[List[StrictStr]] = Field(default=None, description="A list of street names at the beginning of the maneuver, if they are different from the names at the end.")
    time: Union[StrictFloat, StrictInt] = Field(description="The estimated time to complete the entire maneuver, in seconds.")
    length: Union[StrictFloat, StrictInt] = Field(description="The length of the maneuver, in `units`.")
    begin_shape_index: StrictInt = Field(description="The index into the list of shape points for the start of the maneuver.")
    end_shape_index: StrictInt = Field(description="The index into the list of shape points for the end of the maneuver.")
    toll: Optional[StrictBool] = Field(default=False, description="True any portion of the maneuver is subject to a toll.")
    rough: Optional[StrictBool] = Field(default=False, description="True any portion of the maneuver is unpaved or has portions of rough pavement.")
    gate: Optional[StrictBool] = Field(default=False, description="True if a gate is encountered in the course of this maneuver.")
    ferry: Optional[StrictBool] = Field(default=False, description="True if a ferry is encountered in the course of this maneuver.")
    sign: Optional[ManeuverSign] = None
    roundabout_exit_count: Optional[StrictInt] = Field(default=None, description="The exit number of the roundabout to take after entering.")
    depart_instruction: Optional[StrictInt] = Field(default=None, description="The written departure time instruction (typically used in a transit maneuver).")
    verbal_depart_instruction: Optional[StrictInt] = Field(default=None, description="Text suitable for use as a verbal departure time instruction (typically used in a transit maneuver).")
    arrive_instruction: Optional[StrictInt] = Field(default=None, description="The written arrival time instruction (typically used in a transit maneuver).")
    verbal_arrive_instruction: Optional[StrictInt] = Field(default=None, description="Text suitable for use as a verbal departure time instruction (typically used in a transit maneuver).")
    transit_info: Optional[Dict[str, Any]] = Field(default=None, description="Public transit info (not currently supported).")
    verbal_multi_cue: Optional[StrictBool] = Field(default=False, description="True if the `verbal_pre_transition_instruction` has been appended with the verbal instruction of the next maneuver.")
    travel_mode: TravelMode
    travel_type: StrictStr = Field(description="The type of travel over the maneuver. This can be thought of as a specialization of the travel mode. For example, vehicular travel may be via car, motorcycle, etc.; and travel via bicycle may be via a road bike, mountain bike, etc.")
    bss_maneuver_type: Optional[StrictStr] = Field(default=None, description="Describes a bike share action when using bikeshare routing.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["type", "instruction", "verbal_transition_alert_instruction", "verbal_pre_transition_instruction", "verbal_post_transition_instruction", "street_names", "begin_street_names", "time", "length", "begin_shape_index", "end_shape_index", "toll", "rough", "gate", "ferry", "sign", "roundabout_exit_count", "depart_instruction", "verbal_depart_instruction", "arrive_instruction", "verbal_arrive_instruction", "transit_info", "verbal_multi_cue", "travel_mode", "travel_type", "bss_maneuver_type"]

    @field_validator('travel_type')
    def travel_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['car', 'motorcycle', 'bus', 'tractor_trailer', 'motor_scooter', 'foot', 'wheelchair', 'segway', 'road', 'cross', 'hybrid', 'mountain', 'tram', 'metro', 'rail', 'ferry', 'cable_car', 'gondola', 'funicular', 'golf_cart', 'low_speed_vehicle']):
            raise ValueError("must be one of enum values ('car', 'motorcycle', 'bus', 'tractor_trailer', 'motor_scooter', 'foot', 'wheelchair', 'segway', 'road', 'cross', 'hybrid', 'mountain', 'tram', 'metro', 'rail', 'ferry', 'cable_car', 'gondola', 'funicular', 'golf_cart', 'low_speed_vehicle')")
        return value

    @field_validator('bss_maneuver_type')
    def bss_maneuver_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['NoneAction', 'RentBikeAtBikeShare', 'ReturnBikeAtBikeShare']):
            raise ValueError("must be one of enum values ('NoneAction', 'RentBikeAtBikeShare', 'ReturnBikeAtBikeShare')")
        return value

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
        """Create an instance of RouteManeuver from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sign
        if self.sign:
            _dict['sign'] = self.sign.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RouteManeuver from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "instruction": obj.get("instruction"),
            "verbal_transition_alert_instruction": obj.get("verbal_transition_alert_instruction"),
            "verbal_pre_transition_instruction": obj.get("verbal_pre_transition_instruction"),
            "verbal_post_transition_instruction": obj.get("verbal_post_transition_instruction"),
            "street_names": obj.get("street_names"),
            "begin_street_names": obj.get("begin_street_names"),
            "time": obj.get("time"),
            "length": obj.get("length"),
            "begin_shape_index": obj.get("begin_shape_index"),
            "end_shape_index": obj.get("end_shape_index"),
            "toll": obj.get("toll") if obj.get("toll") is not None else False,
            "rough": obj.get("rough") if obj.get("rough") is not None else False,
            "gate": obj.get("gate") if obj.get("gate") is not None else False,
            "ferry": obj.get("ferry") if obj.get("ferry") is not None else False,
            "sign": ManeuverSign.from_dict(obj["sign"]) if obj.get("sign") is not None else None,
            "roundabout_exit_count": obj.get("roundabout_exit_count"),
            "depart_instruction": obj.get("depart_instruction"),
            "verbal_depart_instruction": obj.get("verbal_depart_instruction"),
            "arrive_instruction": obj.get("arrive_instruction"),
            "verbal_arrive_instruction": obj.get("verbal_arrive_instruction"),
            "transit_info": obj.get("transit_info"),
            "verbal_multi_cue": obj.get("verbal_multi_cue") if obj.get("verbal_multi_cue") is not None else False,
            "travel_mode": obj.get("travel_mode"),
            "travel_type": obj.get("travel_type"),
            "bss_maneuver_type": obj.get("bss_maneuver_type")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


