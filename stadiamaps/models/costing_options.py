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


from typing import Optional
from pydantic import BaseModel
from stadiamaps.models.auto_costing_options import AutoCostingOptions
from stadiamaps.models.bicycle_costing_options import BicycleCostingOptions
from stadiamaps.models.motor_scooter_costing_options import MotorScooterCostingOptions
from stadiamaps.models.motorcycle_costing_options import MotorcycleCostingOptions
from stadiamaps.models.pedestrian_costing_options import PedestrianCostingOptions
from stadiamaps.models.truck_costing_options import TruckCostingOptions

class CostingOptions(BaseModel):
    """
    CostingOptions
    """
    auto: Optional[AutoCostingOptions] = None
    bus: Optional[AutoCostingOptions] = None
    taxi: Optional[AutoCostingOptions] = None
    truck: Optional[TruckCostingOptions] = None
    bicycle: Optional[BicycleCostingOptions] = None
    motor_scooter: Optional[MotorScooterCostingOptions] = None
    motorcycle: Optional[MotorcycleCostingOptions] = None
    pedestrian: Optional[PedestrianCostingOptions] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["auto", "bus", "taxi", "truck", "bicycle", "motor_scooter", "motorcycle", "pedestrian"]

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
    def from_json(cls, json_str: str) -> CostingOptions:
        """Create an instance of CostingOptions from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CostingOptions:
        """Create an instance of CostingOptions from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CostingOptions.parse_obj(obj)

        _obj = CostingOptions.parse_obj({
            "auto": AutoCostingOptions.from_dict(obj.get("auto")) if obj.get("auto") is not None else None,
            "bus": AutoCostingOptions.from_dict(obj.get("bus")) if obj.get("bus") is not None else None,
            "taxi": AutoCostingOptions.from_dict(obj.get("taxi")) if obj.get("taxi") is not None else None,
            "truck": TruckCostingOptions.from_dict(obj.get("truck")) if obj.get("truck") is not None else None,
            "bicycle": BicycleCostingOptions.from_dict(obj.get("bicycle")) if obj.get("bicycle") is not None else None,
            "motor_scooter": MotorScooterCostingOptions.from_dict(obj.get("motor_scooter")) if obj.get("motor_scooter") is not None else None,
            "motorcycle": MotorcycleCostingOptions.from_dict(obj.get("motorcycle")) if obj.get("motorcycle") is not None else None,
            "pedestrian": PedestrianCostingOptions.from_dict(obj.get("pedestrian")) if obj.get("pedestrian") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

