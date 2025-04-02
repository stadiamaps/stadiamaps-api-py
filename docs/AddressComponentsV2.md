# AddressComponentsV2

Structured address components.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cross_street** | **str** | The cross street address component (rarely used). | [optional] 
**number** | **str** | The house / building number.  Note that, despite the name, this is not strictly numeric. Values such as 30-1 and 11A may be valid building/house numbers in some areas. | [optional] 
**postal_code** | **str** | The postal code. | [optional] 
**street** | **str** | The street component of the address. | [optional] 
**unit** | **str** | The unit number (where available). | [optional] 

## Example

```python
from stadiamaps.models.address_components_v2 import AddressComponentsV2

# TODO update the JSON string below
json = "{}"
# create an instance of AddressComponentsV2 from a JSON string
address_components_v2_instance = AddressComponentsV2.from_json(json)
# print the JSON string representation of the object
print(AddressComponentsV2.to_json())

# convert the object into a dict
address_components_v2_dict = address_components_v2_instance.to_dict()
# create an instance of AddressComponentsV2 from a dict
address_components_v2_from_dict = AddressComponentsV2.from_dict(address_components_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


