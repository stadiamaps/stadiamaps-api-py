# stadiamaps.model.trace_attributes_base_response.TraceAttributesBaseResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[edges](#edges)** | list, tuple,  | tuple,  | The list of edges matched along the path. | [optional] 
**[admins](#admins)** | list, tuple,  | tuple,  | The set of administrative regions matched along the path. Rather than repeating this information for every end node, the admins in this list are referenced by index. | [optional] 
**[matched_points](#matched_points)** | list, tuple,  | tuple,  | List of match results when using the map_snap shape match algorithm. There is a one-to-one correspondence with the input set of latitude, longitude coordinates and this list of match results. | [optional] 
**osm_changeset** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**shape** | str,  | str,  | The encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm) of the matched path. | [optional] 
**confidence_score** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] value must be a 64 bit float
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# edges

The list of edges matched along the path.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The list of edges matched along the path. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TraceEdge**](TraceEdge.md) | [**TraceEdge**](TraceEdge.md) | [**TraceEdge**](TraceEdge.md) |  | 

# admins

The set of administrative regions matched along the path. Rather than repeating this information for every end node, the admins in this list are referenced by index.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The set of administrative regions matched along the path. Rather than repeating this information for every end node, the admins in this list are referenced by index. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AdminRegion**](AdminRegion.md) | [**AdminRegion**](AdminRegion.md) | [**AdminRegion**](AdminRegion.md) |  | 

# matched_points

List of match results when using the map_snap shape match algorithm. There is a one-to-one correspondence with the input set of latitude, longitude coordinates and this list of match results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of match results when using the map_snap shape match algorithm. There is a one-to-one correspondence with the input set of latitude, longitude coordinates and this list of match results. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MatchedPoint**](MatchedPoint.md) | [**MatchedPoint**](MatchedPoint.md) | [**MatchedPoint**](MatchedPoint.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

