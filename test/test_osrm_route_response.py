# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 7.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stadiamaps.models.osrm_route_response import OsrmRouteResponse

class TestOsrmRouteResponse(unittest.TestCase):
    """OsrmRouteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> OsrmRouteResponse:
        """Test OsrmRouteResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `OsrmRouteResponse`
        """
        model = OsrmRouteResponse()
        if include_optional:
            return OsrmRouteResponse(
                code = 'Ok',
                message = '',
                data_version = '',
                waypoints = [
                    stadiamaps.models.osrm_waypoint.osrmWaypoint(
                        name = '', 
                        location = [
                            1.337
                            ], 
                        distance = 1.337, 
                        hint = '', )
                    ],
                routes = [
                    stadiamaps.models.osrm_route.osrmRoute(
                        distance = 1.337, 
                        duration = 1.337, 
                        geometry = '', 
                        weight = 1.337, 
                        weight_name = '', 
                        legs = [
                            stadiamaps.models.osrm_route_leg.osrmRouteLeg(
                                distance = 1.337, 
                                duration = 1.337, 
                                weight = 1.337, 
                                summary = '', 
                                steps = [
                                    stadiamaps.models.osrm_route_step.osrmRouteStep(
                                        distance = 1.337, 
                                        duration = 1.337, 
                                        geometry = '', 
                                        weight = 1.337, 
                                        name = '', 
                                        ref = '', 
                                        pronunciation = '', 
                                        destinations = stadiamaps.models.destinations.destinations(), 
                                        exits = stadiamaps.models.exits.exits(), 
                                        mode = '', 
                                        maneuver = stadiamaps.models.osrm_step_maneuver.osrmStepManeuver(
                                            location = [
                                                1.337
                                                ], 
                                            instruction = '', 
                                            bearing_before = 56, 
                                            bearing_after = 56, 
                                            type = 'turn', 
                                            modifier = 'uturn', 
                                            exit = 56, ), 
                                        intersections = [
                                            stadiamaps.models.osrm_intersection.osrmIntersection(
                                                location = [
                                                    1.337
                                                    ], 
                                                bearings = [
                                                    56
                                                    ], 
                                                classes = [
                                                    'toll'
                                                    ], 
                                                entry = [
                                                    True
                                                    ], 
                                                in = 56, 
                                                out = 56, 
                                                lanes = [
                                                    stadiamaps.models.osrm_lane.osrmLane(
                                                        indications = [
                                                            'none'
                                                            ], 
                                                        valid = True, )
                                                    ], 
                                                admin_index = 56, 
                                                duration = 1.337, 
                                                turn_duration = 1.337, 
                                                turn_weight = 1.337, 
                                                geometry_index = 56, 
                                                weight = 1.337, )
                                            ], 
                                        rotary_name = '', 
                                        rotary_pronunciation = '', 
                                        driving_side = 'left', 
                                        voice_instructions = [
                                            stadiamaps.models.osrm_voice_instruction.osrmVoiceInstruction(
                                                distance_along_geometry = 1.337, 
                                                announcement = '', 
                                                ssml_announcement = '', )
                                            ], 
                                        banner_instructions = [
                                            stadiamaps.models.osrm_banner_instruction.osrmBannerInstruction(
                                                distance_along_geometry = 1.337, 
                                                primary = stadiamaps.models.osrm_banner_content.osrmBannerContent(
                                                    text = '', 
                                                    type = 'turn', 
                                                    components = [
                                                        stadiamaps.models.osrm_banner_component.osrmBannerComponent(
                                                            text = '', 
                                                            type = 'text', )
                                                        ], ), 
                                                secondary = stadiamaps.models.osrm_banner_content.osrmBannerContent(
                                                    text = '', 
                                                    type = 'turn', ), )
                                            ], 
                                        speed_limit_sign = 'mutcd', 
                                        speed_limit_unit = '', )
                                    ], 
                                annotation = stadiamaps.models.osrm_annotation.osrmAnnotation(
                                    distance = [
                                        1.337
                                        ], 
                                    duration = [
                                        1.337
                                        ], 
                                    weight = [
                                        56
                                        ], 
                                    speed = [
                                        1.337
                                        ], 
                                    maxspeed = [
                                        stadiamaps.models.osrm_speed_limit.osrmSpeedLimit(
                                            unit = 'km/h', 
                                            unknown = True, 
                                            none = True, )
                                        ], ), 
                                via_waypoints = [
                                    stadiamaps.models.osrm_via_waypoint.osrmViaWaypoint(
                                        distance_from_start = 1.337, 
                                        geometry_index = 56, 
                                        waypoint_index = 56, )
                                    ], 
                                admins = [
                                    stadiamaps.models.osrm_admin.osrmAdmin(
                                        iso_3166_1 = '', 
                                        iso_3166_1_alpha3 = '', )
                                    ], )
                            ], )
                    ]
            )
        else:
            return OsrmRouteResponse(
                code = 'Ok',
        )
        """

    def testOsrmRouteResponse(self):
        """Test OsrmRouteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
