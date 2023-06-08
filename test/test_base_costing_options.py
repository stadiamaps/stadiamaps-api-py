# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.1
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import stadiamaps
from stadiamaps.models.base_costing_options import BaseCostingOptions  # noqa: E501
from stadiamaps.rest import ApiException

class TestBaseCostingOptions(unittest.TestCase):
    """BaseCostingOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BaseCostingOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `BaseCostingOptions`
        """
        model = stadiamaps.models.base_costing_options.BaseCostingOptions()  # noqa: E501
        if include_optional :
            return BaseCostingOptions(
                maneuver_penalty = 56, 
                gate_cost = 56, 
                gate_penalty = 56, 
                country_crossing_cost = 56, 
                country_crossing_penalty = 56, 
                service_penalty = 56, 
                service_factor = 1.337, 
                use_living_streets = 0, 
                use_ferry = 0
            )
        else :
            return BaseCostingOptions(
        )
        """

    def testBaseCostingOptions(self):
        """Test BaseCostingOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
