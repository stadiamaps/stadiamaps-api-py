import os
import unittest

import stadiamaps

address = "Põhja pst 27"


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

    def testReverseWithLayerFilter(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.reverse(59.444351, 24.750645,
                                       layers=[stadiamaps.PeliasLayer.ADDRESS, stadiamaps.PeliasLayer.OCEAN])
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

    def testBulk(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.search_bulk([
                stadiamaps.BulkRequest(endpoint="/v1/search",
                                       query=stadiamaps.BulkRequestQuery(stadiamaps.SearchQuery(text=address))),
                stadiamaps.BulkRequest(endpoint="/v1/search/structured",
                                       query=stadiamaps.BulkRequestQuery(stadiamaps.SearchStructuredQuery(
                                           address=address,
                                           country="EE",
                                           layers=[
                                               stadiamaps.PeliasLayer.COARSE,
                                               stadiamaps.PeliasLayer.ADDRESS]))),
            ])

            self.assertEqual(2, len(res))
            for rec in res:
                self.assertEqual(200, rec.status)
                self.assertEqual("Estonia", rec.response.features[0].properties.country)
                self.assertEqual("address", rec.response.features[0].properties.layer)
