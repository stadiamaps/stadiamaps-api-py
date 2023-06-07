# stadiamaps.model.use_hills_costing_option.UseHillsCostingOption

A measure of willingness to take tackle hills. Values near 0 attempt to avoid hills and steeper grades even if it means a longer route, and values near 1 indicates that the user does not fear them. Note that as some routes may be impossible without hills, 0 does not guarantee avoidance of them.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | A measure of willingness to take tackle hills. Values near 0 attempt to avoid hills and steeper grades even if it means a longer route, and values near 1 indicates that the user does not fear them. Note that as some routes may be impossible without hills, 0 does not guarantee avoidance of them. | if omitted the server will use the default value of 0.5value must be a 64 bit float

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

