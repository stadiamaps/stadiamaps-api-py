# BikeNetwork


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mountain** | **bool** |  | [optional] 
**local** | **bool** |  | [optional] 
**regional** | **bool** |  | [optional] 
**national** | **bool** |  | [optional] 

## Example

```python
from stadiamaps.models.bike_network import BikeNetwork

# TODO update the JSON string below
json = "{}"
# create an instance of BikeNetwork from a JSON string
bike_network_instance = BikeNetwork.from_json(json)
# print the JSON string representation of the object
print(BikeNetwork.to_json())

# convert the object into a dict
bike_network_dict = bike_network_instance.to_dict()
# create an instance of BikeNetwork from a dict
bike_network_form_dict = bike_network.from_dict(bike_network_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


