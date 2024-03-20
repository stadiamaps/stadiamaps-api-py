# Contour


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time** | **float** | The time in minutes for the contour. Mutually exclusive of distance. | [optional] 
**distance** | **float** | The distance in km for the contour. Mutually exclusive of time. | [optional] 
**color** | **str** | The color for the output contour, specified as a hex value (without a leading &#x60;#&#x60;). If no color is specified, one will be assigned automatically. | [optional] 

## Example

```python
from stadiamaps.models.contour import Contour

# TODO update the JSON string below
json = "{}"
# create an instance of Contour from a JSON string
contour_instance = Contour.from_json(json)
# print the JSON string representation of the object
print(Contour.to_json())

# convert the object into a dict
contour_dict = contour_instance.to_dict()
# create an instance of Contour from a dict
contour_form_dict = contour.from_dict(contour_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


