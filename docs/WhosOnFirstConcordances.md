# WhosOnFirstConcordances


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eurographics_gisco_id** | **str** |  | [optional] 
**faa_code** | **str** |  | [optional] 
**factual_id** | **str** |  | [optional] 
**fifa_id** | **str** |  | [optional] 
**fips_code** | **str** |  | [optional] 
**fr_gov_epci_code** | **int** | An Open Data France EPCI code. | [optional] 
**fra_insee_code** | **int** | Institut national de la statistique et des études économiques (Insee) code | [optional] 
**geonames_id** | **int** |  | [optional] 
**geoplanet_id** | **int** |  | [optional] 
**hasc_id** | **str** | A Statoids HASC ID. | [optional] 
**iata_code** | **str** |  | [optional] 
**icao_code** | **str** |  | [optional] 
**itu_id** | **str** |  | [optional] 
**karmashapes_id** | **str** |  | [optional] 
**natural_earth_id** | **int** |  | [optional] 
**nuts_2021_id** | **str** | A Eurostat NUTS 2021 ID | [optional] 
**quattroshapes_id** | **int** |  | [optional] 
**quattroshapes_pg_id** | **int** | A Quattroshapes Point Gazetteer ID. | [optional] 
**us_census_geo_id** | **int** |  | [optional] 
**wikidata_id** | **str** |  | [optional] 
**wikipedia_page** | **str** |  | [optional] 

## Example

```python
from stadiamaps.models.whos_on_first_concordances import WhosOnFirstConcordances

# TODO update the JSON string below
json = "{}"
# create an instance of WhosOnFirstConcordances from a JSON string
whos_on_first_concordances_instance = WhosOnFirstConcordances.from_json(json)
# print the JSON string representation of the object
print(WhosOnFirstConcordances.to_json())

# convert the object into a dict
whos_on_first_concordances_dict = whos_on_first_concordances_instance.to_dict()
# create an instance of WhosOnFirstConcordances from a dict
whos_on_first_concordances_from_dict = WhosOnFirstConcordances.from_dict(whos_on_first_concordances_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


