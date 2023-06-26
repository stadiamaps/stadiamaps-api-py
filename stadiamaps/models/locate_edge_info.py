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
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist
from stadiamaps.models.bike_network import BikeNetwork

class LocateEdgeInfo(BaseModel):
    """
    LocateEdgeInfo
    """
    mean_elevation: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The mean elevation, in meters, relative to sea level.")
    shape: Optional[StrictStr] = Field(None, description="An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm). Note that the polyline is always encoded with 6 digits of precision, whereas most implementations default to 5.")
    names: Optional[conlist(StrictStr)] = Field(None, description="A list of names that the edge goes by.")
    bike_network: Optional[BikeNetwork] = None
    way_id: Optional[StrictInt] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["mean_elevation", "shape", "names", "bike_network", "way_id"]

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
    def from_json(cls, json_str: str) -> LocateEdgeInfo:
        """Create an instance of LocateEdgeInfo from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of bike_network
        if self.bike_network:
            _dict['bike_network'] = self.bike_network.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LocateEdgeInfo:
        """Create an instance of LocateEdgeInfo from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LocateEdgeInfo.parse_obj(obj)

        _obj = LocateEdgeInfo.parse_obj({
            "mean_elevation": obj.get("mean_elevation"),
            "shape": obj.get("shape"),
            "names": obj.get("names"),
            "bike_network": BikeNetwork.from_dict(obj.get("bike_network")) if obj.get("bike_network") is not None else None,
            "way_id": obj.get("way_id")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

