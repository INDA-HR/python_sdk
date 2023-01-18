# inda_hr.model.optional_job_ad_language_details.OptionalJobAdLanguageDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[TextPositions](#TextPositions)** | list, tuple,  | tuple,  |  | [optional] 
**RawValue** | str,  | str,  |  | [optional] 
**[RawValues](#RawValues)** | list, tuple,  | tuple,  |  | [optional] 
**IsValidated** | bool,  | BoolClass,  |  | [optional] if omitted the server will use the default value of False
**EntityType** | str,  | str,  |  | [optional] 
**ProficiencyLevel** | str,  | str,  | A descriptive language proficiency level. E.g.: &#x27;Good&#x27;, &#x27;Excellent&#x27;. | [optional] 
**Category** | str,  | str,  |  | [optional] 
**Code** | [**JobAdLanguageCode**](JobAdLanguageCode.md) | [**JobAdLanguageCode**](JobAdLanguageCode.md) |  | [optional] 
**LanguageCode** | str,  | str,  | ISO 639 language code. | [optional] 
**ProficiencyLevelCode** | [**ProficiencyLevelCode**](ProficiencyLevelCode.md) | [**ProficiencyLevelCode**](ProficiencyLevelCode.md) |  | [optional] 

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

