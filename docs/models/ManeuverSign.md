# stadiamaps.model.maneuver_sign.ManeuverSign

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[exit_number_elements](#exit_number_elements)** | list, tuple,  | tuple,  | A list of exit number elements. This is typically just a single value. | [optional] 
**[exit_branch_elements](#exit_branch_elements)** | list, tuple,  | tuple,  | A list of exit branch elements. The text is a subsequent road name or route number after the sign. | [optional] 
**[exit_toward_elements](#exit_toward_elements)** | list, tuple,  | tuple,  | A list of exit name elements. The text is the interchange identifier (used more frequently outside the US). | [optional] 
**[exit_name_elements](#exit_name_elements)** | list, tuple,  | tuple,  | A list of exit name elements. The text is the location where the road ahead goes (typically a city, but occasionally a road name or route number). | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# exit_number_elements

A list of exit number elements. This is typically just a single value.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of exit number elements. This is typically just a single value. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ManeuverSignElement**](ManeuverSignElement.md) | [**ManeuverSignElement**](ManeuverSignElement.md) | [**ManeuverSignElement**](ManeuverSignElement.md) |  | 

# exit_branch_elements

A list of exit branch elements. The text is a subsequent road name or route number after the sign.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of exit branch elements. The text is a subsequent road name or route number after the sign. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ManeuverSignElement**](ManeuverSignElement.md) | [**ManeuverSignElement**](ManeuverSignElement.md) | [**ManeuverSignElement**](ManeuverSignElement.md) |  | 

# exit_toward_elements

A list of exit name elements. The text is the interchange identifier (used more frequently outside the US).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of exit name elements. The text is the interchange identifier (used more frequently outside the US). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ManeuverSignElement**](ManeuverSignElement.md) | [**ManeuverSignElement**](ManeuverSignElement.md) | [**ManeuverSignElement**](ManeuverSignElement.md) |  | 

# exit_name_elements

A list of exit name elements. The text is the location where the road ahead goes (typically a city, but occasionally a road name or route number).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of exit name elements. The text is the location where the road ahead goes (typically a city, but occasionally a road name or route number). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ManeuverSignElement**](ManeuverSignElement.md) | [**ManeuverSignElement**](ManeuverSignElement.md) | [**ManeuverSignElement**](ManeuverSignElement.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

