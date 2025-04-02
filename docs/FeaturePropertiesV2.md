# FeaturePropertiesV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | **List[float]** |  | [optional] 
**geometry** | [**Point**](Point.md) |  | [optional] 
**properties** | [**FeaturePropertiesV2Properties**](FeaturePropertiesV2Properties.md) |  | 
**type** | **str** |  | [optional] 

## Example

```python
from stadiamaps.models.feature_properties_v2 import FeaturePropertiesV2

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturePropertiesV2 from a JSON string
feature_properties_v2_instance = FeaturePropertiesV2.from_json(json)
# print the JSON string representation of the object
print(FeaturePropertiesV2.to_json())

# convert the object into a dict
feature_properties_v2_dict = feature_properties_v2_instance.to_dict()
# create an instance of FeaturePropertiesV2 from a dict
feature_properties_v2_from_dict = FeaturePropertiesV2.from_dict(feature_properties_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


