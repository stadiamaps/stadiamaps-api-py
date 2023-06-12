# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.2
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, conint, validator
from stadiamaps.models.routing_waypoint_all_of_search_filter import RoutingWaypointAllOfSearchFilter

class RoutingWaypoint(BaseModel):
    """
    RoutingWaypoint
    """
    lat: Union[StrictFloat, StrictInt] = Field(..., description="The latitude of a point in the shape.")
    lon: Union[StrictFloat, StrictInt] = Field(..., description="The longitude of a point in the shape.")
    type: Optional[StrictStr] = Field('break', description="A `break` represents the start or end of a leg, and allows reversals. A `through` location is an intermediate waypoint that must be visited between `break`s, but at which reversals are not allowed. A `via` is similar to a `through` except that reversals are allowed. A `break_through` is similar to a `break` in that it can be the start/end of a leg, but does not allow reversals.")
    heading: Optional[conint(strict=True, le=360, ge=0)] = Field(None, description="The preferred direction of travel when starting the route, in integer clockwise degrees from north. North is 0, south is 180, east is 90, and west is 270.")
    heading_tolerance: Optional[conint(strict=True, le=360, ge=0)] = Field(60, description="The tolerance (in degrees) determining whether a street is considered the same direction.")
    minimum_reachability: Optional[conint(strict=True, ge=0)] = Field(50, description="The minimum number of nodes that must be reachable for a given edge to consider that edge as belonging to a connected region. If a candidate edge has fewer connections, it will be considered a disconnected island.")
    radius: Optional[conint(strict=True, ge=0)] = Field(0, description="The distance (in meters) to look for candidate edges around the location for purposes of snapping locations to the route graph. If there are no candidates within this distance, the closest candidate within a reasonable search distance will be used. This is subject to clamping by internal limits.")
    rank_candidates: Optional[StrictBool] = Field(True, description="If true, candidates will be ranked according to their distance from the target location as well as other factors. If false, candidates will only be ranked using their distance from the target.")
    preferred_side: Optional[StrictStr] = Field(None, description="If the location is not offset from the road centerline or is closest to an intersection, this option has no effect. Otherwise, the preferred side of street is used to determine whether or not the location should be visited from the same, opposite or either side of the road with respect to the side of the road the given locale drives on.")
    node_snap_tolerance: Optional[conint(strict=True, ge=0)] = Field(5, description="During edge correlation this is the tolerance (in meters) used to determine whether or not to snap to the intersection rather than along the street, if the snap location is within this distance from the intersection, the intersection is used instead.")
    street_side_tolerance: Optional[conint(strict=True, ge=0)] = Field(5, description="A tolerance in meters from the edge centerline used for determining the side of the street that the location is on. If the distance to the centerline is less than this tolerance, no side will be inferred. Otherwise, the left or right side will be selected depending on the direction of travel.")
    street_side_max_distance: Optional[conint(strict=True, ge=0)] = Field(1000, description="A tolerance in meters from the edge centerline used for determining the side of the street that the location is on. If the distance to the centerline is greater than this tolerance, no side will be inferred. Otherwise, the left or right side will be selected depending on the direction of travel.")
    search_filter: Optional[RoutingWaypointAllOfSearchFilter] = None
    additional_properties: Dict[str, Any] = {}
    __properties = ["lat", "lon", "type", "heading", "heading_tolerance", "minimum_reachability", "radius", "rank_candidates", "preferred_side", "node_snap_tolerance", "street_side_tolerance", "street_side_max_distance", "search_filter"]

    @validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('break', 'through', 'via', 'break_through'):
            raise ValueError("must be one of enum values ('break', 'through', 'via', 'break_through')")
        return value

    @validator('preferred_side')
    def preferred_side_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('same', 'opposite', 'either'):
            raise ValueError("must be one of enum values ('same', 'opposite', 'either')")
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
    def from_json(cls, json_str: str) -> RoutingWaypoint:
        """Create an instance of RoutingWaypoint from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of search_filter
        if self.search_filter:
            _dict['search_filter'] = self.search_filter.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RoutingWaypoint:
        """Create an instance of RoutingWaypoint from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RoutingWaypoint.parse_obj(obj)

        _obj = RoutingWaypoint.parse_obj({
            "lat": obj.get("lat"),
            "lon": obj.get("lon"),
            "type": obj.get("type") if obj.get("type") is not None else 'break',
            "heading": obj.get("heading"),
            "heading_tolerance": obj.get("heading_tolerance") if obj.get("heading_tolerance") is not None else 60,
            "minimum_reachability": obj.get("minimum_reachability") if obj.get("minimum_reachability") is not None else 50,
            "radius": obj.get("radius") if obj.get("radius") is not None else 0,
            "rank_candidates": obj.get("rank_candidates") if obj.get("rank_candidates") is not None else True,
            "preferred_side": obj.get("preferred_side"),
            "node_snap_tolerance": obj.get("node_snap_tolerance") if obj.get("node_snap_tolerance") is not None else 5,
            "street_side_tolerance": obj.get("street_side_tolerance") if obj.get("street_side_tolerance") is not None else 5,
            "street_side_max_distance": obj.get("street_side_max_distance") if obj.get("street_side_max_distance") is not None else 1000,
            "search_filter": RoutingWaypointAllOfSearchFilter.from_dict(obj.get("search_filter")) if obj.get("search_filter") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

