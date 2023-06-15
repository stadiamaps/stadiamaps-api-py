# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.3
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr, validator
from stadiamaps.models.pelias_geo_json_properties_addendum import PeliasGeoJSONPropertiesAddendum
from stadiamaps.models.pelias_layer import PeliasLayer

class PeliasGeoJSONProperties(BaseModel):
    """
    PeliasGeoJSONProperties
    """
    gid: Optional[StrictStr] = Field(None, description="A scoped GID for this result. This can be passed to the place endpoint. Note that these are not always stable. For OSM, Geonames, and Who's on First, these are usually stable, but for other sources like OSM, no stability is guaranteed.")
    source_id: Optional[StrictStr] = Field(None, description="An ID referencing the original data source (specified via source) for the result. These IDs are specific to the source that they originated from. For example, in the case of OSM, these typically look like way/123 or point/123.")
    label: Optional[StrictStr] = Field(None, description="A full, human-readable label. However, you may not necessarily want to use this; be sure to read the docs for name, locality, and region before making a decision. This field is mostly localized. The order of components is generally locally correct (ex: for an address in South Korea, the house number appears after the street name). However, components will use a request language equivalent if one exists (ex: Seoul instead of 서울 if lang=en).")
    layer: Optional[PeliasLayer] = None
    name: Optional[StrictStr] = Field(None, description="The name of the place, the street address including house number, or label of similar relevance. If your app is localized to a specific region, you may get better display results by combining name, locality OR region (or neither?), and postal code together in the local format. Experiment with what works best for your use case.")
    accuracy: Optional[StrictStr] = Field(None, description="The accuracy of the geographic coordinates in the result. This value is a property of the result itself and won't change based on the query. A point result means that the record can reasonably be represented by a single geographic point. Addresses, venues, or interpolated addresses usually have point accuracy. Larger areas, such as a city or country, cannot be represented by a single point, so a centroid is given instead.")
    addendum: Optional[PeliasGeoJSONPropertiesAddendum] = None
    continent: Optional[StrictStr] = None
    continent_gid: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    country_gid: Optional[StrictStr] = None
    neighbourhood: Optional[StrictStr] = None
    neighbourhood_gid: Optional[StrictStr] = None
    borough: Optional[StrictStr] = None
    borough_gid: Optional[StrictStr] = None
    postalcode: Optional[StrictStr] = None
    street: Optional[StrictStr] = None
    housenumber: Optional[StrictStr] = None
    locality: Optional[StrictStr] = Field(None, description="The city, village, town, etc. that the place / address is part of. Note that values may not always match postal or local conventions perfectly.")
    locality_gid: Optional[StrictStr] = None
    county: Optional[StrictStr] = Field(None, description="Administrative divisions between localities and regions. Useful for disambiguating nearby results with similar names.")
    region: Optional[StrictStr] = Field(None, description="Typically the first administrative division within a country. For example, a US state or a Canadian province.")
    region_a: Optional[StrictStr] = Field(None, description="The abbreviation for the region.")
    additional_properties: Dict[str, Any] = {}
    __properties = ["gid", "source_id", "label", "layer", "name", "accuracy", "addendum", "continent", "continent_gid", "country", "country_gid", "neighbourhood", "neighbourhood_gid", "borough", "borough_gid", "postalcode", "street", "housenumber", "locality", "locality_gid", "county", "region", "region_a"]

    @validator('accuracy')
    def accuracy_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('point', 'centroid'):
            raise ValueError("must be one of enum values ('point', 'centroid')")
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
    def from_json(cls, json_str: str) -> PeliasGeoJSONProperties:
        """Create an instance of PeliasGeoJSONProperties from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of addendum
        if self.addendum:
            _dict['addendum'] = self.addendum.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PeliasGeoJSONProperties:
        """Create an instance of PeliasGeoJSONProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PeliasGeoJSONProperties.parse_obj(obj)

        _obj = PeliasGeoJSONProperties.parse_obj({
            "gid": obj.get("gid"),
            "source_id": obj.get("source_id"),
            "label": obj.get("label"),
            "layer": obj.get("layer"),
            "name": obj.get("name"),
            "accuracy": obj.get("accuracy"),
            "addendum": PeliasGeoJSONPropertiesAddendum.from_dict(obj.get("addendum")) if obj.get("addendum") is not None else None,
            "continent": obj.get("continent"),
            "continent_gid": obj.get("continent_gid"),
            "country": obj.get("country"),
            "country_gid": obj.get("country_gid"),
            "neighbourhood": obj.get("neighbourhood"),
            "neighbourhood_gid": obj.get("neighbourhood_gid"),
            "borough": obj.get("borough"),
            "borough_gid": obj.get("borough_gid"),
            "postalcode": obj.get("postalcode"),
            "street": obj.get("street"),
            "housenumber": obj.get("housenumber"),
            "locality": obj.get("locality"),
            "locality_gid": obj.get("locality_gid"),
            "county": obj.get("county"),
            "region": obj.get("region"),
            "region_a": obj.get("region_a")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

