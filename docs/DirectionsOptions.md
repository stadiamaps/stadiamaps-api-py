# DirectionsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**DistanceUnit**](DistanceUnit.md) |  | [optional] 
**language** | [**ValhallaLanguages**](ValhallaLanguages.md) |  | [optional] 
**directions_type** | **str** | The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter. | [optional] [default to 'instructions']

## Example

```python
from stadiamaps.models.directions_options import DirectionsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DirectionsOptions from a JSON string
directions_options_instance = DirectionsOptions.from_json(json)
# print the JSON string representation of the object
print(DirectionsOptions.to_json())

# convert the object into a dict
directions_options_dict = directions_options_instance.to_dict()
# create an instance of DirectionsOptions from a dict
directions_options_from_dict = DirectionsOptions.from_dict(directions_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


