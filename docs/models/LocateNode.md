# stadiamaps.model.locate_node.LocateNode

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[Coordinate](Coordinate.md) | [**Coordinate**](Coordinate.md) | [**Coordinate**](Coordinate.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**traffic_signal** | bool,  | BoolClass,  |  | [optional] 
**type** | [**NodeType**](NodeType.md) | [**NodeType**](NodeType.md) |  | [optional] 
**node_id** | [**NodeId**](NodeId.md) | [**NodeId**](NodeId.md) |  | [optional] 
**access** | [**Access**](Access.md) | [**Access**](Access.md) |  | [optional] 
**edge_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**administrative** | [**Administrative**](Administrative.md) | [**Administrative**](Administrative.md) |  | [optional] 
**intersection_type** | str,  | str,  |  | [optional] must be one of ["regular", "false", "dead-end", "fork", ] 
**density** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**local_edge_count** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**mode_change** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

