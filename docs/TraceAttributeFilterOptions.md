# TraceAttributeFilterOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[TraceAttributeKey]**](TraceAttributeKey.md) |  | 
**action** | **str** | Determines whether the list of attributes will be used as a whitelist or a blacklist. | 

## Example

```python
from stadiamaps.models.trace_attribute_filter_options import TraceAttributeFilterOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TraceAttributeFilterOptions from a JSON string
trace_attribute_filter_options_instance = TraceAttributeFilterOptions.from_json(json)
# print the JSON string representation of the object
print TraceAttributeFilterOptions.to_json()

# convert the object into a dict
trace_attribute_filter_options_dict = trace_attribute_filter_options_instance.to_dict()
# create an instance of TraceAttributeFilterOptions from a dict
trace_attribute_filter_options_form_dict = trace_attribute_filter_options.from_dict(trace_attribute_filter_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


