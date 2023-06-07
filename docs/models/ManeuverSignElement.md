# stadiamaps.model.maneuver_sign_element.ManeuverSignElement

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**text** | str,  | str,  | The interchange sign text (varies based on the context; see the &#x60;maneuverSign&#x60; schema). | 
**is_route_number** | bool,  | BoolClass,  | True if the sign is a route number. | [optional] 
**consecutive_count** | decimal.Decimal, int,  | decimal.Decimal,  | The frequency of this sign element within a set a consecutive signs. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

