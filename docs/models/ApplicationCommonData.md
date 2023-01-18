# inda_hr.model.application_common_data.ApplicationCommonData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Objective** | [**BaseBenefitsValueModelStrictStr**](BaseBenefitsValueModelStrictStr.md) | [**BaseBenefitsValueModelStrictStr**](BaseBenefitsValueModelStrictStr.md) |  | [optional] 
**ProfessionalSummary** | [**BaseBenefitsValueModelStrictStr**](BaseBenefitsValueModelStrictStr.md) | [**BaseBenefitsValueModelStrictStr**](BaseBenefitsValueModelStrictStr.md) |  | [optional] 
**DesiredEmployment** | [**ResumeEmployment**](ResumeEmployment.md) | [**ResumeEmployment**](ResumeEmployment.md) |  | [optional] 
**[DesiredContracts](#DesiredContracts)** | list, tuple,  | tuple,  | A candidate preference towards certain contracts. | [optional] 
**DesiredSalary** | [**ResumeSalary**](ResumeSalary.md) | [**ResumeSalary**](ResumeSalary.md) |  | [optional] 
**[DesiredBenefits](#DesiredBenefits)** | list, tuple,  | tuple,  | A candidate preference towards certain benefits. E.g.: &#x27;Medical Insurance&#x27;, &#x27;Company Phone&#x27;, etc.. | [optional] 
**[DesiredLocations](#DesiredLocations)** | list, tuple,  | tuple,  | A candidate preference towards certain locations. E.g.: Headquarter location, a certain Branch location or home location if remote working is possible. | [optional] 
**RelocationPreferences** | [**RelocationPreferences**](RelocationPreferences.md) | [**RelocationPreferences**](RelocationPreferences.md) |  | [optional] 
**RemoteWorking** | [**JobAdRemoteWorking**](JobAdRemoteWorking.md) | [**JobAdRemoteWorking**](JobAdRemoteWorking.md) |  | [optional] 
**JobShift** | [**JobShift**](JobShift.md) | [**JobShift**](JobShift.md) |  | [optional] 
**[OriginLinks](#OriginLinks)** | list, tuple,  | tuple,  | List of links from which the application is coming from. E.g.: LinkedIn, Indeed, etc.. | [optional] 

# DesiredContracts

A candidate preference towards certain contracts.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A candidate preference towards certain contracts. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResumeContract**](ResumeContract.md) | [**ResumeContract**](ResumeContract.md) | [**ResumeContract**](ResumeContract.md) |  | 

# DesiredBenefits

A candidate preference towards certain benefits. E.g.: 'Medical Insurance', 'Company Phone', etc..

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A candidate preference towards certain benefits. E.g.: &#x27;Medical Insurance&#x27;, &#x27;Company Phone&#x27;, etc.. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ResumeBenefit**](ResumeBenefit.md) | [**ResumeBenefit**](ResumeBenefit.md) | [**ResumeBenefit**](ResumeBenefit.md) |  | 

# DesiredLocations

A candidate preference towards certain locations. E.g.: Headquarter location, a certain Branch location or home location if remote working is possible.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A candidate preference towards certain locations. E.g.: Headquarter location, a certain Branch location or home location if remote working is possible. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BaseLocationsLocation**](BaseLocationsLocation.md) | [**BaseLocationsLocation**](BaseLocationsLocation.md) | [**BaseLocationsLocation**](BaseLocationsLocation.md) |  | 

# OriginLinks

List of links from which the application is coming from. E.g.: LinkedIn, Indeed, etc..

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of links from which the application is coming from. E.g.: LinkedIn, Indeed, etc.. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**JobadLinkLink**](JobadLinkLink.md) | [**JobadLinkLink**](JobadLinkLink.md) | [**JobadLinkLink**](JobadLinkLink.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

