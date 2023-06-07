# HighwayClassification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**internal** | **bool** | Is the edge internal to an intersection? | [optional] 
**link** | **bool** | Is the edge a ramp or turn channel? | [optional] 
**surface** | **str** | A representation of the smoothness of the highway. This is used for costing and access checks based on the vehicle type. | [optional] 
**use** | **str** |  | [optional] 
**classification** | **str** | The classification/importance of the road/path. Used for a variety of purposes including fallback speed estimation and access for certain vehicle types. | [optional] 

## Example

```python
from stadiamaps.models.highway_classification import HighwayClassification

# TODO update the JSON string below
json = "{}"
# create an instance of HighwayClassification from a JSON string
highway_classification_instance = HighwayClassification.from_json(json)
# print the JSON string representation of the object
print HighwayClassification.to_json()

# convert the object into a dict
highway_classification_dict = highway_classification_instance.to_dict()
# create an instance of HighwayClassification from a dict
highway_classification_form_dict = highway_classification.from_dict(highway_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


