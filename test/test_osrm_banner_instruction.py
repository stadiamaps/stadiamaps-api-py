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

from stadiamaps.models.osrm_banner_instruction import OsrmBannerInstruction

class TestOsrmBannerInstruction(unittest.TestCase):
    """OsrmBannerInstruction unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OsrmBannerInstruction:
        """Test OsrmBannerInstruction
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OsrmBannerInstruction`
        """
        model = OsrmBannerInstruction()
        if include_optional:
            return OsrmBannerInstruction(
                distance_along_geometry = 1.337,
                primary = stadiamaps.models.osrm_banner_content.osrmBannerContent(
                    text = '', 
                    type = 'turn', 
                    modifier = 'uturn', 
                    components = [
                        stadiamaps.models.osrm_banner_component.osrmBannerComponent(
                            text = '', 
                            type = 'text', )
                        ], ),
                secondary = stadiamaps.models.osrm_banner_content.osrmBannerContent(
                    text = '', 
                    type = 'turn', 
                    modifier = 'uturn', 
                    components = [
                        stadiamaps.models.osrm_banner_component.osrmBannerComponent(
                            text = '', 
                            type = 'text', )
                        ], )
            )
        else:
            return OsrmBannerInstruction(
                distance_along_geometry = 1.337,
                primary = stadiamaps.models.osrm_banner_content.osrmBannerContent(
                    text = '', 
                    type = 'turn', 
                    modifier = 'uturn', 
                    components = [
                        stadiamaps.models.osrm_banner_component.osrmBannerComponent(
                            text = '', 
                            type = 'text', )
                        ], ),
        )
        """

    def testOsrmBannerInstruction(self):
        """Test OsrmBannerInstruction"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
