# stadiamaps.model.highway_classification.HighwayClassification

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**internal** | bool,  | BoolClass,  | Is the edge internal to an intersection? | [optional] 
**link** | bool,  | BoolClass,  | Is the edge a ramp or turn channel? | [optional] 
**surface** | str,  | str,  | A representation of the smoothness of the highway. This is used for costing and access checks based on the vehicle type. | [optional] must be one of ["paved_smooth", "paved", "paved_rough", "compacted", "dirt", "gravel", "path", "impassable", ] 
**use** | str,  | str,  |  | [optional] must be one of ["road", "ramp", "turn_channel", "track", "driveway", "alley", "parking_aisle", "emergency_access", "drive_through", "culdesac", "living_street", "service_road", "cycleway", "mountain_bike", "sidewalk", "footway", "elevator", "steps", "escalator", "path", "pedestrian", "bridleway", "pedestrian_crossing", "rest_area", "service_area", "other", "rail", "ferry", "rail-ferry", "bus", "egress_connection", "platform_connnection", "transit_connection", "construction", ] 
**classification** | str,  | str,  | The classification/importance of the road/path. Used for a variety of purposes including fallback speed estimation and access for certain vehicle types. | [optional] must be one of ["motorway", "trunk", "primary", "secondary", "tertiary", "unclassified", "residential", "service_other", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

