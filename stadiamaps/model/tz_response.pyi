# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications. All endpoints are versioned individually to allow for granular upgrades. We follow the [Semantic Versioning scheme](https://semver.org/).  # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Contact: support@stadiamaps.com
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from stadiamaps import schemas  # noqa: F401


class TzResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "dst_offset",
            "base_utc_offset",
            "tz_id",
        }
        
        class properties:
            tz_id = schemas.StrSchema
            base_utc_offset = schemas.IntSchema
            dst_offset = schemas.IntSchema
            __annotations__ = {
                "tz_id": tz_id,
                "base_utc_offset": base_utc_offset,
                "dst_offset": dst_offset,
            }
    
    dst_offset: MetaOapg.properties.dst_offset
    base_utc_offset: MetaOapg.properties.base_utc_offset
    tz_id: MetaOapg.properties.tz_id
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tz_id"]) -> MetaOapg.properties.tz_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["base_utc_offset"]) -> MetaOapg.properties.base_utc_offset: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dst_offset"]) -> MetaOapg.properties.dst_offset: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["tz_id", "base_utc_offset", "dst_offset", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tz_id"]) -> MetaOapg.properties.tz_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["base_utc_offset"]) -> MetaOapg.properties.base_utc_offset: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dst_offset"]) -> MetaOapg.properties.dst_offset: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["tz_id", "base_utc_offset", "dst_offset", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        dst_offset: typing.Union[MetaOapg.properties.dst_offset, decimal.Decimal, int, ],
        base_utc_offset: typing.Union[MetaOapg.properties.base_utc_offset, decimal.Decimal, int, ],
        tz_id: typing.Union[MetaOapg.properties.tz_id, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TzResponse':
        return super().__new__(
            cls,
            *_args,
            dst_offset=dst_offset,
            base_utc_offset=base_utc_offset,
            tz_id=tz_id,
            _configuration=_configuration,
            **kwargs,
        )
