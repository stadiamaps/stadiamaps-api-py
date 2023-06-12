import os
import unittest

import stadiamaps


class TestGeospatial(unittest.TestCase):
    def setUp(self):
        self.configuration = stadiamaps.Configuration()
        self.configuration.api_key["ApiKeyAuth"] = os.environ["STADIA_API_KEY"]

    def tearDown(self):
        pass

    def testTZLookup(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeospatialApi(api_client)

            res = api_instance.tz_lookup(37.56, 126.99)
            self.assertEqual("Asia/Seoul", res.tz_id)

    def testElevation(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.GeospatialApi(api_client)

            req = stadiamaps.HeightRequest(id="Seoul", shape=[stadiamaps.Coordinate(lat=37.56, lon=126.99)])
            res = api_instance.elevation(req)
            self.assertEqual(req.id, res.id)
            self.assertGreaterEqual(len(res.height), 1)
            self.assertGreaterEqual(res.height[0], 1)
            self.assertEqual(res.shape, req.shape)
