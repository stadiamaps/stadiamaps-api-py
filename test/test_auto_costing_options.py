# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications. All endpoints are versioned individually to allow for granular upgrades. We follow the [Semantic Versioning scheme](https://semver.org/).  # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest
import datetime

import stadiamaps
from stadiamaps.models.auto_costing_options import AutoCostingOptions  # noqa: E501
from stadiamaps.rest import ApiException

class TestAutoCostingOptions(unittest.TestCase):
    """AutoCostingOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AutoCostingOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AutoCostingOptions`
        """
        model = stadiamaps.models.auto_costing_options.AutoCostingOptions()  # noqa: E501
        if include_optional :
            return AutoCostingOptions(
                maneuver_penalty = 56, 
                gate_cost = 56, 
                gate_penalty = 56, 
                country_crossing_cost = 56, 
                country_crossing_penalty = 56, 
                service_penalty = 56, 
                service_factor = 1.337, 
                use_living_streets = 0, 
                use_ferry = 0, 
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
            return AutoCostingOptions(
        )
        """

    def testAutoCostingOptions(self):
        """Test AutoCostingOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
