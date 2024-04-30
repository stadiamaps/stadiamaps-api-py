# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 6.3.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stadiamaps.models.low_speed_vehicle_costing_options import LowSpeedVehicleCostingOptions

class TestLowSpeedVehicleCostingOptions(unittest.TestCase):
    """LowSpeedVehicleCostingOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LowSpeedVehicleCostingOptions:
        """Test LowSpeedVehicleCostingOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LowSpeedVehicleCostingOptions`
        """
        model = LowSpeedVehicleCostingOptions()
        if include_optional:
            return LowSpeedVehicleCostingOptions(
                maneuver_penalty = 56,
                gate_cost = 56,
                gate_penalty = 56,
                country_crossing_cost = 56,
                country_crossing_penalty = 56,
                service_penalty = 56,
                service_factor = 1.337,
                use_living_streets = 0,
                use_ferry = 0,
                ignore_restrictions = True,
                ignore_non_vehicular_restrictions = True,
                ignore_oneways = True,
                vehicle_type = 'low_speed_vehicle',
                top_speed = 20,
                max_allowed_speed_limit = 20
            )
        else:
            return LowSpeedVehicleCostingOptions(
        )
        """

    def testLowSpeedVehicleCostingOptions(self):
        """Test LowSpeedVehicleCostingOptions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()