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


from typing import Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt

class MatrixDistance(BaseModel):
    """
    MatrixDistance
    """
    distance: Union[StrictFloat, StrictInt] = Field(..., description="The distance (in `units`) between the location in `sources` at `from_index` and the location in `targets` at `to_index`.")
    time: StrictInt = Field(..., description="The travel time (in seconds) between the location in `sources` at `from_index` and the location in `targets` at `to_index`.")
    from_index: StrictInt = Field(..., description="The index of the start location in the `sources` array.")
    to_index: StrictInt = Field(..., description="The index of the end location in the `targets` array.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["distance", "time", "from_index", "to_index"]

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
    def from_json(cls, json_str: str) -> MatrixDistance:
        """Create an instance of MatrixDistance from a JSON string"""
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
    def from_dict(cls, obj: dict) -> MatrixDistance:
        """Create an instance of MatrixDistance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MatrixDistance.parse_obj(obj)

        _obj = MatrixDistance.parse_obj({
            "distance": obj.get("distance"),
            "time": obj.get("time"),
            "from_index": obj.get("from_index"),
            "to_index": obj.get("to_index")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

