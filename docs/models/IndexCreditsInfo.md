# inda_hr.model.index_credits_info.IndexCreditsInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Indexname** | str,  | str,  |  | 
**Suite** | [**SuiteResponse**](SuiteResponse.md) | [**SuiteResponse**](SuiteResponse.md) |  | [optional] 
**[History](#History)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This object contains the history data according to the requested filters. If *Detail* has been set *true* in the request, an array of objects is returned. Each object is composed by the following fields, unless some aggregations have been requested: *APICall* (string), *Datetime* (string), *StatusCode* (int) and *Advanced* (boolean). If aggregation is performed, data is organized in nested objects (see the example below, where a *GroupBy* with *[\&quot;advanced\&quot;, \&quot;api_calls\&quot;]* has been performed). Note that the *property name&amp;ast;* shown in the response examples represents the API call name used to aggregate data if *api_calls* is set in the *GroupBy* field. | [optional] if omitted the server will use the default value of {}

# History

This object contains the history data according to the requested filters. If *Detail* has been set *true* in the request, an array of objects is returned. Each object is composed by the following fields, unless some aggregations have been requested: *APICall* (string), *Datetime* (string), *StatusCode* (int) and *Advanced* (boolean). If aggregation is performed, data is organized in nested objects (see the example below, where a *GroupBy* with *[\"advanced\", \"api_calls\"]* has been performed). Note that the *property name&ast;* shown in the response examples represents the API call name used to aggregate data if *api_calls* is set in the *GroupBy* field.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | This object contains the history data according to the requested filters. If *Detail* has been set *true* in the request, an array of objects is returned. Each object is composed by the following fields, unless some aggregations have been requested: *APICall* (string), *Datetime* (string), *StatusCode* (int) and *Advanced* (boolean). If aggregation is performed, data is organized in nested objects (see the example below, where a *GroupBy* with *[\&quot;advanced\&quot;, \&quot;api_calls\&quot;]* has been performed). Note that the *property name&amp;ast;* shown in the response examples represents the API call name used to aggregate data if *api_calls* is set in the *GroupBy* field. | if omitted the server will use the default value of {}

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[BaseResponse](BaseResponse.md) | [**BaseResponse**](BaseResponse.md) | [**BaseResponse**](BaseResponse.md) |  | 
[any_of_1](#any_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[any_of_2](#any_of_2) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
[GroupByAdvanced](GroupByAdvanced.md) | [**GroupByAdvanced**](GroupByAdvanced.md) | [**GroupByAdvanced**](GroupByAdvanced.md) |  | 
[GroupByAdvancedAPICalls](GroupByAdvancedAPICalls.md) | [**GroupByAdvancedAPICalls**](GroupByAdvancedAPICalls.md) | [**GroupByAdvancedAPICalls**](GroupByAdvancedAPICalls.md) |  | 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**SlimBaseResponse**](SlimBaseResponse.md) | [**SlimBaseResponse**](SlimBaseResponse.md) | any string name can be used but the value must be the correct type | [optional] 

# any_of_2

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | [**GroupByAdvanced**](GroupByAdvanced.md) | [**GroupByAdvanced**](GroupByAdvanced.md) | any string name can be used but the value must be the correct type | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

