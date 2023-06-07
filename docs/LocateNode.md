# LocateNode


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** | The latitude of a point in the shape. | 
**lon** | **float** | The longitude of a point in the shape. | 
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
from stadiamaps.models.locate_node import LocateNode

# TODO update the JSON string below
json = "{}"
# create an instance of LocateNode from a JSON string
locate_node_instance = LocateNode.from_json(json)
# print the JSON string representation of the object
print LocateNode.to_json()

# convert the object into a dict
locate_node_dict = locate_node_instance.to_dict()
# create an instance of LocateNode from a dict
locate_node_form_dict = locate_node.from_dict(locate_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


