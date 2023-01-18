<a name="__pageTop"></a>
# inda_hr.apis.tags.company_management_api.CompanyManagementApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_company_post**](#add_company_post) | **post** /hr/v2/company/ | Add Company
[**company_autocomplete_get**](#company_autocomplete_get) | **get** /hr/v2/company/name/search/autocomplete/ | Company Autocomplete
[**get_company_get**](#get_company_get) | **get** /hr/v2/company/{company_id}/ | Get Company
[**patch_company_patch**](#patch_company_patch) | **patch** /hr/v2/company/{company_id}/ | Patch Company

# **add_company_post**
<a name="add_company_post"></a>
> CompanyIDResponse add_company_post(company_request)

Add Company

 This method adds a company to a shared database and assigns it a *CompanyID* (namely, a Unique Universal ID or UUID4). This method requires an application/json as content type body.  On the right, we provide an example of input structure; further details are available in dedicated sections.  After successfully adding the company to INDA, this method returns the assigned *CompanyID*.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import company_management_api
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

    # example passing only required values which don't have defaults set
    body = CompanyRequest(
        data=CompanyCommonData(
            type=CompanyCommonType(
                value="value_example",
            ),
            size=Size(
                value="value_example",
            ),
            description=BaseLocationsValueModelStrictStr(
                value="value_example",
            ),
            headquarters=[
                Headquarter(
                    name=BaseLocationsValueModelStrictStr(),
                    location=CompanyCommonLocation(
                        city=BaseLocationsValueModelStrictStr(),
                        country=BaseLocationsValueModelStrictStr(),
                        geo_coordinates=ValueModelMongoDBGeoLocation(
                            value=MongoDBGeoLocation(
                                lat=-90.0,
                                lon=-180.0,
                            ),
                        ),
                        country_code=BaseLocationsValueModelStrictStr(),
                        postal_code=BaseLocationsValueModelStrictStr(),
                        street_address=BaseLocationsValueModelStrictStr(),
                        county=BaseLocationsValueModelStrictStr(),
                        region=BaseLocationsValueModelStrictStr(),
                    ),
                )
            ],
            branches=[
                Branch(
                    name=BaseLocationsValueModelStrictStr(),
                    location=CompanyCommonLocation(),
                )
            ],
            industries=[
                CompanyCommonIndustry(
                    value="value_example",
                )
            ],
            specialties=[
                BaseLocationsValueModelStrictStr()
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
            link=JobadLinkLink(),
            products=[
                Asset(
                    name=BaseLocationsValueModelStrictStr(),
                    description=BaseLocationsValueModelStrictStr(),
                    sector=BaseLocationsValueModelStrictStr(),
                    tags=[
                        "tags_example"
                    ],
                )
            ],
            services=[
                Asset()
            ],
            related_companies=[
                RelatedCompany(
                    company_id="company_id_example",
                    relation=Relation(
                        value="value_example",
                    ),
                )
            ],
            name=BaseLocationsValueModelStrictStr(),
        ),
    )
    try:
        # Add Company
        api_response = api_instance.add_company_post(
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CompanyManagementApi->add_company_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CompanyRequest**](../../models/CompanyRequest.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#add_company_post.ApiResponseFor201) | Company Successfully Added
404 | [ApiResponseFor404](#add_company_post.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#add_company_post.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#add_company_post.ApiResponseFor422) | Validation Error

#### add_company_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CompanyIDResponse**](../../models/CompanyIDResponse.md) |  | 


#### add_company_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### add_company_post.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### add_company_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **company_autocomplete_get**
<a name="company_autocomplete_get"></a>
> CompanyAutocompleteResponse company_autocomplete_get(term)

Company Autocomplete

 This method performs company name autocompletion, based on INDA database of companies.  It helps users to explore the aforementioned database and search for companies data.  The *term* to be completed (see *query parameters* below) must contain at least *2* characters, and it is meant to match the *Name* of a company.  The output contains a list of names related to stored companies, along with their IDs.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import company_management_api
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

    # example passing only required values which don't have defaults set
    query_params = {
        'term': "term_example",
    }
    try:
        # Company Autocomplete
        api_response = api_instance.company_autocomplete_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CompanyManagementApi->company_autocomplete_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'term': "term_example",
        'size': 10,
        'token_order': "any",
        'fuzzy': False,
    }
    try:
        # Company Autocomplete
        api_response = api_instance.company_autocomplete_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CompanyManagementApi->company_autocomplete_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
term | TermSchema | | 
size | SizeSchema | | optional
token_order | TokenOrderSchema | | optional
fuzzy | FuzzySchema | | optional


# TermSchema

Token to be completed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Token to be completed | 

# SizeSchema

Response size.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Response size. | if omitted the server will use the default value of 10

# TokenOrderSchema

Whether to autocomplete the term in a sequential way or not. The default *any* value guarantees good performances as well as flexible results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Whether to autocomplete the term in a sequential way or not. The default *any* value guarantees good performances as well as flexible results. | must be one of ["any", "sequential", ] if omitted the server will use the default value of "any"

# FuzzySchema

Fuzzy search. If *True* performs a fuzzy search with max edits set to 2.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Fuzzy search. If *True* performs a fuzzy search with max edits set to 2. | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#company_autocomplete_get.ApiResponseFor200) | Successfully Found Companies
422 | [ApiResponseFor422](#company_autocomplete_get.ApiResponseFor422) | Validation Error

#### company_autocomplete_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CompanyAutocompleteResponse**](../../models/CompanyAutocompleteResponse.md) |  | 


#### company_autocomplete_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_company_get**
<a name="get_company_get"></a>
> GetCompanyResponse get_company_get(company_id)

Get Company

 This method returns the information related to the company stored with id *company_id*.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import company_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'company_id': "company_id_example",
    }
    try:
        # Get Company
        api_response = api_instance.get_company_get(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CompanyManagementApi->get_company_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
company_id | CompanyIdSchema | | 

# CompanyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_company_get.ApiResponseFor200) | Company Successfully Retrieved
404 | [ApiResponseFor404](#get_company_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#get_company_get.ApiResponseFor422) | Validation Error

#### get_company_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetCompanyResponse**](../../models/GetCompanyResponse.md) |  | 


#### get_company_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_company_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_company_patch**
<a name="patch_company_patch"></a>
> PatchCompanyResponse patch_company_patch(company_idpatch_company_request)

Patch Company

 This method updates the information related to the company stored with id *company_id*.  This method accepts an application/json body with the same structure as [Add Company](https://api.inda.ai/hr/docs/v2/#operation/add_company__POST), however in this case all fields are optional. Fields that contain differences between the corresponding original ones are substituted, while new fields are added. Bear in mind that lists are considered as singular value, therefore to modify an entry in a list it is necessary to insert the full list.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import company_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'company_id': "company_id_example",
    }
    body = PatchCompanyRequest(
        data=CompanyCommonOptionalData(
            type=CompanyCommonType(
                value="value_example",
            ),
            size=Size(
                value="value_example",
            ),
            description=BaseLocationsValueModelStrictStr(
                value="value_example",
            ),
            headquarters=[
                Headquarter(
                    name=BaseLocationsValueModelStrictStr(),
                    location=CompanyCommonLocation(
                        city=BaseLocationsValueModelStrictStr(),
                        country=BaseLocationsValueModelStrictStr(),
                        geo_coordinates=ValueModelMongoDBGeoLocation(
                            value=MongoDBGeoLocation(
                                lat=-90.0,
                                lon=-180.0,
                            ),
                        ),
                        country_code=BaseLocationsValueModelStrictStr(),
                        postal_code=BaseLocationsValueModelStrictStr(),
                        street_address=BaseLocationsValueModelStrictStr(),
                        county=BaseLocationsValueModelStrictStr(),
                        region=BaseLocationsValueModelStrictStr(),
                    ),
                )
            ],
            branches=[
                Branch(
                    name=BaseLocationsValueModelStrictStr(),
                    location=CompanyCommonLocation(),
                )
            ],
            industries=[
                CompanyCommonIndustry(
                    value="value_example",
                )
            ],
            specialties=[
                BaseLocationsValueModelStrictStr()
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
            link=JobadLinkLink(),
            products=[
                Asset(
                    name=BaseLocationsValueModelStrictStr(),
                    description=BaseLocationsValueModelStrictStr(),
                    sector=BaseLocationsValueModelStrictStr(),
                    tags=[
                        "tags_example"
                    ],
                )
            ],
            services=[
                Asset()
            ],
            related_companies=[
                RelatedCompany(
                    company_id="company_id_example",
                    relation=Relation(
                        value="value_example",
                    ),
                )
            ],
        ),
    )
    try:
        # Patch Company
        api_response = api_instance.patch_company_patch(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CompanyManagementApi->patch_company_patch: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchCompanyRequest**](../../models/PatchCompanyRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
company_id | CompanyIdSchema | | 

# CompanyIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_company_patch.ApiResponseFor200) | Company Successfully Updated
404 | [ApiResponseFor404](#patch_company_patch.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#patch_company_patch.ApiResponseFor422) | Validation Error

#### patch_company_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchCompanyResponse**](../../models/PatchCompanyResponse.md) |  | 


#### patch_company_patch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### patch_company_patch.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**HTTPValidationError**](../../models/HTTPValidationError.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

