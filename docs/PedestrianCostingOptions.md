# PedestrianCostingOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**walking_speed** | **int** | Walking speed in kph. | [optional] 
**walkway_factor** | **float** | A factor that multiplies the cost when walkways are encountered. | [optional] [default to 1]
**sidewalk_factor** | **float** | A factor that multiplies the cost when sidewalks are encountered. | [optional] [default to 1]
**alley_factor** | **float** | A factor that multiplies the cost when alleys are encountered. | [optional] [default to 2]
**driveway_factor** | **float** | A factor that multiplies the cost when driveways are encountered. | [optional] [default to 5]
**step_penalty** | **int** | A penalty (in seconds) added to each transition onto a path with steps or stairs. | [optional] [default to 30]
**use_ferry** | **float** | A measure of willingness to take ferries. Values near 0 attempt to avoid ferries, and values near 1 will favour them. Note that as some routes may be impossible without ferries, 0 does not guarantee avoidance of them. | [optional] [default to 0.5]
**use_living_streets** | **float** | A measure of willingness to take living streets. Values near 0 attempt to avoid them, and values near 1 will favour them. Note that as some routes may be impossible without living streets, 0 does not guarantee avoidance of them. The default value is 0 for trucks; 0.1 for other motor vehicles; 0.5 for bicycles; and 0.6 for pedestrians. | [optional] 
**use_tracks** | **float** | A measure of willingness to take track roads. Values near 0 attempt to avoid them, and values near 1 will favour them. Note that as some routes may be impossible without track roads, 0 does not guarantee avoidance of them. The default value is 0 for automobiles, busses, and trucks; and 0.5 for all other costing modes. | [optional] 
**use_hills** | **float** | A measure of willingness to take tackle hills. Values near 0 attempt to avoid hills and steeper grades even if it means a longer route, and values near 1 indicates that the user does not fear them. Note that as some routes may be impossible without hills, 0 does not guarantee avoidance of them. | [optional] [default to 0.5]
**use_lit** | **float** | A measure of preference for streets that are lit. 0 indicates indifference toward lit streets, and 1 indicates that unlit streets should be avoided. Note that even with values near 1, there is no guarantee that the returned route will include lit segments. | [optional] [default to 0]
**service_penalty** | **int** | A penalty applied to transitions to service roads. This penalty can be used to reduce the likelihood of suggesting a route with service roads unless absolutely necessary. The default penalty is 15 for cars, busses, motor scooters, and motorcycles; and zero for others. | [optional] 
**service_factor** | **float** | A factor that multiplies the cost when service roads are encountered. The default is 1.2 for cars and busses, and 1 for trucks, motor scooters, and motorcycles. | [optional] [default to 1]
**max_hiking_difficulty** | **int** | The maximum difficulty of hiking trails allowed. This corresponds to the OSM &#x60;sac_scale&#x60;. | [optional] [default to 1]
**bss_rent_cost** | **int** | The estimated cost (in seconds) to rent a bicycle from a sharing station in &#x60;bikeshare&#x60; mode. | [optional] [default to 120]
**bss_rent_penalty** | **int** | A penalty (in seconds) to rent a bicycle in &#x60;bikeshare&#x60; mode. | [optional] [default to 0]

## Example

```python
from stadiamaps.models.pedestrian_costing_options import PedestrianCostingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PedestrianCostingOptions from a JSON string
pedestrian_costing_options_instance = PedestrianCostingOptions.from_json(json)
# print the JSON string representation of the object
print(PedestrianCostingOptions.to_json())

# convert the object into a dict
pedestrian_costing_options_dict = pedestrian_costing_options_instance.to_dict()
# create an instance of PedestrianCostingOptions from a dict
pedestrian_costing_options_form_dict = pedestrian_costing_options.from_dict(pedestrian_costing_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


