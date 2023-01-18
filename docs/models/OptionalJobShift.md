# inda_hr.model.optional_job_shift.OptionalJobShift

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Details** | [**BoolBaseModel**](BoolBaseModel.md) | [**BoolBaseModel**](BoolBaseModel.md) |  | [optional] 
**Type** | [**OptionalJobShiftType**](OptionalJobShiftType.md) | [**OptionalJobShiftType**](OptionalJobShiftType.md) |  | [optional] 
**[Frequency](#Frequency)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The percentage or a range of percentages of the time of the week in which the job is shift based. | [optional] 

# Frequency

The percentage or a range of percentages of the time of the week in which the job is shift based.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The percentage or a range of percentages of the time of the week in which the job is shift based. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ValueModelFloat](ValueModelFloat.md) | [**ValueModelFloat**](ValueModelFloat.md) | [**ValueModelFloat**](ValueModelFloat.md) |  | 
[RangeFloat](RangeFloat.md) | [**RangeFloat**](RangeFloat.md) | [**RangeFloat**](RangeFloat.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

