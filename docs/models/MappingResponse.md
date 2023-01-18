# inda_hr.model.mapping_response.MappingResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Indexname** | str,  | str,  |  | 
**Custom** | bool,  | BoolClass,  | Whether custom fields exist or not. | 
**DocType** | str,  | str,  |  | [optional] 
**[CustomFields](#CustomFields)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Each item of its key-value pairs is the dot-notation path of a custom field and the relative type. | [optional] 
**Multiplier** | decimal.Decimal, int, float,  | decimal.Decimal,  | How much the added custom fields will impact on pricing. | [optional] 

# CustomFields

Each item of its key-value pairs is the dot-notation path of a custom field and the relative type.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Each item of its key-value pairs is the dot-notation path of a custom field and the relative type. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

