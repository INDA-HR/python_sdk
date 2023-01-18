# inda_hr.model.job_ad_remote_working.JobAdRemoteWorking

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Type** | [**JobAdRemoteWorkingType**](JobAdRemoteWorkingType.md) | [**JobAdRemoteWorkingType**](JobAdRemoteWorkingType.md) |  | [optional] 
**[Frequency](#Frequency)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The percentage or a range of percentages of the time of the week in which the job is remote. | [optional] 

# Frequency

The percentage or a range of percentages of the time of the week in which the job is remote.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The percentage or a range of percentages of the time of the week in which the job is remote. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RemoteWorkingFrequencyValue](RemoteWorkingFrequencyValue.md) | [**RemoteWorkingFrequencyValue**](RemoteWorkingFrequencyValue.md) | [**RemoteWorkingFrequencyValue**](RemoteWorkingFrequencyValue.md) |  | 
[RemoteWorkingFrequencyRange](RemoteWorkingFrequencyRange.md) | [**RemoteWorkingFrequencyRange**](RemoteWorkingFrequencyRange.md) | [**RemoteWorkingFrequencyRange**](RemoteWorkingFrequencyRange.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

