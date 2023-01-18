# inda_hr.model.weighted_query_term.WeightedQueryTerm

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Term** | str,  | str,  | The desired term(s) to search for. | 
**Language** | str,  | str,  | The language this term is expressed in. | [optional] must be one of ["it", "en", "fr", "de", "pt", "es", ] 
**Weight** | decimal.Decimal, int, float,  | decimal.Decimal,  | Optional. Must be between &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;0&lt;/code&gt; (excluded) and &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;1&lt;/code&gt;. | [optional] if omitted the server will use the default value of 1.0

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

