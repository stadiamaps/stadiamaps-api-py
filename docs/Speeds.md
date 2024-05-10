# Speeds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predicted** | **bool** | Does this edge have predicted (historical) speed records? | [optional] 
**constrained_flow** | **int** | Speed when there is no traffic, in kph. | [optional] 
**free_flow** | **int** | Speed when there is heavy traffic, in kph. | [optional] 
**type** | **str** | The type of speed which is used when setting default speeds. When &#x60;tagged&#x60;, the explicit &#x60;max_speed&#x60; tags from OpenStreetMap are being used. When &#x60;classified&#x60;, the values are being inferred from the highway classification. | [optional] 
**default** | **int** | The default speed used for calculations. NOTE: Values greater than 250 are used for special cases and should not be treated as literal. | [optional] 

## Example

```python
from stadiamaps.models.speeds import Speeds

# TODO update the JSON string below
json = "{}"
# create an instance of Speeds from a JSON string
speeds_instance = Speeds.from_json(json)
# print the JSON string representation of the object
print(Speeds.to_json())

# convert the object into a dict
speeds_dict = speeds_instance.to_dict()
# create an instance of Speeds from a dict
speeds_from_dict = Speeds.from_dict(speeds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


