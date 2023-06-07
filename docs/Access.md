# Access


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**golf_cart** | **bool** |  | [optional] 
**wheelchair** | **bool** |  | [optional] 
**taxi** | **bool** |  | [optional] 
**hov** | **bool** |  | [optional] 
**truck** | **bool** |  | [optional] 
**emergency** | **bool** |  | [optional] 
**pedestrian** | **bool** |  | [optional] 
**car** | **bool** |  | [optional] 
**bus** | **bool** |  | [optional] 
**bicycle** | **bool** |  | [optional] 
**motorcycle** | **bool** |  | [optional] 
**moped** | **bool** |  | [optional] 

## Example

```python
from stadiamaps.models.access import Access

# TODO update the JSON string below
json = "{}"
# create an instance of Access from a JSON string
access_instance = Access.from_json(json)
# print the JSON string representation of the object
print Access.to_json()

# convert the object into a dict
access_dict = access_instance.to_dict()
# create an instance of Access from a dict
access_form_dict = access.from_dict(access_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


