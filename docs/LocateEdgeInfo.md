# LocateEdgeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mean_elevation** | **float** | The mean elevation, in meters, relative to sea level. | [optional] 
**shape** | **str** | An encoded polyline (https://developers.google.com/maps/documentation/utilities/polylinealgorithm). Note that the polyline is always encoded with 6 digits of precision, whereas most implementations default to 5. | [optional] 
**names** | **List[str]** | A list of names that the edge goes by. | [optional] 
**bike_network** | [**BikeNetwork**](BikeNetwork.md) |  | [optional] 
**way_id** | **int** |  | [optional] 

## Example

```python
from stadiamaps.models.locate_edge_info import LocateEdgeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LocateEdgeInfo from a JSON string
locate_edge_info_instance = LocateEdgeInfo.from_json(json)
# print the JSON string representation of the object
print LocateEdgeInfo.to_json()

# convert the object into a dict
locate_edge_info_dict = locate_edge_info_instance.to_dict()
# create an instance of LocateEdgeInfo from a dict
locate_edge_info_form_dict = locate_edge_info.from_dict(locate_edge_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


