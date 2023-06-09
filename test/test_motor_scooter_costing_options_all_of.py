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
from stadiamaps.models.motor_scooter_costing_options_all_of import MotorScooterCostingOptionsAllOf  # noqa: E501
from stadiamaps.rest import ApiException

class TestMotorScooterCostingOptionsAllOf(unittest.TestCase):
    """MotorScooterCostingOptionsAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MotorScooterCostingOptionsAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MotorScooterCostingOptionsAllOf`
        """
        model = stadiamaps.models.motor_scooter_costing_options_all_of.MotorScooterCostingOptionsAllOf()  # noqa: E501
        if include_optional :
            return MotorScooterCostingOptionsAllOf(
                use_primary = 0, 
                use_hills = 0
            )
        else :
            return MotorScooterCostingOptionsAllOf(
        )
        """

    def testMotorScooterCostingOptionsAllOf(self):
        """Test MotorScooterCostingOptionsAllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
