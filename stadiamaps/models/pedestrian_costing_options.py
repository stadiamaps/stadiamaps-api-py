# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.2
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, confloat, conint

class PedestrianCostingOptions(BaseModel):
    """
    PedestrianCostingOptions
    """
    walking_speed: Optional[conint(strict=True, le=25, ge=0)] = Field(None, description="Walking speed in kph.")
    walkway_factor: Optional[Union[StrictFloat, StrictInt]] = Field(1, description="A factor that multiplies the cost when walkways are encountered.")
    sidewalk_factor: Optional[Union[StrictFloat, StrictInt]] = Field(1, description="A factor that multiplies the cost when sidewalks are encountered.")
    alley_factor: Optional[Union[StrictFloat, StrictInt]] = Field(2, description="A factor that multiplies the cost when alleys are encountered.")
    driveway_factor: Optional[Union[StrictFloat, StrictInt]] = Field(5, description="A factor that multiplies the cost when driveways are encountered.")
    step_penalty: Optional[StrictInt] = Field(30, description="A penalty (in seconds) added to each transition onto a path with steps or stairs.")
    use_ferry: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(0.5, description="A measure of willingness to take ferries. Values near 0 attempt to avoid ferries, and values near 1 will favour them. Note that as some routes may be impossible without ferries, 0 does not guarantee avoidance of them.")
    use_living_streets: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(None, description="A measure of willingness to take living streets. Values near 0 attempt to avoid them, and values near 1 will favour them. Note that as some routes may be impossible without living streets, 0 does not guarantee avoidance of them. The default value is 0 for trucks; 0.1 for other motor vehicles; 0.5 for bicycles; and 0.6 for pedestrians.")
    use_tracks: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(None, description="A measure of willingness to take track roads. Values near 0 attempt to avoid them, and values near 1 will favour them. Note that as some routes may be impossible without track roads, 0 does not guarantee avoidance of them. The default value is 0 for automobiles, busses, and trucks; and 0.5 for all other costing modes.")
    use_hills: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(0.5, description="A measure of willingness to take tackle hills. Values near 0 attempt to avoid hills and steeper grades even if it means a longer route, and values near 1 indicates that the user does not fear them. Note that as some routes may be impossible without hills, 0 does not guarantee avoidance of them.")
    use_lit: Optional[Union[confloat(le=1, ge=0, strict=True), conint(le=1, ge=0, strict=True)]] = Field(0, description="A measure of preference for streets that are lit. 0 indicates indifference toward lit streets, and 1 indicates that unlit streets should be avoided. Note that even with values near 1, there is no guarantee that the returned route will include lit segments.")
    service_penalty: Optional[StrictInt] = Field(None, description="A penalty applied to transitions to service roads. This penalty can be used to reduce the likelihood of suggesting a route with service roads unless absolutely necessary. The default penalty is 15 for cars, busses, motor scooters, and motorcycles; and zero for others.")
    service_factor: Optional[Union[StrictFloat, StrictInt]] = Field(1, description="A factor that multiplies the cost when service roads are encountered. The default is 1.2 for cars and busses, and 1 for trucks, motor scooters, and motorcycles.")
    max_hiking_difficulty: Optional[conint(strict=True, le=6, ge=1)] = Field(1, description="The maximum difficulty of hiking trails allowed. This corresponds to the OSM `sac_scale`.")
    bss_rent_cost: Optional[StrictInt] = Field(120, description="The estimated cost (in seconds) to rent a bicycle from a sharing station in `bikeshare` mode.")
    bss_rent_penalty: Optional[StrictInt] = Field(0, description="A penalty (in seconds) to rent a bicycle in `bikeshare` mode.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["walking_speed", "walkway_factor", "sidewalk_factor", "alley_factor", "driveway_factor", "step_penalty", "use_ferry", "use_living_streets", "use_tracks", "use_hills", "use_lit", "service_penalty", "service_factor", "max_hiking_difficulty", "bss_rent_cost", "bss_rent_penalty"]

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
    def from_json(cls, json_str: str) -> PedestrianCostingOptions:
        """Create an instance of PedestrianCostingOptions from a JSON string"""
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
    def from_dict(cls, obj: dict) -> PedestrianCostingOptions:
        """Create an instance of PedestrianCostingOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PedestrianCostingOptions.parse_obj(obj)

        _obj = PedestrianCostingOptions.parse_obj({
            "walking_speed": obj.get("walking_speed"),
            "walkway_factor": obj.get("walkway_factor") if obj.get("walkway_factor") is not None else 1,
            "sidewalk_factor": obj.get("sidewalk_factor") if obj.get("sidewalk_factor") is not None else 1,
            "alley_factor": obj.get("alley_factor") if obj.get("alley_factor") is not None else 2,
            "driveway_factor": obj.get("driveway_factor") if obj.get("driveway_factor") is not None else 5,
            "step_penalty": obj.get("step_penalty") if obj.get("step_penalty") is not None else 30,
            "use_ferry": obj.get("use_ferry") if obj.get("use_ferry") is not None else 0.5,
            "use_living_streets": obj.get("use_living_streets"),
            "use_tracks": obj.get("use_tracks"),
            "use_hills": obj.get("use_hills") if obj.get("use_hills") is not None else 0.5,
            "use_lit": obj.get("use_lit") if obj.get("use_lit") is not None else 0,
            "service_penalty": obj.get("service_penalty"),
            "service_factor": obj.get("service_factor") if obj.get("service_factor") is not None else 1,
            "max_hiking_difficulty": obj.get("max_hiking_difficulty") if obj.get("max_hiking_difficulty") is not None else 1,
            "bss_rent_cost": obj.get("bss_rent_cost") if obj.get("bss_rent_cost") is not None else 120,
            "bss_rent_penalty": obj.get("bss_rent_penalty") if obj.get("bss_rent_penalty") is not None else 0
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

