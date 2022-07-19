# inda_hr.StandardizedDataApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_size_get**](StandardizedDataApi.md#get_company_size_get) | **GET** /hr/v2/data/company/size/ | Get Company Size
[**get_company_type_get**](StandardizedDataApi.md#get_company_type_get) | **GET** /hr/v2/data/company/type/ | Get Company Type
[**get_contract_type_get**](StandardizedDataApi.md#get_contract_type_get) | **GET** /hr/v2/data/contract/type/ | Get Contract Type
[**get_disability_get**](StandardizedDataApi.md#get_disability_get) | **GET** /hr/v2/data/disability/ | Get Disability
[**get_education_title_get**](StandardizedDataApi.md#get_education_title_get) | **GET** /hr/v2/data/education/title/ | Get Education Title
[**get_email_label_get**](StandardizedDataApi.md#get_email_label_get) | **GET** /hr/v2/data/email/label/ | Get Email Label
[**get_employment_type_get**](StandardizedDataApi.md#get_employment_type_get) | **GET** /hr/v2/data/employment/type/ | Get Employment Type
[**get_field_of_study_get**](StandardizedDataApi.md#get_field_of_study_get) | **GET** /hr/v2/data/education/field-of-study/ | Get Field Of Study
[**get_gender_get**](StandardizedDataApi.md#get_gender_get) | **GET** /hr/v2/data/gender/ | Get Gender
[**get_industries_get**](StandardizedDataApi.md#get_industries_get) | **GET** /hr/v2/data/industries/ | Get Industries
[**get_job_function_get**](StandardizedDataApi.md#get_job_function_get) | **GET** /hr/v2/data/job/function/ | Get Job Function
[**get_jobshift_type_get**](StandardizedDataApi.md#get_jobshift_type_get) | **GET** /hr/v2/data/jobshift/type/ | Get Jobshift Type
[**get_license_code_get**](StandardizedDataApi.md#get_license_code_get) | **GET** /hr/v2/data/license/type/{license_type}/code/ | Get License Code
[**get_license_type_get**](StandardizedDataApi.md#get_license_type_get) | **GET** /hr/v2/data/license/type/ | Get License Type
[**get_link_label_get**](StandardizedDataApi.md#get_link_label_get) | **GET** /hr/v2/data/link/label/ | Get Link Label
[**get_marital_status_get**](StandardizedDataApi.md#get_marital_status_get) | **GET** /hr/v2/data/marital-status/ | Get Marital Status
[**get_name_prefix_get**](StandardizedDataApi.md#get_name_prefix_get) | **GET** /hr/v2/data/name/prefix/ | Get Name Prefix
[**get_name_suffix_get**](StandardizedDataApi.md#get_name_suffix_get) | **GET** /hr/v2/data/name/suffix/ | Get Name Suffix
[**get_patent_status_get**](StandardizedDataApi.md#get_patent_status_get) | **GET** /hr/v2/data/patent/status/ | Get Patent Status
[**get_phone_label_get**](StandardizedDataApi.md#get_phone_label_get) | **GET** /hr/v2/data/phone/label/ | Get Phone Label
[**get_protected_group_get**](StandardizedDataApi.md#get_protected_group_get) | **GET** /hr/v2/data/protected-group/ | Get Protected Group
[**get_remote_working_get**](StandardizedDataApi.md#get_remote_working_get) | **GET** /hr/v2/data/employment/remote-working/ | Get Remote Working
[**get_salary_frequency_get**](StandardizedDataApi.md#get_salary_frequency_get) | **GET** /hr/v2/data/salary/frequency/ | Get Salary Frequency
[**get_salary_type_get**](StandardizedDataApi.md#get_salary_type_get) | **GET** /hr/v2/data/salary/type/ | Get Salary Type
[**get_seniority_level_get**](StandardizedDataApi.md#get_seniority_level_get) | **GET** /hr/v2/data/seniority/level/ | Get Seniority Level


# **get_company_size_get**
> GetExtendedStandardDataResponse get_company_size_get()

Get Company Size

 Lists company size encodings based on [LinkedIn Company Size](https://docs.microsoft.com/en-us/linkedin/shared/references/reference-tables/company-size-codes). 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.get_extended_standard_data_response import GetExtendedStandardDataResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Company Size
        api_response = api_instance.get_company_size_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_company_size_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetExtendedStandardDataResponse**](GetExtendedStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_type_get**
> GetStandardDataResponse get_company_type_get()

Get Company Type

 Lists company type encodings based on LinkedIn Company Types.  English example values:  + <code style='color: #333333; opacity: 0.9'>SELF_EMPLOYED</code> - Self-employed + <code style='color: #333333; opacity: 0.9'>PUBLIC_COMPANY</code> - Public company + <code style='color: #333333; opacity: 0.9'>NON_PROFIT</code> - Nonprofit + <code style='color: #333333; opacity: 0.9'>PARTNERSHIP</code> - Partnership + <code style='color: #333333; opacity: 0.9'>GOVERNMENT_AGENCY</code> - Government agency + <code style='color: #333333; opacity: 0.9'>SELF_OWNED</code> - Sole proprietorship + <code style='color: #333333; opacity: 0.9'>PRIVATELY_HELD</code> - Privately held 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Company Type
        api_response = api_instance.get_company_type_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_company_type_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_contract_type_get**
> GetStandardDataResponse get_contract_type_get()

Get Contract Type

 Lists common contract type encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>CASUAL</code> - Casual + <code style='color: #333333; opacity: 0.9'>TEMPORARY</code> - Temporary + <code style='color: #333333; opacity: 0.9'>PERMANENT</code> - Permanent 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Contract Type
        api_response = api_instance.get_contract_type_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_contract_type_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_disability_get**
> GetStandardDataResponse get_disability_get()

Get Disability

 Lists disability level encodings.  Each level represents a disability severity, as described below:  + <code style='color: #333333; opacity: 0.9'>1</code> - 1: Needs another person's assistance with daily life tasks + <code style='color: #333333; opacity: 0.9'>5</code> - 5: No limitations in functioning + <code style='color: #333333; opacity: 0.9'>4</code> - 4: Experiences difficulty in just one function + <code style='color: #333333; opacity: 0.9'>2</code> - 2: Inability to perform one or more sensory or physical functions + <code style='color: #333333; opacity: 0.9'>3</code> - 3: Experiences difficulties in multiple sensory or physical functions 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Disability
        api_response = api_instance.get_disability_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_disability_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_education_title_get**
> GetStandardDataResponse get_education_title_get()

Get Education Title

 Lists common education title encodings based on LinkedIn Degree values.  English example values:  + <code style='color: #333333; opacity: 0.9'>241</code> - Bachelor of Pharmacy - BPharm + <code style='color: #333333; opacity: 0.9'>1018</code> - Doctor of Pharmacy - PharmD + <code style='color: #333333; opacity: 0.9'>900</code> - Doctor of Philosophy - PhD + <code style='color: #333333; opacity: 0.9'>563</code> - Master of Philosophy - MPhil + <code style='color: #333333; opacity: 0.9'>570</code> - Master of Public Administration - MPA + <code style='color: #333333; opacity: 0.9'>588</code> - Master of Public Health - MPH + <code style='color: #333333; opacity: 0.9'>645</code> - Postgraduate Degree + <code style='color: #333333; opacity: 0.9'>116</code> - Associate of Arts - AA + <code style='color: #333333; opacity: 0.9'>104</code> - Associate of Arts and Sciences - AAS + <code style='color: #333333; opacity: 0.9'>112</code> - Associate of Science - AS + <code style='color: #333333; opacity: 0.9'>259</code> - Bachelor of Applied Science - BASc + <code style='color: #333333; opacity: 0.9'>258</code> - Bachelor of Architecture - BArch + <code style='color: #333333; opacity: 0.9'>350</code> - Bachelor of Arts - BA + <code style='color: #333333; opacity: 0.9'>450</code> - Bachelor of Business Administration - BBA + <code style='color: #333333; opacity: 0.9'>215</code> - Bachelor of Commerce - BCom + <code style='color: #333333; opacity: 0.9'>206</code> - Bachelor of Education - BEd + <code style='color: #333333; opacity: 0.9'>269</code> - Bachelor of Engineering - BE + <code style='color: #333333; opacity: 0.9'>223</code> - Bachelor of Fine Arts - BFA + <code style='color: #333333; opacity: 0.9'>232</code> - Bachelor of Laws - LLB + <code style='color: #333333; opacity: 0.9'>1037</code> - Bachelor of Medicine, Bachelor of Surgery - MBBS + <code style='color: #333333; opacity: 0.9'>400</code> - Bachelor of Science - BS + <code style='color: #333333; opacity: 0.9'>250</code> - Bachelor of Technology - BTech + <code style='color: #333333; opacity: 0.9'>513</code> - Diploma of Education + <code style='color: #333333; opacity: 0.9'>916</code> - Doctor of Arts + <code style='color: #333333; opacity: 0.9'>921</code> - Doctor of Education - EdD + <code style='color: #333333; opacity: 0.9'>1100</code> - Doctor of Law - JD + <code style='color: #333333; opacity: 0.9'>1100</code> - Doctor of Law + <code style='color: #333333; opacity: 0.9'>1000</code> - Doctor of Medicine - MD + <code style='color: #333333; opacity: 0.9'>937</code> - Doctor of Science + <code style='color: #333333; opacity: 0.9'>535</code> - Master of Architecture - MArch + <code style='color: #333333; opacity: 0.9'>536</code> - Master of Arts - MA + <code style='color: #333333; opacity: 0.9'>700</code> - Master of Business Administration - MBA + <code style='color: #333333; opacity: 0.9'>594</code> - Master of Computer Applications - MCA + <code style='color: #333333; opacity: 0.9'>548</code> - Master of Divinity - MDiv + <code style='color: #333333; opacity: 0.9'>550</code> - Master of Education - MEd + <code style='color: #333333; opacity: 0.9'>551</code> - Master of Engineering - MEng + <code style='color: #333333; opacity: 0.9'>603</code> - Master of Fine Arts - MFA + <code style='color: #333333; opacity: 0.9'>555</code> - Master of Laws - LLM + <code style='color: #333333; opacity: 0.9'>557</code> - Master of Library & Information Science - MLIS + <code style='color: #333333; opacity: 0.9'>626</code> - Master of Science - MS + <code style='color: #333333; opacity: 0.9'>589</code> - Master of Social Work - MSW + <code style='color: #333333; opacity: 0.9'>584</code> - Master of Technology - MTech + <code style='color: #333333; opacity: 0.9'>701</code> - Executive MBA + <code style='color: #333333; opacity: 0.9'>500</code> - Master's degree + <code style='color: #333333; opacity: 0.9'>5</code> - Middle School Diploma + <code style='color: #333333; opacity: 0.9'>10</code> - High School Diploma + <code style='color: #333333; opacity: 0.9'>10</code> - GED + <code style='color: #333333; opacity: 0.9'>100</code> - Associate's degree + <code style='color: #333333; opacity: 0.9'>200</code> - Bachelor's degree + <code style='color: #333333; opacity: 0.9'>914</code> - Doctor's Degree + <code style='color: #333333; opacity: 0.9'>750</code> - Engineer's degree + <code style='color: #333333; opacity: 0.9'>160</code> - Higher National Diploma + <code style='color: #333333; opacity: 0.9'>800</code> - Licentiate degree + <code style='color: #333333; opacity: 0.9'>150</code> - Foundation degree 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Education Title
        api_response = api_instance.get_education_title_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_education_title_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_label_get**
> GetStandardDataResponse get_email_label_get()

Get Email Label

 Lists common email labels encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>OTHER</code> - Other + <code style='color: #333333; opacity: 0.9'>BUSINESS</code> - Business + <code style='color: #333333; opacity: 0.9'>PERSONAL</code> - Personal 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Email Label
        api_response = api_instance.get_email_label_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_email_label_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employment_type_get**
> GetExtendedStandardDataResponse get_employment_type_get()

Get Employment Type

 Lists common employment type encodings based on LinkedIn Employment Types.  English example values:  + <code style='color: #333333; opacity: 0.9'>FULL_TIME</code> - Full-time + <code style='color: #333333; opacity: 0.9'>PART_TIME</code> - Part-time + <code style='color: #333333; opacity: 0.9'>CONTRACT</code> - Contract + <code style='color: #333333; opacity: 0.9'>TEMPORARY</code> - Temporary + <code style='color: #333333; opacity: 0.9'>VOLUNTEER</code> - Volunteer + <code style='color: #333333; opacity: 0.9'>INTERNSHIP</code> - Internship + <code style='color: #333333; opacity: 0.9'>SELF_EMPLOYED</code> - Self-employed + <code style='color: #333333; opacity: 0.9'>FREELANCE</code> - Freelance + <code style='color: #333333; opacity: 0.9'>APPRENTICESHIP</code> - Apprenticeship + <code style='color: #333333; opacity: 0.9'>SEASONAL</code> - Seasonal + <code style='color: #333333; opacity: 0.9'>OTHER</code> - Other 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.get_extended_standard_data_response import GetExtendedStandardDataResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Employment Type
        api_response = api_instance.get_employment_type_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_employment_type_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetExtendedStandardDataResponse**](GetExtendedStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_field_of_study_get**
> GetStandardDataResponse get_field_of_study_get()

Get Field Of Study

 Lists fields of study encodings based on LinkedIn Fields of Study.  English example values:  + <code style='color: #333333; opacity: 0.9'>100992</code> - Econometrics and Quantitative Economics + <code style='color: #333333; opacity: 0.9'>101471</code> - Management Sciences and Quantitative Methods + <code style='color: #333333; opacity: 0.9'>100982</code> - Research Methodology and Quantitative Methods + <code style='color: #333333; opacity: 0.9'>100417</code> - Quality Control Technology/Technician + <code style='color: #333333; opacity: 0.9'>100404</code> - Water Quality and Wastewater Treatment Management and Recycling Technology/Technician + <code style='color: #333333; opacity: 0.9'>100921</code> - Psychometrics and Quantitative Psychology + <code style='color: #333333; opacity: 0.9'>100415</code> - Quality Control and Safety Technologies/Technicians + <code style='color: #333333; opacity: 0.9'>100861</code> - Youth Ministry + <code style='color: #333333; opacity: 0.9'>101372</code> - Yoga Teacher Training/Yoga Therapy + <code style='color: #333333; opacity: 0.9'>100980</code> - Youth Services/Administration + <code style='color: #333333; opacity: 0.9'>100603</code> - Children and Youth Library Services + <code style='color: #333333; opacity: 0.9'>100912</code> - Psychology + <code style='color: #333333; opacity: 0.9'>101001</code> - Political Science and Government + <code style='color: #333333; opacity: 0.9'>101460</code> - Human Resources Management/Personnel Administration, General + <code style='color: #333333; opacity: 0.9'>100892</code> - Physics + <code style='color: #333333; opacity: 0.9'>100865</code> - Physical Sciences + <code style='color: #333333; opacity: 0.9'>101419</code> - Project Management + <code style='color: #333333; opacity: 0.9'>101295</code> - Pharmacy + <code style='color: #333333; opacity: 0.9'>100838</code> - Philosophy + <code style='color: #333333; opacity: 0.9'>100974</code> - Public Administration + <code style='color: #333333; opacity: 0.9'>100151</code> - Public Relations/Image Management + <code style='color: #333333; opacity: 0.9'>100180</code> - Computer Programming, Specific Applications + <code style='color: #333333; opacity: 0.9'>101117</code> - Industrial and Product Design + <code style='color: #333333; opacity: 0.9'>101136</code> - Photography + <code style='color: #333333; opacity: 0.9'>100926</code> - Counseling Psychology + <code style='color: #333333; opacity: 0.9'>100580</code> - Legal Assistant/Paralegal + <code style='color: #333333; opacity: 0.9'>100924</code> - Clinical Psychology + <code style='color: #333333; opacity: 0.9'>101414</code> - Non-Profit/Public/Organizational Management + <code style='color: #333333; opacity: 0.9'>100178</code> - Computer Programming + <code style='color: #333333; opacity: 0.9'>100201</code> - Information Technology Project Management + <code style='color: #333333; opacity: 0.9'>100900</code> - Theoretical and Mathematical Physics + <code style='color: #333333; opacity: 0.9'>101421</code> - Organizational Leadership + <code style='color: #333333; opacity: 0.9'>101413</code> - Operations Management and Supervision + <code style='color: #333333; opacity: 0.9'>100877</code> - Organic Chemistry + <code style='color: #333333; opacity: 0.9'>100001</code> - Agriculture, Agriculture Operations, and Related Sciences + <code style='color: #333333; opacity: 0.9'>101482</code> - General Sales, Merchandising and Related Marketing Operations + <code style='color: #333333; opacity: 0.9'>100927</code> - Industrial and Organizational Psychology + <code style='color: #333333; opacity: 0.9'>101408</code> - Business Administration, Management and Operations + <code style='color: #333333; opacity: 0.9'>100374</code> - Operations Research + <code style='color: #333333; opacity: 0.9'>101321</code> - Occupational Therapy/Therapist + <code style='color: #333333; opacity: 0.9'>100150</code> - Organizational Communication, General + <code style='color: #333333; opacity: 0.9'>100677</code> - Marine Biology and Biological Oceanography + <code style='color: #333333; opacity: 0.9'>100169</code> - Graphic and Printing Equipment Operator, General Production + <code style='color: #333333; opacity: 0.9'>101462</code> - Organizational Behavior Studies + <code style='color: #333333; opacity: 0.9'>101432</code> - Business/Office Automation/Technology/Data Entry + <code style='color: #333333; opacity: 0.9'>101487</code> - Specialized Sales, Merchandising and  Marketing Operations + <code style='color: #333333; opacity: 0.9'>101095</code> - Aviation/Airway Management and Operations + <code style='color: #333333; opacity: 0.9'>101287</code> - Optometry + <code style='color: #333333; opacity: 0.9'>100715</code> - Military Operational Art and Science/Studies + <code style='color: #333333; opacity: 0.9'>100891</code> - Oceanography, Chemical and Physical + <code style='color: #333333; opacity: 0.9'>101409</code> - Business Administration and Management, General + <code style='color: #333333; opacity: 0.9'>101475</code> - Marketing + <code style='color: #333333; opacity: 0.9'>100360</code> - Mechanical Engineering + <code style='color: #333333; opacity: 0.9'>100139</code> - Communication and Media Studies + <code style='color: #333333; opacity: 0.9'>100693</code> - Mathematics + <code style='color: #333333; opacity: 0.9'>101476</code> - Marketing/Marketing Management, General + <code style='color: #333333; opacity: 0.9'>101468</code> - Management Information Systems, General + <code style='color: #333333; opacity: 0.9'>101274</code> - Medicine + <code style='color: #333333; opacity: 0.9'>101406</code> - Business, Management, Marketing, and Related Support Services + <code style='color: #333333; opacity: 0.9'>101438</code> - Business/Managerial Economics + <code style='color: #333333; opacity: 0.9'>100447</code> - Engineering/Industrial Management + <code style='color: #333333; opacity: 0.9'>100142</code> - Mass Communication/Media Studies + <code style='color: #333333; opacity: 0.9'>101150</code> - Music + <code style='color: #333333; opacity: 0.9'>101459</code> - Human Resources Management and Services + <code style='color: #333333; opacity: 0.9'>101427</code> - Accounting and Business/Management + <code style='color: #333333; opacity: 0.9'>100761</code> - Mathematics and Computer Science + <code style='color: #333333; opacity: 0.9'>101443</code> - Finance and Financial Management Services + <code style='color: #333333; opacity: 0.9'>100143</code> - Journalism + <code style='color: #333333; opacity: 0.9'>100939</code> - Criminal Justice and Corrections + <code style='color: #333333; opacity: 0.9'>100144</code> - Broadcast Journalism + <code style='color: #333333; opacity: 0.9'>100119</code> - Japanese Studies + <code style='color: #333333; opacity: 0.9'>100462</code> - Japanese Language and Literature + <code style='color: #333333; opacity: 0.9'>100944</code> - Criminal Justice/Police Science + <code style='color: #333333; opacity: 0.9'>100569</code> - Canadian Law/Legal Studies/Jurisprudence + <code style='color: #333333; opacity: 0.9'>100942</code> - Criminal Justice/Safety Studies + <code style='color: #333333; opacity: 0.9'>100847</code> - Jewish/Judaic Studies + <code style='color: #333333; opacity: 0.9'>101158</code> - Jazz/Jazz Studies + <code style='color: #333333; opacity: 0.9'>100037</code> - Agricultural Communication/Journalism + <code style='color: #333333; opacity: 0.9'>100941</code> - Criminal Justice/Law Enforcement Administration + <code style='color: #333333; opacity: 0.9'>100568</code> - American/U.S. Law/Legal Studies/Jurisprudence + <code style='color: #333333; opacity: 0.9'>100281</code> - Junior High/Intermediate/Middle School Education and Teaching + <code style='color: #333333; opacity: 0.9'>101054</code> - Watchmaking and Jewelrymaking + <code style='color: #333333; opacity: 0.9'>101149</code> - Metal and Jewelry Arts + <code style='color: #333333; opacity: 0.9'>100709</code> - Army JROTC/ROTC + <code style='color: #333333; opacity: 0.9'>100707</code> - Air Force JROTC/ROTC + <code style='color: #333333; opacity: 0.9'>100946</code> - Juvenile Corrections + <code style='color: #333333; opacity: 0.9'>100711</code> - Navy/Marine Corps JROTC/ROTC + <code style='color: #333333; opacity: 0.9'>101407</code> - Business/Commerce, General + <code style='color: #333333; opacity: 0.9'>101444</code> - Finance, General + <code style='color: #333333; opacity: 0.9'>100598</code> - General Studies + <code style='color: #333333; opacity: 0.9'>100607</code> - Biology, General + <code style='color: #333333; opacity: 0.9'>101121</code> - Graphic Design + <code style='color: #333333; opacity: 0.9'>101139</code> - Art/Art Studies, General + <code style='color: #333333; opacity: 0.9'>101140</code> - Fine/Studio Arts, General + <code style='color: #333333; opacity: 0.9'>100885</code> - Geology/Earth Science, General + <code style='color: #333333; opacity: 0.9'>100996</code> - Geography + <code style='color: #333333; opacity: 0.9'>100631</code> - Microbiology, General + <code style='color: #333333; opacity: 0.9'>100583</code> - English Language and Literature, General + <code style='color: #333333; opacity: 0.9'>100239</code> - Educational Leadership and Administration, General + <code style='color: #333333; opacity: 0.9'>100140</code> - Communication, General + <code style='color: #333333; opacity: 0.9'>101115</code> - Design and Visual Communications, General + <code style='color: #333333; opacity: 0.9'>100608</code> - Biology/Biological Sciences, General + <code style='color: #333333; opacity: 0.9'>100176</code> - Information Technology + <code style='color: #333333; opacity: 0.9'>100173</code> - Computer and Information Sciences and Support Services + <code style='color: #333333; opacity: 0.9'>101465</code> - International Business + <code style='color: #333333; opacity: 0.9'>100372</code> - Industrial Engineering + <code style='color: #333333; opacity: 0.9'>100999</code> - International Relations and Affairs + <code style='color: #333333; opacity: 0.9'>101120</code> - Interior Design + <code style='color: #333333; opacity: 0.9'>101466</code> - International Business/Trade/Commerce + <code style='color: #333333; opacity: 0.9'>100196</code> - Computer/Information Technology Administration and Management + <code style='color: #333333; opacity: 0.9'>100122</code> - Spanish and Iberian Studies + <code style='color: #333333; opacity: 0.9'>100177</code> - Informatics + <code style='color: #333333; opacity: 0.9'>100773</code> - International/Global Studies + <code style='color: #333333; opacity: 0.9'>101478</code> - International Marketing + <code style='color: #333333; opacity: 0.9'>100602</code> - Library and Information Science + <code style='color: #333333; opacity: 0.9'>100174</code> - Computer and Information Sciences, General + <code style='color: #333333; opacity: 0.9'>101469</code> - Information Resources Management + <code style='color: #333333; opacity: 0.9'>100189</code> - Computer Science + <code style='color: #333333; opacity: 0.9'>101005</code> - Sociology + <code style='color: #333333; opacity: 0.9'>100597</code> - Liberal Arts and Sciences/Liberal Studies + <code style='color: #333333; opacity: 0.9'>100195</code> - Computer Systems Networking and Telecommunications + <code style='color: #333333; opacity: 0.9'>100979</code> - Social Work + <code style='color: #333333; opacity: 0.9'>100349</code> - Computer Software Engineering + <code style='color: #333333; opacity: 0.9'>101511</code> - History + <code style='color: #333333; opacity: 0.9'>101451</code> - Hospitality Administration/Management + <code style='color: #333333; opacity: 0.9'>101196</code> - Health/Health Care Administration/Management + <code style='color: #333333; opacity: 0.9'>101141</code> - Art History, Criticism and Conservation + <code style='color: #333333; opacity: 0.9'>101453</code> - Hotel/Motel Administration/Management + <code style='color: #333333; opacity: 0.9'>100358</code> - Environmental/Environmental Health Engineering + <code style='color: #333333; opacity: 0.9'>100599</code> - Humanities/Humanistic Studies + <code style='color: #333333; opacity: 0.9'>101307</code> - Public Health + <code style='color: #333333; opacity: 0.9'>100792</code> - Health and Physical Education/Fitness + <code style='color: #333333; opacity: 0.9'>101170</code> - Health Services/Allied Health/Health Sciences, General + <code style='color: #333333; opacity: 0.9'>100243</code> - Higher Education/Higher Education Administration + <code style='color: #333333; opacity: 0.9'>100972</code> - Human Services, General + <code style='color: #333333; opacity: 0.9'>100547</code> - Human Development and Family Studies, General + <code style='color: #333333; opacity: 0.9'>101464</code> - Human Resources Development + <code style='color: #333333; opacity: 0.9'>101171</code> - Health and Wellness, General + <code style='color: #333333; opacity: 0.9'>100938</code> - Homeland Security, Law Enforcement, Firefighting and Related Protective Services + <code style='color: #333333; opacity: 0.9'>101315</code> - Health Services Administration + <code style='color: #333333; opacity: 0.9'>101193</code> - Dental Hygiene/Hygienist + <code style='color: #333333; opacity: 0.9'>100540</code> - Foods, Nutrition, and Wellness Studies, General + <code style='color: #333333; opacity: 0.9'>100586</code> - Creative Writing + <code style='color: #333333; opacity: 0.9'>100198</code> - System, Networking, and LAN/WAN Management/Manager + <code style='color: #333333; opacity: 0.9'>101280</code> - Clinical/Medical Social Work + <code style='color: #333333; opacity: 0.9'>100200</code> - Web/Multimedia Management and Webmaster + <code style='color: #333333; opacity: 0.9'>100585</code> - Writing, General + <code style='color: #333333; opacity: 0.9'>100191</code> - Web Page, Digital/Multimedia and Information Resources Design + <code style='color: #333333; opacity: 0.9'>100133</code> - Women's Studies + <code style='color: #333333; opacity: 0.9'>100889</code> - Hydrology and Water Resources Science + <code style='color: #333333; opacity: 0.9'>100078</code> - Wildlife, Fish and Wildlands Science and Management + <code style='color: #333333; opacity: 0.9'>100642</code> - Wildlife Biology + <code style='color: #333333; opacity: 0.9'>100192</code> - Data Modeling/Warehousing and Database Administration + <code style='color: #333333; opacity: 0.9'>100346</code> - Water Resources Engineering + <code style='color: #333333; opacity: 0.9'>101163</code> - Woodwind Instruments + <code style='color: #333333; opacity: 0.9'>100065</code> - Water, Wetlands, and Marine Resources Management + <code style='color: #333333; opacity: 0.9'>101083</code> - Welding Technology/Welder + <code style='color: #333333; opacity: 0.9'>100074</code> - Wood Science and Wood Products/Pulp and Paper Technology + <code style='color: #333333; opacity: 0.9'>101030</code> - Plumbing and Related Water Supply Services + <code style='color: #333333; opacity: 0.9'>100564</code> - Law + <code style='color: #333333; opacity: 0.9'>100582</code> - English Language and Literature/Letters + <code style='color: #333333; opacity: 0.9'>100593</code> - English Literature (British and Commonwealth) + <code style='color: #333333; opacity: 0.9'>101411</code> - Logistics, Materials, and Supply Chain Management + <code style='color: #333333; opacity: 0.9'>100570</code> - Banking, Corporate, Finance, and Securities Law + <code style='color: #333333; opacity: 0.9'>100455</code> - Linguistics + <code style='color: #333333; opacity: 0.9'>100085</code> - Landscape Architecture + <code style='color: #333333; opacity: 0.9'>100600</code> - Library Science + <code style='color: #333333; opacity: 0.9'>100562</code> - Legal Studies, General + <code style='color: #333333; opacity: 0.9'>101256</code> - Clinical Laboratory Science/Medical Technology/Technologist + <code style='color: #333333; opacity: 0.9'>101461</code> - Labor and Industrial Relations + <code style='color: #333333; opacity: 0.9'>100574</code> - International Law and Legal Studies + <code style='color: #333333; opacity: 0.9'>100589</code> - Literature + <code style='color: #333333; opacity: 0.9'>101176</code> - Speech-Language Pathology/Pathologist + <code style='color: #333333; opacity: 0.9'>100280</code> - Elementary Education and Teaching + <code style='color: #333333; opacity: 0.9'>100854</code> - Theology/Theological Studies + <code style='color: #333333; opacity: 0.9'>100353</code> - Telecommunications Engineering + <code style='color: #333333; opacity: 0.9'>100830</code> - Theatre/Theater + <code style='color: #333333; opacity: 0.9'>100390</code> - Electrical, Electronic and Communications Engineering Technology/Technician + <code style='color: #333333; opacity: 0.9'>101452</code> - Tourism and Travel Services Management + <code style='color: #333333; opacity: 0.9'>101480</code> - Taxation + <code style='color: #333333; opacity: 0.9'>100434</code> - Computer Technology/Computer Systems Technology + <code style='color: #333333; opacity: 0.9'>101323</code> - Physical Therapy/Therapist + <code style='color: #333333; opacity: 0.9'>100224</code> - Culinary Arts/Chef Training + <code style='color: #333333; opacity: 0.9'>100258</code> - Special Education and Teaching + <code style='color: #333333; opacity: 0.9'>100250</code> - Educational/Instructional Technology + <code style='color: #333333; opacity: 0.9'>100282</code> - Secondary Education and Teaching + <code style='color: #333333; opacity: 0.9'>100287</code> - Early Childhood Education and Teaching + <code style='color: #333333; opacity: 0.9'>101380</code> - Registered Nursing/Registered Nurse + <code style='color: #333333; opacity: 0.9'>100688</code> - Neuroscience + <code style='color: #333333; opacity: 0.9'>100777</code> - Classical, Ancient Mediterranean and Near Eastern Studies and Archaeology + <code style='color: #333333; opacity: 0.9'>100363</code> - Naval Architecture and Marine Engineering + <code style='color: #333333; opacity: 0.9'>100771</code> - Natural Sciences + <code style='color: #333333; opacity: 0.9'>100218</code> - Cosmetology, Barber/Styling, and Nail Instructor + <code style='color: #333333; opacity: 0.9'>100364</code> - Nuclear Engineering + <code style='color: #333333; opacity: 0.9'>100197</code> - Network and System Administration/Administrator + <code style='color: #333333; opacity: 0.9'>101000</code> - National Security Policy Studies + <code style='color: #333333; opacity: 0.9'>100772</code> - Nutrition Sciences + <code style='color: #333333; opacity: 0.9'>100572</code> - Energy, Environment, and Natural Resources Law + <code style='color: #333333; opacity: 0.9'>100691</code> - Neurobiology and Behavior + <code style='color: #333333; opacity: 0.9'>100541</code> - Human Nutrition + <code style='color: #333333; opacity: 0.9'>100063</code> - Natural Resources Management and Policy + <code style='color: #333333; opacity: 0.9'>100060</code> - Natural Resources/Conservation, General + <code style='color: #333333; opacity: 0.9'>101384</code> - Family Practice Nurse/Nursing + <code style='color: #333333; opacity: 0.9'>101426</code> - Accounting and Finance + <code style='color: #333333; opacity: 0.9'>101445</code> - Banking and Financial Support Services + <code style='color: #333333; opacity: 0.9'>100116</code> - French Studies + <code style='color: #333333; opacity: 0.9'>100793</code> - Sport and Fitness Administration/Management + <code style='color: #333333; opacity: 0.9'>101119</code> - Fashion/Apparel Design + <code style='color: #333333; opacity: 0.9'>101134</code> - Film/Cinema/Video Studies + <code style='color: #333333; opacity: 0.9'>101446</code> - Financial Planning and Services + <code style='color: #333333; opacity: 0.9'>101489</code> - Fashion Merchandising + <code style='color: #333333; opacity: 0.9'>101135</code> - Cinematography and Film/Video Production + <code style='color: #333333; opacity: 0.9'>100544</code> - Facilities Planning and Management + <code style='color: #333333; opacity: 0.9'>100046</code> - Food Science + <code style='color: #333333; opacity: 0.9'>101447</code> - International Finance + <code style='color: #333333; opacity: 0.9'>100494</code> - French Language and Literature + <code style='color: #333333; opacity: 0.9'>101114</code> - Design and Applied Arts + <code style='color: #333333; opacity: 0.9'>101178</code> - Dentistry + <code style='color: #333333; opacity: 0.9'>101174</code> - Communication Sciences and Disorders, General + <code style='color: #333333; opacity: 0.9'>101125</code> - Drama and Dramatics/Theatre Arts, General + <code style='color: #333333; opacity: 0.9'>100993</code> - Development Economics and International Development + <code style='color: #333333; opacity: 0.9'>101297</code> - Pharmaceutics and Drug Design + <code style='color: #333333; opacity: 0.9'>100182</code> - Data Processing + <code style='color: #333333; opacity: 0.9'>100148</code> - Digital Communication and Media/Multimedia + <code style='color: #333333; opacity: 0.9'>101112</code> - Dance + <code style='color: #333333; opacity: 0.9'>101352</code> - Dietetics/Dietitian + <code style='color: #333333; opacity: 0.9'>100855</code> - Divinity/Ministry + <code style='color: #333333; opacity: 0.9'>100094</code> - American/United States Studies/Civilization + <code style='color: #333333; opacity: 0.9'>100081</code> - City/Urban, Community and Regional Planning + <code style='color: #333333; opacity: 0.9'>101006</code> - Urban Studies/Affairs + <code style='color: #333333; opacity: 0.9'>101512</code> - American History (United States) + <code style='color: #333333; opacity: 0.9'>101002</code> - American Government and Politics (United States) + <code style='color: #333333; opacity: 0.9'>100247</code> - Urban Education and Leadership + <code style='color: #333333; opacity: 0.9'>101240</code> - Diagnostic Medical Sonography/Sonographer and Ultrasound Technician + <code style='color: #333333; opacity: 0.9'>100066</code> - Land Use Planning and Management/Development + <code style='color: #333333; opacity: 0.9'>100862</code> - Urban Ministry + <code style='color: #333333; opacity: 0.9'>100073</code> - Urban Forestry + <code style='color: #333333; opacity: 0.9'>100211</code> - Make-Up Artist/Specialist + <code style='color: #333333; opacity: 0.9'>101198</code> - Health Unit Coordinator/Ward Clerk + <code style='color: #333333; opacity: 0.9'>101076</code> - Upholstery/Upholsterer + <code style='color: #333333; opacity: 0.9'>100475</code> - Ukrainian Language and Literature + <code style='color: #333333; opacity: 0.9'>100490</code> - Urdu Language and Literature + <code style='color: #333333; opacity: 0.9'>100112</code> - Ural-Altaic and Central Asian Studies + <code style='color: #333333; opacity: 0.9'>101199</code> - Health Unit Manager/Ward Supervisor + <code style='color: #333333; opacity: 0.9'>100124</code> - Ukraine Studies + <code style='color: #333333; opacity: 0.9'>100522</code> - Uralic Languages, Literatures, and Linguistics + <code style='color: #333333; opacity: 0.9'>100794</code> - Kinesiology and Exercise Science + <code style='color: #333333; opacity: 0.9'>101156</code> - Keyboard Instruments + <code style='color: #333333; opacity: 0.9'>101470</code> - Knowledge Management + <code style='color: #333333; opacity: 0.9'>100120</code> - Korean Studies + <code style='color: #333333; opacity: 0.9'>100463</code> - Korean Language and Literature + <code style='color: #333333; opacity: 0.9'>100226</code> - Food Preparation/Professional Cooking/Kitchen Assistant + <code style='color: #333333; opacity: 0.9'>100286</code> - Kindergarten/Preschool Education and Teaching + <code style='color: #333333; opacity: 0.9'>101326</code> - Kinesiotherapy/Kinesiotherapist + <code style='color: #333333; opacity: 0.9'>100516</code> - Khmer/Cambodian Language and Literature + <code style='color: #333333; opacity: 0.9'>100951</code> - Law Enforcement Record-Keeping and Evidence Management + <code style='color: #333333; opacity: 0.9'>100812</code> - Birthing and Parenting Knowledge and Skills + <code style='color: #333333; opacity: 0.9'>100811</code> - Health-Related Knowledge and Skills + <code style='color: #333333; opacity: 0.9'>100874</code> - Chemistry + <code style='color: #333333; opacity: 0.9'>100347</code> - Computer Engineering + <code style='color: #333333; opacity: 0.9'>100342</code> - Civil Engineering + <code style='color: #333333; opacity: 0.9'>100340</code> - Chemical Engineering + <code style='color: #333333; opacity: 0.9'>100350</code> - Electrical, Electronics and Communications Engineering + <code style='color: #333333; opacity: 0.9'>100990</code> - Economics + <code style='color: #333333; opacity: 0.9'>100351</code> - Electrical and Electronics Engineering + <code style='color: #333333; opacity: 0.9'>100331</code> - Engineering + <code style='color: #333333; opacity: 0.9'>100333</code> - Aerospace, Aeronautical and Astronautical Engineering + <code style='color: #333333; opacity: 0.9'>100337</code> - Biomedical/Medical Engineering + <code style='color: #333333; opacity: 0.9'>101479</code> - Real Estate + <code style='color: #333333; opacity: 0.9'>101330</code> - Veterinary Medicine + <code style='color: #333333; opacity: 0.9'>100168</code> - Animation, Interactive Technology, Video Graphics and Special Effects + <code style='color: #333333; opacity: 0.9'>101109</code> - Visual and Performing Arts + <code style='color: #333333; opacity: 0.9'>101325</code> - Vocational Rehabilitation Counseling/Counselor + <code style='color: #333333; opacity: 0.9'>101221</code> - Veterinary/Animal Health Technology/Technician and Veterinary Assistant + <code style='color: #333333; opacity: 0.9'>101332</code> - Veterinary Sciences/Veterinary Clinical Sciences, General + <code style='color: #333333; opacity: 0.9'>101157</code> - Voice and Opera + <code style='color: #333333; opacity: 0.9'>100633</code> - Virology + <code style='color: #333333; opacity: 0.9'>100019</code> - Viticulture and Enology + <code style='color: #333333; opacity: 0.9'>100162</code> - Photographic and Film/Video Technology/Technician and Assistant + <code style='color: #333333; opacity: 0.9'>101336</code> - Veterinary Pathology and Pathobiology + <code style='color: #333333; opacity: 0.9'>101133</code> - Film/Video and Photographic Arts + <code style='color: #333333; opacity: 0.9'>100658</code> - Vision Science/Physiological Optics + <code style='color: #333333; opacity: 0.9'>101402</code> - Practical Nursing, Vocational Nursing and Nursing Assistants + <code style='color: #333333; opacity: 0.9'>100194</code> - Modeling, Virtual Environments and Simulation + <code style='color: #333333; opacity: 0.9'>101341</code> - Veterinary Preventive Medicine, Epidemiology, and Public Health + <code style='color: #333333; opacity: 0.9'>101335</code> - Veterinary Microbiology and Immunobiology + <code style='color: #333333; opacity: 0.9'>100611</code> - Biochemistry + <code style='color: #333333; opacity: 0.9'>100674</code> - Biotechnology + <code style='color: #333333; opacity: 0.9'>101437</code> - Business/Corporate Communications + <code style='color: #333333; opacity: 0.9'>100638</code> - Zoology/Animal Biology + <code style='color: #333333; opacity: 0.9'>100613</code> - Molecular Biology + <code style='color: #333333; opacity: 0.9'>101547</code> - Zoological Medicine Residency Program + <code style='color: #333333; opacity: 0.9'>101423</code> - Accounting + <code style='color: #333333; opacity: 0.9'>100080</code> - Architecture + <code style='color: #333333; opacity: 0.9'>100152</code> - Advertising + <code style='color: #333333; opacity: 0.9'>100842</code> - Religion/Religious Studies + <code style='color: #333333; opacity: 0.9'>100141</code> - Speech Communication and Rhetoric + <code style='color: #333333; opacity: 0.9'>101036</code> - Mechanics and Repairers, General + <code style='color: #333333; opacity: 0.9'>100420</code> - Mechanical Engineering Related Technologies/Technicians + <code style='color: #333333; opacity: 0.9'>100097</code> - Russian, Central European, East European and Eurasian Studies + <code style='color: #333333; opacity: 0.9'>100147</code> - Radio and Television 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Field Of Study
        api_response = api_instance.get_field_of_study_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_field_of_study_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gender_get**
> GetStandardDataResponse get_gender_get()

Get Gender

 Lists common gender encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>Female</code> - Female: The candidate is a woman. + <code style='color: #333333; opacity: 0.9'>Male</code> - Male: The candidate is a man. + <code style='color: #333333; opacity: 0.9'>NotKnown</code> - Unknown: The gender is not provided. + <code style='color: #333333; opacity: 0.9'>Other</code> - Other: The gender is missing. + <code style='color: #333333; opacity: 0.9'>NotSpecified</code> - Not Specified: The gender is not specified. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Gender
        api_response = api_instance.get_gender_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_gender_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_industries_get**
> GetStandardDataResponse get_industries_get()

Get Industries

 Lists industry encodings based on [LinkedIn Industries](https://docs.microsoft.com/en-us/linkedin/shared/references/reference-tables/industry-codes). 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Industries
        api_response = api_instance.get_industries_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_industries_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_job_function_get**
> GetStandardDataResponse get_job_function_get()

Get Job Function

 Lists job function encodings based on LinkedIn Job Functions.  English example values:  + <code style='color: #333333; opacity: 0.9'>acct</code> - Accounting / Auditing + <code style='color: #333333; opacity: 0.9'>adm</code> - Administrative + <code style='color: #333333; opacity: 0.9'>advr</code> - Advertising + <code style='color: #333333; opacity: 0.9'>anls</code> - Analyst + <code style='color: #333333; opacity: 0.9'>art</code> - Art / Creative + <code style='color: #333333; opacity: 0.9'>bd</code> - Business Development + <code style='color: #333333; opacity: 0.9'>cnsl</code> - Consulting + <code style='color: #333333; opacity: 0.9'>cust</code> - Customer Service + <code style='color: #333333; opacity: 0.9'>dist</code> - Distribution + <code style='color: #333333; opacity: 0.9'>dsgn</code> - Design + <code style='color: #333333; opacity: 0.9'>edu</code> - Education + <code style='color: #333333; opacity: 0.9'>eng</code> - Engineering + <code style='color: #333333; opacity: 0.9'>fin</code> - Finance + <code style='color: #333333; opacity: 0.9'>genb</code> - General Business + <code style='color: #333333; opacity: 0.9'>hcpr</code> - HealthCare Provider + <code style='color: #333333; opacity: 0.9'>hr</code> - Human Resources + <code style='color: #333333; opacity: 0.9'>it</code> - Information Technology + <code style='color: #333333; opacity: 0.9'>lgl</code> - Legal + <code style='color: #333333; opacity: 0.9'>mgmt</code> - Management + <code style='color: #333333; opacity: 0.9'>mnfc</code> - Manufacturing + <code style='color: #333333; opacity: 0.9'>mrkt</code> - Marketing + <code style='color: #333333; opacity: 0.9'>othr</code> - Other + <code style='color: #333333; opacity: 0.9'>pr</code> - Public Relations + <code style='color: #333333; opacity: 0.9'>prch</code> - Purchasing + <code style='color: #333333; opacity: 0.9'>prdm</code> - Product Management + <code style='color: #333333; opacity: 0.9'>prjm</code> - Project Management + <code style='color: #333333; opacity: 0.9'>prod</code> - Production + <code style='color: #333333; opacity: 0.9'>qa</code> - QualityAssurance + <code style='color: #333333; opacity: 0.9'>rsch</code> - Research + <code style='color: #333333; opacity: 0.9'>sale</code> - Sales + <code style='color: #333333; opacity: 0.9'>sci</code> - Science + <code style='color: #333333; opacity: 0.9'>stra</code> - Strategy / Planning + <code style='color: #333333; opacity: 0.9'>supl</code> - Supply Chain + <code style='color: #333333; opacity: 0.9'>trng</code> - Training + <code style='color: #333333; opacity: 0.9'>wrt</code> - Writing / Editing 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Job Function
        api_response = api_instance.get_job_function_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_job_function_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobshift_type_get**
> GetStandardDataResponse get_jobshift_type_get()

Get Jobshift Type

 Lists common job shift type encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>DAY_SHIFT</code> - Day Shift + <code style='color: #333333; opacity: 0.9'>AFTERNOON_SHIFT</code> - Afternoon Shift + <code style='color: #333333; opacity: 0.9'>NIGHT_SHIFT</code> - Night Shift + <code style='color: #333333; opacity: 0.9'>FIXED_SHIFT</code> - Fixed Shift + <code style='color: #333333; opacity: 0.9'>ROTATING_SHIFT</code> - Rotating Shift + <code style='color: #333333; opacity: 0.9'>SPLIT_SHIFT</code> - Split Shift + <code style='color: #333333; opacity: 0.9'>ONCALL_SHIFT</code> - On-call Shift + <code style='color: #333333; opacity: 0.9'>WEEKDAY_SHIFT</code> - Weekday Shift + <code style='color: #333333; opacity: 0.9'>WEEKEND_SHIFT</code> - Weekend Shift 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>it</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Jobshift Type
        api_response = api_instance.get_jobshift_type_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_jobshift_type_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_code_get**
> GetStandardDataResponse get_license_code_get(license_type)

Get License Code

 Given a <code style='color: #333333; opacity: 0.9'>license_type</code>, this method lists the related level encodings.  See [Get License Type](https://api.inda.ai/hr/docs/v2/#operation/get_license_type__GET) to retrieve <code style='color: #333333; opacity: 0.9'>license_type</code> admissible values.  English example for **driving** license type values:  + <code style='color: #333333; opacity: 0.9'>A2</code> - A2: Motorcycles not exceeding a certain power level. The minimum age for category A2 is 18 years. + <code style='color: #333333; opacity: 0.9'>C1E</code> - C1E: A combination of vehicles consisting of a tractor vehicle in category B or C1 and a trailer or semi-trailer which are between mass. The minimum age for category C1E is 18 years. + <code style='color: #333333; opacity: 0.9'>D</code> - D: Motor vehicles designed and constructed for the carriage of more than eight passengers in addition to the driver. Motor vehicles which may be driven with a category D licence may be combined with a trailer having a maximum authorised mass which does not exceed 750 kg. + <code style='color: #333333; opacity: 0.9'>AM</code> - AM: Mopeds. + <code style='color: #333333; opacity: 0.9'>A1</code> - A1: Motorcycles and motor tricycles not exceeding a certain power level. The minimum age for category A1 is 16 years. + <code style='color: #333333; opacity: 0.9'>B1</code> - B1: Quadricycles. The minimum age for category B1 is 16 years. + <code style='color: #333333; opacity: 0.9'>D1</code> - D1: Motor vehicles or carriage of no more than 16 passengers including the driver and with a maximum length. Motor vehicles in this category may be combined with a trailer not exceeding a maximum authorised mass. The minimum age for categories D1 is 21 years. + <code style='color: #333333; opacity: 0.9'>B</code> - B: Motor vehicles not exceeding certain authorised mass. The minimum age for category B is 18 years. + <code style='color: #333333; opacity: 0.9'>C</code> - C: Motor vehicles whose maximum authorised exceed a mass and carriage of no more than eight passengers, including the driver. Motor vehicles in this category may be combined with a trailer not exceeding a maximum authorised mass. The minimum age for category C is 21 years. + <code style='color: #333333; opacity: 0.9'>DE</code> - DE: Combination of vehicles where the tractor vehicle is in category D and its trailer not exceeds a maximum authorised mass. The minimum age for categories DE is fixed at 24 years. + <code style='color: #333333; opacity: 0.9'>A</code> - A: Motor tricycles not exceeding a certain power level and a minimum age of 21 years. + <code style='color: #333333; opacity: 0.9'>BE</code> - BE: A combination of vehicles consisting of a tractor vehicle in category B and a trailer or semi-trailer not exceeding a certain mass. The minimum age for category BE is 18 years. + <code style='color: #333333; opacity: 0.9'>C1</code> - C1: Motor vehicles which are between mass. The minimum age for category C1 is 18 years. + <code style='color: #333333; opacity: 0.9'>CE</code> - CE: A combination of vehicles where the tractor vehicle is category C and its trailer or semi-trailer does not exceed a maximum authorised mass. The minimum age for categories CE is 21 years. + <code style='color: #333333; opacity: 0.9'>D1E</code> - D1E: A combination of vehicles where the tractor vehicle is category C1 and its trailer does not exceed a maximum authorised mass. The minimum age for categories D1E is fixed at 21 years. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    license_type = "license_type_example" # str | 
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get License Code
        api_response = api_instance.get_license_code_get(license_type)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_license_code_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get License Code
        api_response = api_instance.get_license_code_get(license_type, lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_license_code_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **license_type** | **str**|  |
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_license_type_get**
> GetStandardDataResponse get_license_type_get()

Get License Type

 Lists common license type encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>DRIVING</code> - Driving license 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get License Type
        api_response = api_instance.get_license_type_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_license_type_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_link_label_get**
> GetStandardDataResponse get_link_label_get()

Get Link Label

 Lists common link label encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>TWITTER</code> - Twitter + <code style='color: #333333; opacity: 0.9'>INSTAGRAM</code> - Instagram + <code style='color: #333333; opacity: 0.9'>LINKEDIN</code> - LinkedIn + <code style='color: #333333; opacity: 0.9'>GITHUB</code> - GitHub + <code style='color: #333333; opacity: 0.9'>YOUTUBE</code> - YouTube + <code style='color: #333333; opacity: 0.9'>FACEBOOK</code> - Facebook + <code style='color: #333333; opacity: 0.9'>WIKIPEDIA</code> - Wikipedia + <code style='color: #333333; opacity: 0.9'>OTHER</code> - Other 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Link Label
        api_response = api_instance.get_link_label_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_link_label_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_marital_status_get**
> GetStandardDataResponse get_marital_status_get()

Get Marital Status

 Lists common marital status encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>MARRIED</code> - Married + <code style='color: #333333; opacity: 0.9'>WIDOWED</code> - Widowed + <code style='color: #333333; opacity: 0.9'>SEPARATED</code> - Separated + <code style='color: #333333; opacity: 0.9'>DIVORCED</code> - Divorced + <code style='color: #333333; opacity: 0.9'>SINGLE</code> - Single + <code style='color: #333333; opacity: 0.9'>DOMESTIC_PARTNERSHIP</code> - Domestic partnership 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Marital Status
        api_response = api_instance.get_marital_status_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_marital_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_name_prefix_get**
> GetStandardDataResponse get_name_prefix_get()

Get Name Prefix

 Lists common name prefix encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>PROF</code> - Prof. + <code style='color: #333333; opacity: 0.9'>MR</code> - Mr. + <code style='color: #333333; opacity: 0.9'>MRS</code> - Mrs. + <code style='color: #333333; opacity: 0.9'>MX</code> - Mx. + <code style='color: #333333; opacity: 0.9'>MS</code> - Ms. + <code style='color: #333333; opacity: 0.9'>LAWYER</code> - Lawyer + <code style='color: #333333; opacity: 0.9'>MISS</code> - Miss. + <code style='color: #333333; opacity: 0.9'>DR</code> - Dr. + <code style='color: #333333; opacity: 0.9'>ENG</code> - Eng. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Name Prefix
        api_response = api_instance.get_name_prefix_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_name_prefix_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_name_suffix_get**
> GetStandardDataResponse get_name_suffix_get()

Get Name Suffix

 Lists common name suffix encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>SR</code> - Sr. + <code style='color: #333333; opacity: 0.9'>II</code> - II + <code style='color: #333333; opacity: 0.9'>III</code> - III + <code style='color: #333333; opacity: 0.9'>JR</code> - Jr. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Name Suffix
        api_response = api_instance.get_name_suffix_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_name_suffix_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_patent_status_get**
> GetStandardDataResponse get_patent_status_get()

Get Patent Status

 Lists common patent status encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>PatentPending</code> - Pending: The patent’s processing is pending. + <code style='color: #333333; opacity: 0.9'>PatentFiled</code> - Filed: The patent has been filed. + <code style='color: #333333; opacity: 0.9'>PatentIssued</code> - Issued: The patent has been issued. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Patent Status
        api_response = api_instance.get_patent_status_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_patent_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_phone_label_get**
> GetStandardDataResponse get_phone_label_get()

Get Phone Label

 Lists common phone label encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>BUSINESS</code> - Business + <code style='color: #333333; opacity: 0.9'>PERSONAL</code> - Personal + <code style='color: #333333; opacity: 0.9'>FAX</code> - Fax + <code style='color: #333333; opacity: 0.9'>OTHER</code> - Other 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Phone Label
        api_response = api_instance.get_phone_label_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_phone_label_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_protected_group_get**
> GetStandardDataResponse get_protected_group_get()

Get Protected Group

 Lists common protected group encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>ETHNICITY</code> - Ethnicity + <code style='color: #333333; opacity: 0.9'>NATIONAL_ORIGIN</code> - National Origin + <code style='color: #333333; opacity: 0.9'>RELIGION</code> - Religion + <code style='color: #333333; opacity: 0.9'>VETERAN_STATUS</code> - Veteran Status + <code style='color: #333333; opacity: 0.9'>GENETIC_INFORMATION</code> - Genetic Information + <code style='color: #333333; opacity: 0.9'>RACE</code> - Race + <code style='color: #333333; opacity: 0.9'>GENDER</code> - Gender + <code style='color: #333333; opacity: 0.9'>GENDER_IDENTITY</code> - Gender Identity + <code style='color: #333333; opacity: 0.9'>PREGNANCY</code> - Pregnancy + <code style='color: #333333; opacity: 0.9'>AGE</code> - Age + <code style='color: #333333; opacity: 0.9'>CITIZENSHIP_STATUS</code> - Citizenship Status + <code style='color: #333333; opacity: 0.9'>MARITAL_STATUS</code> - Marital Status + <code style='color: #333333; opacity: 0.9'>SEXUAL_ORIENTATION</code> - Sexual Orientation + <code style='color: #333333; opacity: 0.9'>DISABILITY</code> - Disability + <code style='color: #333333; opacity: 0.9'>FAMILIAL_STATUS</code> - Familial Status 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Protected Group
        api_response = api_instance.get_protected_group_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_protected_group_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remote_working_get**
> GetStandardDataResponse get_remote_working_get()

Get Remote Working

 Lists remote working options based on LinkedIn Remote Working.  English example values:  + <code style='color: #333333; opacity: 0.9'>ON-SITE</code> - On-site: Employees come to work in-person. + <code style='color: #333333; opacity: 0.9'>HYBRID</code> - Hybrid: Employees work on-site and off-site. + <code style='color: #333333; opacity: 0.9'>REMOTE</code> - Remote: Employees work off-site. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Remote Working
        api_response = api_instance.get_remote_working_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_remote_working_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_salary_frequency_get**
> GetStandardDataResponse get_salary_frequency_get()

Get Salary Frequency

 Lists common salary frequency encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>YEARLY</code> - Yearly + <code style='color: #333333; opacity: 0.9'>MONTHLY</code> - Monthly + <code style='color: #333333; opacity: 0.9'>WEEKLY</code> - Weekly + <code style='color: #333333; opacity: 0.9'>DAILY</code> - Daily + <code style='color: #333333; opacity: 0.9'>HOURLY</code> - Hourly 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Salary Frequency
        api_response = api_instance.get_salary_frequency_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_salary_frequency_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_salary_type_get**
> GetStandardDataResponse get_salary_type_get()

Get Salary Type

 Lists common salary type encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>NET</code> - Net + <code style='color: #333333; opacity: 0.9'>GROSS</code> - Gross 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.get_standard_data_response import GetStandardDataResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Salary Type
        api_response = api_instance.get_salary_type_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_salary_type_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetStandardDataResponse**](GetStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_seniority_level_get**
> GetExtendedStandardDataResponse get_seniority_level_get()

Get Seniority Level

 Lists common seniority level encodings.  English example values:  + <code style='color: #333333; opacity: 0.9'>1</code> - Unpaid + <code style='color: #333333; opacity: 0.9'>2</code> - Training + <code style='color: #333333; opacity: 0.9'>4</code> - Entry-level + <code style='color: #333333; opacity: 0.9'>7</code> - Senior + <code style='color: #333333; opacity: 0.9'>8</code> - Manager + <code style='color: #333333; opacity: 0.9'>9</code> - Director + <code style='color: #333333; opacity: 0.9'>11</code> - Vice President (VP) + <code style='color: #333333; opacity: 0.9'>12</code> - Chief X Officer (CxO) + <code style='color: #333333; opacity: 0.9'>13</code> - Partner + <code style='color: #333333; opacity: 0.9'>14</code> - Owner + <code style='color: #333333; opacity: 0.9'>3</code> - Internship + <code style='color: #333333; opacity: 0.9'>5</code> - Associate + <code style='color: #333333; opacity: 0.9'>6</code> - Mid-Senior level + <code style='color: #333333; opacity: 0.9'>10</code> - Executive + <code style='color: #333333; opacity: 0.9'>0</code> - Not Applicable 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import standardized_data_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.get_extended_standard_data_response import GetExtendedStandardDataResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: APIKey
configuration = inda_hr.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with inda_hr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = standardized_data_api.StandardizedDataApi(api_client)
    lang = "it" # str | The language in which the 'Value' is returned. Supported languages: <code style='color: #333333; opacity: 0.9'>it</code>, <code style='color: #333333; opacity: 0.9'>en</code>, <code style='color: #333333; opacity: 0.9'>es</code>, <code style='color: #333333; opacity: 0.9'>pt</code>, <code style='color: #333333; opacity: 0.9'>de</code>, <code style='color: #333333; opacity: 0.9'>fr</code>, <code style='color: #333333; opacity: 0.9'>pl</code> (optional) if omitted the server will use the default value of "it"
    codes = [
        None,
    ] # [bool, date, datetime, dict, float, int, list, str, none_type] | If <code style='color: #333333; opacity: 0.9'>null</code> the API returns all the corresponding <code style='color: #333333; opacity: 0.9'>lang</code> data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Seniority Level
        api_response = api_instance.get_seniority_level_get(lang=lang, codes=codes)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StandardizedDataApi->get_seniority_level_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lang** | **str**| The language in which the &#39;Value&#39; is returned. Supported languages: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;it&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;en&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;es&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pt&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;de&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;fr&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;pl&lt;/code&gt; | [optional] if omitted the server will use the default value of "it"
 **codes** | [**[bool, date, datetime, dict, float, int, list, str, none_type]**](bool, date, datetime, dict, float, int, list, str, none_type.md)| If &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;null&lt;/code&gt; the API returns all the corresponding &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;lang&lt;/code&gt; data. | [optional]

### Return type

[**GetExtendedStandardDataResponse**](GetExtendedStandardDataResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

