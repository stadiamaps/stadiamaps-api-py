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

from stadiamaps.models.point import Point

class TestPoint(unittest.TestCase):
    """Point unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Point:
        """Test Point
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Point`
        """
        model = Point()
        if include_optional:
            return Point(
                coordinates = [
                    1.337
                    ],
                type = ''
            )
        else:
            return Point(
                coordinates = [
                    1.337
                    ],
                type = '',
        )
        """

    def testPoint(self):
        """Test Point"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
