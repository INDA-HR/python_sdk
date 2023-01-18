# inda_hr.model.docs_search_query.DocsSearchQuery

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[QueryTerms](#QueryTerms)** | list, tuple,  | tuple,  | List of terms with which the query is performed.Each term is composed by a *term*, its *language* and a *weight*representing the relevance the associated term should have. | 
**QueryFilters** | [**QueryFilters**](QueryFilters.md) | [**QueryFilters**](QueryFilters.md) |  | [optional] 

# QueryTerms

List of terms with which the query is performed.Each term is composed by a *term*, its *language* and a *weight*representing the relevance the associated term should have.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of terms with which the query is performed.Each term is composed by a *term*, its *language* and a *weight*representing the relevance the associated term should have. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WeightedQueryTerm**](WeightedQueryTerm.md) | [**WeightedQueryTerm**](WeightedQueryTerm.md) | [**WeightedQueryTerm**](WeightedQueryTerm.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

