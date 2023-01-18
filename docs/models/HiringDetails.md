# inda_hr.model.hiring_details.HiringDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ApplicationDate** | str, date,  | str,  | The application date keeps track of the first time the candidate applies to a Job Advertisement. It is a replica of the hiring pipeline step corresponding to the status &#x27;APPLIED&#x27;. Format: &#x27;YYYY-MM-DD&#x27;. | value must conform to RFC-3339 full-date YYYY-MM-DD
**HiringDate** | str, date,  | str,  | The hiring date keeps track of the date in which the candidate has been hired. It is a replica of the hiring pipeline step corresponding to the status &#x27;HIRED&#x27;. Format: &#x27;YYYY-MM-DD&#x27;. | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**[HiringPipeline](#HiringPipeline)** | list, tuple,  | tuple,  | The hiring pipeline is meant to register the candidate history through the hiring process, thus registering both forward and backward steps in any order. | [optional] 

# HiringPipeline

The hiring pipeline is meant to register the candidate history through the hiring process, thus registering both forward and backward steps in any order.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | The hiring pipeline is meant to register the candidate history through the hiring process, thus registering both forward and backward steps in any order. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**HiringPipelineStage**](HiringPipelineStage.md) | [**HiringPipelineStage**](HiringPipelineStage.md) | [**HiringPipelineStage**](HiringPipelineStage.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

