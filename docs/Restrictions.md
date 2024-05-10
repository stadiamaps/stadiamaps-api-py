# Restrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**golf_cart** | **bool** |  | [optional] 
**truck** | **bool** |  | [optional] 
**pedestrian** | **bool** |  | [optional] 
**wheelchair** | **bool** |  | [optional] 
**taxi** | **bool** |  | [optional] 
**hov** | **bool** |  | [optional] 
**emergency** | **bool** |  | [optional] 
**motorcycle** | **bool** |  | [optional] 
**car** | **bool** |  | [optional] 
**moped** | **bool** |  | [optional] 
**bus** | **bool** |  | [optional] 
**bicycle** | **bool** |  | [optional] 

## Example

```python
from stadiamaps.models.restrictions import Restrictions

# TODO update the JSON string below
json = "{}"
# create an instance of Restrictions from a JSON string
restrictions_instance = Restrictions.from_json(json)
# print the JSON string representation of the object
print(Restrictions.to_json())

# convert the object into a dict
restrictions_dict = restrictions_instance.to_dict()
# create an instance of Restrictions from a dict
restrictions_from_dict = Restrictions.from_dict(restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


