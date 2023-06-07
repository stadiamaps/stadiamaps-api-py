# stadiamaps.model.costing_model.CostingModel

Costing models for determining the most optimal route to take. Note that bikeshare and motorcycle are still in beta. While Valhalla supports multimodal routing, we do not currently process transit data and have excluded it from the list. See https://valhalla.readthedocs.io/en/latest/api/turn-by-turn/api-reference/#costing-models for detailed descriptions of each model.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Costing models for determining the most optimal route to take. Note that bikeshare and motorcycle are still in beta. While Valhalla supports multimodal routing, we do not currently process transit data and have excluded it from the list. See https://valhalla.readthedocs.io/en/latest/api/turn-by-turn/api-reference/#costing-models for detailed descriptions of each model. | must be one of ["auto", "bus", "taxi", "truck", "bicycle", "bikeshare", "motor_scooter", "motorcycle", "pedestrian", ] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

