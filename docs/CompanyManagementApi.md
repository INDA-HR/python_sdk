# inda_hr.CompanyManagementApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_company_post**](CompanyManagementApi.md#add_company_post) | **POST** /hr/v2/company/ | Add Company
[**company_autocomplete_get**](CompanyManagementApi.md#company_autocomplete_get) | **GET** /hr/v2/company/name/search/autocomplete/ | Company Autocomplete
[**get_company_get**](CompanyManagementApi.md#get_company_get) | **GET** /hr/v2/company/{company_id}/ | Get Company
[**patch_company_patch**](CompanyManagementApi.md#patch_company_patch) | **PATCH** /hr/v2/company/{company_id}/ | Patch Company


# **add_company_post**
> CompanyIDResponse add_company_post(company_request)

Add Company

 This method adds a company to a shared database and assigns it a *CompanyID* (namely, a Unique Universal ID or UUID4). This method requires an application/json as content type body.  On the right, we provide an example of input structure; further details are available in dedicated sections.  After successfully adding the company to INDA, this method returns the assigned *CompanyID*.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import company_management_api
from inda_hr.model.company_request import CompanyRequest
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.company_id_response import CompanyIDResponse
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
    api_instance = company_management_api.CompanyManagementApi(api_client)
    company_request = CompanyRequest(
        data=CompanyCommonData(
            type=CompanyCommonType(
                value="value_example",
            ),
            size=Size(
                value="value_example",
            ),
            description=BaseEmploymentsValueModelStrictStr(
                value="value_example",
            ),
            headquarters=[
                Headquarter(
                    name=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    location=CompanyCommonLocation(
                        city=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        country=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        geo_coordinates=ValueModelGeoLocation(
                            value=GeoLocation(
                                lat=-90.0,
                                lon=-180.0,
                            ),
                        ),
                        country_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        postal_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        street_address=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        county=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        region=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                ),
            ],
            branches=[
                Branch(
                    name=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    location=CompanyCommonLocation(
                        city=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        country=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        geo_coordinates=ValueModelGeoLocation(
                            value=GeoLocation(
                                lat=-90.0,
                                lon=-180.0,
                            ),
                        ),
                        country_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        postal_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        street_address=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        county=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        region=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                ),
            ],
            industries=[
                CompanyCommonIndustry(
                    value="value_example",
                ),
            ],
            specialties=[
                BaseEmploymentsValueModelStrictStr(
                    value="value_example",
                ),
            ],
            founded=FoundationYear(
                value="value_example",
            ),
            logo=JobadLinkLink(
                url=JobadLinkURL(
                    value="value_example",
                ),
                label=JobadLinkLinkLabel(
                    value="value_example",
                ),
            ),
            link=JobadLinkLink(
                url=JobadLinkURL(
                    value="value_example",
                ),
                label=JobadLinkLinkLabel(
                    value="value_example",
                ),
            ),
            products=[
                Asset(
                    name=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    description=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    sector=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    tags=[
                        "tags_example",
                    ],
                ),
            ],
            services=[
                Asset(
                    name=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    description=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    sector=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    tags=[
                        "tags_example",
                    ],
                ),
            ],
            related_companies=[
                RelatedCompany(
                    company_id="company_id_example",
                    relation=Relation(
                        value="value_example",
                    ),
                ),
            ],
            name=BaseEmploymentsValueModelStrictStr(
                value="value_example",
            ),
        ),
    ) # CompanyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Add Company
        api_response = api_instance.add_company_post(company_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CompanyManagementApi->add_company_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_request** | [**CompanyRequest**](CompanyRequest.md)|  |

### Return type

[**CompanyIDResponse**](CompanyIDResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Company Successfully Added |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_autocomplete_get**
> CompanyAutocompleteResponse company_autocomplete_get(term)

Company Autocomplete

 This method performs company name autocompletion, based on INDA database of companies.  It helps users to explore the aforementioned database and search for companies data.  The *term* to be completed (see *query parameters* below) must contain at least *2* characters, and it is meant to match the *Name* of a company.  The output contains a list of names related to stored companies, along with their IDs.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import company_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.company_autocomplete_response import CompanyAutocompleteResponse
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
    api_instance = company_management_api.CompanyManagementApi(api_client)
    term = "term_example" # str | Token to be completed

    # example passing only required values which don't have defaults set
    try:
        # Company Autocomplete
        api_response = api_instance.company_autocomplete_get(term)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CompanyManagementApi->company_autocomplete_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Token to be completed |

### Return type

[**CompanyAutocompleteResponse**](CompanyAutocompleteResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Found Companies |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_get**
> GetCompanyResponse get_company_get(company_id)

Get Company

 This method returns the information related to the company stored with id *company_id*.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import company_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.get_company_response import GetCompanyResponse
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
    api_instance = company_management_api.CompanyManagementApi(api_client)
    company_id = "company_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Company
        api_response = api_instance.get_company_get(company_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CompanyManagementApi->get_company_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |

### Return type

[**GetCompanyResponse**](GetCompanyResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company Successfully Retrieved |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_company_patch**
> PatchCompanyResponse patch_company_patch(company_id, patch_company_request)

Patch Company

 This method updates the information related to the company stored with id *company_id*.  This method accepts an application/json body with the same structure as [Add Company](https://api.inda.ai/hr/docs/v2/#operation/add_company__POST), however in this case all fields are optional. Fields that contain differences between the corresponding original ones are substituted, while new fields are added. Bear in mind that lists are considered as singular value, therefore to modify an entry in a list it is necessary to insert the full list.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import company_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.patch_company_request import PatchCompanyRequest
from inda_hr.model.patch_company_response import PatchCompanyResponse
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
    api_instance = company_management_api.CompanyManagementApi(api_client)
    company_id = "company_id_example" # str | 
    patch_company_request = PatchCompanyRequest(
        data=CompanyCommonOptionalData(
            type=CompanyCommonType(
                value="value_example",
            ),
            size=Size(
                value="value_example",
            ),
            description=JobadSectionsValueModelStrictStr(
                value="value_example",
            ),
            headquarters=[
                Headquarter(
                    name=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    location=CompanyCommonLocation(
                        city=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        country=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        geo_coordinates=ValueModelGeoLocation(
                            value=GeoLocation(
                                lat=-90.0,
                                lon=-180.0,
                            ),
                        ),
                        country_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        postal_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        street_address=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        county=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        region=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                ),
            ],
            branches=[
                Branch(
                    name=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    location=CompanyCommonLocation(
                        city=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        country=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        geo_coordinates=ValueModelGeoLocation(
                            value=GeoLocation(
                                lat=-90.0,
                                lon=-180.0,
                            ),
                        ),
                        country_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        postal_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        street_address=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        county=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        region=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                ),
            ],
            industries=[
                CompanyCommonIndustry(
                    value="value_example",
                ),
            ],
            specialties=[
                JobadSectionsValueModelStrictStr(
                    value="value_example",
                ),
            ],
            founded=FoundationYear(
                value="value_example",
            ),
            logo=JobadLinkLink(
                url=JobadLinkURL(
                    value="value_example",
                ),
                label=JobadLinkLinkLabel(
                    value="value_example",
                ),
            ),
            link=JobadLinkLink(
                url=JobadLinkURL(
                    value="value_example",
                ),
                label=JobadLinkLinkLabel(
                    value="value_example",
                ),
            ),
            products=[
                Asset(
                    name=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    description=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    sector=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    tags=[
                        "tags_example",
                    ],
                ),
            ],
            services=[
                Asset(
                    name=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    description=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    sector=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    tags=[
                        "tags_example",
                    ],
                ),
            ],
            related_companies=[
                RelatedCompany(
                    company_id="company_id_example",
                    relation=Relation(
                        value="value_example",
                    ),
                ),
            ],
        ),
    ) # PatchCompanyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Patch Company
        api_response = api_instance.patch_company_patch(company_id, patch_company_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CompanyManagementApi->patch_company_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**|  |
 **patch_company_request** | [**PatchCompanyRequest**](PatchCompanyRequest.md)|  |

### Return type

[**PatchCompanyResponse**](PatchCompanyResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company Successfully Updated |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

