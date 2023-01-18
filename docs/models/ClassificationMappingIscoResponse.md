# inda_hr.model.classification_mapping_isco_response.ClassificationMappingIscoResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ISCOCode** | str,  | str,  | This field shows the ISCO occupation code. | 
**ISCOOccupation** | str,  | str,  | This field shows the ISCO occupation. | [optional] 
**[MappingO*NET](#MappingO*NET)** | list, tuple,  | tuple,  | This field shows the mapping to O*NET. | [optional] 
**[MappingESCO](#MappingESCO)** | list, tuple,  | tuple,  | This field shows the mapping to ESCO. | [optional] 
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

