# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 7.0.0
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
from stadiamaps.models.annotation_filters import AnnotationFilters
from stadiamaps.models.coordinate import Coordinate
from stadiamaps.models.costing_options import CostingOptions
from stadiamaps.models.distance_unit import DistanceUnit
from stadiamaps.models.matrix_costing_model import MatrixCostingModel
from stadiamaps.models.valhalla_languages import ValhallaLanguages
from typing import Optional, Set
from typing_extensions import Self

class OptimizedRouteRequest(BaseModel):
    """
    OptimizedRouteRequest
    """ # noqa: E501
    units: Optional[DistanceUnit] = DistanceUnit.KM
    language: Optional[ValhallaLanguages] = ValhallaLanguages.EN_MINUS_US
    directions_type: Optional[StrictStr] = Field(default='instructions', description="The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter.")
    format: Optional[StrictStr] = Field(default=None, description="The output response format. The default JSON format is extremely compact and ideal for web or data-constrained use cases where you want to fetch additional attributes on demand in small chunks. The OSRM format is much richer and is configurable with significantly more info for turn-by-turn navigation use cases.")
    banner_instructions: Optional[StrictBool] = Field(default=None, description="Optionally includes helpful banners with timing information for turn-by-turn navigation. This is only available in the OSRM format.")
    voice_instructions: Optional[StrictBool] = Field(default=None, description="Optionally includes voice instructions with timing information for turn-by-turn navigation. This is only available in the OSRM format.")
    filters: Optional[AnnotationFilters] = None
    id: Optional[StrictStr] = Field(default=None, description="An identifier to disambiguate requests (echoed by the server).")
    locations: Annotated[List[Coordinate], Field(min_length=3)] = Field(description="The list of locations. The first and last are assumed to be the start and end points, and all intermediate points are locations that you want to visit along the way.")
    costing: MatrixCostingModel
    costing_options: Optional[CostingOptions] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["units", "language", "directions_type", "format", "banner_instructions", "voice_instructions", "filters", "id", "locations", "costing", "costing_options"]

    @field_validator('directions_type')
    def directions_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'maneuvers', 'instructions']):
            raise ValueError("must be one of enum values ('none', 'maneuvers', 'instructions')")
        return value

    @field_validator('format')
    def format_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['json', 'osrm']):
            raise ValueError("must be one of enum values ('json', 'osrm')")
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
        """Create an instance of OptimizedRouteRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in locations (list)
        _items = []
        if self.locations:
            for _item_locations in self.locations:
                if _item_locations:
                    _items.append(_item_locations.to_dict())
            _dict['locations'] = _items
        # override the default output from pydantic by calling `to_dict()` of costing_options
        if self.costing_options:
            _dict['costing_options'] = self.costing_options.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OptimizedRouteRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "units": obj.get("units") if obj.get("units") is not None else DistanceUnit.KM,
            "language": obj.get("language") if obj.get("language") is not None else ValhallaLanguages.EN_MINUS_US,
            "directions_type": obj.get("directions_type") if obj.get("directions_type") is not None else 'instructions',
            "format": obj.get("format"),
            "banner_instructions": obj.get("banner_instructions"),
            "voice_instructions": obj.get("voice_instructions"),
            "filters": AnnotationFilters.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "id": obj.get("id"),
            "locations": [Coordinate.from_dict(_item) for _item in obj["locations"]] if obj.get("locations") is not None else None,
            "costing": obj.get("costing"),
            "costing_options": CostingOptions.from_dict(obj["costing_options"]) if obj.get("costing_options") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


