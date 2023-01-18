# inda_hr.model.search_job_ad_match_response.SearchJobAdMatchResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[Out](#Out)** | list, tuple,  | tuple,  |  | 
**Total** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of elements in a certain index. | [optional] if omitted the server will use the default value of 0
**Hits** | decimal.Decimal, int,  | decimal.Decimal,  | Number of elements in a search query. | [optional] if omitted the server will use the default value of 0
**SearchID** | str,  | str,  | This ID is used in order to retrieve the result of a certain search query or scroll to the next search batch. | [optional] 

# Out

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SearchJobAdElement**](SearchJobAdElement.md) | [**SearchJobAdElement**](SearchJobAdElement.md) | [**SearchJobAdElement**](SearchJobAdElement.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

