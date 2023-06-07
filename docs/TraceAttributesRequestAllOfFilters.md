# TraceAttributesRequestAllOfFilters

If present, provides either a whitelist or a blacklist of keys to include/exclude in the response. This key is optional, and if omitted from the request, all available info will be returned.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[TraceAttributeKey]**](TraceAttributeKey.md) |  | 
**action** | **str** | Determines whether the list of attributes will be used as a whitelist or a blacklist. | 

## Example

```python
from stadiamaps.models.trace_attributes_request_all_of_filters import TraceAttributesRequestAllOfFilters

# TODO update the JSON string below
json = "{}"
# create an instance of TraceAttributesRequestAllOfFilters from a JSON string
trace_attributes_request_all_of_filters_instance = TraceAttributesRequestAllOfFilters.from_json(json)
# print the JSON string representation of the object
print TraceAttributesRequestAllOfFilters.to_json()

# convert the object into a dict
trace_attributes_request_all_of_filters_dict = trace_attributes_request_all_of_filters_instance.to_dict()
# create an instance of TraceAttributesRequestAllOfFilters from a dict
trace_attributes_request_all_of_filters_form_dict = trace_attributes_request_all_of_filters.from_dict(trace_attributes_request_all_of_filters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


