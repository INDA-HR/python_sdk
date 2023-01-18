# inda_hr.model.application_status_request.ApplicationStatusRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Status** | str,  | str,  | The status describes the hiring pipeline level. The statuses are: &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;APPLIED&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;SOURCED&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;SCREEN&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;INTERVIEW&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;EVALUATION&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;OFFER&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;HIRED&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;DISQUALIFIED&lt;/code&gt;. | must be one of ["APPLIED", "SOURCED", "SCREEN", "INTERVIEW", "EVALUATION", "OFFER", "HIRED", "DISQUALIFIED", ] 
**Date** | str, datetime,  | str,  | The date in which the status changed. Format: &#x27;YYYY-MM-DD&#x27; or &#x27;YYYY-MM-DD[T]HH:MM[:SS[.ffffff]][Z or [±]HH[:]MM]]]&#x27;. | value must conform to RFC-3339 date-time
**Description** | str,  | str,  | A brief description indicating the reason why the state has changed. E.g.: the status &#x27;DISQUALIFIED&#x27; could be used both to exclude candidates which are unsuitable or those who refused the job offer. | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

