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


class RoutingWaypoint(
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
                    
                    
                    class heading(
                        schemas.IntSchema
                    ):
                        pass
                    
                    
                    class heading_tolerance(
                        schemas.IntSchema
                    ):
                        pass
                    
                    
                    class minimum_reachability(
                        schemas.IntSchema
                    ):
                        pass
                    
                    
                    class radius(
                        schemas.IntSchema
                    ):
                        pass
                    rank_candidates = schemas.BoolSchema
                    
                    
                    class preferred_side(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def SAME(cls):
                            return cls("same")
                        
                        @schemas.classproperty
                        def OPPOSITE(cls):
                            return cls("opposite")
                        
                        @schemas.classproperty
                        def EITHER(cls):
                            return cls("either")
                    
                    
                    class node_snap_tolerance(
                        schemas.IntSchema
                    ):
                        pass
                    
                    
                    class street_side_tolerance(
                        schemas.IntSchema
                    ):
                        pass
                    
                    
                    class street_side_max_distance(
                        schemas.IntSchema
                    ):
                        pass
                    
                    
                    class search_filter(
                        schemas.DictSchema
                    ):
                    
                    
                        class MetaOapg:
                            
                            class properties:
                                exclude_tunnel = schemas.BoolSchema
                                exclude_bridge = schemas.BoolSchema
                                exclude_ramp = schemas.BoolSchema
                                exclude_closures = schemas.BoolSchema
                                
                                
                                class min_road_class(
                                    schemas.ComposedSchema,
                                ):
                                
                                
                                    class MetaOapg:
                                        
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
                                                RoadClass,
                                            ]
                                
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'min_road_class':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                
                                
                                class max_road_class(
                                    schemas.ComposedSchema,
                                ):
                                
                                
                                    class MetaOapg:
                                        
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
                                                RoadClass,
                                            ]
                                
                                
                                    def __new__(
                                        cls,
                                        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                                        _configuration: typing.Optional[schemas.Configuration] = None,
                                        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                                    ) -> 'max_road_class':
                                        return super().__new__(
                                            cls,
                                            *_args,
                                            _configuration=_configuration,
                                            **kwargs,
                                        )
                                __annotations__ = {
                                    "exclude_tunnel": exclude_tunnel,
                                    "exclude_bridge": exclude_bridge,
                                    "exclude_ramp": exclude_ramp,
                                    "exclude_closures": exclude_closures,
                                    "min_road_class": min_road_class,
                                    "max_road_class": max_road_class,
                                }
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["exclude_tunnel"]) -> MetaOapg.properties.exclude_tunnel: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["exclude_bridge"]) -> MetaOapg.properties.exclude_bridge: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["exclude_ramp"]) -> MetaOapg.properties.exclude_ramp: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["exclude_closures"]) -> MetaOapg.properties.exclude_closures: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["min_road_class"]) -> MetaOapg.properties.min_road_class: ...
                        
                        @typing.overload
                        def __getitem__(self, name: typing_extensions.Literal["max_road_class"]) -> MetaOapg.properties.max_road_class: ...
                        
                        @typing.overload
                        def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                        
                        def __getitem__(self, name: typing.Union[typing_extensions.Literal["exclude_tunnel", "exclude_bridge", "exclude_ramp", "exclude_closures", "min_road_class", "max_road_class", ], str]):
                            # dict_instance[name] accessor
                            return super().__getitem__(name)
                        
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["exclude_tunnel"]) -> typing.Union[MetaOapg.properties.exclude_tunnel, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["exclude_bridge"]) -> typing.Union[MetaOapg.properties.exclude_bridge, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["exclude_ramp"]) -> typing.Union[MetaOapg.properties.exclude_ramp, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["exclude_closures"]) -> typing.Union[MetaOapg.properties.exclude_closures, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["min_road_class"]) -> typing.Union[MetaOapg.properties.min_road_class, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: typing_extensions.Literal["max_road_class"]) -> typing.Union[MetaOapg.properties.max_road_class, schemas.Unset]: ...
                        
                        @typing.overload
                        def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                        
                        def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["exclude_tunnel", "exclude_bridge", "exclude_ramp", "exclude_closures", "min_road_class", "max_road_class", ], str]):
                            return super().get_item_oapg(name)
                        
                    
                        def __new__(
                            cls,
                            *_args: typing.Union[dict, frozendict.frozendict, ],
                            exclude_tunnel: typing.Union[MetaOapg.properties.exclude_tunnel, bool, schemas.Unset] = schemas.unset,
                            exclude_bridge: typing.Union[MetaOapg.properties.exclude_bridge, bool, schemas.Unset] = schemas.unset,
                            exclude_ramp: typing.Union[MetaOapg.properties.exclude_ramp, bool, schemas.Unset] = schemas.unset,
                            exclude_closures: typing.Union[MetaOapg.properties.exclude_closures, bool, schemas.Unset] = schemas.unset,
                            min_road_class: typing.Union[MetaOapg.properties.min_road_class, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                            max_road_class: typing.Union[MetaOapg.properties.max_road_class, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
                            _configuration: typing.Optional[schemas.Configuration] = None,
                            **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                        ) -> 'search_filter':
                            return super().__new__(
                                cls,
                                *_args,
                                exclude_tunnel=exclude_tunnel,
                                exclude_bridge=exclude_bridge,
                                exclude_ramp=exclude_ramp,
                                exclude_closures=exclude_closures,
                                min_road_class=min_road_class,
                                max_road_class=max_road_class,
                                _configuration=_configuration,
                                **kwargs,
                            )
                    __annotations__ = {
                        "heading": heading,
                        "heading_tolerance": heading_tolerance,
                        "minimum_reachability": minimum_reachability,
                        "radius": radius,
                        "rank_candidates": rank_candidates,
                        "preferred_side": preferred_side,
                        "node_snap_tolerance": node_snap_tolerance,
                        "street_side_tolerance": street_side_tolerance,
                        "street_side_max_distance": street_side_max_distance,
                        "search_filter": search_filter,
                    }
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["heading"]) -> MetaOapg.properties.heading: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["heading_tolerance"]) -> MetaOapg.properties.heading_tolerance: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["minimum_reachability"]) -> MetaOapg.properties.minimum_reachability: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["radius"]) -> MetaOapg.properties.radius: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["rank_candidates"]) -> MetaOapg.properties.rank_candidates: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["preferred_side"]) -> MetaOapg.properties.preferred_side: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["node_snap_tolerance"]) -> MetaOapg.properties.node_snap_tolerance: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["street_side_tolerance"]) -> MetaOapg.properties.street_side_tolerance: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["street_side_max_distance"]) -> MetaOapg.properties.street_side_max_distance: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["search_filter"]) -> MetaOapg.properties.search_filter: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["heading", "heading_tolerance", "minimum_reachability", "radius", "rank_candidates", "preferred_side", "node_snap_tolerance", "street_side_tolerance", "street_side_max_distance", "search_filter", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["heading"]) -> typing.Union[MetaOapg.properties.heading, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["heading_tolerance"]) -> typing.Union[MetaOapg.properties.heading_tolerance, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["minimum_reachability"]) -> typing.Union[MetaOapg.properties.minimum_reachability, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["radius"]) -> typing.Union[MetaOapg.properties.radius, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["rank_candidates"]) -> typing.Union[MetaOapg.properties.rank_candidates, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["preferred_side"]) -> typing.Union[MetaOapg.properties.preferred_side, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["node_snap_tolerance"]) -> typing.Union[MetaOapg.properties.node_snap_tolerance, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["street_side_tolerance"]) -> typing.Union[MetaOapg.properties.street_side_tolerance, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["street_side_max_distance"]) -> typing.Union[MetaOapg.properties.street_side_max_distance, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["search_filter"]) -> typing.Union[MetaOapg.properties.search_filter, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["heading", "heading_tolerance", "minimum_reachability", "radius", "rank_candidates", "preferred_side", "node_snap_tolerance", "street_side_tolerance", "street_side_max_distance", "search_filter", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *_args: typing.Union[dict, frozendict.frozendict, ],
                heading: typing.Union[MetaOapg.properties.heading, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                heading_tolerance: typing.Union[MetaOapg.properties.heading_tolerance, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                minimum_reachability: typing.Union[MetaOapg.properties.minimum_reachability, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                radius: typing.Union[MetaOapg.properties.radius, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                rank_candidates: typing.Union[MetaOapg.properties.rank_candidates, bool, schemas.Unset] = schemas.unset,
                preferred_side: typing.Union[MetaOapg.properties.preferred_side, str, schemas.Unset] = schemas.unset,
                node_snap_tolerance: typing.Union[MetaOapg.properties.node_snap_tolerance, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                street_side_tolerance: typing.Union[MetaOapg.properties.street_side_tolerance, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                street_side_max_distance: typing.Union[MetaOapg.properties.street_side_max_distance, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                search_filter: typing.Union[MetaOapg.properties.search_filter, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *_args,
                    heading=heading,
                    heading_tolerance=heading_tolerance,
                    minimum_reachability=minimum_reachability,
                    radius=radius,
                    rank_candidates=rank_candidates,
                    preferred_side=preferred_side,
                    node_snap_tolerance=node_snap_tolerance,
                    street_side_tolerance=street_side_tolerance,
                    street_side_max_distance=street_side_max_distance,
                    search_filter=search_filter,
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
                SimpleRoutingWaypoint,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RoutingWaypoint':
        return super().__new__(
            cls,
            *_args,
            _configuration=_configuration,
            **kwargs,
        )

from stadiamaps.model.road_class import RoadClass
from stadiamaps.model.simple_routing_waypoint import SimpleRoutingWaypoint
