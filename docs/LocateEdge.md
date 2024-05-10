# LocateEdge


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_id** | [**NodeId**](NodeId.md) |  | [optional] 
**way_id** | **int** | The OSM way ID associated with this edge (absent in verbose response; see the edge info). | [optional] 
**correlated_lat** | **float** |  | 
**correlated_lon** | **float** |  | 
**percent_along** | **float** |  | 
**side_of_street** | **str** |  | 
**linear_reference** | **str** | A base64-encoded [OpenLR location reference](https://www.openlr-association.com/fileadmin/user_upload/openlr-whitepaper_v1.5.pdf), for a graph edge of the road network matched by the query. | [optional] 
**outbound_reach** | **int** |  | [optional] 
**heading** | **float** |  | [optional] 
**inbound_reach** | **int** |  | [optional] 
**distance** | **float** |  | [optional] 
**predicted_speeds** | **List[int]** | Predicted speed information based on historical data. If available, this will include 2016 entries. Each entry represents 5 minutes, where the first entry represents midnight on Monday, the second entry represents 00:05 on Monday, etc. | [optional] 
**edge_info** | [**LocateEdgeInfo**](LocateEdgeInfo.md) |  | [optional] 
**edge** | [**LocateDetailedEdge**](LocateDetailedEdge.md) |  | [optional] 
**warnings** | **List[str]** |  | [optional] 

## Example

```python
from stadiamaps.models.locate_edge import LocateEdge

# TODO update the JSON string below
json = "{}"
# create an instance of LocateEdge from a JSON string
locate_edge_instance = LocateEdge.from_json(json)
# print the JSON string representation of the object
print(LocateEdge.to_json())

# convert the object into a dict
locate_edge_dict = locate_edge_instance.to_dict()
# create an instance of LocateEdge from a dict
locate_edge_from_dict = LocateEdge.from_dict(locate_edge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


