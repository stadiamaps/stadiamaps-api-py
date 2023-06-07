# TraceAttributesResponseAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**units** | [**ValhallaLongUnits**](ValhallaLongUnits.md) |  | [optional] 
**alternate_paths** | [**List[TraceAttributesBaseResponse]**](TraceAttributesBaseResponse.md) | Alternate paths, if any, that were not classified as the best match. | [optional] 

## Example

```python
from stadiamaps.models.trace_attributes_response_all_of import TraceAttributesResponseAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of TraceAttributesResponseAllOf from a JSON string
trace_attributes_response_all_of_instance = TraceAttributesResponseAllOf.from_json(json)
# print the JSON string representation of the object
print TraceAttributesResponseAllOf.to_json()

# convert the object into a dict
trace_attributes_response_all_of_dict = trace_attributes_response_all_of_instance.to_dict()
# create an instance of TraceAttributesResponseAllOf from a dict
trace_attributes_response_all_of_form_dict = trace_attributes_response_all_of.from_dict(trace_attributes_response_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


