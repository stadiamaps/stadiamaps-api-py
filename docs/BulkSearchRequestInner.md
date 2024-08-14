# BulkSearchRequestInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** |  | [optional] 
**query** | [**SearchStructuredQuery**](SearchStructuredQuery.md) |  | [optional] 

## Example

```python
from stadiamaps.models.bulk_search_request_inner import BulkSearchRequestInner

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSearchRequestInner from a JSON string
bulk_search_request_inner_instance = BulkSearchRequestInner.from_json(json)
# print the JSON string representation of the object
print(BulkSearchRequestInner.to_json())

# convert the object into a dict
bulk_search_request_inner_dict = bulk_search_request_inner_instance.to_dict()
# create an instance of BulkSearchRequestInner from a dict
bulk_search_request_inner_from_dict = BulkSearchRequestInner.from_dict(bulk_search_request_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


