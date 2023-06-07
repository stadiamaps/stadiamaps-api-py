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


class LocateEdge(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def edge_id() -> typing.Type['NodeId']:
                return NodeId
            correlated_lat = schemas.Float64Schema
            correlated_lon = schemas.Float64Schema
            percent_along = schemas.Float64Schema
            
            
            class side_of_street(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def LEFT(cls):
                    return cls("left")
                
                @schemas.classproperty
                def RIGHT(cls):
                    return cls("right")
                
                @schemas.classproperty
                def NEITHER(cls):
                    return cls("neither")
            linear_reference = schemas.StrSchema
            outbound_reach = schemas.IntSchema
            heading = schemas.Float32Schema
            inbound_reach = schemas.IntSchema
            distance = schemas.Float32Schema
            
            
            class predicted_speeds(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.IntSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, decimal.Decimal, int, ]], typing.List[typing.Union[MetaOapg.items, decimal.Decimal, int, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'predicted_speeds':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def edge_info() -> typing.Type['LocateEdgeInfo']:
                return LocateEdgeInfo
        
            @staticmethod
            def edge() -> typing.Type['LocateDetailedEdge']:
                return LocateDetailedEdge
            
            
            class warnings(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'warnings':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            __annotations__ = {
                "edge_id": edge_id,
                "correlated_lat": correlated_lat,
                "correlated_lon": correlated_lon,
                "percent_along": percent_along,
                "side_of_street": side_of_street,
                "linear_reference": linear_reference,
                "outbound_reach": outbound_reach,
                "heading": heading,
                "inbound_reach": inbound_reach,
                "distance": distance,
                "predicted_speeds": predicted_speeds,
                "edge_info": edge_info,
                "edge": edge,
                "warnings": warnings,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edge_id"]) -> 'NodeId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["correlated_lat"]) -> MetaOapg.properties.correlated_lat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["correlated_lon"]) -> MetaOapg.properties.correlated_lon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["percent_along"]) -> MetaOapg.properties.percent_along: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["side_of_street"]) -> MetaOapg.properties.side_of_street: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["linear_reference"]) -> MetaOapg.properties.linear_reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["outbound_reach"]) -> MetaOapg.properties.outbound_reach: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["heading"]) -> MetaOapg.properties.heading: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inbound_reach"]) -> MetaOapg.properties.inbound_reach: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["distance"]) -> MetaOapg.properties.distance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["predicted_speeds"]) -> MetaOapg.properties.predicted_speeds: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edge_info"]) -> 'LocateEdgeInfo': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["edge"]) -> 'LocateDetailedEdge': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["warnings"]) -> MetaOapg.properties.warnings: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["edge_id", "correlated_lat", "correlated_lon", "percent_along", "side_of_street", "linear_reference", "outbound_reach", "heading", "inbound_reach", "distance", "predicted_speeds", "edge_info", "edge", "warnings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edge_id"]) -> typing.Union['NodeId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["correlated_lat"]) -> typing.Union[MetaOapg.properties.correlated_lat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["correlated_lon"]) -> typing.Union[MetaOapg.properties.correlated_lon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["percent_along"]) -> typing.Union[MetaOapg.properties.percent_along, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["side_of_street"]) -> typing.Union[MetaOapg.properties.side_of_street, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["linear_reference"]) -> typing.Union[MetaOapg.properties.linear_reference, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["outbound_reach"]) -> typing.Union[MetaOapg.properties.outbound_reach, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["heading"]) -> typing.Union[MetaOapg.properties.heading, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inbound_reach"]) -> typing.Union[MetaOapg.properties.inbound_reach, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["distance"]) -> typing.Union[MetaOapg.properties.distance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["predicted_speeds"]) -> typing.Union[MetaOapg.properties.predicted_speeds, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edge_info"]) -> typing.Union['LocateEdgeInfo', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["edge"]) -> typing.Union['LocateDetailedEdge', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["warnings"]) -> typing.Union[MetaOapg.properties.warnings, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["edge_id", "correlated_lat", "correlated_lon", "percent_along", "side_of_street", "linear_reference", "outbound_reach", "heading", "inbound_reach", "distance", "predicted_speeds", "edge_info", "edge", "warnings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        edge_id: typing.Union['NodeId', schemas.Unset] = schemas.unset,
        correlated_lat: typing.Union[MetaOapg.properties.correlated_lat, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        correlated_lon: typing.Union[MetaOapg.properties.correlated_lon, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        percent_along: typing.Union[MetaOapg.properties.percent_along, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        side_of_street: typing.Union[MetaOapg.properties.side_of_street, str, schemas.Unset] = schemas.unset,
        linear_reference: typing.Union[MetaOapg.properties.linear_reference, str, schemas.Unset] = schemas.unset,
        outbound_reach: typing.Union[MetaOapg.properties.outbound_reach, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        heading: typing.Union[MetaOapg.properties.heading, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        inbound_reach: typing.Union[MetaOapg.properties.inbound_reach, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        distance: typing.Union[MetaOapg.properties.distance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        predicted_speeds: typing.Union[MetaOapg.properties.predicted_speeds, list, tuple, schemas.Unset] = schemas.unset,
        edge_info: typing.Union['LocateEdgeInfo', schemas.Unset] = schemas.unset,
        edge: typing.Union['LocateDetailedEdge', schemas.Unset] = schemas.unset,
        warnings: typing.Union[MetaOapg.properties.warnings, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LocateEdge':
        return super().__new__(
            cls,
            *_args,
            edge_id=edge_id,
            correlated_lat=correlated_lat,
            correlated_lon=correlated_lon,
            percent_along=percent_along,
            side_of_street=side_of_street,
            linear_reference=linear_reference,
            outbound_reach=outbound_reach,
            heading=heading,
            inbound_reach=inbound_reach,
            distance=distance,
            predicted_speeds=predicted_speeds,
            edge_info=edge_info,
            edge=edge,
            warnings=warnings,
            _configuration=_configuration,
            **kwargs,
        )

from stadiamaps.model.locate_detailed_edge import LocateDetailedEdge
from stadiamaps.model.locate_edge_info import LocateEdgeInfo
from stadiamaps.model.node_id import NodeId
