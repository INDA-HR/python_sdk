# inda_hr.model.indexed_document_failures_response.IndexedDocumentFailuresResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Indexname** | str,  | str,  |  | 
**Count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**[Failures](#Failures)** | list, tuple,  | tuple,  |  | 
**DocType** | str,  | str,  |  | [optional] 
**ImportID** | str,  | str,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# Failures

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IndexedDocumentFailure**](IndexedDocumentFailure.md) | [**IndexedDocumentFailure**](IndexedDocumentFailure.md) | [**IndexedDocumentFailure**](IndexedDocumentFailure.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

