# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 9.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stadiamaps.models.addendum_v2 import AddendumV2

class TestAddendumV2(unittest.TestCase):
    """AddendumV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddendumV2:
        """Test AddendumV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddendumV2`
        """
        model = AddendumV2()
        if include_optional:
            return AddendumV2(
                foursquare = stadiamaps.models.foursquare_addendum.FoursquareAddendum(
                    tel = '', 
                    website = '', ),
                geonames = stadiamaps.models.geonames_addendum.GeonamesAddendum(
                    feature_code = '', ),
                osm = stadiamaps.models.open_street_map_addendum.OpenStreetMapAddendum(
                    brand = '', 
                    iata = '', 
                    icao = '', 
                    opening_hours = '', 
                    operator = '', 
                    phone = '', 
                    website = '', 
                    wikidata = '', 
                    wikipedia = '', ),
                whosonfirst_concordances = stadiamaps.models.whos_on_first_concordances.WhosOnFirstConcordances(
                    eurographics_gisco_id = '', 
                    faa_code = '', 
                    factual_id = '', 
                    fifa_id = '', 
                    fips_code = '', 
                    fr_gov_epci_code = 56, 
                    fra_insee_code = 56, 
                    geonames_id = 56, 
                    geoplanet_id = 56, 
                    hasc_id = '', 
                    iata_code = '', 
                    icao_code = '', 
                    itu_id = '', 
                    karmashapes_id = 56, 
                    natural_earth_id = '', 
                    nuts_2021_id = '', 
                    quattroshapes_id = 56, 
                    quattroshapes_pg_id = 56, 
                    us_census_geo_id = 56, 
                    wikidata_id = '', 
                    wikipedia_page = '', )
            )
        else:
            return AddendumV2(
        )
        """

    def testAddendumV2(self):
        """Test AddendumV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
