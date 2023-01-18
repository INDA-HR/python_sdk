# inda_hr.model.university_public_metadata.UniversityPublicMetadata

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**LastModified** | str, datetime,  | str,  | Date of last update. Format: &#x27;YYYY-MM-DD[T]HH:MM[:SS[.ffffff]][Z or [±]HH[:]MM]]]&#x27;. | value must conform to RFC-3339 date-time
**CreationDate** | str, datetime,  | str,  | Date of creation. Format: &#x27;YYYY-MM-DD[T]HH:MM[:SS[.ffffff]][Z or [±]HH[:]MM]]]&#x27;. | value must conform to RFC-3339 date-time
**Exists** | bool,  | BoolClass,  | Whether the University still exists today or not. | [optional] if omitted the server will use the default value of True

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

