# OsrmLane


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indications** | **List[str]** | A list of indication (e.g. marking on the road) specifying the turn lane. A road can have multiple indications (e.g. an arrow pointing straight and left). | 
**valid** | **bool** | True if the lane is a valid choice for the current maneuver. | 

## Example

```python
from stadiamaps.models.osrm_lane import OsrmLane

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmLane from a JSON string
osrm_lane_instance = OsrmLane.from_json(json)
# print the JSON string representation of the object
print(OsrmLane.to_json())

# convert the object into a dict
osrm_lane_dict = osrm_lane_instance.to_dict()
# create an instance of OsrmLane from a dict
osrm_lane_from_dict = OsrmLane.from_dict(osrm_lane_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


