# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 6.1.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from stadiamaps.models.contour import Contour
from stadiamaps.models.coordinate import Coordinate
from stadiamaps.models.costing_options import CostingOptions
from stadiamaps.models.isochrone_costing_model import IsochroneCostingModel
from typing import Optional, Set
from typing_extensions import Self

class IsochroneRequest(BaseModel):
    """
    IsochroneRequest
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="An identifier to disambiguate requests (echoed by the server).")
    locations: List[Coordinate]
    costing: IsochroneCostingModel
    costing_options: Optional[CostingOptions] = None
    contours: Annotated[List[Contour], Field(min_length=1, max_length=4)]
    polygons: Optional[StrictBool] = Field(default=False, description="If true, the generated GeoJSON will use polygons. The default is to use LineStrings. Polygon output makes it easier to render overlapping areas in some visualization tools (such as MapLibre renderers).")
    denoise: Optional[Union[Annotated[float, Field(le=1, strict=True, ge=0)], Annotated[int, Field(le=1, strict=True, ge=0)]]] = Field(default=1, description="A value in the range [0, 1] which will be used to smooth out or remove smaller contours. A value of 1 will only return the largest contour for a given time value. A value of 0.5 drops any contours that are less than half the area of the largest contour in the set of contours for that same time value.")
    generalize: Optional[Union[StrictFloat, StrictInt]] = Field(default=200.0, description="The value in meters to be used as a tolerance for Douglas-Peucker generalization.")
    show_locations: Optional[StrictBool] = Field(default=False, description="If true, then the output GeoJSON will include the input locations as two MultiPoint features: one for the exact input coordinates, and a second for the route network node location that the point was snapped to.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "locations", "costing", "costing_options", "contours", "polygons", "denoise", "generalize", "show_locations"]

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
        """Create an instance of IsochroneRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item in self.locations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of costing_options
        if self.costing_options:
            _dict['costing_options'] = self.costing_options.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in contours (list)
        _items = []
        if self.contours:
            for _item in self.contours:
                if _item:
                    _items.append(_item.to_dict())
            _dict['contours'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IsochroneRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "locations": [Coordinate.from_dict(_item) for _item in obj["locations"]] if obj.get("locations") is not None else None,
            "costing": obj.get("costing"),
            "costing_options": CostingOptions.from_dict(obj["costing_options"]) if obj.get("costing_options") is not None else None,
            "contours": [Contour.from_dict(_item) for _item in obj["contours"]] if obj.get("contours") is not None else None,
            "polygons": obj.get("polygons") if obj.get("polygons") is not None else False,
            "denoise": obj.get("denoise") if obj.get("denoise") is not None else 1,
            "generalize": obj.get("generalize") if obj.get("generalize") is not None else 200.0,
            "show_locations": obj.get("show_locations") if obj.get("show_locations") is not None else False
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


