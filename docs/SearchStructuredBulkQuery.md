# SearchStructuredBulkQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** |  | [optional] 
**query** | [**SearchStructuredQuery**](SearchStructuredQuery.md) |  | [optional] 

## Example

```python
from stadiamaps.models.search_structured_bulk_query import SearchStructuredBulkQuery

# TODO update the JSON string below
json = "{}"
# create an instance of SearchStructuredBulkQuery from a JSON string
search_structured_bulk_query_instance = SearchStructuredBulkQuery.from_json(json)
# print the JSON string representation of the object
print(SearchStructuredBulkQuery.to_json())

# convert the object into a dict
search_structured_bulk_query_dict = search_structured_bulk_query_instance.to_dict()
# create an instance of SearchStructuredBulkQuery from a dict
search_structured_bulk_query_from_dict = SearchStructuredBulkQuery.from_dict(search_structured_bulk_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


