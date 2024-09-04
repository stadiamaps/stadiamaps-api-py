# OsrmAnnotation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | **List[float]** | The distance, in meters, between each pair of coordinates. | [optional] 
**duration** | **List[float]** | The duration between each pair of coordinates, in seconds. | [optional] 
**weight** | **List[int]** |  | [optional] 
**speed** | **List[float]** | The estimated speed of travel between each pair of coordinates in meters/sec. | [optional] 
**maxspeed** | [**List[OsrmSpeedLimit]**](OsrmSpeedLimit.md) |  | [optional] 

## Example

```python
from stadiamaps.models.osrm_annotation import OsrmAnnotation

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmAnnotation from a JSON string
osrm_annotation_instance = OsrmAnnotation.from_json(json)
# print the JSON string representation of the object
print(OsrmAnnotation.to_json())

# convert the object into a dict
osrm_annotation_dict = osrm_annotation_instance.to_dict()
# create an instance of OsrmAnnotation from a dict
osrm_annotation_from_dict = OsrmAnnotation.from_dict(osrm_annotation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


