# inda_hr.model.job_ad_matching_data.JobAdMatchingData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**JobDescription** | [**JobDescription**](JobDescription.md) | [**JobDescription**](JobDescription.md) |  | 
**[Skills](#Skills)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Required or preferred skills. | 
**JobTitle** | [**JobTitleHeader**](JobTitleHeader.md) | [**JobTitleHeader**](JobTitleHeader.md) |  | 
**EmployerID** | str,  | str,  | CompanyID of the employer company. | [optional] 
**[ContactInfo](#ContactInfo)** | list, tuple,  | tuple,  | Whom to contact for the job position. | [optional] 
**[JobLocations](#JobLocations)** | list, tuple,  | tuple,  | Locations of the opened position. | [optional] 
**RelocationPreferences** | [**RelocationPreferences**](RelocationPreferences.md) | [**RelocationPreferences**](RelocationPreferences.md) |  | [optional] 
**RemoteWorking** | [**JobAdRemoteWorking**](JobAdRemoteWorking.md) | [**JobAdRemoteWorking**](JobAdRemoteWorking.md) |  | [optional] 
**Experience** | [**Experience**](Experience.md) | [**Experience**](Experience.md) |  | [optional] 
**Education** | [**OptionalRequiredAndPreferredEducation**](OptionalRequiredAndPreferredEducation.md) | [**OptionalRequiredAndPreferredEducation**](OptionalRequiredAndPreferredEducation.md) |  | [optional] 
**Languages** | [**OptionalRequiredAndPreferredConListLanguages**](OptionalRequiredAndPreferredConListLanguages.md) | [**OptionalRequiredAndPreferredConListLanguages**](OptionalRequiredAndPreferredConListLanguages.md) |  | [optional] 
**[RelatedJobTitles](#RelatedJobTitles)** | list, tuple,  | tuple,  | Additional Job Titles related to the opened position. | [optional] 
**Employment** | [**JobTitleEmployment**](JobTitleEmployment.md) | [**JobTitleEmployment**](JobTitleEmployment.md) |  | [optional] 
**Contract** | [**JobAdContract**](JobAdContract.md) | [**JobAdContract**](JobAdContract.md) |  | [optional] 
**Publisher** | [**Publisher**](Publisher.md) | [**Publisher**](Publisher.md) |  | [optional] 
**JobShift** | [**JobShift**](JobShift.md) | [**JobShift**](JobShift.md) |  | [optional] 
**NumberOfOpenings** | [**ValueModelInt**](ValueModelInt.md) | [**ValueModelInt**](ValueModelInt.md) |  | [optional] 
**Link** | [**JobadLinkLink**](JobadLinkLink.md) | [**JobadLinkLink**](JobadLinkLink.md) |  | [optional] 
**[AdvertisementSites](#AdvertisementSites)** | list, tuple,  | tuple,  | Advertising sites for the job offer. | [optional] 
**Salary** | [**JobAdSalary**](JobAdSalary.md) | [**JobAdSalary**](JobAdSalary.md) |  | [optional] 
**[Benefits](#Benefits)** | list, tuple,  | tuple,  | Offered benefits. | [optional] 
**ExpirationDate** | [**ValueModelDatetime**](ValueModelDatetime.md) | [**ValueModelDatetime**](ValueModelDatetime.md) |  | [optional] 
**Status** | [**JobadCommonValueModelStr**](JobadCommonValueModelStr.md) | [**JobadCommonValueModelStr**](JobadCommonValueModelStr.md) |  | [optional] 

# Skills

Required or preferred skills.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | Required or preferred skills. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[RequiredAndPreferredConListSkills](RequiredAndPreferredConListSkills.md) | [**RequiredAndPreferredConListSkills**](RequiredAndPreferredConListSkills.md) | [**RequiredAndPreferredConListSkills**](RequiredAndPreferredConListSkills.md) |  | 
[RequiredConListSkills](RequiredConListSkills.md) | [**RequiredConListSkills**](RequiredConListSkills.md) | [**RequiredConListSkills**](RequiredConListSkills.md) |  | 
[PreferredConListSkills](PreferredConListSkills.md) | [**PreferredConListSkills**](PreferredConListSkills.md) | [**PreferredConListSkills**](PreferredConListSkills.md) |  | 

# ContactInfo

Whom to contact for the job position.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Whom to contact for the job position. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**JobadContactInfoContactInfo**](JobadContactInfoContactInfo.md) | [**JobadContactInfoContactInfo**](JobadContactInfoContactInfo.md) | [**JobadContactInfoContactInfo**](JobadContactInfoContactInfo.md) |  | 

# JobLocations

Locations of the opened position.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Locations of the opened position. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BaseLocationsLocation**](BaseLocationsLocation.md) | [**BaseLocationsLocation**](BaseLocationsLocation.md) | [**BaseLocationsLocation**](BaseLocationsLocation.md) |  | 

# RelatedJobTitles

Additional Job Titles related to the opened position.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Additional Job Titles related to the opened position. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OptionalJobAdJobTitle**](OptionalJobAdJobTitle.md) | [**OptionalJobAdJobTitle**](OptionalJobAdJobTitle.md) | [**OptionalJobAdJobTitle**](OptionalJobAdJobTitle.md) |  | 

# AdvertisementSites

Advertising sites for the job offer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Advertising sites for the job offer. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**JobadLinkLink**](JobadLinkLink.md) | [**JobadLinkLink**](JobadLinkLink.md) | [**JobadLinkLink**](JobadLinkLink.md) |  | 

# Benefits

Offered benefits.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Offered benefits. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**JobAdBenefit**](JobAdBenefit.md) | [**JobAdBenefit**](JobAdBenefit.md) | [**JobAdBenefit**](JobAdBenefit.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

