# LocateNodeAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**traffic_signal** | **bool** |  | [optional] 
**type** | [**NodeType**](NodeType.md) |  | [optional] 
**node_id** | [**NodeId**](NodeId.md) |  | [optional] 
**access** | [**Access**](Access.md) |  | [optional] 
**edge_count** | **int** |  | [optional] 
**administrative** | [**Administrative**](Administrative.md) |  | [optional] 
**intersection_type** | **str** |  | [optional] 
**density** | **int** |  | [optional] 
**local_edge_count** | **int** |  | [optional] 
**mode_change** | **bool** |  | [optional] 

## Example

```python
from stadiamaps.models.locate_node_all_of import LocateNodeAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of LocateNodeAllOf from a JSON string
locate_node_all_of_instance = LocateNodeAllOf.from_json(json)
# print the JSON string representation of the object
print LocateNodeAllOf.to_json()

# convert the object into a dict
locate_node_all_of_dict = locate_node_all_of_instance.to_dict()
# create an instance of LocateNodeAllOf from a dict
locate_node_all_of_form_dict = locate_node_all_of.from_dict(locate_node_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


