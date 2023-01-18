# inda_hr.model.multi_entity_mapping.MultiEntityMapping

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[Errors](#Errors)** | list, tuple,  | tuple,  |  | 
**[Entities](#Entities)** | list, tuple,  | tuple,  |  | 
**Total** | decimal.Decimal, int,  | decimal.Decimal,  | Total number of elements in a certain index. | [optional] if omitted the server will use the default value of 0
**Hits** | decimal.Decimal, int,  | decimal.Decimal,  | Number of elements in a search query. | [optional] if omitted the server will use the default value of 0

# Entities

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IdEntityMapping**](IdEntityMapping.md) | [**IdEntityMapping**](IdEntityMapping.md) | [**IdEntityMapping**](IdEntityMapping.md) |  | 

# Errors

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IdEntityErrors**](IdEntityErrors.md) | [**IdEntityErrors**](IdEntityErrors.md) | [**IdEntityErrors**](IdEntityErrors.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

