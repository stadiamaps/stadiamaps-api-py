# IsochroneFeature


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**properties** | [**IsochroneProperties**](IsochroneProperties.md) |  | [optional] 
**geometry** | **Dict[str, object]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from stadiamaps.models.isochrone_feature import IsochroneFeature

# TODO update the JSON string below
json = "{}"
# create an instance of IsochroneFeature from a JSON string
isochrone_feature_instance = IsochroneFeature.from_json(json)
# print the JSON string representation of the object
print(IsochroneFeature.to_json())

# convert the object into a dict
isochrone_feature_dict = isochrone_feature_instance.to_dict()
# create an instance of IsochroneFeature from a dict
isochrone_feature_from_dict = IsochroneFeature.from_dict(isochrone_feature_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


