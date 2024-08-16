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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from stadiamaps.models.coordinate import Coordinate
from typing import Optional, Set
from typing_extensions import Self

class HeightResponse(BaseModel):
    """
    HeightResponse
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="An identifier to disambiguate requests (echoed by the server).")
    shape: Optional[List[Coordinate]] = None
    encoded_polyline: Optional[StrictStr] = Field(default=None, description="The input polyline.")
    height: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="The list of heights for each point, in meters. Present only if `range` is `false`. Null values indicate missing data.")
    range_height: Optional[List[Annotated[List[Union[StrictFloat, StrictInt]], Field(min_length=2, max_length=2)]]] = Field(default=None, description="The list of ranges and heights for each point in the shape, where each entry is an array of length 2. Present only if `range` is `true`. In each pair, the first element represents the range or distance along the input locations. It is the cumulative distance along the previous coordinates in the shape up to the current coordinate. This value for the first coordinate in the shape will always be 0. The second element in the pair represents the height or elevation at the associated coordinate. The height is null if no height data exists for a given location. Both values are expressed in meters.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "shape", "encoded_polyline", "height", "range_height"]

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
        """Create an instance of HeightResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in shape (list)
        _items = []
        if self.shape:
            for _item in self.shape:
                if _item:
                    _items.append(_item.to_dict())
            _dict['shape'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of HeightResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "shape": [Coordinate.from_dict(_item) for _item in obj["shape"]] if obj.get("shape") is not None else None,
            "encoded_polyline": obj.get("encoded_polyline"),
            "height": obj.get("height"),
            "range_height": obj.get("range_height")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


