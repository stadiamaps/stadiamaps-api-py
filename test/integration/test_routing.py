import os
import unittest

import stadiamaps
from stadiamaps import AnnotationFilters

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
                costing_options=stadiamaps.CostingOptions(auto=stadiamaps.AutoCostingOptions(use_tolls=0.7)),
                units=stadiamaps.DistanceUnit.MI,
            )

            res = api_instance.route(req).actual_instance
            self.assertEqual(req.id, res.id)
            self.assertEqual(0, res.trip.status)
            self.assertEqual("miles", res.trip.units)
            self.assertEqual(len(res.trip.legs), 1)
            self.assertEqual(len(res.alternates or []), 0)

    def testNavigationRoute(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.RouteRequest(
                id="route",
                locations=[
                    stadiamaps.RoutingWaypoint.from_dict(location_a),
                    stadiamaps.RoutingWaypoint.from_dict(location_b)
                ],
                costing=stadiamaps.CostingModel.AUTO,
                costing_options=stadiamaps.CostingOptions(auto=stadiamaps.AutoCostingOptions(use_tolls=0.7)),
                units=stadiamaps.DistanceUnit.MI,
                format="osrm",
                banner_instructions=True,
                filters=AnnotationFilters(action="include", attributes=["shape_attributes.speed_limit"])
            )

            res = api_instance.route(req).actual_instance
            self.assertEqual("Ok", res.code)
            self.assertEqual(len(res.routes), 1)
            has_banner_instructions = False
            for step in res.routes[0].legs[0].steps:
                if len(step.banner_instructions) > 0:
                    has_banner_instructions = True

            self.assertTrue(has_banner_instructions)

    def testRouteWithAlternates(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.RouteRequest(
                id="route",
                locations=[
                    stadiamaps.RoutingWaypoint.from_dict(location_a),
                    stadiamaps.RoutingWaypoint.from_dict(location_b)
                ],
                costing=stadiamaps.CostingModel.AUTO,
                costing_options=stadiamaps.CostingOptions(auto=stadiamaps.AutoCostingOptions(use_tolls=0.7)),
                units=stadiamaps.DistanceUnit.MI,
                alternates=1,
            )

            res = api_instance.route(req).actual_instance
            self.assertEqual(req.id, res.id)
            self.assertEqual(0, res.trip.status)
            self.assertEqual("miles", res.trip.units)
            self.assertEqual(len(res.trip.legs), 1)
            self.assertEqual(len(res.alternates), 1)

    def testRouteWithElevation(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.RouteRequest(
                id="route",
                locations=[
                    stadiamaps.RoutingWaypoint.from_dict(location_a),
                    stadiamaps.RoutingWaypoint.from_dict(location_b)
                ],
                costing=stadiamaps.CostingModel.AUTO,
                costing_options=stadiamaps.CostingOptions(auto=stadiamaps.AutoCostingOptions(use_tolls=0.7)),
                units=stadiamaps.DistanceUnit.MI,
                elevation_interval=30,
            )

            res = api_instance.route(req).actual_instance
            self.assertEqual(req.id, res.id)
            self.assertEqual(0, res.trip.status)
            self.assertEqual("miles", res.trip.units)
            self.assertEqual(len(res.trip.legs), 1)
            self.assertGreater(len(res.trip.legs[0].elevation), 1)

    def testHybridBicycleRoute(self):
        # Regression test for user-reported issue
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.RouteRequest(
                id="route",
                locations=[
                    stadiamaps.RoutingWaypoint.from_dict(location_a),
                    stadiamaps.RoutingWaypoint.from_dict(location_b)
                ],
                costing=stadiamaps.CostingModel.BICYCLE,
                costing_options=stadiamaps.CostingOptions(
                    bicycle=stadiamaps.BicycleCostingOptions(bicycle_type='Hybrid', use_roads=0.4, use_hills=0.6)),
                units=stadiamaps.DistanceUnit.KM,
            )

            res = api_instance.route(req).actual_instance
            self.assertEqual(req.id, res.id)
            self.assertEqual(0, res.trip.status)
            self.assertEqual("kilometers", res.trip.units)
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
                costing=stadiamaps.MatrixCostingModel.AUTO,
                costing_options=stadiamaps.CostingOptions(auto=stadiamaps.AutoCostingOptions(use_tolls=0.7)),
                units=stadiamaps.DistanceUnit.MI,
            )

            res = api_instance.optimized_route(req).actual_instance
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
                    stadiamaps.MatrixWaypoint.from_dict(location_a),
                ],
                targets=[
                    stadiamaps.MatrixWaypoint.from_dict(location_b),
                    stadiamaps.MatrixWaypoint.from_dict(location_c),
                ],
                costing=stadiamaps.MatrixCostingModel.PEDESTRIAN,
            )

            res = api_instance.time_distance_matrix(req)
            self.assertEqual(req.id, res.id)
            self.assertEqual(len(req.sources), len(res.sources))
            self.assertEqual(len(req.targets), len(res.targets))
            self.assertGreater(len(res.sources_to_targets[0]), 1)
            self.assertEqual("kilometers", res.units)

    def testTimeDistanceMatrixWithUnroutableLegs(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            # At least one of these is not routable; make sure we handle it gracefully
            req = stadiamaps.MatrixRequest(
                id="matrix",
                sources=[
                    stadiamaps.MatrixWaypoint.from_dict({
                        "lon": 22.726262,
                        "lat": 58.891957
                    }),
                    stadiamaps.MatrixWaypoint.from_dict({
                        "lon": 23.762758,
                        "lat": 59.1558
                    }),
                ],
                targets=[
                    stadiamaps.MatrixWaypoint.from_dict({
                        "lon": 23.846605,
                        "lat": 59.176153
                    }),
                    stadiamaps.MatrixWaypoint.from_dict({
                        "lon": 23.096114,
                        "lat": 59.562853
                    }),
                ],
                costing=stadiamaps.MatrixCostingModel.BICYCLE,
            )

            res = api_instance.time_distance_matrix(req)
            self.assertEqual(req.id, res.id)
            self.assertEqual(len(req.sources), len(res.sources))
            self.assertGreater(len(res.sources_to_targets[0]), 1)
            self.assertEqual("kilometers", res.units)

    def testNearestRoads(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.NearestRoadsRequest(
                locations=[stadiamaps.Coordinate.from_dict(loc) for loc in (location_a, location_b, location_c)]
            )
            res = api_instance.nearest_roads(req)
            self.assertEqual(len(res), 3)
            self.assertGreaterEqual(len(res[0].edges), 1)

    def testIsochrone(self):
        with stadiamaps.ApiClient(self.configuration) as api_client:
            api_instance = stadiamaps.RoutingApi(api_client)

            req = stadiamaps.IsochroneRequest(
                id="isochrone",
                locations=[stadiamaps.Coordinate.from_dict(location_a)],
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
                units=stadiamaps.DistanceUnit.MI,
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
                encoded_polyline="ge~jkAbakppC_AJ}_@hEsCZiCXuo@dH{l@pGuaBtPjBr`@`Bt]bDpu@FbDy@fEcAjEgOja@_BfE]zDoIzTaF~MwLtZsDjJwJ~ViF`N_DjI_AzBcDbIsJ~UqIvSqLvYoAzCwJdVmLjY_DzH_FzLuYls@aYhr@Uj@iCpGu@jBmLjYeJ~T_C|FoBzEkGrO}FtNaFxGkHpQeArHcGbOeEfK}D`K}Shi@uWxp@gMv[wBnFiAtCmMl[aB`EoKrW}Mj\\kDlI}K~WeBdEeHxPgF~LiBjE{BnF_EpJsD|I}Rte@sNp]Uj@aQ|b@w^||@_EtJi^`_AaC~F}Qnc@cHlOgA~B}DnIqG~M_NbXeO~X{O~X}\\nl@oFjJyRt\\iJ|NiGxJ{KbPeLtO_HhIyGjI_GbHc]v_@mNnOgWdYcFvFsGtFkBiEWg@cAfAqBnBnCnFaErDiTlSiWdV_O~N{QrOcFrE{IjIaGrC}G|IeEbGwDdGeDfGsDtHmDbIgI~SyEdMaBpEeB|E_BnEsLl\\qLj\\nxAfoA`Lr`ApB|Rz@`Lr@nLp@tJfCzW~Fhi@r@bGv@tF`AnFdA|ErA~EzAxE~BzF|I`SjAxC|@nCl@zB`@lBXtBPhBJ`BDfB@dDCjDGxDqIv}BUrIKpFE|C@|CFhD`@nM`@lJPnDJhAdkA|fMob@i`@gAZfEhgAT|FpDvEnKISjr@pHfe@dHjCvM{F{Lak@q@mZq[bbC~OnAvRvWcHrVzK`GzH}TxGdDoDrKyHlVwG`TvGaTfI|EnBxBZvBGj]AnDAlC\\lB~K~ZtoAlEuExOy@bFi@xHFxF^fEl@rDfBxGbC~GjEdKjQbm@oG|YvBpFrMbV~GlMlGtJtFlHlEjFnGtJzDjGzDvHjBtFrD`IzB`DzD~ClDjBzDjCzChAjD~@?vF^tHx@vGpA~DbB`CpBhArCSrDk@dEkAxB_AbC_BpBkB`@K`B]pFp@fDx@tDh@`BHrCJ~CKd@S`Bk@fAcA`AtP`UxCcAfUsChq@wBSkBSiB[}BiAwMbOvMcO|BhAhBZjBRvBRwC`o@g@vJjBeC~@c@tAz@xF`NnX~p@zAlDtAvA|Bv@xBQ??fo@vsBJhDpc@`aDhBrHzCtHzHtP}Vz_@iFjIiFpIoEbIaJnPzf@d_BuAlQiA~^qd@|dMcCru@G|Cq@|^]z_@LnV^x]RtHd@xP`Bdb@pCbStApIpAjFdCnHlCtFtBlDxDxEdBfBnCnC`~B`yMhA`A|bHvr`@~CxVbF_A~a@yJbS}EvDXdM|AvJ{F{gAjtDgCddC|f@jyDbEtPxuG|scBsDxMahGvkYlXhT`DvCfChC|BjCfBlC|C`GvDdI~_@jbAhJ`Vt|AltGoH~FcTdLqDlA}Af@zhAgl@jEzSnCnNnCjOfBnL~C`XfA~J|@`Kj@hJXtHzAtm@v@xSZrEh@pDdApDfDxFaDxDiA`DG~FpBz^v@tL~@hIt@jDhAdDpYxf@feAbhB{]va@iPuXaBeD`BdDhPtX{JjM~Jz]|@TvPaOjJ~OvNtV|N|Vla@xr@zWjd@fAjBkGlHuUnXqB`CaFgIoK_QmF`HuJcPiFfHo@~BUtBFtA`@zAdA~AfQ|Vb@p@|@rJcCrCxQ|YhmNn`hAk@zECnEbV`x@dBnBlGdAlCX|m@o[tBkDdAoFf@mCdMwGvE~NzGhLzDxE}FtIcC|Bcu@xq@eBzCe@hC~x@t~ElhZpalAln@mSAjKp@pJyKpBqSxHh|KdwX~eMnjv@B_BV_BXeAt@y@fLaChRwBdO]tKXpN~Cz[`N_A`CcArIjC|qAUjHmAnG}BzEyDxDyeAli@hoDxhMpHxEaBdMh@jN~I``@jLpk@v@~D~e@nqE|@`ChBlCRzAP`B|CvHl\\yNlT{HCnGLvBxFn[fBzJ~A|IzAnGpBrGrCvFnOtVfEdIhEvJhBpFiLpH{d@fZiAdE\\hF`tDtzJCFzt@lg@mCpIiDtKhDuKlCqIrD_MbNid@sY}Q{LiJkIqHHaI]wEX{H|AwG`HaNnBzBtLjK`MxIbNrI`e@xYxKjJpIrI~HrKzG`NzErKtDdL~C`OdCtOhFvj@mLdC[F|SxzB~LyBzAxPhChYl@`E`AbExAdDjBxC|BvBtBfBlCpAdDz@nDl@|D^pGf@lSzAxIn@kAxScA|QTvAf@~AdNtSrg@taCfAxGyHfF{KdHiAp@vc@rrBw@hOk@|K~bBh|W~CnHfF`GdMnGpH`AlIm@nh@kL~gAfrOCbMbAbMD`@~@pRMhLNrRaBbB?fLvG`@zC\\|I~@SrOI`FzAfGoKpJqKpJ}@pLjPf\\rFT`H}AhBjA|HXClFyAdHuD~Jm\\oDsUkAwM]eMxrBqLvcCoC|{@e@jk@rBrjD`Ar|CJz{C[l~B[|nA_ExnAgGds@wGxd@}G~f@mDvSkDpTsArIuNd~@cGxi@sHxcAy@bWcAfl@y@|m@aBhz@sAbp@[hNIbDqCncBuDn|CaA~pAEvJn@bnApAtaA`@dZfErr@xDrh@`Du@|EiEp@cEfBcF^|EsAzIaFbFcFnBdEbi@h@~GpFf@n@hA^rCnBb[qALkHj@NdKFhGkAvc@e@fFuB`LiAjG_Phw@q@fDwIrb@Ev@dCdJlBdCnC~@dFDwB~AbCdGfE`J}B~Km@lD?lArAdFcEdHoDzGyFrJpXlw@rCOpCIbA`@dAdA|CrJvBlBtB@~D{AjB]~A^dBdDeAdAuGdFzElOte@b{AhAlF~@hEdQzk@zGpV`BhK|@|HdArGlBhGmAlAiMdH`EfYjInObG|E~K|EfGrB`P~D_IxD_HdBeErBn@pn@KfKPpFl@xAbBjBnC~Vl@pFdG|b@iFbBzNjcApZjiBzd@vmCvL~s@tHiCdFh]pBnKpAlI`S|iAbBzJhIoDpL~r@jXuJvDvKqEzDkBp@pCpKyPlKkHbEyHdFlDtV~DjUbDvRsEpDeBoJeCoN[dQsAfMuDpImH`GiE`Dqf@zv@}a@vq@iDlMib@br@oRvYyIrNi[vg@cC|DqDvPoS~dCgLre@mJ|RkEjHkIpKuJ|HkOfJse@bXg^|Qy^~ZiH`JeC`DeNhYw@~AkGdS{Gt]mGtr@gGbr@wAlh@mBdgAa@vUqD|oA{K~zCcLfxAaBrX`NbEvMlRwMmRaNcEGnA_@dMCnB?hU@fJTfL^bJfFSbC_EcC~DfJa@gJ`@gFR\\|Q^zSR`KYz[Izc@CdJK|[C~Mg@~N_@fN}@bQ}Ktt@aBvKyiFy}JgP|Uqg@ds@mD|D_yAhaByB`GgB|HaAtF[dH?hFH|HjAxGxBxG`CvDnXp^`PaX~HcJrp@_p@",
                costing=stadiamaps.MapMatchCostingModel.PEDESTRIAN,
                units=stadiamaps.DistanceUnit.MI,
            )
            res = api_instance.trace_attributes(req)
            self.assertEqual(req.id, res.id)
            self.assertEqual("miles", res.units)
            self.assertGreaterEqual(len(res.admins), 1)
            self.assertGreater(len(res.edges), 1)
            self.assertGreater(len(res.matched_points), 1)
            self.assertGreater(len(res.shape), 1)
