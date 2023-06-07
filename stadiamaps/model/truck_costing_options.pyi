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


class TruckCostingOptions(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                
                class properties:
                    height = schemas.Float64Schema
                    width = schemas.Float64Schema
                    length = schemas.Float64Schema
                    weight = schemas.Float64Schema
                    axle_load = schemas.Float64Schema
                    hazmat = schemas.BoolSchema
                    __annotations__ = {
                        "height": height,
                        "width": width,
                        "length": length,
                        "weight": weight,
                        "axle_load": axle_load,
                        "hazmat": hazmat,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["height"]) -> MetaOapg.properties.height: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["width"]) -> MetaOapg.properties.width: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["length"]) -> MetaOapg.properties.length: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["weight"]) -> MetaOapg.properties.weight: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["axle_load"]) -> MetaOapg.properties.axle_load: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["hazmat"]) -> MetaOapg.properties.hazmat: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["height", "width", "length", "weight", "axle_load", "hazmat", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["height"]) -> typing.Union[MetaOapg.properties.height, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["width"]) -> typing.Union[MetaOapg.properties.width, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["length"]) -> typing.Union[MetaOapg.properties.length, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["weight"]) -> typing.Union[MetaOapg.properties.weight, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["axle_load"]) -> typing.Union[MetaOapg.properties.axle_load, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["hazmat"]) -> typing.Union[MetaOapg.properties.hazmat, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["height", "width", "length", "weight", "axle_load", "hazmat", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                height: typing.Union[MetaOapg.properties.height, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                width: typing.Union[MetaOapg.properties.width, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                length: typing.Union[MetaOapg.properties.length, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                weight: typing.Union[MetaOapg.properties.weight, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                axle_load: typing.Union[MetaOapg.properties.axle_load, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
                hazmat: typing.Union[MetaOapg.properties.hazmat, bool, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    height=height,
                    width=width,
                    length=length,
                    weight=weight,
                    axle_load=axle_load,
                    hazmat=hazmat,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                AutoCostingOptions,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TruckCostingOptions':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from stadiamaps.model.auto_costing_options import AutoCostingOptions
