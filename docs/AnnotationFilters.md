# AnnotationFilters


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** |  | [optional] 
**attributes** | **List[str]** | A set of granular attributes to include between every pair of coordinates along the route. This can significantly increase the response size. | [optional] 

## Example

```python
from stadiamaps.models.annotation_filters import AnnotationFilters

# TODO update the JSON string below
json = "{}"
# create an instance of AnnotationFilters from a JSON string
annotation_filters_instance = AnnotationFilters.from_json(json)
# print the JSON string representation of the object
print(AnnotationFilters.to_json())

# convert the object into a dict
annotation_filters_dict = annotation_filters_instance.to_dict()
# create an instance of AnnotationFilters from a dict
annotation_filters_from_dict = AnnotationFilters.from_dict(annotation_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


