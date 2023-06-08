import os
import unittest

import stadiamaps


class TestGeocoding(unittest.TestCase):
    def setUp(self):
        self.configuration = stadiamaps.Configuration()
        self.configuration.api_key['ApiKeyAuth'] = os.environ["STADIA_API_KEY"]

    def tearDown(self):
        pass

    def testAutocomplete(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            # Create an instance of the API class
            api_instance = stadiamaps.GeocodingApi(api_client)
            text = 'Põhja pst 27a'  # str | The place name (address, venue name, etc.) to search for.

            # Search and geocode quickly based on partial input.
            api_response = api_instance.autocomplete(text)
            self.assertEqual("Estonia", api_response.features[0].properties.country)
