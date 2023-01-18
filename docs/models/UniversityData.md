# inda_hr.model.university_data.UniversityData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Overview** | [**Overview**](Overview.md) | [**Overview**](Overview.md) |  | 
**Location** | [**UniversityLocationsLocation**](UniversityLocationsLocation.md) | [**UniversityLocationsLocation**](UniversityLocationsLocation.md) |  | [optional] 
**[OtherLocations](#OtherLocations)** | list, tuple,  | tuple,  | University&#x27;s branches locations. | [optional] 
**ContactInfo** | [**UniversityContactsContactInfo**](UniversityContactsContactInfo.md) | [**UniversityContactsContactInfo**](UniversityContactsContactInfo.md) |  | [optional] 
**Accreditations** | [**OptionalAccreditations**](OptionalAccreditations.md) | [**OptionalAccreditations**](OptionalAccreditations.md) |  | [optional] 
**Admissions** | [**OptionalAdmissions**](OptionalAdmissions.md) | [**OptionalAdmissions**](OptionalAdmissions.md) |  | [optional] 
**CarnegieClassification** | [**OptionalCarnegieClassification**](OptionalCarnegieClassification.md) | [**OptionalCarnegieClassification**](OptionalCarnegieClassification.md) |  | [optional] 
**FacilitiesAndServices** | [**OptionalFacilitiesAndServices**](OptionalFacilitiesAndServices.md) | [**OptionalFacilitiesAndServices**](OptionalFacilitiesAndServices.md) |  | [optional] 
**[Faculties](#Faculties)** | list, tuple,  | tuple,  | List of available faculties. | [optional] 
**[MembershipsAndAffiliations](#MembershipsAndAffiliations)** | list, tuple,  | tuple,  | List of University&#x27;s memberships and affiliations. | [optional] 
**[YearlyTuitionRange](#YearlyTuitionRange)** | list, tuple,  | tuple,  | List of indicative tuition ranges for local/international students and undergraduate/postgraduate students. | [optional] 
**SizeAndProfile** | [**OptionalSizeAndProfile**](OptionalSizeAndProfile.md) | [**OptionalSizeAndProfile**](OptionalSizeAndProfile.md) |  | [optional] 
**[StudyAreas](#StudyAreas)** | list, tuple,  | tuple,  | General overview of the University&#x27;s academic offer. | [optional] 
**Logo** | [**ValueModelBytes**](ValueModelBytes.md) | [**ValueModelBytes**](ValueModelBytes.md) |  | [optional] 

# OtherLocations

University's branches locations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | University&#x27;s branches locations. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UniversityLocationsLocation**](UniversityLocationsLocation.md) | [**UniversityLocationsLocation**](UniversityLocationsLocation.md) | [**UniversityLocationsLocation**](UniversityLocationsLocation.md) |  | 

# Faculties

List of available faculties.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of available faculties. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# MembershipsAndAffiliations

List of University's memberships and affiliations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of University&#x27;s memberships and affiliations. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# YearlyTuitionRange

List of indicative tuition ranges for local/international students and undergraduate/postgraduate students.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of indicative tuition ranges for local/international students and undergraduate/postgraduate students. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**OptionalTuition**](OptionalTuition.md) | [**OptionalTuition**](OptionalTuition.md) | [**OptionalTuition**](OptionalTuition.md) |  | 

# StudyAreas

General overview of the University's academic offer.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | General overview of the University&#x27;s academic offer. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**StudyAreas**](StudyAreas.md) | [**StudyAreas**](StudyAreas.md) | [**StudyAreas**](StudyAreas.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

