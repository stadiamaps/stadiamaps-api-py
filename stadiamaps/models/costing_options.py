# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 6.3.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from stadiamaps.models.auto_costing_options import AutoCostingOptions
from stadiamaps.models.bicycle_costing_options import BicycleCostingOptions
from stadiamaps.models.low_speed_vehicle_costing_options import LowSpeedVehicleCostingOptions
from stadiamaps.models.motor_scooter_costing_options import MotorScooterCostingOptions
from stadiamaps.models.motorcycle_costing_options import MotorcycleCostingOptions
from stadiamaps.models.pedestrian_costing_options import PedestrianCostingOptions
from stadiamaps.models.truck_costing_options import TruckCostingOptions
from typing import Optional, Set
from typing_extensions import Self

class CostingOptions(BaseModel):
    """
    CostingOptions
    """ # noqa: E501
    auto: Optional[AutoCostingOptions] = None
    bus: Optional[AutoCostingOptions] = None
    taxi: Optional[AutoCostingOptions] = None
    truck: Optional[TruckCostingOptions] = None
    bicycle: Optional[BicycleCostingOptions] = None
    motor_scooter: Optional[MotorScooterCostingOptions] = None
    motorcycle: Optional[MotorcycleCostingOptions] = None
    pedestrian: Optional[PedestrianCostingOptions] = None
    low_speed_vehicle: Optional[LowSpeedVehicleCostingOptions] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["auto", "bus", "taxi", "truck", "bicycle", "motor_scooter", "motorcycle", "pedestrian", "low_speed_vehicle"]

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
        """Create an instance of CostingOptions from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of auto
        if self.auto:
            _dict['auto'] = self.auto.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bus
        if self.bus:
            _dict['bus'] = self.bus.to_dict()
        # override the default output from pydantic by calling `to_dict()` of taxi
        if self.taxi:
            _dict['taxi'] = self.taxi.to_dict()
        # override the default output from pydantic by calling `to_dict()` of truck
        if self.truck:
            _dict['truck'] = self.truck.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bicycle
        if self.bicycle:
            _dict['bicycle'] = self.bicycle.to_dict()
        # override the default output from pydantic by calling `to_dict()` of motor_scooter
        if self.motor_scooter:
            _dict['motor_scooter'] = self.motor_scooter.to_dict()
        # override the default output from pydantic by calling `to_dict()` of motorcycle
        if self.motorcycle:
            _dict['motorcycle'] = self.motorcycle.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pedestrian
        if self.pedestrian:
            _dict['pedestrian'] = self.pedestrian.to_dict()
        # override the default output from pydantic by calling `to_dict()` of low_speed_vehicle
        if self.low_speed_vehicle:
            _dict['low_speed_vehicle'] = self.low_speed_vehicle.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CostingOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "auto": AutoCostingOptions.from_dict(obj["auto"]) if obj.get("auto") is not None else None,
            "bus": AutoCostingOptions.from_dict(obj["bus"]) if obj.get("bus") is not None else None,
            "taxi": AutoCostingOptions.from_dict(obj["taxi"]) if obj.get("taxi") is not None else None,
            "truck": TruckCostingOptions.from_dict(obj["truck"]) if obj.get("truck") is not None else None,
            "bicycle": BicycleCostingOptions.from_dict(obj["bicycle"]) if obj.get("bicycle") is not None else None,
            "motor_scooter": MotorScooterCostingOptions.from_dict(obj["motor_scooter"]) if obj.get("motor_scooter") is not None else None,
            "motorcycle": MotorcycleCostingOptions.from_dict(obj["motorcycle"]) if obj.get("motorcycle") is not None else None,
            "pedestrian": PedestrianCostingOptions.from_dict(obj["pedestrian"]) if obj.get("pedestrian") is not None else None,
            "low_speed_vehicle": LowSpeedVehicleCostingOptions.from_dict(obj["low_speed_vehicle"]) if obj.get("low_speed_vehicle") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


