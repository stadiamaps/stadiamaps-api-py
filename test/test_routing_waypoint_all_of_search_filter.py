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
from stadiamaps.models.routing_waypoint_all_of_search_filter import RoutingWaypointAllOfSearchFilter  # noqa: E501
from stadiamaps.rest import ApiException

class TestRoutingWaypointAllOfSearchFilter(unittest.TestCase):
    """RoutingWaypointAllOfSearchFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoutingWaypointAllOfSearchFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoutingWaypointAllOfSearchFilter`
        """
        model = stadiamaps.models.routing_waypoint_all_of_search_filter.RoutingWaypointAllOfSearchFilter()  # noqa: E501
        if include_optional :
            return RoutingWaypointAllOfSearchFilter(
                exclude_tunnel = True, 
                exclude_bridge = True, 
                exclude_ramp = True, 
                exclude_closures = True, 
                min_road_class = 'motorway', 
                max_road_class = 'motorway'
            )
        else :
            return RoutingWaypointAllOfSearchFilter(
        )
        """

    def testRoutingWaypointAllOfSearchFilter(self):
        """Test RoutingWaypointAllOfSearchFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
