# IsochroneProperties


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fill_color** | **str** |  | [optional] 
**opacity** | **float** |  | [optional] 
**fill** | **str** |  | [optional] 
**fill_opacity** | **float** |  | [optional] 
**color** | **str** |  | [optional] 
**contour** | **float** |  | [optional] 
**metric** | **str** |  | [optional] 

## Example

```python
from stadiamaps.models.isochrone_properties import IsochroneProperties

# TODO update the JSON string below
json = "{}"
# create an instance of IsochroneProperties from a JSON string
isochrone_properties_instance = IsochroneProperties.from_json(json)
# print the JSON string representation of the object
print(IsochroneProperties.to_json())

# convert the object into a dict
isochrone_properties_dict = isochrone_properties_instance.to_dict()
# create an instance of IsochroneProperties from a dict
isochrone_properties_form_dict = isochrone_properties.from_dict(isochrone_properties_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


