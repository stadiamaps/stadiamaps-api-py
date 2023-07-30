# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.6
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conlist, validator
from stadiamaps.models.edge_sign import EdgeSign
from stadiamaps.models.edge_use import EdgeUse
from stadiamaps.models.end_node import EndNode
from stadiamaps.models.road_class import RoadClass
from stadiamaps.models.travel_mode import TravelMode
from stadiamaps.models.traversability import Traversability

class TraceEdge(BaseModel):
    """
    TraceEdge
    """
    names: Optional[conlist(StrictStr)] = Field(None, description="The name(s) of the road at this edge, if any.")
    length: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The length of this edge in `units`.")
    speed: Optional[StrictInt] = Field(None, description="The speed of this edge in `units`/hr, in terms of average/free-flow speed for routing purposes. This is affected by any number of factors such as the road service, vehicle type, etc. and not just the posted speed limits.")
    road_class: Optional[RoadClass] = None
    begin_heading: Optional[StrictInt] = Field(None, description="The direction at the beginning of an edge. The units are degrees clockwise from north.")
    end_heading: Optional[StrictInt] = Field(None, description="The direction at the end of an edge. The units are degrees clockwise from north.")
    begin_shape_index: Optional[StrictInt] = Field(None, description="Index into the list of shape points for the start of the edge.")
    end_shape_index: Optional[StrictInt] = Field(None, description="Index into the list of shape points for the end of the edge.")
    traversability: Optional[Traversability] = None
    use: Optional[EdgeUse] = None
    toll: Optional[StrictBool] = Field(None, description="True if the edge has a toll.")
    unpaved: Optional[StrictBool] = Field(None, description="True if the edge has rough payment.")
    tunnel: Optional[StrictBool] = Field(None, description="True if the edge has a tunnel.")
    bridge: Optional[StrictBool] = Field(None, description="True if the edge has a bridge.")
    roundabout: Optional[StrictBool] = Field(None, description="True if the edge has a roundabout.")
    internal_intersection: Optional[StrictBool] = Field(None, description="True if the edge has an internal intersection.")
    drive_on_right: Optional[StrictBool] = Field(None, description="True if the edge is in an area where you must drive on the right side of the road.")
    surface: Optional[StrictStr] = Field(None, description="The type of surface for the edge.")
    sign: Optional[EdgeSign] = None
    travel_mode: Optional[TravelMode] = None
    vehicle_type: Optional[StrictStr] = None
    pedestrian_type: Optional[StrictStr] = None
    bicycle_type: Optional[StrictStr] = None
    transit_type: Optional[StrictStr] = None
    id: Optional[StrictInt] = None
    way_id: Optional[StrictInt] = Field(None, description="The way identifier of the edge in OSM.")
    weighted_grade: Optional[Union[StrictFloat, StrictInt]] = Field(None, description="The weighted grade factor. Valhalla manufactures a weighted grade from elevation data. It is a measure used for hill avoidance in routing - sort of a relative energy use along an edge. But since an edge in Valhalla can possibly go up and down over several hills it might not equate to what you would normally think of as grade.")
    max_upward_grade: Optional[StrictInt] = Field(None, description="The maximum upward slope. A value of 32768 indicates no elevation data is available for this edge.")
    max_downward_grade: Optional[StrictInt] = Field(None, description="The maximum downward slope. A value of 32768 indicates no elevation data is available for this edge.")
    mean_elevation: Optional[StrictInt] = Field(None, description="The mean elevation along the edge. Units are meters by default. If the `units` are specified as miles, then the mean elevation is returned in feet. A value of 32768 indicates no elevation data is available for this edge.")
    lane_count: Optional[StrictInt] = Field(None, description="The number of lanes for this edge.")
    cycle_lane: Optional[StrictStr] = Field(None, description="The type of cycle lane (if any) along this edge.")
    bicycle_network: Optional[StrictInt] = Field(None, description="The type of bicycle network, if any. This is an integer comprised of constants bitwise or'd together. For example, a route that's part of both a local and mountain network would have a value of 12. 1 - National 2 - Regional 4 - Local 8 - Mountain")
    sac_scale: Optional[StrictInt] = Field(None, description="The difficulty of the hiking trail according to the SAC scale. 0 - No Sac Scale 1 - Hiking 2 - Mountain hiking 3 - Demanding mountain hiking 4 - Alpine hiking 5 - Demanding alpine hiking 6 - Difficult alpine hiking")
    sidewalk: Optional[StrictStr] = None
    density: Optional[StrictInt] = None
    speed_limit: Optional[Any] = Field(None, description="The speed limit along the edge measured in `units`/hr. This may be either an integer or the string \"unlimited\" if speed limit data is available. If absent, there is no speed limit data available.")
    truck_speed: Optional[StrictInt] = Field(None, description="The truck speed of this edge in `units`/hr, in terms of average/free-flow speed for routing purposes. This is affected by any number of factors such as the road service, vehicle type, etc. and not just the posted speed limits.")
    truck_route: Optional[StrictBool] = Field(None, description="True if the edge is part of a truck route/network.")
    end_node: Optional[EndNode] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["names", "length", "speed", "road_class", "begin_heading", "end_heading", "begin_shape_index", "end_shape_index", "traversability", "use", "toll", "unpaved", "tunnel", "bridge", "roundabout", "internal_intersection", "drive_on_right", "surface", "sign", "travel_mode", "vehicle_type", "pedestrian_type", "bicycle_type", "transit_type", "id", "way_id", "weighted_grade", "max_upward_grade", "max_downward_grade", "mean_elevation", "lane_count", "cycle_lane", "bicycle_network", "sac_scale", "sidewalk", "density", "speed_limit", "truck_speed", "truck_route", "end_node"]

    @validator('surface')
    def surface_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('paved_smooth', 'paved', 'paved_rough', 'compacted', 'dirt', 'gravel', 'path', 'impassable'):
            raise ValueError("must be one of enum values ('paved_smooth', 'paved', 'paved_rough', 'compacted', 'dirt', 'gravel', 'path', 'impassable')")
        return value

    @validator('vehicle_type')
    def vehicle_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('car', 'motorcycle', 'bus', 'tractor_trailer'):
            raise ValueError("must be one of enum values ('car', 'motorcycle', 'bus', 'tractor_trailer')")
        return value

    @validator('pedestrian_type')
    def pedestrian_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('foot', 'wheelchair', 'segway'):
            raise ValueError("must be one of enum values ('foot', 'wheelchair', 'segway')")
        return value

    @validator('bicycle_type')
    def bicycle_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('road', 'cross', 'hybrid', 'mountain'):
            raise ValueError("must be one of enum values ('road', 'cross', 'hybrid', 'mountain')")
        return value

    @validator('transit_type')
    def transit_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('tram', 'metro', 'rail', 'bus', 'ferry', 'cable_car', 'gondola', 'funicular'):
            raise ValueError("must be one of enum values ('tram', 'metro', 'rail', 'bus', 'ferry', 'cable_car', 'gondola', 'funicular')")
        return value

    @validator('cycle_lane')
    def cycle_lane_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('none', 'shared', 'dedicated', 'separated'):
            raise ValueError("must be one of enum values ('none', 'shared', 'dedicated', 'separated')")
        return value

    @validator('sidewalk')
    def sidewalk_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('left', 'right', 'both', 'none'):
            raise ValueError("must be one of enum values ('left', 'right', 'both', 'none')")
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
    def from_json(cls, json_str: str) -> TraceEdge:
        """Create an instance of TraceEdge from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of sign
        if self.sign:
            _dict['sign'] = self.sign.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_node
        if self.end_node:
            _dict['end_node'] = self.end_node.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if speed_limit (nullable) is None
        # and __fields_set__ contains the field
        if self.speed_limit is None and "speed_limit" in self.__fields_set__:
            _dict['speed_limit'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TraceEdge:
        """Create an instance of TraceEdge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return TraceEdge.parse_obj(obj)

        _obj = TraceEdge.parse_obj({
            "names": obj.get("names"),
            "length": obj.get("length"),
            "speed": obj.get("speed"),
            "road_class": obj.get("road_class"),
            "begin_heading": obj.get("begin_heading"),
            "end_heading": obj.get("end_heading"),
            "begin_shape_index": obj.get("begin_shape_index"),
            "end_shape_index": obj.get("end_shape_index"),
            "traversability": obj.get("traversability"),
            "use": obj.get("use"),
            "toll": obj.get("toll"),
            "unpaved": obj.get("unpaved"),
            "tunnel": obj.get("tunnel"),
            "bridge": obj.get("bridge"),
            "roundabout": obj.get("roundabout"),
            "internal_intersection": obj.get("internal_intersection"),
            "drive_on_right": obj.get("drive_on_right"),
            "surface": obj.get("surface"),
            "sign": EdgeSign.from_dict(obj.get("sign")) if obj.get("sign") is not None else None,
            "travel_mode": obj.get("travel_mode"),
            "vehicle_type": obj.get("vehicle_type"),
            "pedestrian_type": obj.get("pedestrian_type"),
            "bicycle_type": obj.get("bicycle_type"),
            "transit_type": obj.get("transit_type"),
            "id": obj.get("id"),
            "way_id": obj.get("way_id"),
            "weighted_grade": obj.get("weighted_grade"),
            "max_upward_grade": obj.get("max_upward_grade"),
            "max_downward_grade": obj.get("max_downward_grade"),
            "mean_elevation": obj.get("mean_elevation"),
            "lane_count": obj.get("lane_count"),
            "cycle_lane": obj.get("cycle_lane"),
            "bicycle_network": obj.get("bicycle_network"),
            "sac_scale": obj.get("sac_scale"),
            "sidewalk": obj.get("sidewalk"),
            "density": obj.get("density"),
            "speed_limit": obj.get("speed_limit"),
            "truck_speed": obj.get("truck_speed"),
            "truck_route": obj.get("truck_route"),
            "end_node": EndNode.from_dict(obj.get("end_node")) if obj.get("end_node") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

