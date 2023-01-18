# inda_hr.model.optional_esco_skill_match.OptionalEscoSkillMatch

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
**SkillType** | str,  | str,  | This field shows the skill type according with the ESCO classification. | [optional] 
**ReuseLevel** | str,  | str,  | This field shows the reuse level according with the ESCO classification. | [optional] 
**ConceptUri** | str,  | str,  | This field shows the URI according with the ESCO classification. | [optional] 
**[Occupations](#Occupations)** | list, tuple,  | tuple,  | This field shows the list of ESCO occupations. | [optional] 

# Occupations

This field shows the list of ESCO occupations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This field shows the list of ESCO occupations. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OptionalEscoOccupationSkill**](OptionalEscoOccupationSkill.md) | [**OptionalEscoOccupationSkill**](OptionalEscoOccupationSkill.md) | [**OptionalEscoOccupationSkill**](OptionalEscoOccupationSkill.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

