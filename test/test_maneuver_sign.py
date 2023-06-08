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
from stadiamaps.models.maneuver_sign import ManeuverSign  # noqa: E501
from stadiamaps.rest import ApiException

class TestManeuverSign(unittest.TestCase):
    """ManeuverSign unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ManeuverSign
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ManeuverSign`
        """
        model = stadiamaps.models.maneuver_sign.ManeuverSign()  # noqa: E501
        if include_optional :
            return ManeuverSign(
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
                    stadiamaps.models.maneuver_sign_element.maneuverSignElement(
                        text = '', 
                        is_route_number = True, 
                        consecutive_count = 56, )
                    ], 
                exit_name_elements = [
                    stadiamaps.models.maneuver_sign_element.maneuverSignElement(
                        text = '', 
                        is_route_number = True, 
                        consecutive_count = 56, )
                    ]
            )
        else :
            return ManeuverSign(
        )
        """

    def testManeuverSign(self):
        """Test ManeuverSign"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
