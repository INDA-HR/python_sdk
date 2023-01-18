# inda_hr.model.section_details.SectionDetails

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Language** | str,  | str,  | Language of this section. If missing, the language of the job title is assumed to correspond to the language of the job advert. | [optional] must be one of ["de", "pt", "fr", "es", "en", "it", ] 
**Weight** | decimal.Decimal, int, float,  | decimal.Decimal,  | Weight of the section. | [optional] if omitted the server will use the default value of 0.8

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

