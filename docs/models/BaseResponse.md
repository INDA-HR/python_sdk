# inda_hr.model.base_response.BaseResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Count** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**[Prices](#Prices)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**[Detail](#Detail)** | list, tuple,  | tuple,  |  | [optional] 

# Prices

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | decimal.Decimal, int, float,  | decimal.Decimal,  | any string name can be used but the value must be the correct type | [optional] 

# Detail

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**HistoryDetail**](HistoryDetail.md) | [**HistoryDetail**](HistoryDetail.md) | [**HistoryDetail**](HistoryDetail.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

