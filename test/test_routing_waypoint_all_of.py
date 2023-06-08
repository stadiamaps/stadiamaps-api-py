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
from stadiamaps.models.routing_waypoint_all_of import RoutingWaypointAllOf  # noqa: E501
from stadiamaps.rest import ApiException

class TestRoutingWaypointAllOf(unittest.TestCase):
    """RoutingWaypointAllOf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoutingWaypointAllOf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoutingWaypointAllOf`
        """
        model = stadiamaps.models.routing_waypoint_all_of.RoutingWaypointAllOf()  # noqa: E501
        if include_optional :
            return RoutingWaypointAllOf(
                heading = 0, 
                heading_tolerance = 0, 
                minimum_reachability = 0, 
                radius = 0, 
                rank_candidates = True, 
                preferred_side = 'same', 
                node_snap_tolerance = 0, 
                street_side_tolerance = 0, 
                street_side_max_distance = 0, 
                search_filter = stadiamaps.models.routing_waypoint_all_of_search_filter.routingWaypoint_allOf_search_filter(
                    exclude_tunnel = True, 
                    exclude_bridge = True, 
                    exclude_ramp = True, 
                    exclude_closures = True, 
                    min_road_class = null, 
                    max_road_class = null, )
            )
        else :
            return RoutingWaypointAllOf(
        )
        """

    def testRoutingWaypointAllOf(self):
        """Test RoutingWaypointAllOf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
