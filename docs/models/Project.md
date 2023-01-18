# inda_hr.model.project.Project

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ProjectName** | [**BaseModelsName**](BaseModelsName.md) | [**BaseModelsName**](BaseModelsName.md) |  | [optional] 
**Description** | [**Description**](Description.md) | [**Description**](Description.md) |  | [optional] 
**[Roles](#Roles)** | list, tuple,  | tuple,  | Roles played in the project. | [optional] 
**[Keywords](#Keywords)** | list, tuple,  | tuple,  | Keywords describing the project. | [optional] 
**StartDate** | [**Date**](Date.md) | [**Date**](Date.md) |  | [optional] 
**EndDate** | [**Date**](Date.md) | [**Date**](Date.md) |  | [optional] 
**Ongoing** | [**Ongoing**](Ongoing.md) | [**Ongoing**](Ongoing.md) |  | [optional] 
**Link** | [**ResumeLinkLink**](ResumeLinkLink.md) | [**ResumeLinkLink**](ResumeLinkLink.md) |  | [optional] 

# Roles

Roles played in the project.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Roles played in the project. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Role**](Role.md) | [**Role**](Role.md) | [**Role**](Role.md) |  | 

# Keywords

Keywords describing the project.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Keywords describing the project. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Keyword**](Keyword.md) | [**Keyword**](Keyword.md) | [**Keyword**](Keyword.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

