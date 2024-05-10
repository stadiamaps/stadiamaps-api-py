# EdgeSign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exit_number** | **List[str]** |  | [optional] 
**exit_branch** | **List[str]** |  | [optional] 
**exit_toward** | **List[str]** |  | [optional] 
**exit_name** | **List[str]** |  | [optional] 

## Example

```python
from stadiamaps.models.edge_sign import EdgeSign

# TODO update the JSON string below
json = "{}"
# create an instance of EdgeSign from a JSON string
edge_sign_instance = EdgeSign.from_json(json)
# print the JSON string representation of the object
print(EdgeSign.to_json())

# convert the object into a dict
edge_sign_dict = edge_sign_instance.to_dict()
# create an instance of EdgeSign from a dict
edge_sign_from_dict = EdgeSign.from_dict(edge_sign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


