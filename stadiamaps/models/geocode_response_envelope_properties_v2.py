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
from typing_extensions import Annotated
from stadiamaps.models.feature_properties_v2 import FeaturePropertiesV2
from stadiamaps.models.geocoding_meta import GeocodingMeta
from typing import Optional, Set
from typing_extensions import Self

class GeocodeResponseEnvelopePropertiesV2(BaseModel):
    """
    The GeoJSON response envelope.  This is parameterized over the feature properties type to allow for changes between versions.
    """ # noqa: E501
    bbox: Optional[Annotated[List[Union[StrictFloat, StrictInt]], Field(min_length=4, max_length=4)]] = Field(default=None, description="The geographic bounding box covering all features in the result set.  This is empty for autocomplete results.")
    features: List[FeaturePropertiesV2]
    geocoding: GeocodingMeta
    type: StrictStr = Field(description="The GeoJSON object type as defined in RFC 7946.  NOTE: This is always FeatureCollection, as the response envelope is designed to hold multiple results.")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["bbox", "features", "geocoding", "type"]

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
        """Create an instance of GeocodeResponseEnvelopePropertiesV2 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item_features in self.features:
                if _item_features:
                    _items.append(_item_features.to_dict())
            _dict['features'] = _items
        # override the default output from pydantic by calling `to_dict()` of geocoding
        if self.geocoding:
            _dict['geocoding'] = self.geocoding.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if bbox (nullable) is None
        # and model_fields_set contains the field
        if self.bbox is None and "bbox" in self.model_fields_set:
            _dict['bbox'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GeocodeResponseEnvelopePropertiesV2 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "bbox": obj.get("bbox"),
            "features": [FeaturePropertiesV2.from_dict(_item) for _item in obj["features"]] if obj.get("features") is not None else None,
            "geocoding": GeocodingMeta.from_dict(obj["geocoding"]) if obj.get("geocoding") is not None else None,
            "type": obj.get("type")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


