# Administrative


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** | The ISO 3166-1 alpha-2 country code of the administrative region. | [optional] 
**country** | **str** | The full country name. | [optional] 
**iso_3166_2** | **str** | The ISO 3166-2 code identifying the principal subdivision (ex: provinces or states) within a country. | [optional] 
**state** | **str** | The full state or province name. | [optional] 

## Example

```python
from stadiamaps.models.administrative import Administrative

# TODO update the JSON string below
json = "{}"
# create an instance of Administrative from a JSON string
administrative_instance = Administrative.from_json(json)
# print the JSON string representation of the object
print(Administrative.to_json())

# convert the object into a dict
administrative_dict = administrative_instance.to_dict()
# create an instance of Administrative from a dict
administrative_form_dict = administrative.from_dict(administrative_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


