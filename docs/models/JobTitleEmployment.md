# inda_hr.model.job_title_employment.JobTitleEmployment

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Code** | [**BaseBenefitsValueModelStrictStr**](BaseBenefitsValueModelStrictStr.md) | [**BaseBenefitsValueModelStrictStr**](BaseBenefitsValueModelStrictStr.md) |  | [optional] 
**Category** | [**BaseBenefitsValueModelStrictStr**](BaseBenefitsValueModelStrictStr.md) | [**BaseBenefitsValueModelStrictStr**](BaseBenefitsValueModelStrictStr.md) |  | [optional] 
**Type** | [**EmploymentType**](EmploymentType.md) | [**EmploymentType**](EmploymentType.md) |  | [optional] 
**[Industries](#Industries)** | list, tuple,  | tuple,  | Employment industries. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details. | [optional] 
**[FunctionalAreas](#FunctionalAreas)** | list, tuple,  | tuple,  |  | [optional] 
**[Activities](#Activities)** | list, tuple,  | tuple,  |  | [optional] 

# Industries

Employment industries. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Employment industries. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BaseEmploymentsIndustry**](BaseEmploymentsIndustry.md) | [**BaseEmploymentsIndustry**](BaseEmploymentsIndustry.md) | [**BaseEmploymentsIndustry**](BaseEmploymentsIndustry.md) |  | 

# FunctionalAreas

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BaseBenefitsValueModelStrictStr**](BaseBenefitsValueModelStrictStr.md) | [**BaseBenefitsValueModelStrictStr**](BaseBenefitsValueModelStrictStr.md) | [**BaseBenefitsValueModelStrictStr**](BaseBenefitsValueModelStrictStr.md) |  | 

# Activities

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Activity**](Activity.md) | [**Activity**](Activity.md) | [**Activity**](Activity.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

