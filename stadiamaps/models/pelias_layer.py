# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.1
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import json
import pprint
import re  # noqa: F401
from aenum import Enum, no_arg





class PeliasLayer(str, Enum):
    """
    Our database is organized into several layers (in the GIS sense of the term) as follows:  - `venue`: Points of interest, businesses, and things with walls - `address`: Places with a street address - `street`: Streets, roads, highways - `county`: Places that issue passports, nations, nation-states - `macroregion`: A related group of regions (mostly in Europe) - `region`: The first administrative division within a country (usually states and provinces) - `macrocounty`: A related group of counties (mostly in Europe) - `county`: Official governmental areas; usually bigger than a locality, but almost always smaller than a region - `locality`: Towns, hamlets, cities, etc. - `localadmin`: Local administrative boundaries - `borough`: Local administrative boundaries within cities (not widely used, but present in places such as NYC and Mexico City) - `neighbourhood`: Social communities and neighborhoods (note the British spelling in the API!) - `postalcode`: Postal codes used by mail services (note: not used for reverse geocoding) - `coarse`: An alias for simultaneously using all administrative layers (everything except `venue` and `address`) 
    """

    """
    allowed enum values
    """
    VENUE = 'venue'
    ADDRESS = 'address'
    STREET = 'street'
    COUNTRY = 'country'
    MACROREGION = 'macroregion'
    REGION = 'region'
    MACROCOUNTY = 'macrocounty'
    COUNTY = 'county'
    LOCALITY = 'locality'
    LOCALADMIN = 'localadmin'
    BOROUGH = 'borough'
    NEIGHBOURHOOD = 'neighbourhood'
    POSTALCODE = 'postalcode'
    COARSE = 'coarse'

    @classmethod
    def from_json(cls, json_str: str) -> PeliasLayer:
        """Create an instance of PeliasLayer from a JSON string"""
        return PeliasLayer(json.loads(json_str))


