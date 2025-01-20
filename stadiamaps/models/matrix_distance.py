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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class MatrixDistance(BaseModel):
    """
    MatrixDistance
    """ # noqa: E501
    distance: Optional[Union[StrictFloat, StrictInt]] = Field(description="The distance (in `units`) between the location in `sources` at `from_index` and the location in `targets` at `to_index`. This value may be 0 in the case that the source and destination are the same, and `null` if no route was found between the locations.")
    time: Optional[StrictInt] = Field(description="The travel time (in seconds) between the location in `sources` at `from_index` and the location in `targets` at `to_index`. This value may be 0 in the case that the source and destination are the same, and `null` if no route was found between the locations.")
    from_index: StrictInt = Field(description="The index of the start location in the `sources` array.")
    to_index: StrictInt = Field(description="The index of the end location in the `targets` array.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["distance", "time", "from_index", "to_index"]

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
        """Create an instance of MatrixDistance from a JSON string"""
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

        # set to None if distance (nullable) is None
        # and model_fields_set contains the field
        if self.distance is None and "distance" in self.model_fields_set:
            _dict['distance'] = None

        # set to None if time (nullable) is None
        # and model_fields_set contains the field
        if self.time is None and "time" in self.model_fields_set:
            _dict['time'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MatrixDistance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
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


