# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 6.6.3
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

class BaseCostingOptions(BaseModel):
    """
    BaseCostingOptions
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
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["maneuver_penalty", "gate_cost", "gate_penalty", "country_crossing_cost", "country_crossing_penalty", "service_penalty", "service_factor", "use_living_streets", "use_ferry", "ignore_restrictions", "ignore_non_vehicular_restrictions", "ignore_oneways"]

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
        """Create an instance of BaseCostingOptions from a JSON string"""
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
        """Create an instance of BaseCostingOptions from a dict"""
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
            "ignore_oneways": obj.get("ignore_oneways")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


