# inda_hr.model.resume_common_data.ResumeCommonData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**JobTitle** | [**OptionalResumeJobTitle**](OptionalResumeJobTitle.md) | [**OptionalResumeJobTitle**](OptionalResumeJobTitle.md) |  | [optional] 
**PersonalInfo** | [**PersonalInfo**](PersonalInfo.md) | [**PersonalInfo**](PersonalInfo.md) |  | [optional] 
**ContactInfo** | [**ResumeContactInfoContactInfo**](ResumeContactInfoContactInfo.md) | [**ResumeContactInfoContactInfo**](ResumeContactInfoContactInfo.md) |  | [optional] 
**PersonLocation** | [**PersonLocation**](PersonLocation.md) | [**PersonLocation**](PersonLocation.md) |  | [optional] 
**Headline** | [**Text**](Text.md) | [**Text**](Text.md) |  | [optional] 
**[EducationExperiences](#EducationExperiences)** | list, tuple,  | tuple,  | Candidate&#x27;s education experiences. | [optional] 
**[WorkExperiences](#WorkExperiences)** | list, tuple,  | tuple,  | Candidate&#x27;s employment history. | [optional] 
**CoverLetter** | [**Text**](Text.md) | [**Text**](Text.md) |  | [optional] 
**[References](#References)** | list, tuple,  | tuple,  | Candidate&#x27;s references. | [optional] 
**ProfileSummary** | [**ProfileSummary**](ProfileSummary.md) | [**ProfileSummary**](ProfileSummary.md) |  | [optional] 
**[Skills](#Skills)** | list, tuple,  | tuple,  | Candidate&#x27;s skills. | [optional] 
**[JobTitles](#JobTitles)** | list, tuple,  | tuple,  | Candidate&#x27;s job titles. | [optional] 
**[Languages](#Languages)** | list, tuple,  | tuple,  | Candidate&#x27;s language skills. | [optional] 
**[Certifications](#Certifications)** | list, tuple,  | tuple,  | Certifications earned by the candidate. | [optional] 
**[Publications](#Publications)** | list, tuple,  | tuple,  | Candidate&#x27;s publications, both academic papers and books. | [optional] 
**[Awards](#Awards)** | list, tuple,  | tuple,  | List of the awards won by the candidate. | [optional] 
**[Projects](#Projects)** | list, tuple,  | tuple,  | Projects the candidate worked or works on. | [optional] 
**[Achievements](#Achievements)** | list, tuple,  | tuple,  | Achievements earned by the candidate. | [optional] 
**[Patents](#Patents)** | list, tuple,  | tuple,  | Candidate&#x27;s patents. | [optional] 
**[HobbiesAndInterests](#HobbiesAndInterests)** | list, tuple,  | tuple,  | List of candidate&#x27;s hobbies and interests. | [optional] 
**[Licenses](#Licenses)** | list, tuple,  | tuple,  | Candidate&#x27;s licenses. | [optional] 
**[Volunteering](#Volunteering)** | list, tuple,  | tuple,  | Candidate&#x27;s works as volunteer. | [optional] 
**[ConferenceAndSeminars](#ConferenceAndSeminars)** | list, tuple,  | tuple,  | Conferences and seminars that the candidate may have partecipated in. | [optional] 
**[MilitaryHistory](#MilitaryHistory)** | list, tuple,  | tuple,  | Candidate&#x27;s military history. | [optional] 
**[Others](#Others)** | list, tuple,  | tuple,  | Candidate&#x27;s additional information not covered by the previous fields. | [optional] 

# EducationExperiences

Candidate's education experiences.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s education experiences. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EducationExperience**](EducationExperience.md) | [**EducationExperience**](EducationExperience.md) | [**EducationExperience**](EducationExperience.md) |  | 

# WorkExperiences

Candidate's employment history.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s employment history. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**WorkExperience**](WorkExperience.md) | [**WorkExperience**](WorkExperience.md) | [**WorkExperience**](WorkExperience.md) |  | 

# References

Candidate's references.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s references. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Reference**](Reference.md) | [**Reference**](Reference.md) | [**Reference**](Reference.md) |  | 

# Skills

Candidate's skills.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s skills. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OptionalResumeSkill**](OptionalResumeSkill.md) | [**OptionalResumeSkill**](OptionalResumeSkill.md) | [**OptionalResumeSkill**](OptionalResumeSkill.md) |  | 

# JobTitles

Candidate's job titles.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s job titles. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OptionalResumeJobTitle**](OptionalResumeJobTitle.md) | [**OptionalResumeJobTitle**](OptionalResumeJobTitle.md) | [**OptionalResumeJobTitle**](OptionalResumeJobTitle.md) |  | 

# Languages

Candidate's language skills.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s language skills. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OptionalResumeLanguage**](OptionalResumeLanguage.md) | [**OptionalResumeLanguage**](OptionalResumeLanguage.md) | [**OptionalResumeLanguage**](OptionalResumeLanguage.md) |  | 

# Certifications

Certifications earned by the candidate.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Certifications earned by the candidate. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Certification**](Certification.md) | [**Certification**](Certification.md) | [**Certification**](Certification.md) |  | 

# Publications

Candidate's publications, both academic papers and books.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s publications, both academic papers and books. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Publication**](Publication.md) | [**Publication**](Publication.md) | [**Publication**](Publication.md) |  | 

# Awards

List of the awards won by the candidate.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of the awards won by the candidate. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Award**](Award.md) | [**Award**](Award.md) | [**Award**](Award.md) |  | 

# Projects

Projects the candidate worked or works on.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Projects the candidate worked or works on. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Project**](Project.md) | [**Project**](Project.md) | [**Project**](Project.md) |  | 

# Achievements

Achievements earned by the candidate.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Achievements earned by the candidate. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Achievement**](Achievement.md) | [**Achievement**](Achievement.md) | [**Achievement**](Achievement.md) |  | 

# Patents

Candidate's patents.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s patents. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Patent**](Patent.md) | [**Patent**](Patent.md) | [**Patent**](Patent.md) |  | 

# HobbiesAndInterests

List of candidate's hobbies and interests.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of candidate&#x27;s hobbies and interests. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Text**](Text.md) | [**Text**](Text.md) | [**Text**](Text.md) |  | 

# Licenses

Candidate's licenses.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s licenses. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**License**](License.md) | [**License**](License.md) | [**License**](License.md) |  | 

# Volunteering

Candidate's works as volunteer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s works as volunteer. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Event**](Event.md) | [**Event**](Event.md) | [**Event**](Event.md) |  | 

# ConferenceAndSeminars

Conferences and seminars that the candidate may have partecipated in.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Conferences and seminars that the candidate may have partecipated in. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Event**](Event.md) | [**Event**](Event.md) | [**Event**](Event.md) |  | 

# MilitaryHistory

Candidate's military history.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s military history. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**MilitaryService**](MilitaryService.md) | [**MilitaryService**](MilitaryService.md) | [**MilitaryService**](MilitaryService.md) |  | 

# Others

Candidate's additional information not covered by the previous fields.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Candidate&#x27;s additional information not covered by the previous fields. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Other**](Other.md) | [**Other**](Other.md) | [**Other**](Other.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

