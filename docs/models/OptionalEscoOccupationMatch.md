# inda_hr.model.optional_esco_occupation_match.OptionalEscoOccupationMatch

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Score** | decimal.Decimal, int, float,  | decimal.Decimal,  | This field shows the similarity score calculate by the model. | [optional] 
**ConceptType** | str,  | str,  | This field shows the concept type according with the ESCO classification. | [optional] 
**PreferredLabel** | str,  | str,  | This field shows the preferred label according with the ESCO classification. | [optional] 
**AltLabels** | str,  | str,  | This field shows the alternative labels according with the ESCO classification. | [optional] 
**Description** | str,  | str,  | This field shows the description according with the ESCO classification. | [optional] 
**Language** | str,  | str,  | This field shows the language. | [optional] 
**MatchDetails** | [**OptionalEscoMatchDetails**](OptionalEscoMatchDetails.md) | [**OptionalEscoMatchDetails**](OptionalEscoMatchDetails.md) |  | [optional] 
**ISCOGroup** | str,  | str,  | This field shows the ISCO group according with the ESCO classification. | [optional] 
**Code** | str,  | str,  | This field shows the ESCO occupation code according with the ESCO classification. | [optional] 
**[Skills](#Skills)** | list, tuple,  | tuple,  | This field shows the list of ESCO skills. | [optional] 

# Skills

This field shows the list of ESCO skills.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This field shows the list of ESCO skills. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OptionalEscoSkill**](OptionalEscoSkill.md) | [**OptionalEscoSkill**](OptionalEscoSkill.md) | [**OptionalEscoSkill**](OptionalEscoSkill.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

