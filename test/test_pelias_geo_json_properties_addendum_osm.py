# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications. All endpoints are versioned individually to allow for granular upgrades. We follow the [Semantic Versioning scheme](https://semver.org/).  # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import stadiamaps
from stadiamaps.models.pelias_geo_json_properties_addendum_osm import PeliasGeoJSONPropertiesAddendumOsm  # noqa: E501
from stadiamaps.rest import ApiException

class TestPeliasGeoJSONPropertiesAddendumOsm(unittest.TestCase):
    """PeliasGeoJSONPropertiesAddendumOsm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PeliasGeoJSONPropertiesAddendumOsm
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PeliasGeoJSONPropertiesAddendumOsm`
        """
        model = stadiamaps.models.pelias_geo_json_properties_addendum_osm.PeliasGeoJSONPropertiesAddendumOsm()  # noqa: E501
        if include_optional :
            return PeliasGeoJSONPropertiesAddendumOsm(
                website = '', 
                wikipedia = '', 
                wikidata = '', 
                phone = ''
            )
        else :
            return PeliasGeoJSONPropertiesAddendumOsm(
        )
        """

    def testPeliasGeoJSONPropertiesAddendumOsm(self):
        """Test PeliasGeoJSONPropertiesAddendumOsm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
