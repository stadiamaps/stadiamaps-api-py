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

from stadiamaps.models.context import Context

class TestContext(unittest.TestCase):
    """Context unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Context:
        """Test Context
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Context`
        """
        model = Context()
        if include_optional:
            return Context(
                iso_3166_a2 = '',
                iso_3166_a3 = '',
                whosonfirst = stadiamaps.models.wof_context.WofContext(
                    borough = stadiamaps.models.wof_context_component.WofContextComponent(
                        abbreviation = '', 
                        gid = '', 
                        name = '', ), 
                    continent = stadiamaps.models.wof_context_component.WofContextComponent(
                        abbreviation = '', 
                        gid = '', 
                        name = '', ), 
                    country = , 
                    county = , 
                    dependency = , 
                    localadmin = , 
                    locality = , 
                    macrocounty = , 
                    macroregion = , 
                    neighbourhood = , 
                    region = , )
            )
        else:
            return Context(
                whosonfirst = stadiamaps.models.wof_context.WofContext(
                    borough = stadiamaps.models.wof_context_component.WofContextComponent(
                        abbreviation = '', 
                        gid = '', 
                        name = '', ), 
                    continent = stadiamaps.models.wof_context_component.WofContextComponent(
                        abbreviation = '', 
                        gid = '', 
                        name = '', ), 
                    country = , 
                    county = , 
                    dependency = , 
                    localadmin = , 
                    locality = , 
                    macrocounty = , 
                    macroregion = , 
                    neighbourhood = , 
                    region = , ),
        )
        """

    def testContext(self):
        """Test Context"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
