# inda_hr.model.job_ad_job_title_details.JobAdJobTitleDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Weight** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | 
**[TextPositions](#TextPositions)** | list, tuple,  | tuple,  |  | [optional] 
**RawValue** | str,  | str,  |  | [optional] 
**[RawValues](#RawValues)** | list, tuple,  | tuple,  |  | [optional] 
**IsValidated** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**EntityType** | str,  | str,  |  | [optional] 
**ProficiencyLevel** | str,  | str,  |  | [optional] 
**Category** | str,  | str,  |  | [optional] 
**Code** | [**JobAdJobTitleCode**](JobAdJobTitleCode.md) | [**JobAdJobTitleCode**](JobAdJobTitleCode.md) |  | [optional] 

# TextPositions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TextPosition**](TextPosition.md) | [**TextPosition**](TextPosition.md) | [**TextPosition**](TextPosition.md) |  | 

# RawValues

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TextDetails**](TextDetails.md) | [**TextDetails**](TextDetails.md) | [**TextDetails**](TextDetails.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)
