import typing_extensions

from stadiamaps.apis.tags import TagValues
from stadiamaps.apis.tags.geocoding_api import GeocodingApi
from stadiamaps.apis.tags.geospatial_api import GeospatialApi
from stadiamaps.apis.tags.routing_api import RoutingApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.GEOCODING: GeocodingApi,
        TagValues.GEOSPATIAL: GeospatialApi,
        TagValues.ROUTING: RoutingApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.GEOCODING: GeocodingApi,
        TagValues.GEOSPATIAL: GeospatialApi,
        TagValues.ROUTING: RoutingApi,
    }
)
