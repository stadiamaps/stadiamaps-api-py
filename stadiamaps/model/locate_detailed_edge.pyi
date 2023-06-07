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


class LocateDetailedEdge(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            sidewalk_left = schemas.BoolSchema
            sidewalk_right = schemas.BoolSchema
            lane_count = schemas.IntSchema
            stop_sign = schemas.BoolSchema
            
            
            class sac_scale(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("none")
                
                @schemas.classproperty
                def HIKING(cls):
                    return cls("hiking")
                
                @schemas.classproperty
                def MOUNTAIN_HIKING(cls):
                    return cls("mountain hiking")
                
                @schemas.classproperty
                def DEMANDING_MOUNTAIN_HIKING(cls):
                    return cls("demanding mountain hiking")
                
                @schemas.classproperty
                def ALPINE_HIKING(cls):
                    return cls("alpine hiking")
                
                @schemas.classproperty
                def DEMANDING_ALPINE_HIKING(cls):
                    return cls("demanding alpine hiking")
                
                @schemas.classproperty
                def DIFFICULT_ALPINE_HIKING(cls):
                    return cls("difficult alpine hiking")
            yield_sign = schemas.BoolSchema
            not_thru = schemas.BoolSchema
            forward = schemas.BoolSchema
        
            @staticmethod
            def end_node() -> typing.Type['NodeId']:
                return NodeId
            truck_route = schemas.BoolSchema
        
            @staticmethod
            def speeds() -> typing.Type['Speeds']:
                return Speeds
            bike_network = schemas.BoolSchema
            round_about = schemas.BoolSchema
            traffic_signal = schemas.BoolSchema
            access_restriction = schemas.BoolSchema
            destination_only = schemas.BoolSchema
        
            @staticmethod
            def geo_attributes() -> typing.Type['GeoAttributes']:
                return GeoAttributes
        
            @staticmethod
            def start_restriction() -> typing.Type['Restrictions']:
                return Restrictions
            
            
            class cycle_lane(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def NONE(cls):
                    return cls("none")
                
                @schemas.classproperty
                def SHARED(cls):
                    return cls("shared")
                
                @schemas.classproperty
                def DEDICATED(cls):
                    return cls("dedicated")
                
                @schemas.classproperty
                def SEPARATED(cls):
                    return cls("separated")
        
            @staticmethod
            def end_restriction() -> typing.Type['Restrictions']:
                return Restrictions
            seasonal = schemas.BoolSchema
            country_crossing = schemas.BoolSchema
            part_of_complex_restriction = schemas.BoolSchema
            has_sign = schemas.BoolSchema
        
            @staticmethod
            def access() -> typing.Type['Restrictions']:
                return Restrictions
            bridge = schemas.BoolSchema
        
            @staticmethod
            def classification() -> typing.Type['HighwayClassification']:
                return HighwayClassification
            toll = schemas.BoolSchema
            tunnel = schemas.BoolSchema
            __annotations__ = {
                "sidewalk_left": sidewalk_left,
                "sidewalk_right": sidewalk_right,
                "lane_count": lane_count,
                "stop_sign": stop_sign,
                "sac_scale": sac_scale,
                "yield_sign": yield_sign,
                "not_thru": not_thru,
                "forward": forward,
                "end_node": end_node,
                "truck_route": truck_route,
                "speeds": speeds,
                "bike_network": bike_network,
                "round_about": round_about,
                "traffic_signal": traffic_signal,
                "access_restriction": access_restriction,
                "destination_only": destination_only,
                "geo_attributes": geo_attributes,
                "start_restriction": start_restriction,
                "cycle_lane": cycle_lane,
                "end_restriction": end_restriction,
                "seasonal": seasonal,
                "country_crossing": country_crossing,
                "part_of_complex_restriction": part_of_complex_restriction,
                "has_sign": has_sign,
                "access": access,
                "bridge": bridge,
                "classification": classification,
                "toll": toll,
                "tunnel": tunnel,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sidewalk_left"]) -> MetaOapg.properties.sidewalk_left: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sidewalk_right"]) -> MetaOapg.properties.sidewalk_right: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lane_count"]) -> MetaOapg.properties.lane_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stop_sign"]) -> MetaOapg.properties.stop_sign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sac_scale"]) -> MetaOapg.properties.sac_scale: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["yield_sign"]) -> MetaOapg.properties.yield_sign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["not_thru"]) -> MetaOapg.properties.not_thru: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["forward"]) -> MetaOapg.properties.forward: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_node"]) -> 'NodeId': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["truck_route"]) -> MetaOapg.properties.truck_route: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["speeds"]) -> 'Speeds': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bike_network"]) -> MetaOapg.properties.bike_network: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["round_about"]) -> MetaOapg.properties.round_about: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["traffic_signal"]) -> MetaOapg.properties.traffic_signal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access_restriction"]) -> MetaOapg.properties.access_restriction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["destination_only"]) -> MetaOapg.properties.destination_only: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["geo_attributes"]) -> 'GeoAttributes': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_restriction"]) -> 'Restrictions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["cycle_lane"]) -> MetaOapg.properties.cycle_lane: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["end_restriction"]) -> 'Restrictions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seasonal"]) -> MetaOapg.properties.seasonal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country_crossing"]) -> MetaOapg.properties.country_crossing: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["part_of_complex_restriction"]) -> MetaOapg.properties.part_of_complex_restriction: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_sign"]) -> MetaOapg.properties.has_sign: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["access"]) -> 'Restrictions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bridge"]) -> MetaOapg.properties.bridge: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["classification"]) -> 'HighwayClassification': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toll"]) -> MetaOapg.properties.toll: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tunnel"]) -> MetaOapg.properties.tunnel: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["sidewalk_left", "sidewalk_right", "lane_count", "stop_sign", "sac_scale", "yield_sign", "not_thru", "forward", "end_node", "truck_route", "speeds", "bike_network", "round_about", "traffic_signal", "access_restriction", "destination_only", "geo_attributes", "start_restriction", "cycle_lane", "end_restriction", "seasonal", "country_crossing", "part_of_complex_restriction", "has_sign", "access", "bridge", "classification", "toll", "tunnel", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sidewalk_left"]) -> typing.Union[MetaOapg.properties.sidewalk_left, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sidewalk_right"]) -> typing.Union[MetaOapg.properties.sidewalk_right, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lane_count"]) -> typing.Union[MetaOapg.properties.lane_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stop_sign"]) -> typing.Union[MetaOapg.properties.stop_sign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sac_scale"]) -> typing.Union[MetaOapg.properties.sac_scale, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["yield_sign"]) -> typing.Union[MetaOapg.properties.yield_sign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["not_thru"]) -> typing.Union[MetaOapg.properties.not_thru, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["forward"]) -> typing.Union[MetaOapg.properties.forward, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_node"]) -> typing.Union['NodeId', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["truck_route"]) -> typing.Union[MetaOapg.properties.truck_route, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["speeds"]) -> typing.Union['Speeds', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bike_network"]) -> typing.Union[MetaOapg.properties.bike_network, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["round_about"]) -> typing.Union[MetaOapg.properties.round_about, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["traffic_signal"]) -> typing.Union[MetaOapg.properties.traffic_signal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access_restriction"]) -> typing.Union[MetaOapg.properties.access_restriction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["destination_only"]) -> typing.Union[MetaOapg.properties.destination_only, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["geo_attributes"]) -> typing.Union['GeoAttributes', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_restriction"]) -> typing.Union['Restrictions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["cycle_lane"]) -> typing.Union[MetaOapg.properties.cycle_lane, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["end_restriction"]) -> typing.Union['Restrictions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seasonal"]) -> typing.Union[MetaOapg.properties.seasonal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country_crossing"]) -> typing.Union[MetaOapg.properties.country_crossing, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["part_of_complex_restriction"]) -> typing.Union[MetaOapg.properties.part_of_complex_restriction, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_sign"]) -> typing.Union[MetaOapg.properties.has_sign, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["access"]) -> typing.Union['Restrictions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bridge"]) -> typing.Union[MetaOapg.properties.bridge, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["classification"]) -> typing.Union['HighwayClassification', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toll"]) -> typing.Union[MetaOapg.properties.toll, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tunnel"]) -> typing.Union[MetaOapg.properties.tunnel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["sidewalk_left", "sidewalk_right", "lane_count", "stop_sign", "sac_scale", "yield_sign", "not_thru", "forward", "end_node", "truck_route", "speeds", "bike_network", "round_about", "traffic_signal", "access_restriction", "destination_only", "geo_attributes", "start_restriction", "cycle_lane", "end_restriction", "seasonal", "country_crossing", "part_of_complex_restriction", "has_sign", "access", "bridge", "classification", "toll", "tunnel", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        sidewalk_left: typing.Union[MetaOapg.properties.sidewalk_left, bool, schemas.Unset] = schemas.unset,
        sidewalk_right: typing.Union[MetaOapg.properties.sidewalk_right, bool, schemas.Unset] = schemas.unset,
        lane_count: typing.Union[MetaOapg.properties.lane_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        stop_sign: typing.Union[MetaOapg.properties.stop_sign, bool, schemas.Unset] = schemas.unset,
        sac_scale: typing.Union[MetaOapg.properties.sac_scale, str, schemas.Unset] = schemas.unset,
        yield_sign: typing.Union[MetaOapg.properties.yield_sign, bool, schemas.Unset] = schemas.unset,
        not_thru: typing.Union[MetaOapg.properties.not_thru, bool, schemas.Unset] = schemas.unset,
        forward: typing.Union[MetaOapg.properties.forward, bool, schemas.Unset] = schemas.unset,
        end_node: typing.Union['NodeId', schemas.Unset] = schemas.unset,
        truck_route: typing.Union[MetaOapg.properties.truck_route, bool, schemas.Unset] = schemas.unset,
        speeds: typing.Union['Speeds', schemas.Unset] = schemas.unset,
        bike_network: typing.Union[MetaOapg.properties.bike_network, bool, schemas.Unset] = schemas.unset,
        round_about: typing.Union[MetaOapg.properties.round_about, bool, schemas.Unset] = schemas.unset,
        traffic_signal: typing.Union[MetaOapg.properties.traffic_signal, bool, schemas.Unset] = schemas.unset,
        access_restriction: typing.Union[MetaOapg.properties.access_restriction, bool, schemas.Unset] = schemas.unset,
        destination_only: typing.Union[MetaOapg.properties.destination_only, bool, schemas.Unset] = schemas.unset,
        geo_attributes: typing.Union['GeoAttributes', schemas.Unset] = schemas.unset,
        start_restriction: typing.Union['Restrictions', schemas.Unset] = schemas.unset,
        cycle_lane: typing.Union[MetaOapg.properties.cycle_lane, str, schemas.Unset] = schemas.unset,
        end_restriction: typing.Union['Restrictions', schemas.Unset] = schemas.unset,
        seasonal: typing.Union[MetaOapg.properties.seasonal, bool, schemas.Unset] = schemas.unset,
        country_crossing: typing.Union[MetaOapg.properties.country_crossing, bool, schemas.Unset] = schemas.unset,
        part_of_complex_restriction: typing.Union[MetaOapg.properties.part_of_complex_restriction, bool, schemas.Unset] = schemas.unset,
        has_sign: typing.Union[MetaOapg.properties.has_sign, bool, schemas.Unset] = schemas.unset,
        access: typing.Union['Restrictions', schemas.Unset] = schemas.unset,
        bridge: typing.Union[MetaOapg.properties.bridge, bool, schemas.Unset] = schemas.unset,
        classification: typing.Union['HighwayClassification', schemas.Unset] = schemas.unset,
        toll: typing.Union[MetaOapg.properties.toll, bool, schemas.Unset] = schemas.unset,
        tunnel: typing.Union[MetaOapg.properties.tunnel, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LocateDetailedEdge':
        return super().__new__(
            cls,
            *_args,
            sidewalk_left=sidewalk_left,
            sidewalk_right=sidewalk_right,
            lane_count=lane_count,
            stop_sign=stop_sign,
            sac_scale=sac_scale,
            yield_sign=yield_sign,
            not_thru=not_thru,
            forward=forward,
            end_node=end_node,
            truck_route=truck_route,
            speeds=speeds,
            bike_network=bike_network,
            round_about=round_about,
            traffic_signal=traffic_signal,
            access_restriction=access_restriction,
            destination_only=destination_only,
            geo_attributes=geo_attributes,
            start_restriction=start_restriction,
            cycle_lane=cycle_lane,
            end_restriction=end_restriction,
            seasonal=seasonal,
            country_crossing=country_crossing,
            part_of_complex_restriction=part_of_complex_restriction,
            has_sign=has_sign,
            access=access,
            bridge=bridge,
            classification=classification,
            toll=toll,
            tunnel=tunnel,
            _configuration=_configuration,
            **kwargs,
        )

from stadiamaps.model.geo_attributes import GeoAttributes
from stadiamaps.model.highway_classification import HighwayClassification
from stadiamaps.model.node_id import NodeId
from stadiamaps.model.restrictions import Restrictions
from stadiamaps.model.speeds import Speeds
