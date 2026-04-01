# CostingModel

A routing profile that determines which roads you can access, and how desirable they are based on the type of travel and other parameters. Profiles with a `_traffic` suffix use heuristically-selected traffic data sources to improve ETA and time-dependent route quality while balancing the credit cost. The `_traffic_premium` profiles leverage multiple types of data for maximum accuracy. Traffic-influenced profiles use the same costing options as their base profile (e.g., use the `auto` key in `costing_options` for `auto_traffic`).

## Enum

* `AUTO` (value: `'auto'`)

* `AUTO_TRAFFIC` (value: `'auto_traffic'`)

* `AUTO_TRAFFIC_PREMIUM` (value: `'auto_traffic_premium'`)

* `BUS` (value: `'bus'`)

* `BUS_TRAFFIC` (value: `'bus_traffic'`)

* `BUS_TRAFFIC_PREMIUM` (value: `'bus_traffic_premium'`)

* `TAXI` (value: `'taxi'`)

* `TAXI_TRAFFIC` (value: `'taxi_traffic'`)

* `TAXI_TRAFFIC_PREMIUM` (value: `'taxi_traffic_premium'`)

* `TRUCK` (value: `'truck'`)

* `TRUCK_TRAFFIC` (value: `'truck_traffic'`)

* `TRUCK_TRAFFIC_PREMIUM` (value: `'truck_traffic_premium'`)

* `BICYCLE` (value: `'bicycle'`)

* `BIKESHARE` (value: `'bikeshare'`)

* `MOTOR_SCOOTER` (value: `'motor_scooter'`)

* `MOTORCYCLE` (value: `'motorcycle'`)

* `PEDESTRIAN` (value: `'pedestrian'`)

* `LOW_SPEED_VEHICLE` (value: `'low_speed_vehicle'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


