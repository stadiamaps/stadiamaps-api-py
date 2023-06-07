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


class MatrixResponse(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "sources_to_targets",
            "sources",
            "units",
            "targets",
        }
        
        class properties:
            
            
            class sources(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    min_items = 1
                    
                    
                    class items(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Coordinate']:
                                return Coordinate
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['Coordinate'], typing.List['Coordinate']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Coordinate':
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, list, tuple, ]], typing.List[typing.Union[MetaOapg.items, list, tuple, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sources':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class targets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    min_items = 1
                    
                    
                    class items(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['Coordinate']:
                                return Coordinate
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['Coordinate'], typing.List['Coordinate']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'Coordinate':
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, list, tuple, ]], typing.List[typing.Union[MetaOapg.items, list, tuple, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'targets':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            
            
            class sources_to_targets(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    min_items = 1
                    
                    
                    class items(
                        schemas.ListSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            @staticmethod
                            def items() -> typing.Type['MatrixDistance']:
                                return MatrixDistance
                    
                        def __new__(
                            cls,
                            _arg: typing.Union[typing.Tuple['MatrixDistance'], typing.List['MatrixDistance']],
                            _configuration: typing.Optional[schemas.Configuration] = None,
                        ) -> 'items':
                            return super().__new__(
                                cls,
                                _arg,
                                _configuration=_configuration,
                            )
                    
                        def __getitem__(self, i: int) -> 'MatrixDistance':
                            return super().__getitem__(i)
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, list, tuple, ]], typing.List[typing.Union[MetaOapg.items, list, tuple, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sources_to_targets':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def units() -> typing.Type['ValhallaLongUnits']:
                return ValhallaLongUnits
            id = schemas.StrSchema
            
            
            class warnings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Warning']:
                        return Warning
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Warning'], typing.List['Warning']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'warnings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Warning':
                    return super().__getitem__(i)
            __annotations__ = {
                "sources": sources,
                "targets": targets,
                "sources_to_targets": sources_to_targets,
                "units": units,
                "id": id,
                "warnings": warnings,
            }
    
    sources_to_targets: MetaOapg.properties.sources_to_targets
    sources: MetaOapg.properties.sources
    units: 'ValhallaLongUnits'
    targets: MetaOapg.properties.targets
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sources"]) -> MetaOapg.properties.sources: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["targets"]) -> MetaOapg.properties.targets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sources_to_targets"]) -> MetaOapg.properties.sources_to_targets: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["units"]) -> 'ValhallaLongUnits': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["warnings"]) -> MetaOapg.properties.warnings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sources", "targets", "sources_to_targets", "units", "id", "warnings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sources"]) -> MetaOapg.properties.sources: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["targets"]) -> MetaOapg.properties.targets: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sources_to_targets"]) -> MetaOapg.properties.sources_to_targets: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["units"]) -> 'ValhallaLongUnits': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["warnings"]) -> typing.Union[MetaOapg.properties.warnings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sources", "targets", "sources_to_targets", "units", "id", "warnings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        sources_to_targets: typing.Union[MetaOapg.properties.sources_to_targets, list, tuple, ],
        sources: typing.Union[MetaOapg.properties.sources, list, tuple, ],
        units: 'ValhallaLongUnits',
        targets: typing.Union[MetaOapg.properties.targets, list, tuple, ],
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        warnings: typing.Union[MetaOapg.properties.warnings, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MatrixResponse':
        return super().__new__(
            cls,
            *_args,
            sources_to_targets=sources_to_targets,
            sources=sources,
            units=units,
            targets=targets,
            id=id,
            warnings=warnings,
            _configuration=_configuration,
            **kwargs,
        )

from stadiamaps.model.coordinate import Coordinate
from stadiamaps.model.matrix_distance import MatrixDistance
from stadiamaps.model.valhalla_long_units import ValhallaLongUnits
from stadiamaps.model.warning import Warning
