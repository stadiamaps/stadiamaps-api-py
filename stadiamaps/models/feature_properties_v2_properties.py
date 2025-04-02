# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 9.0.0
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
from stadiamaps.models.addendum_v2 import AddendumV2
from stadiamaps.models.address_components_v2 import AddressComponentsV2
from stadiamaps.models.context import Context
from stadiamaps.models.match_type import MatchType
from stadiamaps.models.precision import Precision
from stadiamaps.models.source_attribution import SourceAttribution
from typing import Optional, Set
from typing_extensions import Self

class FeaturePropertiesV2Properties(BaseModel):
    """
    The GeoJSON properties object.
    """ # noqa: E501
    addendum: Optional[AddendumV2] = None
    address_components: Optional[AddressComponentsV2] = None
    coarse_location: Optional[StrictStr] = Field(default=None, description="The coarse-grained location of the place (e.g. Seoul, South Korea).  In search experiences, this is typically the second line of a result cell.")
    confidence: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The level of confidence (0.0 - 1.0) that the result is what you actually searched for.  This is not necessarily the same as relevance (results are returned sorted by relevance already), but rather how closely the explicit or inferred components match the result. This is only present for forward geocoding responses (not autocomplete or place details).")
    context: Optional[Context] = None
    distance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The distance from the search focus point, in kilometers.")
    formatted_address_line: Optional[StrictStr] = Field(default=None, description="The address formatted as a single line, following local postal conventions for ordering and separators.")
    formatted_address_lines: Optional[List[StrictStr]] = Field(default=None, description="Address components split up into lines, following local postal conventions for ordering and separators.")
    gid: StrictStr = Field(description="The globally unique identifier for this result.  You can use this to uniquely identify a place, and to get the full details from the place details endpoint.  NOTE: While GIDs are unique, they may not necessarily be stable in all datasets.")
    layer: StrictStr = Field(description="The data layer containing the place (e.g. \"address\" or \"poi\").")
    match_type: Optional[MatchType] = Field(default=None, description="The type of match (forward geocoding endpoints only).")
    name: StrictStr = Field(description="The best name for the place, accounting for request language preferences.  When building an autocomplete search experience, this is the primary display string.")
    precision: Precision
    sources: Optional[List[SourceAttribution]] = Field(default=None, description="A list of sources from which the result is derived.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["addendum", "address_components", "coarse_location", "confidence", "context", "distance", "formatted_address_line", "formatted_address_lines", "gid", "layer", "match_type", "name", "precision", "sources"]

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
        """Create an instance of FeaturePropertiesV2Properties from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of addendum
        if self.addendum:
            _dict['addendum'] = self.addendum.to_dict()
        # override the default output from pydantic by calling `to_dict()` of address_components
        if self.address_components:
            _dict['address_components'] = self.address_components.to_dict()
        # override the default output from pydantic by calling `to_dict()` of context
        if self.context:
            _dict['context'] = self.context.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sources (list)
        _items = []
        if self.sources:
            for _item_sources in self.sources:
                if _item_sources:
                    _items.append(_item_sources.to_dict())
            _dict['sources'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if addendum (nullable) is None
        # and model_fields_set contains the field
        if self.addendum is None and "addendum" in self.model_fields_set:
            _dict['addendum'] = None

        # set to None if address_components (nullable) is None
        # and model_fields_set contains the field
        if self.address_components is None and "address_components" in self.model_fields_set:
            _dict['address_components'] = None

        # set to None if coarse_location (nullable) is None
        # and model_fields_set contains the field
        if self.coarse_location is None and "coarse_location" in self.model_fields_set:
            _dict['coarse_location'] = None

        # set to None if confidence (nullable) is None
        # and model_fields_set contains the field
        if self.confidence is None and "confidence" in self.model_fields_set:
            _dict['confidence'] = None

        # set to None if context (nullable) is None
        # and model_fields_set contains the field
        if self.context is None and "context" in self.model_fields_set:
            _dict['context'] = None

        # set to None if distance (nullable) is None
        # and model_fields_set contains the field
        if self.distance is None and "distance" in self.model_fields_set:
            _dict['distance'] = None

        # set to None if match_type (nullable) is None
        # and model_fields_set contains the field
        if self.match_type is None and "match_type" in self.model_fields_set:
            _dict['match_type'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FeaturePropertiesV2Properties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addendum": AddendumV2.from_dict(obj["addendum"]) if obj.get("addendum") is not None else None,
            "address_components": AddressComponentsV2.from_dict(obj["address_components"]) if obj.get("address_components") is not None else None,
            "coarse_location": obj.get("coarse_location"),
            "confidence": obj.get("confidence"),
            "context": Context.from_dict(obj["context"]) if obj.get("context") is not None else None,
            "distance": obj.get("distance"),
            "formatted_address_line": obj.get("formatted_address_line"),
            "formatted_address_lines": obj.get("formatted_address_lines"),
            "gid": obj.get("gid"),
            "layer": obj.get("layer"),
            "match_type": obj.get("match_type"),
            "name": obj.get("name"),
            "precision": obj.get("precision"),
            "sources": [SourceAttribution.from_dict(_item) for _item in obj["sources"]] if obj.get("sources") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


