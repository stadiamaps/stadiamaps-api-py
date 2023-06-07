import typing_extensions

from stadiamaps.paths import PathValues
from stadiamaps.apis.paths.tz_lookup_v1 import TzLookupV1
from stadiamaps.apis.paths.elevation_v1 import ElevationV1
from stadiamaps.apis.paths.route_v1 import RouteV1
from stadiamaps.apis.paths.nearest_roads_v1 import NearestRoadsV1
from stadiamaps.apis.paths.matrix_v1 import MatrixV1
from stadiamaps.apis.paths.isochrone_v1 import IsochroneV1
from stadiamaps.apis.paths.optimized_route_v1 import OptimizedRouteV1
from stadiamaps.apis.paths.map_match_v1 import MapMatchV1
from stadiamaps.apis.paths.trace_attributes_v1 import TraceAttributesV1
from stadiamaps.apis.paths.geocoding_v1_autocomplete import GeocodingV1Autocomplete
from stadiamaps.apis.paths.geocoding_v1_search import GeocodingV1Search
from stadiamaps.apis.paths.geocoding_v1_search_structured import GeocodingV1SearchStructured
from stadiamaps.apis.paths.geocoding_v1_reverse import GeocodingV1Reverse
from stadiamaps.apis.paths.geocoding_v1_place import GeocodingV1Place

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.TZ_LOOKUP_V1: TzLookupV1,
        PathValues.ELEVATION_V1: ElevationV1,
        PathValues.ROUTE_V1: RouteV1,
        PathValues.NEAREST_ROADS_V1: NearestRoadsV1,
        PathValues.MATRIX_V1: MatrixV1,
        PathValues.ISOCHRONE_V1: IsochroneV1,
        PathValues.OPTIMIZED_ROUTE_V1: OptimizedRouteV1,
        PathValues.MAP_MATCH_V1: MapMatchV1,
        PathValues.TRACE_ATTRIBUTES_V1: TraceAttributesV1,
        PathValues.GEOCODING_V1_AUTOCOMPLETE: GeocodingV1Autocomplete,
        PathValues.GEOCODING_V1_SEARCH: GeocodingV1Search,
        PathValues.GEOCODING_V1_SEARCH_STRUCTURED: GeocodingV1SearchStructured,
        PathValues.GEOCODING_V1_REVERSE: GeocodingV1Reverse,
        PathValues.GEOCODING_V1_PLACE: GeocodingV1Place,
    }
)

path_to_api = PathToApi(
    {
        PathValues.TZ_LOOKUP_V1: TzLookupV1,
        PathValues.ELEVATION_V1: ElevationV1,
        PathValues.ROUTE_V1: RouteV1,
        PathValues.NEAREST_ROADS_V1: NearestRoadsV1,
        PathValues.MATRIX_V1: MatrixV1,
        PathValues.ISOCHRONE_V1: IsochroneV1,
        PathValues.OPTIMIZED_ROUTE_V1: OptimizedRouteV1,
        PathValues.MAP_MATCH_V1: MapMatchV1,
        PathValues.TRACE_ATTRIBUTES_V1: TraceAttributesV1,
        PathValues.GEOCODING_V1_AUTOCOMPLETE: GeocodingV1Autocomplete,
        PathValues.GEOCODING_V1_SEARCH: GeocodingV1Search,
        PathValues.GEOCODING_V1_SEARCH_STRUCTURED: GeocodingV1SearchStructured,
        PathValues.GEOCODING_V1_REVERSE: GeocodingV1Reverse,
        PathValues.GEOCODING_V1_PLACE: GeocodingV1Place,
    }
)
