# inda_hr.model.entity_input.EntityInput

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**EntityType** | str,  | str,  |  | 
**InputString** | str,  | str,  |  | 
**[AllowedOutputs](#AllowedOutputs)** | list, tuple,  | tuple,  |  | 
**InputLanguage** | str,  | str,  |  | [optional] if omitted the server will use the default value of "it"
**OutputLanguage** | str,  | str,  |  | [optional] if omitted the server will use the default value of "it"
**Severity** | decimal.Decimal, int, float,  | decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0.5

# AllowedOutputs

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AllowedOutput**](AllowedOutput.md) | [**AllowedOutput**](AllowedOutput.md) | [**AllowedOutput**](AllowedOutput.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

