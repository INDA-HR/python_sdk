# inda_hr.model.esco_jobtitle_response.EscoJobtitleResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Hits** | decimal.Decimal, int,  | decimal.Decimal,  | Number of elements in a search query. | [optional] if omitted the server will use the default value of 0
**[ESCOClassification](#ESCOClassification)** | list, tuple,  | tuple,  | This field shows the result of the ESCO classification. | [optional] 

# ESCOClassification

This field shows the result of the ESCO classification.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This field shows the result of the ESCO classification. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OptionalEscoOccupationMatch**](OptionalEscoOccupationMatch.md) | [**OptionalEscoOccupationMatch**](OptionalEscoOccupationMatch.md) | [**OptionalEscoOccupationMatch**](OptionalEscoOccupationMatch.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

