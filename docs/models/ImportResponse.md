# inda_hr.model.import_response.ImportResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[Resumes](#Resumes)** | list, tuple,  | tuple,  |  | 
**Stats** | [**UploadStats**](UploadStats.md) | [**UploadStats**](UploadStats.md) |  | 
**ImportID** | str,  | str,  |  | 
**[Errors](#Errors)** | list, tuple,  | tuple,  |  | [optional] 

# Resumes

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ImportItemResponse**](ImportItemResponse.md) | [**ImportItemResponse**](ImportItemResponse.md) | [**ImportItemResponse**](ImportItemResponse.md) |  | 

# Errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ImportErrorResponse**](ImportErrorResponse.md) | [**ImportErrorResponse**](ImportErrorResponse.md) | [**ImportErrorResponse**](ImportErrorResponse.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

