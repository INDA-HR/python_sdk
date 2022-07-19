# HiringDetails


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**application_date** | **date** | The application date keeps track of the first time the candidate applies to a Job Advertisement. It is a replica of the hiring pipeline step corresponding to the status &#39;APPLIED&#39;. Format: &#39;YYYY-MM-DD&#39;. | 
**hiring_date** | **date** | The hiring date keeps track of the date in which the candidate has been hired. It is a replica of the hiring pipeline step corresponding to the status &#39;HIRED&#39;. Format: &#39;YYYY-MM-DD&#39;. | [optional] 
**hiring_pipeline** | [**[HiringPipelineStage]**](HiringPipelineStage.md) | The hiring pipeline is meant to register the candidate history through the hiring process, thus registering both forward and backward steps in any order. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


