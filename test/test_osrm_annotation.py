# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 7.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stadiamaps.models.osrm_annotation import OsrmAnnotation

class TestOsrmAnnotation(unittest.TestCase):
    """OsrmAnnotation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OsrmAnnotation:
        """Test OsrmAnnotation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OsrmAnnotation`
        """
        model = OsrmAnnotation()
        if include_optional:
            return OsrmAnnotation(
                distance = [
                    1.337
                    ],
                duration = [
                    1.337
                    ],
                weight = [
                    56
                    ],
                speed = [
                    1.337
                    ],
                maxspeed = [
                    stadiamaps.models.osrm_speed_limit.osrmSpeedLimit(
                        speed = 56, 
                        unit = 'km/h', 
                        unknown = True, 
                        none = True, )
                    ]
            )
        else:
            return OsrmAnnotation(
                distance = [
                    1.337
                    ],
                duration = [
                    1.337
                    ],
        )
        """

    def testOsrmAnnotation(self):
        """Test OsrmAnnotation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
