# OsrmSpeedLimit

The speed limit between the pair of coordinates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**speed** | **int** |  | [optional] 
**unit** | **str** | The unit of measure for the speed. Always included if speed is present. | [optional] 
**unknown** | **bool** | True if the speed limit is not known. | [optional] 
**var_none** | **bool** | True if there is no explicit speed limit (ex: some Autobahn sections) | [optional] 

## Example

```python
from stadiamaps.models.osrm_speed_limit import OsrmSpeedLimit

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmSpeedLimit from a JSON string
osrm_speed_limit_instance = OsrmSpeedLimit.from_json(json)
# print the JSON string representation of the object
print(OsrmSpeedLimit.to_json())

# convert the object into a dict
osrm_speed_limit_dict = osrm_speed_limit_instance.to_dict()
# create an instance of OsrmSpeedLimit from a dict
osrm_speed_limit_from_dict = OsrmSpeedLimit.from_dict(osrm_speed_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


