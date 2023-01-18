# inda_hr.model.feedback_education_experience.FeedbackEducationExperience

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Duration** | [**BaseDuration**](BaseDuration.md) | [**BaseDuration**](BaseDuration.md) |  | [optional] 
**EducationTitle** | [**FeedbackEducationTitle**](FeedbackEducationTitle.md) | [**FeedbackEducationTitle**](FeedbackEducationTitle.md) |  | [optional] 
**FieldOfStudy** | [**FeedbackFieldOfStudy**](FeedbackFieldOfStudy.md) | [**FeedbackFieldOfStudy**](FeedbackFieldOfStudy.md) |  | [optional] 
**FinalGrade** | [**FinalGrade**](FinalGrade.md) | [**FinalGrade**](FinalGrade.md) |  | [optional] 
**EducationLevelCode** | [**ResumeEducationExperiencesEducationLevelCode**](ResumeEducationExperiencesEducationLevelCode.md) | [**ResumeEducationExperiencesEducationLevelCode**](ResumeEducationExperiencesEducationLevelCode.md) |  | [optional] 
**Description** | [**Description**](Description.md) | [**Description**](Description.md) |  | [optional] 
**StartDate** | [**Date**](Date.md) | [**Date**](Date.md) |  | [optional] 
**EndDate** | [**Date**](Date.md) | [**Date**](Date.md) |  | [optional] 
**Ongoing** | [**Ongoing**](Ongoing.md) | [**Ongoing**](Ongoing.md) |  | [optional] 
**Location** | [**ResumeLocationsLocation**](ResumeLocationsLocation.md) | [**ResumeLocationsLocation**](ResumeLocationsLocation.md) |  | [optional] 
**Organization** | [**FeedbackOrganization**](FeedbackOrganization.md) | [**FeedbackOrganization**](FeedbackOrganization.md) |  | [optional] 
**[Courses](#Courses)** | list, tuple,  | tuple,  | List of attended courses. | [optional] 
**ID** | str,  | str,  | Unique identifier for the current experience. | [optional] 

# Courses

List of attended courses.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of attended courses. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Text**](Text.md) | [**Text**](Text.md) | [**Text**](Text.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

