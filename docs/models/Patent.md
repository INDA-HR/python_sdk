# inda_hr.model.patent.Patent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**PatentTitle** | [**Title**](Title.md) | [**Title**](Title.md) |  | [optional] 
**PatentID** | [**Text**](Text.md) | [**Text**](Text.md) |  | [optional] 
**PatentStatus** | [**PatentStatus**](PatentStatus.md) | [**PatentStatus**](PatentStatus.md) |  | [optional] 
**Description** | [**Description**](Description.md) | [**Description**](Description.md) |  | [optional] 
**[InventorNames](#InventorNames)** | list, tuple,  | tuple,  | List of the patent inventors. | [optional] 
**IssuingAuthority** | [**Organization**](Organization.md) | [**Organization**](Organization.md) |  | [optional] 

# InventorNames

List of the patent inventors.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of the patent inventors. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResumePersonNamePersonName**](ResumePersonNamePersonName.md) | [**ResumePersonNamePersonName**](ResumePersonNamePersonName.md) | [**ResumePersonNamePersonName**](ResumePersonNamePersonName.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

