# IndexCreditsInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indexname** | **str** |  | 
**suite** | [**SuiteResponse**](SuiteResponse.md) |  | [optional] 
**history** | **bool, date, datetime, dict, float, int, list, str, none_type** | This object contains the history data according to the requested filters. If *Detail* has been set *true* in the request, an array of objects is returned. Each object is composed by the following fields, unless some aggregations have been requested: *APICall* (string), *Datetime* (string), *StatusCode* (int) and *Advanced* (boolean). If aggregation is performed, data is organized in nested objects (see the example below, where a *GroupBy* with *[\&quot;advanced\&quot;, \&quot;api_calls\&quot;]* has been performed). Note that the *property name&amp;ast;* shown in the response examples represents the API call name used to aggregate data if *api_calls* is set in the *GroupBy* field. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


