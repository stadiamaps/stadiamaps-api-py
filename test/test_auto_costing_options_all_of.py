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
from stadiamaps.models.auto_costing_options_all_of import AutoCostingOptionsAllOf  # noqa: E501
from stadiamaps.rest import ApiException

class TestAutoCostingOptionsAllOf(unittest.TestCase):
    """AutoCostingOptionsAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AutoCostingOptionsAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AutoCostingOptionsAllOf`
        """
        model = stadiamaps.models.auto_costing_options_all_of.AutoCostingOptionsAllOf()  # noqa: E501
        if include_optional :
            return AutoCostingOptionsAllOf(
                height = 1.337, 
                width = 1.337, 
                toll_booth_cost = 56, 
                toll_booth_penalty = 56, 
                ferry_cost = 56, 
                use_highways = 0, 
                use_tolls = 0, 
                use_tracks = 0, 
                top_speed = 10, 
                shortest = True, 
                ignore_closures = True, 
                include_hov2 = True, 
                include_hov3 = True, 
                include_hot = True
            )
        else :
            return AutoCostingOptionsAllOf(
        )
        """

    def testAutoCostingOptionsAllOf(self):
        """Test AutoCostingOptionsAllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
