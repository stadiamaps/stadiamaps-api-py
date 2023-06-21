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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr, conlist, validator
from stadiamaps.models.locate_detailed_edge import LocateDetailedEdge
from stadiamaps.models.locate_edge_info import LocateEdgeInfo
from stadiamaps.models.node_id import NodeId

class LocateEdge(BaseModel):
    """
    LocateEdge
    """
    edge_id: Optional[NodeId] = None
    correlated_lat: Optional[Union[StrictFloat, StrictInt]] = None
    correlated_lon: Optional[Union[StrictFloat, StrictInt]] = None
    percent_along: Optional[Union[StrictFloat, StrictInt]] = None
    side_of_street: Optional[StrictStr] = None
    linear_reference: Optional[StrictStr] = Field(None, description="A base64-encoded [OpenLR location reference](https://www.openlr-association.com/fileadmin/user_upload/openlr-whitepaper_v1.5.pdf), for a graph edge of the road network matched by the query.")
    outbound_reach: Optional[StrictInt] = None
    heading: Optional[Union[StrictFloat, StrictInt]] = None
    inbound_reach: Optional[StrictInt] = None
    distance: Optional[Union[StrictFloat, StrictInt]] = None
    predicted_speeds: Optional[conlist(StrictInt)] = Field(None, description="Predicted speed information based on historical data. If available, this will include 2016 entries. Each entry represents 5 minutes, where the first entry represents midnight on Monday, the second entry represents 00:05 on Monday, etc.")
    edge_info: Optional[LocateEdgeInfo] = None
    edge: Optional[LocateDetailedEdge] = None
    warnings: Optional[conlist(StrictStr)] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["edge_id", "correlated_lat", "correlated_lon", "percent_along", "side_of_street", "linear_reference", "outbound_reach", "heading", "inbound_reach", "distance", "predicted_speeds", "edge_info", "edge", "warnings"]

    @validator('side_of_street')
    def side_of_street_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('left', 'right', 'neither'):
            raise ValueError("must be one of enum values ('left', 'right', 'neither')")
        return value

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
    def from_json(cls, json_str: str) -> LocateEdge:
        """Create an instance of LocateEdge from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of edge_id
        if self.edge_id:
            _dict['edge_id'] = self.edge_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of edge_info
        if self.edge_info:
            _dict['edge_info'] = self.edge_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of edge
        if self.edge:
            _dict['edge'] = self.edge.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> LocateEdge:
        """Create an instance of LocateEdge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return LocateEdge.parse_obj(obj)

        _obj = LocateEdge.parse_obj({
            "edge_id": NodeId.from_dict(obj.get("edge_id")) if obj.get("edge_id") is not None else None,
            "correlated_lat": obj.get("correlated_lat"),
            "correlated_lon": obj.get("correlated_lon"),
            "percent_along": obj.get("percent_along"),
            "side_of_street": obj.get("side_of_street"),
            "linear_reference": obj.get("linear_reference"),
            "outbound_reach": obj.get("outbound_reach"),
            "heading": obj.get("heading"),
            "inbound_reach": obj.get("inbound_reach"),
            "distance": obj.get("distance"),
            "predicted_speeds": obj.get("predicted_speeds"),
            "edge_info": LocateEdgeInfo.from_dict(obj.get("edge_info")) if obj.get("edge_info") is not None else None,
            "edge": LocateDetailedEdge.from_dict(obj.get("edge")) if obj.get("edge") is not None else None,
            "warnings": obj.get("warnings")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

