# BulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** |  | [optional] 
**query** | [**BulkRequestQuery**](BulkRequestQuery.md) |  | [optional] 

## Example

```python
from stadiamaps.models.bulk_request import BulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkRequest from a JSON string
bulk_request_instance = BulkRequest.from_json(json)
# print the JSON string representation of the object
print(BulkRequest.to_json())

# convert the object into a dict
bulk_request_dict = bulk_request_instance.to_dict()
# create an instance of BulkRequest from a dict
bulk_request_from_dict = BulkRequest.from_dict(bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


