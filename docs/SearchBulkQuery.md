# SearchBulkQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** |  | [optional] 
**query** | [**SearchQuery**](SearchQuery.md) |  | [optional] 

## Example

```python
from stadiamaps.models.search_bulk_query import SearchBulkQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SearchBulkQuery from a JSON string
search_bulk_query_instance = SearchBulkQuery.from_json(json)
# print the JSON string representation of the object
print(SearchBulkQuery.to_json())

# convert the object into a dict
search_bulk_query_dict = search_bulk_query_instance.to_dict()
# create an instance of SearchBulkQuery from a dict
search_bulk_query_from_dict = SearchBulkQuery.from_dict(search_bulk_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


