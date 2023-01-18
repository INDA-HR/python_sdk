# inda_hr.model.transition_recommendation_value.TransitionRecommendationValue

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**DestinationLabel** | str,  | str,  | This field shows the destination label according with the ESCO classification. | [optional] 
**DestinationCode** | str,  | str,  | This field shows the destination ESCO code. | [optional] 
**Similarity** | decimal.Decimal, int, float,  | decimal.Decimal,  | This field shows the similarity between the origin and destination occupation. | [optional] 
**IsDesirable** | str,  | str,  | This field shows if the destination occupation is desirable. Where desirable means that offers comparable or higher levels of pay. | [optional] 
**IsSafeDesirable** | str,  | str,  | This field shows if the destination occupation is safe desirable. Where safe desirable means that it is desirable and will likely reduce a worker&#x27;s exposure to automation risk. | [optional] 
**IsStrictlySafeDesirable** | str,  | str,  | This field shows if the destination occupation is strictly safe desirable. Where strictly safe desirable means that it is safe desirable and with an higher prevalence of bottleneck tasks.  | [optional] 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

