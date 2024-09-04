# OsrmVoiceInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance_along_geometry** | **float** | How far (in meters) from the upcoming maneuver the instruction should be announced. | 
**announcement** | **str** | The plain-text announcement. | 
**ssml_announcement** | **str** | The announcement in Speech Synthesis Markup Language (SSML). Supported TTS engines include Amazon Polly and Apple&#39;s AVSpeechSynthesizer. | [optional] 

## Example

```python
from stadiamaps.models.osrm_voice_instruction import OsrmVoiceInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of OsrmVoiceInstruction from a JSON string
osrm_voice_instruction_instance = OsrmVoiceInstruction.from_json(json)
# print the JSON string representation of the object
print(OsrmVoiceInstruction.to_json())

# convert the object into a dict
osrm_voice_instruction_dict = osrm_voice_instruction_instance.to_dict()
# create an instance of OsrmVoiceInstruction from a dict
osrm_voice_instruction_from_dict = OsrmVoiceInstruction.from_dict(osrm_voice_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


