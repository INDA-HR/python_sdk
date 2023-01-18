# inda_hr.model.duration_range_v10.DurationRangeV10

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Score** | decimal.Decimal, int, float,  | decimal.Decimal,  | Normalized score. Min Score is 0 and Max Score is 1. | 
**[Range](#Range)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 

# Range

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RangeModelInt](RangeModelInt.md) | [**RangeModelInt**](RangeModelInt.md) | [**RangeModelInt**](RangeModelInt.md) |  | 
[RangeModelGTEInt](RangeModelGTEInt.md) | [**RangeModelGTEInt**](RangeModelGTEInt.md) | [**RangeModelGTEInt**](RangeModelGTEInt.md) |  | 
[RangeModelLTEInt](RangeModelLTEInt.md) | [**RangeModelLTEInt**](RangeModelLTEInt.md) | [**RangeModelLTEInt**](RangeModelLTEInt.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

