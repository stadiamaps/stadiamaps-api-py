# BulkSearchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | 
**response** | [**GeocodeResponse**](GeocodeResponse.md) |  | [optional] 
**msg** | **str** | An error message describing what went wrong (if the status is not 200). | [optional] 

## Example

```python
from stadiamaps.models.bulk_search_response import BulkSearchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSearchResponse from a JSON string
bulk_search_response_instance = BulkSearchResponse.from_json(json)
# print the JSON string representation of the object
print(BulkSearchResponse.to_json())

# convert the object into a dict
bulk_search_response_dict = bulk_search_response_instance.to_dict()
# create an instance of BulkSearchResponse from a dict
bulk_search_response_from_dict = BulkSearchResponse.from_dict(bulk_search_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


