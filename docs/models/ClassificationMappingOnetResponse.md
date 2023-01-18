# inda_hr.model.classification_mapping_onet_response.ClassificationMappingOnetResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**O*NETCode** | str,  | str,  | This field shows the O*NET occupation code. | 
**O*NETOccupation** | str,  | str,  | This field shows the O*NET occupation. | [optional] 
**[MappingESCO](#MappingESCO)** | list, tuple,  | tuple,  | This field shows the mapping to ESCO. | [optional] 
**[MappingISCO](#MappingISCO)** | list, tuple,  | tuple,  | This field shows the mapping to ISCO. | [optional] 
**[MappingISTAT](#MappingISTAT)** | list, tuple,  | tuple,  | This field shows the mapping to ISTAT. | [optional] 

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

