# stadiamaps.model.routing_waypoint.RoutingWaypoint

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[SimpleRoutingWaypoint](SimpleRoutingWaypoint.md) | [**SimpleRoutingWaypoint**](SimpleRoutingWaypoint.md) | [**SimpleRoutingWaypoint**](SimpleRoutingWaypoint.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**heading** | decimal.Decimal, int,  | decimal.Decimal,  | The preferred direction of travel when starting the route, in integer clockwise degrees from north. North is 0, south is 180, east is 90, and west is 270. | [optional] 
**heading_tolerance** | decimal.Decimal, int,  | decimal.Decimal,  | The tolerance (in degrees) determining whether a street is considered the same direction. | [optional] if omitted the server will use the default value of 60
**minimum_reachability** | decimal.Decimal, int,  | decimal.Decimal,  | The minimum number of nodes that must be reachable for a given edge to consider that edge as belonging to a connected region. If a candidate edge has fewer connections, it will be considered a disconnected island. | [optional] if omitted the server will use the default value of 50
**radius** | decimal.Decimal, int,  | decimal.Decimal,  | The distance (in meters) to look for candidate edges around the location for purposes of snapping locations to the route graph. If there are no candidates within this distance, the closest candidate within a reasonable search distance will be used. This is subject to clamping by internal limits. | [optional] if omitted the server will use the default value of 0
**rank_candidates** | bool,  | BoolClass,  | If true, candidates will be ranked according to their distance from the target location as well as other factors. If false, candidates will only be ranked using their distance from the target. | [optional] if omitted the server will use the default value of True
**preferred_side** | str,  | str,  | If the location is not offset from the road centerline or is closest to an intersection, this option has no effect. Otherwise, the preferred side of street is used to determine whether or not the location should be visited from the same, opposite or either side of the road with respect to the side of the road the given locale drives on. | [optional] must be one of ["same", "opposite", "either", ] 
**node_snap_tolerance** | decimal.Decimal, int,  | decimal.Decimal,  | During edge correlation this is the tolerance (in meters) used to determine whether or not to snap to the intersection rather than along the street, if the snap location is within this distance from the intersection, the intersection is used instead. | [optional] if omitted the server will use the default value of 5
**street_side_tolerance** | decimal.Decimal, int,  | decimal.Decimal,  | A tolerance in meters from the edge centerline used for determining the side of the street that the location is on. If the distance to the centerline is less than this tolerance, no side will be inferred. Otherwise, the left or right side will be selected depending on the direction of travel. | [optional] if omitted the server will use the default value of 5
**street_side_max_distance** | decimal.Decimal, int,  | decimal.Decimal,  | A tolerance in meters from the edge centerline used for determining the side of the street that the location is on. If the distance to the centerline is greater than this tolerance, no side will be inferred. Otherwise, the left or right side will be selected depending on the direction of travel. | [optional] if omitted the server will use the default value of 1000
**[search_filter](#search_filter)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# search_filter

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**exclude_tunnel** | bool,  | BoolClass,  | Excludes roads marked as tunnels | [optional] if omitted the server will use the default value of False
**exclude_bridge** | bool,  | BoolClass,  | Excludes roads marked as bridges | [optional] if omitted the server will use the default value of False
**exclude_ramp** | bool,  | BoolClass,  | Excludes roads marked as ramps | [optional] if omitted the server will use the default value of False
**exclude_closures** | bool,  | BoolClass,  | Excludes roads marked as closed | [optional] if omitted the server will use the default value of True
**[min_road_class](#min_road_class)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The lowest road class allowed | [optional] if omitted the server will use the default value of service_other
**[max_road_class](#max_road_class)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The highest road class allowed | [optional] if omitted the server will use the default value of motorway
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# min_road_class

The lowest road class allowed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The lowest road class allowed | if omitted the server will use the default value of service_other

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RoadClass](RoadClass.md) | [**RoadClass**](RoadClass.md) | [**RoadClass**](RoadClass.md) |  | 

# max_road_class

The highest road class allowed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The highest road class allowed | if omitted the server will use the default value of motorway

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RoadClass](RoadClass.md) | [**RoadClass**](RoadClass.md) | [**RoadClass**](RoadClass.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

