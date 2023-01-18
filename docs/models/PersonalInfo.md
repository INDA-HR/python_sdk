# inda_hr.model.personal_info.PersonalInfo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**PersonName** | [**ResumePersonNamePersonName**](ResumePersonNamePersonName.md) | [**ResumePersonNamePersonName**](ResumePersonNamePersonName.md) |  | [optional] 
**Birthdate** | [**Date**](Date.md) | [**Date**](Date.md) |  | [optional] 
**Age** | [**Age**](Age.md) | [**Age**](Age.md) |  | [optional] 
**[Nationalities](#Nationalities)** | list, tuple,  | tuple,  | Person&#x27;s list of nationalities. | [optional] 
**[Citizenships](#Citizenships)** | list, tuple,  | tuple,  | Person&#x27;s list of citizenships. | [optional] 
**Gender** | [**Gender**](Gender.md) | [**Gender**](Gender.md) |  | [optional] 
**Disability** | [**Disability**](Disability.md) | [**Disability**](Disability.md) |  | [optional] 
**[ProtectedGroups](#ProtectedGroups)** | list, tuple,  | tuple,  | Protected groups to which the person belongs. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details. | [optional] 
**MaritalStatus** | [**MaritalStatus**](MaritalStatus.md) | [**MaritalStatus**](MaritalStatus.md) |  | [optional] 
**NumberOfChildren** | [**NumberOfChildren**](NumberOfChildren.md) | [**NumberOfChildren**](NumberOfChildren.md) |  | [optional] 

# Nationalities

Person's list of nationalities.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Person&#x27;s list of nationalities. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Nationality**](Nationality.md) | [**Nationality**](Nationality.md) | [**Nationality**](Nationality.md) |  | 

# Citizenships

Person's list of citizenships.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Person&#x27;s list of citizenships. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Citizenship**](Citizenship.md) | [**Citizenship**](Citizenship.md) | [**Citizenship**](Citizenship.md) |  | 

# ProtectedGroups

Protected groups to which the person belongs. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Protected groups to which the person belongs. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ProtectedGroup**](ProtectedGroup.md) | [**ProtectedGroup**](ProtectedGroup.md) | [**ProtectedGroup**](ProtectedGroup.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

