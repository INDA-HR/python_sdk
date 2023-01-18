# inda_hr.model.upskilling.Upskilling

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ESCOClassification** | [**ESCOOccupationValue**](ESCOOccupationValue.md) | [**ESCOOccupationValue**](ESCOOccupationValue.md) |  | [optional] 
**[TransitionRecommendation](#TransitionRecommendation)** | list, tuple,  | tuple,  | This field shows the list of transition recommendations. | [optional] 
**[Skills](#Skills)** | list, tuple,  | tuple,  | This field shows the list of the combined skills according with the ESCO classification. | [optional] 

# TransitionRecommendation

This field shows the list of transition recommendations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This field shows the list of transition recommendations. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**TransitionRecommendationValue**](TransitionRecommendationValue.md) | [**TransitionRecommendationValue**](TransitionRecommendationValue.md) | [**TransitionRecommendationValue**](TransitionRecommendationValue.md) |  | 

# Skills

This field shows the list of the combined skills according with the ESCO classification.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | This field shows the list of the combined skills according with the ESCO classification. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SlimSkill**](SlimSkill.md) | [**SlimSkill**](SlimSkill.md) | [**SlimSkill**](SlimSkill.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

