# IsochroneResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**features** | [**List[IsochroneFeature]**](IsochroneFeature.md) |  | 
**type** | **str** |  | 

## Example

```python
from stadiamaps.models.isochrone_response import IsochroneResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IsochroneResponse from a JSON string
isochrone_response_instance = IsochroneResponse.from_json(json)
# print the JSON string representation of the object
print IsochroneResponse.to_json()

# convert the object into a dict
isochrone_response_dict = isochrone_response_instance.to_dict()
# create an instance of IsochroneResponse from a dict
isochrone_response_form_dict = isochrone_response.from_dict(isochrone_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


