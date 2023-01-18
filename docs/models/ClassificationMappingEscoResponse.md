# inda_hr.model.classification_mapping_esco_response.ClassificationMappingEscoResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ESCOCode** | str,  | str,  | This field shows the ESCO occupation code. | 
**ESCOOccupation** | str,  | str,  | This field shows the ESCO occupation. | [optional] 
**[MappingO*NET](#MappingO*NET)** | list, tuple,  | tuple,  | This field shows the mapping to O*NET. | [optional] 
**[MappingISCO](#MappingISCO)** | list, tuple,  | tuple,  | This field shows the mapping to ISCO. | [optional] 
**[MappingISTAT](#MappingISTAT)** | list, tuple,  | tuple,  | This field shows the mapping to ISTAT. | [optional] 

# MappingO*NET

This field shows the mapping to O*NET.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This field shows the mapping to O*NET. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OnetMapping**](OnetMapping.md) | [**OnetMapping**](OnetMapping.md) | [**OnetMapping**](OnetMapping.md) |  | 

# MappingISCO

This field shows the mapping to ISCO.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This field shows the mapping to ISCO. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IscoMapping**](IscoMapping.md) | [**IscoMapping**](IscoMapping.md) | [**IscoMapping**](IscoMapping.md) |  | 

# MappingISTAT

This field shows the mapping to ISTAT.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This field shows the mapping to ISTAT. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**IstatMapping**](IstatMapping.md) | [**IstatMapping**](IstatMapping.md) | [**IstatMapping**](IstatMapping.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

