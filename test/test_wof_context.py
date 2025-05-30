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

from stadiamaps.models.wof_context import WofContext

class TestWofContext(unittest.TestCase):
    """WofContext unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WofContext:
        """Test WofContext
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WofContext`
        """
        model = WofContext()
        if include_optional:
            return WofContext(
                borough = stadiamaps.models.wof_context_component.WofContextComponent(
                    abbreviation = '', 
                    gid = '', 
                    name = '', ),
                continent = stadiamaps.models.wof_context_component.WofContextComponent(
                    abbreviation = '', 
                    gid = '', 
                    name = '', ),
                country = stadiamaps.models.wof_context_component.WofContextComponent(
                    abbreviation = '', 
                    gid = '', 
                    name = '', ),
                county = stadiamaps.models.wof_context_component.WofContextComponent(
                    abbreviation = '', 
                    gid = '', 
                    name = '', ),
                dependency = stadiamaps.models.wof_context_component.WofContextComponent(
                    abbreviation = '', 
                    gid = '', 
                    name = '', ),
                localadmin = stadiamaps.models.wof_context_component.WofContextComponent(
                    abbreviation = '', 
                    gid = '', 
                    name = '', ),
                locality = stadiamaps.models.wof_context_component.WofContextComponent(
                    abbreviation = '', 
                    gid = '', 
                    name = '', ),
                macrocounty = stadiamaps.models.wof_context_component.WofContextComponent(
                    abbreviation = '', 
                    gid = '', 
                    name = '', ),
                macroregion = stadiamaps.models.wof_context_component.WofContextComponent(
                    abbreviation = '', 
                    gid = '', 
                    name = '', ),
                neighbourhood = stadiamaps.models.wof_context_component.WofContextComponent(
                    abbreviation = '', 
                    gid = '', 
                    name = '', ),
                region = stadiamaps.models.wof_context_component.WofContextComponent(
                    abbreviation = '', 
                    gid = '', 
                    name = '', )
            )
        else:
            return WofContext(
        )
        """

    def testWofContext(self):
        """Test WofContext"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
