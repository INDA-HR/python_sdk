# inda_hr.model.upskilling_request.UpskillingRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**OriginOccupation** | str,  | str,  | Origin occupation for which transition recommendations will be generated. | 
**[Skills](#Skills)** | list, tuple,  | tuple,  | List of skills to combine with the origin occupation skillset. | 
**TransitionType** | str,  | str,  | Transition type. | must be one of ["viable", "desirable", "safe_desirable", "strictly_safe_desirable", ] 

# Skills

List of skills to combine with the origin occupation skillset.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of skills to combine with the origin occupation skillset. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

