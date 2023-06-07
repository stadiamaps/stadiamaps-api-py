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
from stadiamaps.models.map_match_request import MapMatchRequest  # noqa: E501
from stadiamaps.rest import ApiException

class TestMapMatchRequest(unittest.TestCase):
    """MapMatchRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test MapMatchRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MapMatchRequest`
        """
        model = stadiamaps.models.map_match_request.MapMatchRequest()  # noqa: E501
        if include_optional :
            return MapMatchRequest(
                id = 'kesklinn', 
                shape = [
                    null
                    ], 
                encoded_polyline = '', 
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
                shape_match = 'edge_walk', 
                directions_options = stadiamaps.models.directions_options.directionsOptions(
                    units = 'km', 
                    language = 'en-US', 
                    directions_type = 'instructions', ), 
                begin_time = 56, 
                durations = 56, 
                use_timestamps = True, 
                trace_options = stadiamaps.models.map_match_trace_options.mapMatchTraceOptions(
                    search_radius = 56, 
                    gps_accuracy = 1.337, 
                    breakage_distance = 1.337, 
                    interpolation_distance = 1.337, 
                    turn_penalty_factor = 56, ), 
                linear_references = True
            )
        else :
            return MapMatchRequest(
                costing = 'auto',
        )
        """

    def testMapMatchRequest(self):
        """Test MapMatchRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
