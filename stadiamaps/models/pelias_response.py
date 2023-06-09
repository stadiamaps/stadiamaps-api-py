# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.5
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, conlist
from stadiamaps.models.pelias_geo_json_feature import PeliasGeoJSONFeature
from stadiamaps.models.pelias_response_geocoding import PeliasResponseGeocoding

class PeliasResponse(BaseModel):
    """
    PeliasResponse
    """
    geocoding: PeliasResponseGeocoding = Field(...)
    bbox: Optional[conlist(Union[StrictFloat, StrictInt], max_items=4, min_items=4)] = Field(None, description="An array of 4 floating point numbers representing the (W, S, E, N) extremes of the features found.")
    features: conlist(PeliasGeoJSONFeature) = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["geocoding", "bbox", "features"]

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
    def from_json(cls, json_str: str) -> PeliasResponse:
        """Create an instance of PeliasResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of geocoding
        if self.geocoding:
            _dict['geocoding'] = self.geocoding.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item in self.features:
                if _item:
                    _items.append(_item.to_dict())
            _dict['features'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PeliasResponse:
        """Create an instance of PeliasResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PeliasResponse.parse_obj(obj)

        _obj = PeliasResponse.parse_obj({
            "geocoding": PeliasResponseGeocoding.from_dict(obj.get("geocoding")) if obj.get("geocoding") is not None else None,
            "bbox": obj.get("bbox"),
            "features": [PeliasGeoJSONFeature.from_dict(_item) for _item in obj.get("features")] if obj.get("features") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

