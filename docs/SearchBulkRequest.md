# SearchBulkRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** |  | [optional] 
**query** | [**SearchStructuredQuery**](SearchStructuredQuery.md) |  | [optional] 

## Example

```python
from stadiamaps.models.search_bulk_request import SearchBulkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchBulkRequest from a JSON string
search_bulk_request_instance = SearchBulkRequest.from_json(json)
# print the JSON string representation of the object
print(SearchBulkRequest.to_json())

# convert the object into a dict
search_bulk_request_dict = search_bulk_request_instance.to_dict()
# create an instance of SearchBulkRequest from a dict
search_bulk_request_from_dict = SearchBulkRequest.from_dict(search_bulk_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


