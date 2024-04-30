# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 6.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stadiamaps.models.route_response_alternates_inner import RouteResponseAlternatesInner

class TestRouteResponseAlternatesInner(unittest.TestCase):
    """RouteResponseAlternatesInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RouteResponseAlternatesInner:
        """Test RouteResponseAlternatesInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RouteResponseAlternatesInner`
        """
        model = RouteResponseAlternatesInner()
        if include_optional:
            return RouteResponseAlternatesInner(
                trip = stadiamaps.models.route_trip.routeTrip(
                    status = 56, 
                    status_message = '', 
                    units = 'kilometers', 
                    language = 'en-US', 
                    locations = [
                        null
                        ], 
                    legs = [
                        stadiamaps.models.route_leg.routeLeg(
                            maneuvers = [
                                stadiamaps.models.route_maneuver.routeManeuver(
                                    type = 56, 
                                    instruction = '', 
                                    verbal_transition_alert_instruction = '', 
                                    verbal_pre_transition_instruction = '', 
                                    verbal_post_transition_instruction = '', 
                                    street_names = [
                                        'A1'
                                        ], 
                                    begin_street_names = [
                                        'A1'
                                        ], 
                                    time = 1.337, 
                                    length = 1.337, 
                                    begin_shape_index = 56, 
                                    end_shape_index = 56, 
                                    toll = True, 
                                    rough = True, 
                                    gate = True, 
                                    ferry = True, 
                                    sign = stadiamaps.models.maneuver_sign.maneuverSign(
                                        exit_number_elements = [
                                            stadiamaps.models.maneuver_sign_element.maneuverSignElement(
                                                text = '', 
                                                is_route_number = True, 
                                                consecutive_count = 56, )
                                            ], 
                                        exit_branch_elements = [
                                            stadiamaps.models.maneuver_sign_element.maneuverSignElement(
                                                text = '', 
                                                is_route_number = True, 
                                                consecutive_count = 56, )
                                            ], 
                                        exit_toward_elements = [
                                            
                                            ], 
                                        exit_name_elements = [
                                            
                                            ], ), 
                                    roundabout_exit_count = 56, 
                                    depart_instruction = 56, 
                                    verbal_depart_instruction = 56, 
                                    arrive_instruction = 56, 
                                    verbal_arrive_instruction = 56, 
                                    transit_info = { }, 
                                    verbal_multi_cue = True, 
                                    travel_mode = 'drive', 
                                    travel_type = 'car', 
                                    bss_maneuver_type = 'NoneAction', )
                                ], 
                            shape = '', 
                            summary = stadiamaps.models.route_summary.routeSummary(
                                time = 1.337, 
                                length = 1.337, 
                                min_lat = 1.337, 
                                max_lat = 1.337, 
                                min_lon = 1.337, 
                                max_lon = 1.337, ), )
                        ], 
                    summary = stadiamaps.models.route_summary.routeSummary(
                        time = 1.337, 
                        length = 1.337, 
                        min_lat = 1.337, 
                        max_lat = 1.337, 
                        min_lon = 1.337, 
                        max_lon = 1.337, ), )
            )
        else:
            return RouteResponseAlternatesInner(
        )
        """

    def testRouteResponseAlternatesInner(self):
        """Test RouteResponseAlternatesInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()