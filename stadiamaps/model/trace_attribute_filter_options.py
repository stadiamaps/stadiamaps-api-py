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


class TraceAttributeFilterOptions(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "action",
            "attributes",
        }
        
        class properties:
            
            
            class attributes(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    min_items = 1
                    
                    @staticmethod
                    def items() -> typing.Type['TraceAttributeKey']:
                        return TraceAttributeKey
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TraceAttributeKey'], typing.List['TraceAttributeKey']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'attributes':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TraceAttributeKey':
                    return super().__getitem__(i)
            
            
            class action(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "include": "INCLUDE",
                        "exclude": "EXCLUDE",
                    }
                
                @schemas.classproperty
                def INCLUDE(cls):
                    return cls("include")
                
                @schemas.classproperty
                def EXCLUDE(cls):
                    return cls("exclude")
            __annotations__ = {
                "attributes": attributes,
                "action": action,
            }
    
    action: MetaOapg.properties.action
    attributes: MetaOapg.properties.attributes
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["attributes", "action", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["attributes"]) -> MetaOapg.properties.attributes: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["attributes", "action", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        action: typing.Union[MetaOapg.properties.action, str, ],
        attributes: typing.Union[MetaOapg.properties.attributes, list, tuple, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TraceAttributeFilterOptions':
        return super().__new__(
            cls,
            *_args,
            action=action,
            attributes=attributes,
            _configuration=_configuration,
            **kwargs,
        )

from stadiamaps.model.trace_attribute_key import TraceAttributeKey
