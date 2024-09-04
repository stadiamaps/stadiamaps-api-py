# OsrmBaseApiResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | 
**message** | **str** |  | [optional] 
**data_version** | **str** |  | [optional] 

## Example

```python
from stadiamaps.models.osrm_base_api_response import OsrmBaseApiResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmBaseApiResponse from a JSON string
osrm_base_api_response_instance = OsrmBaseApiResponse.from_json(json)
# print the JSON string representation of the object
print(OsrmBaseApiResponse.to_json())

# convert the object into a dict
osrm_base_api_response_dict = osrm_base_api_response_instance.to_dict()
# create an instance of OsrmBaseApiResponse from a dict
osrm_base_api_response_from_dict = OsrmBaseApiResponse.from_dict(osrm_base_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


