import os
import unittest

import stadiamaps


class TestEUEndpoint(unittest.TestCase):
    def setUp(self):
        self.configuration = stadiamaps.Configuration(host="https://api-eu.stadiamaps.com")
        self.configuration.api_key["ApiKeyAuth"] = os.environ["STADIA_API_KEY"]

    def tearDown(self):
        pass

    def testAutocomplete(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.autocomplete("Põhja pst 27")
            self.assertEqual("Estonia", res.features[0].properties.country)
            self.assertEqual("address", res.features[0].properties.layer)
