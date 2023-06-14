import os
import unittest

import stadiamaps

address = "Põhja pst 27a"


class TestGeocoding(unittest.TestCase):
    def setUp(self):
        self.configuration = stadiamaps.Configuration()
        self.configuration.api_key["ApiKeyAuth"] = os.environ["STADIA_API_KEY"]

    def tearDown(self):
        pass

    def testAutocomplete(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.autocomplete(text=address)
            self.assertEqual("Estonia", res.features[0].properties.country)
            self.assertEqual("address", res.features[0].properties.layer)

    def testSearch(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.search(address)
            self.assertEqual("Estonia", res.features[0].properties.country)
            self.assertEqual("address", res.features[0].properties.layer)

    def testStructuredSearch(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.search_structured(address=address, country="Estonia")
            self.assertEqual("Estonia", res.features[0].properties.country)
            self.assertEqual("address", res.features[0].properties.layer)

    def testReverse(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.reverse(59.444351, 24.750645)
            self.assertEqual("Estonia", res.features[0].properties.country)
            self.assertEqual("address", res.features[0].properties.layer)

    def testReverseUncommonLayer(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            # Middle of the Gulf of Oman
            res = api_instance.reverse(24.750645, 59.444351)
            self.assertEqual("marinearea", res.features[0].properties.layer)

    def testPlace(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.place(["openstreetmap:address:way/109867749"])
            self.assertEqual(1, len(res.features))
            self.assertEqual("Estonia", res.features[0].properties.country)
            self.assertEqual("address", res.features[0].properties.layer)
