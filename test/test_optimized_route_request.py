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
from stadiamaps.models.optimized_route_request import OptimizedRouteRequest  # noqa: E501
from stadiamaps.rest import ApiException

class TestOptimizedRouteRequest(unittest.TestCase):
    """OptimizedRouteRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test OptimizedRouteRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OptimizedRouteRequest`
        """
        model = stadiamaps.models.optimized_route_request.OptimizedRouteRequest()  # noqa: E501
        if include_optional :
            return OptimizedRouteRequest(
                id = 'kesklinn', 
                locations = [
                    stadiamaps.models.coordinate.coordinate(
                        lat = 59.436884, 
                        lon = 24.742595, )
                    ], 
                costing = 'auto', 
                costing_options = stadiamaps.models.costing_options.costingOptions(
                    auto = null, 
                    bus = null, 
                    taxi = null, 
                    truck = null, 
                    bicycle = null, 
                    motor_scooter = null, 
                    motorcycle = null, 
                    pedestrian = stadiamaps.models.pedestrian_costing_options.pedestrianCostingOptions(
                        walking_speed = 0.5, 
                        walkway_factor = 1.337, 
                        sidewalk_factor = 1.337, 
                        alley_factor = 1.337, 
                        driveway_factor = 1.337, 
                        step_penalty = 56, 
                        use_ferry = 0, 
                        use_living_streets = 0, 
                        use_tracks = 0, 
                        use_hills = 0, 
                        use_lit = 0, 
                        service_penalty = 56, 
                        service_factor = 1.337, 
                        max_hiking_difficulty = 1, 
                        bss_rent_cost = 56, 
                        bss_rent_penalty = 56, ), ), 
                directions_options = stadiamaps.models.directions_options.directionsOptions(
                    units = 'km', 
                    language = 'en-US', 
                    directions_type = 'instructions', )
            )
        else :
            return OptimizedRouteRequest(
                locations = [
                    stadiamaps.models.coordinate.coordinate(
                        lat = 59.436884, 
                        lon = 24.742595, )
                    ],
                costing = 'auto',
        )
        """

    def testOptimizedRouteRequest(self):
        """Test OptimizedRouteRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
