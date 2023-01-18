# inda_hr.model.feedback_work_experience.FeedbackWorkExperience

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Seniority** | [**BaseSeniority**](BaseSeniority.md) | [**BaseSeniority**](BaseSeniority.md) |  | [optional] 
**Duration** | [**BaseDuration**](BaseDuration.md) | [**BaseDuration**](BaseDuration.md) |  | [optional] 
**PositionTitle** | [**FeedbackJobTitle**](FeedbackJobTitle.md) | [**FeedbackJobTitle**](FeedbackJobTitle.md) |  | [optional] 
**Description** | [**Description**](Description.md) | [**Description**](Description.md) |  | [optional] 
**StartDate** | [**Date**](Date.md) | [**Date**](Date.md) |  | [optional] 
**EndDate** | [**Date**](Date.md) | [**Date**](Date.md) |  | [optional] 
**Ongoing** | [**Ongoing**](Ongoing.md) | [**Ongoing**](Ongoing.md) |  | [optional] 
**Location** | [**ResumeLocationsLocation**](ResumeLocationsLocation.md) | [**ResumeLocationsLocation**](ResumeLocationsLocation.md) |  | [optional] 
**RemoteWorking** | [**RemoteWorking**](RemoteWorking.md) | [**RemoteWorking**](RemoteWorking.md) |  | [optional] 
**Employer** | [**Organization**](Organization.md) | [**Organization**](Organization.md) |  | [optional] 
**[Industries](#Industries)** | list, tuple,  | tuple,  | Industries related to the experience. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details. | [optional] 
**[Skills](#Skills)** | list, tuple,  | tuple,  | Skills related to the experience. | [optional] 
**ID** | str,  | str,  | Unique identifier for the current experience. | [optional] 

# Industries

Industries related to the experience. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Industries related to the experience. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResumeWorkExperiencesIndustry**](ResumeWorkExperiencesIndustry.md) | [**ResumeWorkExperiencesIndustry**](ResumeWorkExperiencesIndustry.md) | [**ResumeWorkExperiencesIndustry**](ResumeWorkExperiencesIndustry.md) |  | 

# Skills

Skills related to the experience.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Skills related to the experience. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OptionalResumeSkill**](OptionalResumeSkill.md) | [**OptionalResumeSkill**](OptionalResumeSkill.md) | [**OptionalResumeSkill**](OptionalResumeSkill.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

