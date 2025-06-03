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

    def testAutocompleteV1(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.autocomplete(text=address, lang="en")
            self.assertEqual("Estonia", res.features[0].properties.country)
            self.assertEqual("address", res.features[0].properties.layer)

    def testAutocompleteV2(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.autocomplete_v2(text=address, lang="en")
            self.assertEqual(None, res.features[0].properties.context)
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

    def testReverseV2(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.reverse_v2(59.444351, 24.750645, lang="en")
            self.assertEqual("EST", res.features[0].properties.context.iso_3166_a3)

    def testReverseWithLayerFilter(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.reverse(59.444351, 24.750645,
                                       layers=[stadiamaps.GeocodingLayer.ADDRESS, stadiamaps.GeocodingLayer.OCEAN])
            self.assertEqual("Estonia", res.features[0].properties.country)
            self.assertEqual("address", res.features[0].properties.layer)

    def testReverseWithLayerFilterV2(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.reverse_v2(59.444351, 24.750645,
                                          layers=[stadiamaps.LayerId.ADDRESS, stadiamaps.LayerId.OCEAN],
                                          lang="en")
            self.assertEqual("EST", res.features[0].properties.context.iso_3166_a3)
            self.assertEqual("address", res.features[0].properties.layer)

    def testReverseUncommonLayer(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            # Middle of the Gulf of Oman
            res = api_instance.reverse(24.750645, 59.444351)
            self.assertEqual("marinearea", res.features[0].properties.layer)

    def testReverseUncommonLayerV2(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            # Middle of the Gulf of Oman
            res = api_instance.reverse_v2(24.750645, 59.444351, lang="en")
            self.assertEqual("marinearea", res.features[0].properties.layer)

    def testPlaceV1(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.place_details(["openstreetmap:address:way/109867749"])
            self.assertEqual(1, len(res.features))
            self.assertEqual("Estonia", res.features[0].properties.country)
            self.assertEqual("address", res.features[0].properties.layer)

    def testPlaceV2(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.place_details_v2(["openstreetmap:address:way/109867749"], lang="en")
            self.assertEqual(1, len(res.features))
            self.assertEqual("Estonia", res.features[0].properties.context.whosonfirst.country.name)
            self.assertEqual("EST", res.features[0].properties.context.iso_3166_a3)
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
                                               stadiamaps.GeocodingLayer.COARSE,
                                               stadiamaps.GeocodingLayer.ADDRESS]))),
            ])

            self.assertEqual(2, len(res))
            for rec in res:
                self.assertEqual(200, rec.status)
                self.assertEqual("Estonia", rec.response.features[0].properties.country)
                self.assertEqual("address", rec.response.features[0].properties.layer)

    def testBulkPostalcodeRegression(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeocodingApi(api_client)

            res = api_instance.search_bulk([
                stadiamaps.BulkRequest(endpoint="/v1/search/structured",
                                       query=stadiamaps.BulkRequestQuery(stadiamaps.SearchStructuredQuery(
                                           locality="Aach",
                                           postalcode="78267",
                                           region="North Rhine-Westphalia",
                                           country="Germany"))),
            ])

            self.assertEqual(1, len(res))
            rec = res[0]
            self.assertEqual(200, rec.status)
            self.assertEqual("Germany", rec.response.features[0].properties.country)
            self.assertEqual("postalcode", rec.response.features[0].properties.layer)
            self.assertEqual("78267", rec.response.features[0].properties.postalcode)
