# inda_hr.model.company_common_optional_data.CompanyCommonOptionalData

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**Type** | [**CompanyCommonType**](CompanyCommonType.md) | [**CompanyCommonType**](CompanyCommonType.md) |  | [optional] 
**Size** | [**Size**](Size.md) | [**Size**](Size.md) |  | [optional] 
**Description** | [**BaseLocationsValueModelStrictStr**](BaseLocationsValueModelStrictStr.md) | [**BaseLocationsValueModelStrictStr**](BaseLocationsValueModelStrictStr.md) |  | [optional] 
**[Headquarters](#Headquarters)** | list, tuple,  | tuple,  | Company headquarters. | [optional] 
**[Branches](#Branches)** | list, tuple,  | tuple,  | Company branches. | [optional] 
**[Industries](#Industries)** | list, tuple,  | tuple,  | Company industries. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details. | [optional] 
**[Specialties](#Specialties)** | list, tuple,  | tuple,  | Keywords useful to provide additional detail about company industries. | [optional] 
**Founded** | [**FoundationYear**](FoundationYear.md) | [**FoundationYear**](FoundationYear.md) |  | [optional] 
**Logo** | [**JobadLinkLink**](JobadLinkLink.md) | [**JobadLinkLink**](JobadLinkLink.md) |  | [optional] 
**Link** | [**JobadLinkLink**](JobadLinkLink.md) | [**JobadLinkLink**](JobadLinkLink.md) |  | [optional] 
**[Products](#Products)** | list, tuple,  | tuple,  | Company main products. | [optional] 
**[Services](#Services)** | list, tuple,  | tuple,  | Services provided by the company. | [optional] 
**[RelatedCompanies](#RelatedCompanies)** | list, tuple,  | tuple,  | Details about related companies. | [optional] 

# Headquarters

Company headquarters.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Company headquarters. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Headquarter**](Headquarter.md) | [**Headquarter**](Headquarter.md) | [**Headquarter**](Headquarter.md) |  | 

# Branches

Company branches.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Company branches. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Branch**](Branch.md) | [**Branch**](Branch.md) | [**Branch**](Branch.md) |  | 

# Industries

Company industries. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Company industries. Check the [Standardized Data](https://api.inda.ai/hr/docs/v2/#tag/Standardized-Data) section for more details. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CompanyCommonIndustry**](CompanyCommonIndustry.md) | [**CompanyCommonIndustry**](CompanyCommonIndustry.md) | [**CompanyCommonIndustry**](CompanyCommonIndustry.md) |  | 

# Specialties

Keywords useful to provide additional detail about company industries.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Keywords useful to provide additional detail about company industries. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BaseLocationsValueModelStrictStr**](BaseLocationsValueModelStrictStr.md) | [**BaseLocationsValueModelStrictStr**](BaseLocationsValueModelStrictStr.md) | [**BaseLocationsValueModelStrictStr**](BaseLocationsValueModelStrictStr.md) |  | 

# Products

Company main products.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Company main products. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Asset**](Asset.md) | [**Asset**](Asset.md) | [**Asset**](Asset.md) |  | 

# Services

Services provided by the company.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Services provided by the company. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Asset**](Asset.md) | [**Asset**](Asset.md) | [**Asset**](Asset.md) |  | 

# RelatedCompanies

Details about related companies.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Details about related companies. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**RelatedCompany**](RelatedCompany.md) | [**RelatedCompany**](RelatedCompany.md) | [**RelatedCompany**](RelatedCompany.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

