# MatrixRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**units** | [**DistanceUnit**](DistanceUnit.md) |  | [optional] 
**language** | [**ValhallaLanguages**](ValhallaLanguages.md) |  | [optional] 
**directions_type** | **str** | The level of directional narrative to include. Locations and times will always be returned, but narrative generation verbosity can be controlled with this parameter. | [optional] [default to 'instructions']
**id** | **str** | An identifier to disambiguate requests (echoed by the server). | [optional] 
**sources** | [**List[Coordinate]**](Coordinate.md) | The list of starting locations | 
**targets** | [**List[Coordinate]**](Coordinate.md) | The list of ending locations | 
**costing** | [**MatrixCostingModel**](MatrixCostingModel.md) |  | 
**costing_options** | [**CostingOptions**](CostingOptions.md) |  | [optional] 
**matrix_locations** | **int** | Only applicable to one-to-many or many-to-one requests. This defaults to all locations. When specified explicitly, this option allows a partial result to be returned. This is basically equivalent to \&quot;find the closest/best locations out of the full set.\&quot; This can have a dramatic improvement for large requests. | [optional] 

## Example

```python
from stadiamaps.models.matrix_request import MatrixRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatrixRequest from a JSON string
matrix_request_instance = MatrixRequest.from_json(json)
# print the JSON string representation of the object
print(MatrixRequest.to_json())

# convert the object into a dict
matrix_request_dict = matrix_request_instance.to_dict()
# create an instance of MatrixRequest from a dict
matrix_request_form_dict = matrix_request.from_dict(matrix_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


