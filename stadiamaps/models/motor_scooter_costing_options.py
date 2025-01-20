# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 8.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class MotorScooterCostingOptions(BaseModel):
    """
    MotorScooterCostingOptions
    """ # noqa: E501
    maneuver_penalty: Optional[StrictInt] = Field(default=5, description="A penalty (in seconds) applied when transitioning between roads (determined by name).")
    gate_cost: Optional[StrictInt] = Field(default=15, description="The estimated cost (in seconds) when a gate is encountered.")
    gate_penalty: Optional[StrictInt] = Field(default=300, description="A penalty (in seconds) applied to the route cost when a gate is encountered. This penalty can be used to reduce the likelihood of suggesting a route with gates unless absolutely necessary.")
    country_crossing_cost: Optional[StrictInt] = Field(default=600, description="The estimated cost (in seconds) when encountering an international border.")
    country_crossing_penalty: Optional[StrictInt] = Field(default=0, description="A penalty applied to transitions to international border crossings. This penalty can be used to reduce the likelihood of suggesting a route with border crossings unless absolutely necessary.")
    service_penalty: Optional[StrictInt] = Field(default=None, description="A penalty applied to transitions to service roads. This penalty can be used to reduce the likelihood of suggesting a route with service roads unless absolutely necessary. The default penalty is 15 for cars, busses, motor scooters, and motorcycles; and zero for others.")
    service_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=1, description="A factor that multiplies the cost when service roads are encountered. The default is 1.2 for cars and busses, and 1 for trucks, motor scooters, and motorcycles.")
    use_living_streets: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=None, description="A measure of willingness to take living streets. Values near 0 attempt to avoid them, and values near 1 will favour them. Note that as some routes may be impossible without living streets, 0 does not guarantee avoidance of them. The default value is 0 for trucks; 0.1 for other motor vehicles; 0.5 for bicycles; and 0.6 for pedestrians.")
    use_ferry: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=0.5, description="A measure of willingness to take ferries. Values near 0 attempt to avoid ferries, and values near 1 will favour them. Note that as some routes may be impossible without ferries, 0 does not guarantee avoidance of them.")
    ignore_restrictions: Optional[StrictBool] = Field(default=None, description="If set to true, ignores any restrictions (eg: turn and conditional restrictions). Useful for matching GPS traces to the road network regardless of restrictions.")
    ignore_non_vehicular_restrictions: Optional[StrictBool] = Field(default=None, description="If set to true, ignores most restrictions (eg: turn and conditional restrictions), but still respects restrictions that impact vehicle safety such as weight and size.")
    ignore_oneways: Optional[StrictBool] = Field(default=None, description="If set to true, ignores directional restrictions on roads. Useful for matching GPS traces to the road network regardless of restrictions.")
    height: Optional[Union[StrictFloat, StrictInt]] = Field(default=1.9, description="The height of the automobile (in meters).")
    width: Optional[Union[StrictFloat, StrictInt]] = Field(default=1.6, description="The width of the automobile (in meters).")
    toll_booth_cost: Optional[StrictInt] = Field(default=15, description="The estimated cost (in seconds) when a toll booth is encountered.")
    toll_booth_penalty: Optional[StrictInt] = Field(default=0, description="A penalty (in seconds) applied to the route cost when a toll booth is encountered. This penalty can be used to reduce the likelihood of suggesting a route with toll booths unless absolutely necessary.")
    ferry_cost: Optional[StrictInt] = Field(default=300, description="The estimated cost (in seconds) when a ferry is encountered.")
    use_highways: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=0.5, description="A measure of willingness to take highways. Values near 0 attempt to avoid highways, and values near 1 will favour them. Note that as some routes may be impossible without highways, 0 does not guarantee avoidance of them.")
    use_tolls: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=0.5, description="A measure of willingness to take toll roads. Values near 0 attempt to avoid tolls, and values near 1 will favour them. Note that as some routes may be impossible without tolls, 0 does not guarantee avoidance of them.")
    use_tracks: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=None, description="A measure of willingness to take track roads. Values near 0 attempt to avoid them, and values near 1 will favour them. Note that as some routes may be impossible without track roads, 0 does not guarantee avoidance of them. The default value is 0 for automobiles, busses, and trucks; and 0.5 for all other costing modes.")
    top_speed: Optional[Annotated[int, Field(le=252, strict=True, ge=10)]] = Field(default=140, description="The top speed (in kph) that the vehicle is capable of travelling.")
    shortest: Optional[StrictBool] = Field(default=False, description="If true changes the cost metric to be quasi-shortest (pure distance-based) costing. This will disable ALL other costing factors.")
    ignore_closures: Optional[StrictBool] = Field(default=False, description="If true, ignores all known closures. This option cannot be set if `location.search_filter.exclude_closures` is also specified.")
    include_hov2: Optional[StrictBool] = Field(default=False, description="If true, indicates the desire to include HOV roads with a 2-occupant requirement in the route when advantageous.")
    include_hov3: Optional[StrictBool] = Field(default=False, description="If true, indicates the desire to include HOV roads with a 3-occupant requirement in the route when advantageous.")
    include_hot: Optional[StrictBool] = Field(default=False, description="If true, indicates the desire to include toll roads which require the driver to pay a toll if the occupant requirement isn't met")
    alley_factor: Optional[Union[StrictFloat, StrictInt]] = Field(default=1, description="A factor that multiplies the cost when alleys are encountered.")
    use_primary: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=0.5, description="A measure of willingness to use primary roads. Values near 0 attempt to avoid primary roads and stay on roads with lower speeds, and values near 1 indicate the rider is more comfortable on these roads.")
    use_hills: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=0.5, description="A measure of willingness to take tackle hills. Values near 0 attempt to avoid hills and steeper grades even if it means a longer route, and values near 1 indicates that the rider does not fear them. Note that as some routes may be impossible without hills, 0 does not guarantee avoidance of them.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["maneuver_penalty", "gate_cost", "gate_penalty", "country_crossing_cost", "country_crossing_penalty", "service_penalty", "service_factor", "use_living_streets", "use_ferry", "ignore_restrictions", "ignore_non_vehicular_restrictions", "ignore_oneways", "height", "width", "toll_booth_cost", "toll_booth_penalty", "ferry_cost", "use_highways", "use_tolls", "use_tracks", "top_speed", "shortest", "ignore_closures", "include_hov2", "include_hov3", "include_hot", "alley_factor", "use_primary", "use_hills"]

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
        """Create an instance of MotorScooterCostingOptions from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MotorScooterCostingOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maneuver_penalty": obj.get("maneuver_penalty") if obj.get("maneuver_penalty") is not None else 5,
            "gate_cost": obj.get("gate_cost") if obj.get("gate_cost") is not None else 15,
            "gate_penalty": obj.get("gate_penalty") if obj.get("gate_penalty") is not None else 300,
            "country_crossing_cost": obj.get("country_crossing_cost") if obj.get("country_crossing_cost") is not None else 600,
            "country_crossing_penalty": obj.get("country_crossing_penalty") if obj.get("country_crossing_penalty") is not None else 0,
            "service_penalty": obj.get("service_penalty"),
            "service_factor": obj.get("service_factor") if obj.get("service_factor") is not None else 1,
            "use_living_streets": obj.get("use_living_streets"),
            "use_ferry": obj.get("use_ferry") if obj.get("use_ferry") is not None else 0.5,
            "ignore_restrictions": obj.get("ignore_restrictions"),
            "ignore_non_vehicular_restrictions": obj.get("ignore_non_vehicular_restrictions"),
            "ignore_oneways": obj.get("ignore_oneways"),
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
            "include_hot": obj.get("include_hot") if obj.get("include_hot") is not None else False,
            "alley_factor": obj.get("alley_factor") if obj.get("alley_factor") is not None else 1,
            "use_primary": obj.get("use_primary") if obj.get("use_primary") is not None else 0.5,
            "use_hills": obj.get("use_hills") if obj.get("use_hills") is not None else 0.5
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


