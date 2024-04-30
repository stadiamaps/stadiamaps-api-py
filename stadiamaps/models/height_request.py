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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from stadiamaps.models.coordinate import Coordinate
from typing import Optional, Set
from typing_extensions import Self

class HeightRequest(BaseModel):
    """
    HeightRequest
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="An identifier to disambiguate requests (echoed by the server).")
    shape: Optional[List[Coordinate]] = Field(default=None, description="REQUIRED if `encoded_polyline` is not present.")
    encoded_polyline: Optional[StrictStr] = Field(default=None, description="REQUIRED if `shape` is not present. An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm).")
    shape_format: Optional[StrictStr] = Field(default='polyline6', description="Specifies whether the polyline is encoded with 6 digit precision (polyline6) or 5 digit precision (polyline5).")
    range: Optional[StrictBool] = Field(default=False, description="Controls whether or not the returned array is one-dimensional (height only) or two-dimensional (with a range and height). The range dimension can be used to generate a graph or steepness gradient along a route.")
    height_precision: Optional[Annotated[int, Field(le=2, strict=True, ge=0)]] = Field(default=0, description="The decimal precision (number of digits after the point) of the output. When 0, integer values are returned. Valid values are 0, 1, and 2.")
    resample_distance: Optional[Annotated[int, Field(strict=True, ge=10)]] = Field(default=None, description="The distance at which the input polyline should be sampled to provide uniform distances between points. If not set, the input shape will be used as-is.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "shape", "encoded_polyline", "shape_format", "range", "height_precision", "resample_distance"]

    @field_validator('shape_format')
    def shape_format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['polyline6', 'polyline5']):
            raise ValueError("must be one of enum values ('polyline6', 'polyline5')")
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
        """Create an instance of HeightRequest from a JSON string"""
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
        """Create an instance of HeightRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "shape": [Coordinate.from_dict(_item) for _item in obj["shape"]] if obj.get("shape") is not None else None,
            "encoded_polyline": obj.get("encoded_polyline"),
            "shape_format": obj.get("shape_format") if obj.get("shape_format") is not None else 'polyline6',
            "range": obj.get("range") if obj.get("range") is not None else False,
            "height_precision": obj.get("height_precision") if obj.get("height_precision") is not None else 0,
            "resample_distance": obj.get("resample_distance")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


