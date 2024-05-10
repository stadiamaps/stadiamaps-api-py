# NodeId


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**value** | **int** |  | [optional] 
**tile_id** | **int** |  | [optional] 
**level** | **int** |  | [optional] 

## Example

```python
from stadiamaps.models.node_id import NodeId

# TODO update the JSON string below
json = "{}"
# create an instance of NodeId from a JSON string
node_id_instance = NodeId.from_json(json)
# print the JSON string representation of the object
print(NodeId.to_json())

# convert the object into a dict
node_id_dict = node_id_instance.to_dict()
# create an instance of NodeId from a dict
node_id_from_dict = NodeId.from_dict(node_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


