# LocateObject


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**input_lat** | **float** | The input (searched) latitude. | [optional] 
**input_lon** | **float** | The input (searched) longitude. | [optional] 
**nodes** | [**List[LocateNode]**](LocateNode.md) |  | [optional] 
**edges** | [**List[LocateEdge]**](LocateEdge.md) |  | [optional] 

## Example

```python
from stadiamaps.models.locate_object import LocateObject

# TODO update the JSON string below
json = "{}"
# create an instance of LocateObject from a JSON string
locate_object_instance = LocateObject.from_json(json)
# print the JSON string representation of the object
print(LocateObject.to_json())

# convert the object into a dict
locate_object_dict = locate_object_instance.to_dict()
# create an instance of LocateObject from a dict
locate_object_form_dict = locate_object.from_dict(locate_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


