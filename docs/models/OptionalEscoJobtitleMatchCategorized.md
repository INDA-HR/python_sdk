# inda_hr.model.optional_esco_jobtitle_match_categorized.OptionalEscoJobtitleMatchCategorized

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Code** | str,  | str,  | This field shows the ESCO code. | [optional] 
**PreferredLabel** | str,  | str,  | This field shows the preferred label according with the ESCO classification. | [optional] 
**Description** | str,  | str,  | This field shows the description according with the ESCO classification. | [optional] 
**Language** | str,  | str,  | This field shows the language. | [optional] 
**Score** | decimal.Decimal, int, float,  | decimal.Decimal,  | This field shows the similarity score calculate by the model. | [optional] 
**OccupationHierarchy** | [**OccupationHierarchy**](OccupationHierarchy.md) | [**OccupationHierarchy**](OccupationHierarchy.md) |  | [optional] 
**[Industries](#Industries)** | list, tuple,  | tuple,  | This field shows the top three industries related with the occupation. | [optional] 
**[JobFunctions](#JobFunctions)** | list, tuple,  | tuple,  | This field shows the top three job functions related with the occupation. | [optional] 

# Industries

This field shows the top three industries related with the occupation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This field shows the top three industries related with the occupation. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Industries**](Industries.md) | [**Industries**](Industries.md) | [**Industries**](Industries.md) |  | 

# JobFunctions

This field shows the top three job functions related with the occupation.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This field shows the top three job functions related with the occupation. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Jobfunctions**](Jobfunctions.md) | [**Jobfunctions**](Jobfunctions.md) | [**Jobfunctions**](Jobfunctions.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

