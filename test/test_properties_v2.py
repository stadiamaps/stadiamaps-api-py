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

from stadiamaps.models.properties_v2 import PropertiesV2

class TestPropertiesV2(unittest.TestCase):
    """PropertiesV2 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PropertiesV2:
        """Test PropertiesV2
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PropertiesV2`
        """
        model = PropertiesV2()
        if include_optional:
            return PropertiesV2(
                addendum = None,
                address_components = stadiamaps.models.address_components_v2.AddressComponentsV2(
                    cross_street = '', 
                    number = '', 
                    postal_code = '', 
                    street = '', 
                    unit = '', ),
                coarse_location = '',
                confidence = 1.337,
                context = stadiamaps.models.context.Context(
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
                        region = , ), ),
                distance = 1.337,
                formatted_address_line = '',
                formatted_address_lines = [
                    ''
                    ],
                gid = '',
                layer = '',
                name = '',
                precision = 'point',
                sources = [
                    stadiamaps.models.source_attribution.SourceAttribution(
                        fixit_url = '', 
                        source = '', 
                        source_id = '', )
                    ]
            )
        else:
            return PropertiesV2(
                gid = '',
                layer = '',
                name = '',
                precision = 'point',
        )
        """

    def testPropertiesV2(self):
        """Test PropertiesV2"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
