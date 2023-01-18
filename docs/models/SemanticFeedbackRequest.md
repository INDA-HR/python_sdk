# inda_hr.model.semantic_feedback_request.SemanticFeedbackRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Feedback** | decimal.Decimal, int,  | decimal.Decimal,  | The allowed values are &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;0&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;1&lt;/code&gt;, and &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;-1&lt;/code&gt;. &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;0&lt;/code&gt; indicates that the rank is agreeable (i.e., it is not far from the rank expected by the user); &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;1&lt;/code&gt; indicates that the rank should have been significantly larger; &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;-1&lt;/code&gt; indicates that the rank should have been significantly smaller. | must be one of [-1, 0, 1, ] 
**[Terms](#Terms)** | list, tuple,  | tuple,  | List of Query Terms and Weights used to perform the Semantic Search. | 
**Rank** | decimal.Decimal, int,  | decimal.Decimal,  | Rank of the item in the Semantic Search output. | 
**[Evidence](#Evidence)** | list, tuple,  | tuple,  | Optional. *Terms* field from the [Search Resumes Evidence](https://api.inda.ai/hr/docs/v2/#operation/search_resumes_evidence__POST) response. | [optional] 

# Terms

List of Query Terms and Weights used to perform the Semantic Search.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Query Terms and Weights used to perform the Semantic Search. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WeightedQueryTerm**](WeightedQueryTerm.md) | [**WeightedQueryTerm**](WeightedQueryTerm.md) | [**WeightedQueryTerm**](WeightedQueryTerm.md) |  | 

# Evidence

Optional. *Terms* field from the [Search Resumes Evidence](https://api.inda.ai/hr/docs/v2/#operation/search_resumes_evidence__POST) response.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Optional. *Terms* field from the [Search Resumes Evidence](https://api.inda.ai/hr/docs/v2/#operation/search_resumes_evidence__POST) response. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SearchTerm**](SearchTerm.md) | [**SearchTerm**](SearchTerm.md) | [**SearchTerm**](SearchTerm.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

