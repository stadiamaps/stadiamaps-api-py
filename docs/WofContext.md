# WofContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**borough** | [**WofContextComponent**](WofContextComponent.md) |  | [optional] 
**continent** | [**WofContextComponent**](WofContextComponent.md) |  | [optional] 
**country** | [**WofContextComponent**](WofContextComponent.md) |  | [optional] 
**county** | [**WofContextComponent**](WofContextComponent.md) |  | [optional] 
**dependency** | [**WofContextComponent**](WofContextComponent.md) |  | [optional] 
**localadmin** | [**WofContextComponent**](WofContextComponent.md) |  | [optional] 
**locality** | [**WofContextComponent**](WofContextComponent.md) |  | [optional] 
**macrocounty** | [**WofContextComponent**](WofContextComponent.md) |  | [optional] 
**macroregion** | [**WofContextComponent**](WofContextComponent.md) |  | [optional] 
**neighbourhood** | [**WofContextComponent**](WofContextComponent.md) |  | [optional] 
**region** | [**WofContextComponent**](WofContextComponent.md) |  | [optional] 

## Example

```python
from stadiamaps.models.wof_context import WofContext

# TODO update the JSON string below
json = "{}"
# create an instance of WofContext from a JSON string
wof_context_instance = WofContext.from_json(json)
# print the JSON string representation of the object
print(WofContext.to_json())

# convert the object into a dict
wof_context_dict = wof_context_instance.to_dict()
# create an instance of WofContext from a dict
wof_context_from_dict = WofContext.from_dict(wof_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


