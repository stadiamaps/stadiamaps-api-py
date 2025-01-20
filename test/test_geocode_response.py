# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 8.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stadiamaps.models.geocode_response import GeocodeResponse

class TestGeocodeResponse(unittest.TestCase):
    """GeocodeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeocodeResponse:
        """Test GeocodeResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeocodeResponse`
        """
        model = GeocodeResponse()
        if include_optional:
            return GeocodeResponse(
                geocoding = stadiamaps.models.geocoding_object.geocodingObject(
                    attribution = '', 
                    query = { }, 
                    warnings = [
                        ''
                        ], 
                    errors = [
                        ''
                        ], ),
                bbox = [
                    1.337
                    ],
                features = [
                    stadiamaps.models.geocoding_geo_json_feature.geocodingGeoJSONFeature(
                        type = 'Feature', 
                        geometry = null, 
                        properties = { }, 
                        bbox = [
                            1.337
                            ], )
                    ]
            )
        else:
            return GeocodeResponse(
                geocoding = stadiamaps.models.geocoding_object.geocodingObject(
                    attribution = '', 
                    query = { }, 
                    warnings = [
                        ''
                        ], 
                    errors = [
                        ''
                        ], ),
                features = [
                    stadiamaps.models.geocoding_geo_json_feature.geocodingGeoJSONFeature(
                        type = 'Feature', 
                        geometry = null, 
                        properties = { }, 
                        bbox = [
                            1.337
                            ], )
                    ],
        )
        """

    def testGeocodeResponse(self):
        """Test GeocodeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
