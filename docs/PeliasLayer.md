# PeliasLayer

Our database is organized into several layers (in the GIS sense of the term) as follows:  - `venue`: Points of interest, businesses, and things with walls - `address`: Places with a street address - `street`: Streets, roads, highways - `county`: Places that issue passports, nations, nation-states - `macroregion`: A related group of regions (mostly in Europe) - `region`: The first administrative division within a country (usually states and provinces) - `macrocounty`: A related group of counties (mostly in Europe) - `county`: Official governmental areas; usually bigger than a locality, but almost always smaller than a region - `locality`: Towns, hamlets, cities, etc. - `localadmin`: Local administrative boundaries - `borough`: Local administrative boundaries within cities (not widely used, but present in places such as NYC and Mexico City) - `neighbourhood`: Social communities and neighborhoods (note the British spelling in the API!) - `postalcode`: Postal codes used by mail services (note: not used for reverse geocoding) - `coarse`: An alias for simultaneously using all administrative layers (everything except `venue` and `address`) - `marinearea`: Places with fishes and boats. - `ocean`: A really big marine area. 

## Enum

* `VENUE` (value: `'venue'`)

* `ADDRESS` (value: `'address'`)

* `STREET` (value: `'street'`)

* `COUNTRY` (value: `'country'`)

* `MACROREGION` (value: `'macroregion'`)

* `REGION` (value: `'region'`)

* `MACROCOUNTY` (value: `'macrocounty'`)

* `COUNTY` (value: `'county'`)

* `LOCALITY` (value: `'locality'`)

* `LOCALADMIN` (value: `'localadmin'`)

* `BOROUGH` (value: `'borough'`)

* `NEIGHBOURHOOD` (value: `'neighbourhood'`)

* `POSTALCODE` (value: `'postalcode'`)

* `COARSE` (value: `'coarse'`)

* `DEPENDENCY` (value: `'dependency'`)

* `MACROHOOD` (value: `'macrohood'`)

* `MARINEAREA` (value: `'marinearea'`)

* `DISPUTED` (value: `'disputed'`)

* `EMPIRE` (value: `'empire'`)

* `CONTINENT` (value: `'continent'`)

* `OCEAN` (value: `'ocean'`)

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


