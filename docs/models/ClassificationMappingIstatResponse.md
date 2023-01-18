# inda_hr.model.classification_mapping_istat_response.ClassificationMappingIstatResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ISTATCode** | str,  | str,  | This field shows the ISTAT occupation code. | 
**ISTATOccupation** | str,  | str,  | This field shows the ISTAT occupation. | [optional] 
**[MappingO*NET](#MappingO*NET)** | list, tuple,  | tuple,  | This field shows the mapping to O*NET. | [optional] 
**[MappingISCO](#MappingISCO)** | list, tuple,  | tuple,  | This field shows the mapping to ISCO. | [optional] 
**[MappingESCO](#MappingESCO)** | list, tuple,  | tuple,  | This field shows the mapping to ESCO. | [optional] 

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

# MappingESCO

This field shows the mapping to ESCO.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This field shows the mapping to ESCO. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EscoMapping**](EscoMapping.md) | [**EscoMapping**](EscoMapping.md) | [**EscoMapping**](EscoMapping.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

