import os
import unittest

import stadiamaps

location_a = {"lat": 40.042072, "lon": -76.306572}
location_b = {"lat": 39.992115, "lon": -76.781559}
location_c = {"lat": 39.984519, "lon": -76.6956}


class TestRouting(unittest.TestCase):
    def setUp(self):
        self.configuration = stadiamaps.Configuration()
        self.configuration.api_key['ApiKeyAuth'] = os.environ["STADIA_API_KEY"]

    def tearDown(self):
        pass

    def testRoute(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.RouteRequest(
                id="route",
                locations=[
                    stadiamaps.RoutingWaypoint.from_dict(location_a),
                    stadiamaps.RoutingWaypoint.from_dict(location_b)
                ],
                costing=stadiamaps.CostingModel.AUTO,
                costing_options=stadiamaps.CostingOptions(auto=stadiamaps.AutoCostingOptions(use_tolls=1)),
                directions_options=stadiamaps.DirectionsOptions(units=stadiamaps.DistanceUnit.MI)
            )

            res = api_instance.route(req)
            self.assertEqual(req.id, res.id)
            self.assertEqual(0, res.trip.status)
            self.assertEqual("miles", res.trip.units)
            self.assertEqual(len(res.trip.legs), 1)

    def testOptimizedRoute(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.OptimizedRouteRequest(
                id="optimized_route",
                locations=[
                    stadiamaps.Coordinate.from_dict(location_a),
                    stadiamaps.Coordinate.from_dict(location_b),
                    stadiamaps.Coordinate.from_dict(location_c)
                ],
                costing=stadiamaps.CostingModel.AUTO,
                costing_options=stadiamaps.CostingOptions(auto=stadiamaps.AutoCostingOptions(use_tolls=1)),
                directions_options=stadiamaps.DirectionsOptions(units=stadiamaps.DistanceUnit.MI)
            )

            res = api_instance.optimized_route(req)
            self.assertEqual(req.id, res.id)
            self.assertEqual(0, res.trip.status)
            self.assertEqual("miles", res.trip.units)
            self.assertGreater(len(res.trip.legs), 1)

    def testTimeDistanceMatrix(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.MatrixRequest(
                id="matrix",
                sources=[
                    stadiamaps.Coordinate.from_dict(location_a),
                ],
                targets=[
                    stadiamaps.Coordinate.from_dict(location_b),
                    stadiamaps.Coordinate.from_dict(location_c),
                ],
                costing=stadiamaps.MatrixCostingModel.PEDESTRIAN,
            )

            res = api_instance.time_distance_matrix(req)
            self.assertEqual(req.id, res.id)
            self.assertEqual([req.sources], res.sources)
            self.assertEqual([req.targets], res.targets)
            self.assertGreaterEqual(len(res.sources_to_targets), 1)
            self.assertEqual("kilometers", res.units)
