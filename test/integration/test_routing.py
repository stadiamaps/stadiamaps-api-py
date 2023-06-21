import os
import unittest

import stadiamaps

location_a = {"lat": 40.042072, "lon": -76.306572}
location_b = {"lat": 39.992115, "lon": -76.781559}
location_c = {"lat": 39.984519, "lon": -76.6956}


class TestRouting(unittest.TestCase):
    def setUp(self):
        self.configuration = stadiamaps.Configuration()
        self.configuration.api_key["ApiKeyAuth"] = os.environ["STADIA_API_KEY"]

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
                    stadiamaps.Coordinate.from_dict(location_c),
                    stadiamaps.Coordinate.from_dict(location_a),
                ],
                costing=stadiamaps.CostingModel.AUTO,
                costing_options=stadiamaps.CostingOptions(auto=stadiamaps.AutoCostingOptions(use_tolls=0.7)),
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

    def testNearestRoads(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.NearestRoadsRequest(
                locations=[location_a]
            )
            res = api_instance.nearest_roads(req)
            self.assertGreaterEqual(len(res), 1)
            self.assertGreaterEqual(len(res[0].edges), 1)

    def testIsochrone(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.IsochroneRequest(
                id="isochrone",
                locations=[location_a],
                costing=stadiamaps.IsochroneCostingModel.PEDESTRIAN,
                contours=[
                    stadiamaps.Contour(time=5, color="aabbcc")
                ],
                polygons=True,
            )
            res = api_instance.isochrone(req)
            self.assertEqual(req.id, res.id)
            self.assertGreaterEqual(len(res.features), 1)

    def testMapMatch(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.MapMatchRequest(
                id="map_match",
                encoded_polyline="_grbgAh~{nhF?lBAzBFvBHxBEtBKdB?fB@dBZdBb@hBh@jBb@x@\\|@x@pB\\x@v@hBl@nBPbCXtBn@|@z@ZbAEbAa@~@q@z@QhA]pAUpAVhAPlAWtASpAAdA[dASdAQhAIlARjANnAZhAf@n@`A?lB^nCRbA\\xB`@vBf@tBTbCFbARzBZvBThBRnBNrBP`CHbCF`CNdCb@vBX`ARlAJfADhA@dAFdAP`AR`Ah@hBd@bBl@rBV|B?vB]tBCvBBhAF`CFnBXtAVxAVpAVtAb@|AZ`Bd@~BJfA@fAHdADhADhABjAGzAInAAjAB|BNbCR|BTjBZtB`@lBh@lB\\|Bl@rBXtBN`Al@g@t@?nAA~AKvACvAAlAMdAU`Ac@hAShAI`AJ`AIdAi@bAu@|@k@p@]p@a@bAc@z@g@~@Ot@Bz@f@X`BFtBXdCLbAf@zBh@fBb@xAb@nATjAKjAW`BI|AEpAHjAPdAAfAGdAFjAv@p@XlAVnA?~A?jAInAPtAVxAXnAf@tBDpBJpBXhBJfBDpAZ|Ax@pAz@h@~@lA|@bAnAd@hAj@tAR~AKxAc@xAShA]hAIdAAjA]~A[v@BhB?dBSv@Ct@CvAI~@Oz@Pv@dAz@lAj@~A^`B^|AXvAVpAXdBh@~Ap@fCh@hB\\zBN`Aj@xBFdA@jALbAPbAJdAHdAJbAHbAHfAJhALbA\\lBTvBAdC@bC@jCKjASbC?`CM`CDpB\\xAj@tB\\fA\\bAVfAJdAJbAXz@L|BO`AOdCDdA@~B\\z@l@v@l@v@l@r@j@t@b@x@b@r@z@jBVfCJdAJdANbCPfCF|BRhBS~BS`AYbAe@~BQdA",
                costing=stadiamaps.MapMatchCostingModel.PEDESTRIAN,
                directions_options=stadiamaps.DirectionsOptions(units=stadiamaps.DistanceUnit.MI),
                linear_references=True,
            )
            res = api_instance.map_match(req)
            self.assertEqual(req.id, res.id)
            self.assertEqual(0, res.trip.status)
            self.assertEqual("miles", res.trip.units)
            self.assertEqual(len(res.trip.legs), 1)

    def testTraceAttributes(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.TraceAttributesRequest(
                id="trace",
                encoded_polyline="_grbgAh~{nhF?lBAzBFvBHxBEtBKdB?fB@dBZdBb@hBh@jBb@x@\\|@x@pB\\x@v@hBl@nBPbCXtBn@|@z@ZbAEbAa@~@q@z@QhA]pAUpAVhAPlAWtASpAAdA[dASdAQhAIlARjANnAZhAf@n@`A?lB^nCRbA\\xB`@vBf@tBTbCFbARzBZvBThBRnBNrBP`CHbCF`CNdCb@vBX`ARlAJfADhA@dAFdAP`AR`Ah@hBd@bBl@rBV|B?vB]tBCvBBhAF`CFnBXtAVxAVpAVtAb@|AZ`Bd@~BJfA@fAHdADhADhABjAGzAInAAjAB|BNbCR|BTjBZtB`@lBh@lB\\|Bl@rBXtBN`Al@g@t@?nAA~AKvACvAAlAMdAU`Ac@hAShAI`AJ`AIdAi@bAu@|@k@p@]p@a@bAc@z@g@~@Ot@Bz@f@X`BFtBXdCLbAf@zBh@fBb@xAb@nATjAKjAW`BI|AEpAHjAPdAAfAGdAFjAv@p@XlAVnA?~A?jAInAPtAVxAXnAf@tBDpBJpBXhBJfBDpAZ|Ax@pAz@h@~@lA|@bAnAd@hAj@tAR~AKxAc@xAShA]hAIdAAjA]~A[v@BhB?dBSv@Ct@CvAI~@Oz@Pv@dAz@lAj@~A^`B^|AXvAVpAXdBh@~Ap@fCh@hB\\zBN`Aj@xBFdA@jALbAPbAJdAHdAJbAHbAHfAJhALbA\\lBTvBAdC@bC@jCKjASbC?`CM`CDpB\\xAj@tB\\fA\\bAVfAJdAJbAXz@L|BO`AOdCDdA@~B\\z@l@v@l@v@l@r@j@t@b@x@b@r@z@jBVfCJdAJdANbCPfCF|BRhBS~BS`AYbAe@~BQdA",
                costing=stadiamaps.MapMatchCostingModel.PEDESTRIAN,
                directions_options=stadiamaps.DirectionsOptions(units=stadiamaps.DistanceUnit.MI),
            )
            res = api_instance.trace_attributes(req)
            self.assertEqual(req.id, res.id)
            self.assertEqual("miles", res.units)
            self.assertGreaterEqual(len(res.admins), 1)
            self.assertGreater(len(res.edges), 1)
            self.assertGreater(len(res.matched_points), 1)
            self.assertGreater(len(res.shape), 1)
