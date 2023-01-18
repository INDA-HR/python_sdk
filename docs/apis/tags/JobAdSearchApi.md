<a name="__pageTop"></a>
# inda_hr.apis.tags.job_ad_search_api.JobAdSearchApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**full_text_search_on_jobads_post**](#full_text_search_on_jobads_post) | **post** /hr/v2/index/{indexname}/jobads/search/full-text/ | Full-Text Search on JobAds
[**search_applications_post**](#search_applications_post) | **post** /hr/v2/index/{indexname}/resume/{resume_id}/applications/jobads/search/ | Search Applications

# **full_text_search_on_jobads_post**
<a name="full_text_search_on_jobads_post"></a>
> FoundJobAdsResponse full_text_search_on_jobads_post(indexname)

Full-Text Search on JobAds

This is the most common way to search a text document through the job advertisements stored in the index *indexname*.  This function takes as input a list of objects containing the terms you wish to search for, please consider that tokens (individual words) grouped together in the same *QueryTerms* element will be queried separately in an **OR** clause, whereas different *QueryTerms* elements will be joined by an **AND** clause. To put it in words, the query will retrieve documents that match at least one word from each element in *QueryTerms*.  This behaviour can be modified in one of two ways:  + The **default_operator** query parameter, which defaults to OR, can be set to AND in order to only find documents that contain ALL of the tokens in a given *query_terms* element. + The **\"** (double quotes) operator, which can be used to wrap strings made up of multiple tokens in order to find documents that contain those words exactly in the order they are presented (sentence match). Remember to escape double quotes in your JSON inputs with a backslash.  Each *QueryTerms* element can be negated with the parameter **Exclude** set to *true*. This is equivalent to setting it in a **NOT** clause.  It's also possible to use wildcards to perform jolly searches, the supported wildcards are:  + \\*: Can be used to match any number of characters in the middle (ad\\*ment) or at the end (doc\\*) of a word. + ?: Can be used to match a single character in any position (?xample).  All queries are case-insensitive and have some amount of fuzziness by default, meaning that typos and character transpositions will be included in the matches. Additionally, filters can be added to form boolean queries on indexed fields. For a comprehensive list and explanation of filters, see the [*Query Filters*](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) section, the structure is the same.  Query parameters are used to specify the *offset* and *size* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored; in order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  The use of caching is highly recommended to improve the performances.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_search_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.found_job_ads_response import FoundJobAdsResponse
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.job_ad_full_text_search import JobAdFullTextSearch
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
    api_instance = job_ad_search_api.JobAdSearchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    try:
        # Full-Text Search on JobAds
        api_response = api_instance.full_text_search_on_jobads_post(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdSearchApi->full_text_search_on_jobads_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'default_operator': "OR",
        'cache': True,
        'cache_time': 300,
        'size': 50,
        'offset': 0,
        'min_score': 0,
        'search_id': "search_id_example",
    }
    body = JobAdFullTextSearch(
        query_terms=[
            JobadRequestsSimpleTerm(
                term="term_example",
                exclude=False,
            )
        ],
        query_filters=QueryFilters(
            must=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value=dict(),
                )
            ],
            should=[
                FilterField()
            ],
            must_not=[
                FilterField()
            ],
            filter=[
                FilterField()
            ],
        ),
    )
    try:
        # Full-Text Search on JobAds
        api_response = api_instance.full_text_search_on_jobads_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdSearchApi->full_text_search_on_jobads_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
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
[**JobAdFullTextSearch**](../../models/JobAdFullTextSearch.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
default_operator | DefaultOperatorSchema | | optional
cache | CacheSchema | | optional
cache_time | CacheTimeSchema | | optional
size | SizeSchema | | optional
offset | OffsetSchema | | optional
min_score | MinScoreSchema | | optional
search_id | SearchIdSchema | | optional


# DefaultOperatorSchema

Optional. Change this to *AND* if you wish documents to match ALLof the tokens in a single query_terms element.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Change this to *AND* if you wish documents to match ALLof the tokens in a single query_terms element. | must be one of ["AND", "OR", ] if omitted the server will use the default value of "OR"

# CacheSchema

Optional. Whether the search results should be cached or not.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Optional. Whether the search results should be cached or not. | if omitted the server will use the default value of True

# CacheTimeSchema

Optional. Seconds. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>false</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Seconds. Ignored if *cache* is &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;false&lt;/code&gt;. | if omitted the server will use the default value of 300

# SizeSchema

Optional. Number of documents to return.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to return. | if omitted the server will use the default value of 50

# OffsetSchema

Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to skip. Ignored if *cache* is &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;true&lt;/code&gt;. | if omitted the server will use the default value of 0

# MinScoreSchema

Optional. Minimum pertinence score.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Optional. Minimum pertinence score. | if omitted the server will use the default value of 0

# SearchIdSchema

Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#full_text_search_on_jobads_post.ApiResponseFor200) | Successful Response
415 | [ApiResponseFor415](#full_text_search_on_jobads_post.ApiResponseFor415) | Unsupported Media Type
400 | [ApiResponseFor400](#full_text_search_on_jobads_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#full_text_search_on_jobads_post.ApiResponseFor422) | Validation Error

#### full_text_search_on_jobads_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FoundJobAdsResponse**](../../models/FoundJobAdsResponse.md) |  | 


#### full_text_search_on_jobads_post.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### full_text_search_on_jobads_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### full_text_search_on_jobads_post.ApiResponseFor422
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

# **search_applications_post**
<a name="search_applications_post"></a>
> FoundJobAdsResponse search_applications_post(indexnameresume_id)

Search Applications

This method is meant to return those job advertisements that the resume of ID *resume_id* have applied to, if they respect the given query.  Users may specify [query filters](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) to apply on both [Applications](https://api.inda.ai/hr/docs/v2/#tag/Application-Management) and [JobAds](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Management) indexed fields.  Query parameters are used to specify the *cache_time* and *size* of the search. The method will automatically cache each search for *cache_time* seconds. In order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_search_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.job_ad_search_query import JobAdSearchQuery
from inda_hr.model.found_job_ads_response import FoundJobAdsResponse
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
    api_instance = job_ad_search_api.JobAdSearchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
    }
    try:
        # Search Applications
        api_response = api_instance.search_applications_post(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdSearchApi->search_applications_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
        'cache_time': 300,
        'size': 50,
        'search_id': "search_id_example",
    }
    body = JobAdSearchQuery(
        query_filters=BaseJobAdSearchQuery(
            application=QueryFilters(
                must=[
                    FilterField(
                        field="field_example",
                        type="type_example",
                        value=dict(),
                    )
                ],
                should=[
                    FilterField()
                ],
                must_not=[
                    FilterField()
                ],
                filter=[
                    FilterField()
                ],
            ),
            job_ad=QueryFilters(),
        ),
    )
    try:
        # Search Applications
        api_response = api_instance.search_applications_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdSearchApi->search_applications_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
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
[**JobAdSearchQuery**](../../models/JobAdSearchQuery.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cache_time | CacheTimeSchema | | optional
size | SizeSchema | | optional
search_id | SearchIdSchema | | optional


# CacheTimeSchema

Optional. Seconds.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Seconds. | if omitted the server will use the default value of 300

# SizeSchema

Optional. Number of documents to return.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to return. | if omitted the server will use the default value of 50

# SearchIdSchema

Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 
resume_id | ResumeIdSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResumeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_applications_post.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#search_applications_post.ApiResponseFor404) | Not Found
415 | [ApiResponseFor415](#search_applications_post.ApiResponseFor415) | Unsupported Media Type
400 | [ApiResponseFor400](#search_applications_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#search_applications_post.ApiResponseFor422) | Validation Error

#### search_applications_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FoundJobAdsResponse**](../../models/FoundJobAdsResponse.md) |  | 


#### search_applications_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_applications_post.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_applications_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_applications_post.ApiResponseFor422
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

