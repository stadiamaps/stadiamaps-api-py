# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 10.0.1
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from stadiamaps.models.access import Access
from stadiamaps.models.administrative import Administrative
from stadiamaps.models.node_id import NodeId
from stadiamaps.models.node_type import NodeType
from typing import Optional, Set
from typing_extensions import Self

class LocateNode(BaseModel):
    """
    LocateNode
    """ # noqa: E501
    lat: Union[Annotated[float, Field(le=90, strict=True, ge=-90)], Annotated[int, Field(le=90, strict=True, ge=-90)]] = Field(description="The latitude of a point in the shape.")
    lon: Union[Annotated[float, Field(le=180, strict=True, ge=-180)], Annotated[int, Field(le=180, strict=True, ge=-180)]] = Field(description="The longitude of a point in the shape.")
    traffic_signal: Optional[StrictBool] = None
    type: Optional[NodeType] = None
    node_id: Optional[NodeId] = None
    access: Optional[Access] = None
    edge_count: Optional[StrictInt] = None
    administrative: Optional[Administrative] = None
    intersection_type: Optional[StrictStr] = None
    density: Optional[StrictInt] = None
    local_edge_count: Optional[StrictInt] = None
    mode_change: Optional[StrictBool] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["lat", "lon", "traffic_signal", "type", "node_id", "access", "edge_count", "administrative", "intersection_type", "density", "local_edge_count", "mode_change"]

    @field_validator('intersection_type')
    def intersection_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['regular', 'false', 'dead-end', 'fork']):
            raise ValueError("must be one of enum values ('regular', 'false', 'dead-end', 'fork')")
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
        """Create an instance of LocateNode from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of node_id
        if self.node_id:
            _dict['node_id'] = self.node_id.to_dict()
        # override the default output from pydantic by calling `to_dict()` of access
        if self.access:
            _dict['access'] = self.access.to_dict()
        # override the default output from pydantic by calling `to_dict()` of administrative
        if self.administrative:
            _dict['administrative'] = self.administrative.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LocateNode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lat": obj.get("lat"),
            "lon": obj.get("lon"),
            "traffic_signal": obj.get("traffic_signal"),
            "type": obj.get("type"),
            "node_id": NodeId.from_dict(obj["node_id"]) if obj.get("node_id") is not None else None,
            "access": Access.from_dict(obj["access"]) if obj.get("access") is not None else None,
            "edge_count": obj.get("edge_count"),
            "administrative": Administrative.from_dict(obj["administrative"]) if obj.get("administrative") is not None else None,
            "intersection_type": obj.get("intersection_type"),
            "density": obj.get("density"),
            "local_edge_count": obj.get("local_edge_count"),
            "mode_change": obj.get("mode_change")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


