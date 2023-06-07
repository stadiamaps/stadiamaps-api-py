# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from stadiamaps.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    TZ_LOOKUP_V1 = "/tz/lookup/v1"
    ELEVATION_V1 = "/elevation/v1"
    ROUTE_V1 = "/route/v1"
    NEAREST_ROADS_V1 = "/nearest_roads/v1"
    MATRIX_V1 = "/matrix/v1"
    ISOCHRONE_V1 = "/isochrone/v1"
    OPTIMIZED_ROUTE_V1 = "/optimized_route/v1"
    MAP_MATCH_V1 = "/map_match/v1"
    TRACE_ATTRIBUTES_V1 = "/trace_attributes/v1"
    GEOCODING_V1_AUTOCOMPLETE = "/geocoding/v1/autocomplete"
    GEOCODING_V1_SEARCH = "/geocoding/v1/search"
    GEOCODING_V1_SEARCH_STRUCTURED = "/geocoding/v1/search/structured"
    GEOCODING_V1_REVERSE = "/geocoding/v1/reverse"
    GEOCODING_V1_PLACE = "/geocoding/v1/place"
