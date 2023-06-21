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


from typing import List, Optional
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist
from stadiamaps.models.coordinate import Coordinate
from stadiamaps.models.costing_options import CostingOptions
from stadiamaps.models.directions_options import DirectionsOptions
from stadiamaps.models.matrix_costing_model import MatrixCostingModel

class MatrixRequest(BaseModel):
    """
    MatrixRequest
    """
    id: Optional[StrictStr] = Field(None, description="An identifier to disambiguate requests (echoed by the server).")
    sources: conlist(Coordinate, min_items=1) = Field(..., description="The list of starting locations")
    targets: conlist(Coordinate, min_items=1) = Field(..., description="The list of ending locations")
    costing: MatrixCostingModel = Field(...)
    costing_options: Optional[CostingOptions] = None
    matrix_locations: Optional[StrictInt] = Field(None, description="Only applicable to one-to-many or many-to-one requests. This defaults to all locations. When specified explicitly, this option allows a partial result to be returned. This is basically equivalent to \"find the closest/best locations out of the full set.\" This can have a dramatic improvement for large requests.")
    directions_options: Optional[DirectionsOptions] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "sources", "targets", "costing", "costing_options", "matrix_locations", "directions_options"]

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
    def from_json(cls, json_str: str) -> MatrixRequest:
        """Create an instance of MatrixRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in sources (list)
        _items = []
        if self.sources:
            for _item in self.sources:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sources'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in targets (list)
        _items = []
        if self.targets:
            for _item in self.targets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['targets'] = _items
        # override the default output from pydantic by calling `to_dict()` of costing_options
        if self.costing_options:
            _dict['costing_options'] = self.costing_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of directions_options
        if self.directions_options:
            _dict['directions_options'] = self.directions_options.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MatrixRequest:
        """Create an instance of MatrixRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MatrixRequest.parse_obj(obj)

        _obj = MatrixRequest.parse_obj({
            "id": obj.get("id"),
            "sources": [Coordinate.from_dict(_item) for _item in obj.get("sources")] if obj.get("sources") is not None else None,
            "targets": [Coordinate.from_dict(_item) for _item in obj.get("targets")] if obj.get("targets") is not None else None,
            "costing": obj.get("costing"),
            "costing_options": CostingOptions.from_dict(obj.get("costing_options")) if obj.get("costing_options") is not None else None,
            "matrix_locations": obj.get("matrix_locations"),
            "directions_options": DirectionsOptions.from_dict(obj.get("directions_options")) if obj.get("directions_options") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

