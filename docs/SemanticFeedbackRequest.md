# SemanticFeedbackRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**terms** | [**[WeightedQueryTerm]**](WeightedQueryTerm.md) | List of Query Terms and Weights used to perform the Semantic Search. | 
**rank** | **int** | Rank of the item in the Semantic Search output. | 
**feedback** | **int** | The allowed values are &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;0&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;1&lt;/code&gt;, and &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;-1&lt;/code&gt;. &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;0&lt;/code&gt; indicates that the rank is agreeable (i.e., it is not far from the rank expected by the user); &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;1&lt;/code&gt; indicates that the rank should have been significantly larger; &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;-1&lt;/code&gt; indicates that the rank should have been significantly smaller. | 
**evidence** | [**[SearchTerm]**](SearchTerm.md) | Optional. *Terms* field from the [Search Resumes Evidence](https://api.inda.ai/hr/docs/v2/#operation/search_resumes_evidence__POST) response. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


