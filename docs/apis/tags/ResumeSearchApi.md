<a name="__pageTop"></a>
# inda_hr.apis.tags.resume_search_api.ResumeSearchApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**full_text_search_on_resumes_post**](#full_text_search_on_resumes_post) | **post** /hr/v2/index/{indexname}/resumes/search/full-text/ | Full-Text Search on Resumes
[**search_applicants_post**](#search_applicants_post) | **post** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resumes/search/ | Search Applicants
[**search_resumes_evidence_post**](#search_resumes_evidence_post) | **post** /hr/v2/index/{indexname}/resumes/search/semantic/evidence/ | Search Resumes Evidence
[**search_resumes_post**](#search_resumes_post) | **post** /hr/v2/index/{indexname}/resumes/search/semantic/ | Search Resumes

# **full_text_search_on_resumes_post**
<a name="full_text_search_on_resumes_post"></a>
> FoundDocsResponse full_text_search_on_resumes_post(indexname)

Full-Text Search on Resumes

This is the most common way to search a text document through the resumes stored in the index *indexname*. This function takes as input a list of objects containing the terms you wish to search for, please consider that tokens (individual words) grouped together in the same *QueryTerms* element will be queried separately in an **OR** clause, whereas different *QueryTerms* elements will be joined by an **AND** clause. To put it in words, the query will retrieve documents that match at least one word from each element in *QueryTerms*.  This behaviour can be modified in one of two ways:  + The **default_operator** query parameter, which defaults to OR, can be set to AND in order to only find documents that contain ALL of the tokens in a given *QueryTerms* element. + The **\"** (double quotes) operator, which can be used to wrap strings made up of multiple tokens in order to find documents that contain those words exactly in the order they are presented (sentence match). Remember to escape double quotes in your JSON inputs with a backslash.  Each *QueryTerms* element can be negated with the parameter **Exclude** set to *true*. This is equivalent to setting it in a **NOT** clause.  It's also possible to use wildcards to perform jolly searches, the supported wildcards are:  + \\*: Can be used to match any number of characters in the middle (ad\\*ment) or at the end (doc\\*) of a word. + ?: Can be used to match a single character in any position (?xample).  All queries are case-insensitive and have some amount of fuzziness by default, meaning that typos and character transpositions will be included in the matches. Additionally, filters can be added to form boolean queries on indexed fields. For a comprehensive list and explanation of filters, see the [*Query Filters*](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) section, the structure is the same.  The method returns a list of JSON documents, each of which contains a resume; the resumes are sorted according to a **pertinence score** determined by their relevance to the used query terms.  Query parameters are used to specify the *offset*, *size* and *min_score* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored because it's meant navigate the entire search response (in chunks of size *size*) through the *search_id*. The use of caching is highly recommended to improve the performance. Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_search_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.found_docs_response import FoundDocsResponse
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.traditional_docs_search_query import TraditionalDocsSearchQuery
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
    api_instance = resume_search_api.ResumeSearchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    try:
        # Full-Text Search on Resumes
        api_response = api_instance.full_text_search_on_resumes_post(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->full_text_search_on_resumes_post: %s\n" % e)

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
    body = TraditionalDocsSearchQuery(
        query_terms=[
            SemanticCommonSimpleTerm(
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
        # Full-Text Search on Resumes
        api_response = api_instance.full_text_search_on_resumes_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->full_text_search_on_resumes_post: %s\n" % e)
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
[**TraditionalDocsSearchQuery**](../../models/TraditionalDocsSearchQuery.md) |  | 


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
200 | [ApiResponseFor200](#full_text_search_on_resumes_post.ApiResponseFor200) | Successful Response
415 | [ApiResponseFor415](#full_text_search_on_resumes_post.ApiResponseFor415) | Unsupported Media Type
400 | [ApiResponseFor400](#full_text_search_on_resumes_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#full_text_search_on_resumes_post.ApiResponseFor422) | Validation Error

#### full_text_search_on_resumes_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FoundDocsResponse**](../../models/FoundDocsResponse.md) |  | 


#### full_text_search_on_resumes_post.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### full_text_search_on_resumes_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### full_text_search_on_resumes_post.ApiResponseFor422
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

# **search_applicants_post**
<a name="search_applicants_post"></a>
> FoundCandidatesResponse search_applicants_post(indexnamejobad_id)

Search Applicants

This method is meant to return those applicants (i.e., resumes) of the job advert with ID *jobad_id* that respect the given query.  Users may specify [query filters](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) to apply on both [Applications](https://api.inda.ai/hr/docs/v2/#tag/Application-Management) and [Resumes](https://api.inda.ai/hr/docs/v2/#tag/Resume-Management) indexed fields.  Query parameters are used to specify the *cache_time* and *size* of the search. The method will automatically cache each search for *cache_time* seconds. In order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_search_api
from inda_hr.model.found_candidates_response import FoundCandidatesResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.candidate_search_query import CandidateSearchQuery
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
    api_instance = resume_search_api.ResumeSearchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
    }
    query_params = {
    }
    try:
        # Search Applicants
        api_response = api_instance.search_applicants_post(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_applicants_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
    }
    query_params = {
        'cache_time': 300,
        'size': 50,
        'search_id': "search_id_example",
    }
    body = CandidateSearchQuery(
        query_filters=BaseCandidateSearchQuery(
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
            resume=QueryFilters(),
        ),
    )
    try:
        # Search Applicants
        api_response = api_instance.search_applicants_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_applicants_post: %s\n" % e)
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
[**CandidateSearchQuery**](../../models/CandidateSearchQuery.md) |  | 


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
jobad_id | JobadIdSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["auto", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", ] 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#search_applicants_post.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#search_applicants_post.ApiResponseFor404) | Not Found
415 | [ApiResponseFor415](#search_applicants_post.ApiResponseFor415) | Unsupported Media Type
400 | [ApiResponseFor400](#search_applicants_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#search_applicants_post.ApiResponseFor422) | Validation Error

#### search_applicants_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FoundCandidatesResponse**](../../models/FoundCandidatesResponse.md) |  | 


#### search_applicants_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_applicants_post.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_applicants_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_applicants_post.ApiResponseFor422
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

# **search_resumes_evidence_post**
<a name="search_resumes_evidence_post"></a>
> [SearchEvidence] search_resumes_evidence_post(indexnameevidence_request)

Search Resumes Evidence

Provides evidence for [Search Resumes](https://api.inda.ai/hr/docs/v2/#operation/search_resumes__POST) by returning the *size* most relevant words in each resume *resume_id* (listed into the list *resume_ids*) with respect to the *QueryTerms*. Note that -- unlike in the Related Words methods ([Similar Words](https://api.inda.ai/hr/docs/v2/#operation/similar_words__POST) and [Similar Words In Doc](https://api.inda.ai/hr/docs/v2/#operation/similar_words_in_resume__POST)) -- the elements of *QueryTerms* are combined together. Hence, the output minimizes the distance from all query terms simultaneously.  It returns a list of objects each containing the resume *resume_id* (*ID*) and a list of *Terms*.  Any *resume_id* not corresponding to an available resume in the index *indexname* will be ignored.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_search_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.search_evidence import SearchEvidence
from inda_hr.model.evidence_request import EvidenceRequest
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
    api_instance = resume_search_api.ResumeSearchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    body = EvidenceRequest(
        query_terms=[
            WeightedQueryTerm(
                term="term_example",
                language="it",
                weight=1.0,
            )
        ],
        resume_ids=[
            "resume_ids_example"
        ],
    )
    try:
        # Search Resumes Evidence
        api_response = api_instance.search_resumes_evidence_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_resumes_evidence_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'size': 3,
        'src_lang': "it",
    }
    body = EvidenceRequest(
        query_terms=[
            WeightedQueryTerm(
                term="term_example",
                language="it",
                weight=1.0,
            )
        ],
        resume_ids=[
            "resume_ids_example"
        ],
    )
    try:
        # Search Resumes Evidence
        api_response = api_instance.search_resumes_evidence_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_resumes_evidence_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
[**EvidenceRequest**](../../models/EvidenceRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
size | SizeSchema | | optional
src_lang | SrcLangSchema | | optional


# SizeSchema

Number of elements to be returned, must be greater than <code style='color: #333333; opacity: 0.9'>0</code> and smaller or equal to <code style='color: #333333; opacity: 0.9'>5</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Number of elements to be returned, must be greater than &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;0&lt;/code&gt; and smaller or equal to &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;5&lt;/code&gt;. | if omitted the server will use the default value of 3

# SrcLangSchema

Queries language. If left empty each query's language will detected automatically, if not it is not explicitly set into the request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Queries language. If left empty each query&#x27;s language will detected automatically, if not it is not explicitly set into the request body. | must be one of ["it", "en", "fr", "de", "pt", "es", ] 

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
200 | [ApiResponseFor200](#search_resumes_evidence_post.ApiResponseFor200) | Successfully Found Evidence
400 | [ApiResponseFor400](#search_resumes_evidence_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#search_resumes_evidence_post.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#search_resumes_evidence_post.ApiResponseFor422) | Unprocessable Entity

#### search_resumes_evidence_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**SearchEvidence**]({{complexTypePrefix}}SearchEvidence.md) | [**SearchEvidence**]({{complexTypePrefix}}SearchEvidence.md) | [**SearchEvidence**]({{complexTypePrefix}}SearchEvidence.md) |  | 

#### search_resumes_evidence_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_resumes_evidence_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_resumes_evidence_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **search_resumes_post**
<a name="search_resumes_post"></a>
> FoundDocsResponse search_resumes_post(indexname)

Search Resumes

This method performs a semantic search of resumes in index *indexname* according to the given query.  Compared with traditional search engines, *INDA Semantic Search* enables users to search in a pool of resumes in a more flexible way: search results are not limited to term matches but they include all resumes that are semantically close to the query.  Furthermore, in order to tackle the bias problem, INDA automatically ignores specific fields (such as name, gender, age and nationality) during the initial processing of each candidate data. We are constantly working on reduce the bias in original data so that INDA results may be as fair as possible.  The semantic search can be complemented with a traditional filter-based search through the [filters](https://api.inda.ai/hr/docs/v2/#tag/Search) built inside the *QueryFilters* field.  The desired query must be specified in the application/json content type body (see the example on the right). The elements of *QueryTerms* are mandatory and each of them must be associated with a weight between <code style='color: #333333; opacity: 0.9'>0</code> and <code style='color: #333333; opacity: 0.9'>1</code>, which determines the importance of the term in the search.  The method returns a list of JSON documents, each of which contains a resume; the resumes are sorted according to a **pertinence score** determined on the basis of their semantic similarity with the query terms. Note that each resume is evaluated based on the semantic similarity with respect to all query terms (where each query term is weighted according to its *weight*).  Query parameters are used to specify the *offset*, *size* and *min_score* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored because to navigate the entire search response (in chunks of size *size*) through the *search_id*. The use of caching is highly recommended to improve the performance. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Please consider to use the [Semantic Search Feedback](https://api.inda.ai/hr/docs/v2/#operation/semantic_search_feedback__POST) to evaluate the provided ranking  of resumes. It is very useful to improve our algorithms' performances.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_search_api
from inda_hr.model.docs_search_query import DocsSearchQuery
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.found_docs_response import FoundDocsResponse
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
    api_instance = resume_search_api.ResumeSearchApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    try:
        # Search Resumes
        api_response = api_instance.search_resumes_post(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_resumes_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'cache': True,
        'cache_time': 300,
        'size': 50,
        'offset': 0,
        'min_score': 0,
        'search_id': "search_id_example",
        'src_lang': "it",
        'dst_lang': [
        "es"
    ],
    }
    body = DocsSearchQuery(
        query_terms=[
            WeightedQueryTerm(
                term="term_example",
                language="it",
                weight=1.0,
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
        # Search Resumes
        api_response = api_instance.search_resumes_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_resumes_post: %s\n" % e)
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
[**DocsSearchQuery**](../../models/DocsSearchQuery.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cache | CacheSchema | | optional
cache_time | CacheTimeSchema | | optional
size | SizeSchema | | optional
offset | OffsetSchema | | optional
min_score | MinScoreSchema | | optional
search_id | SearchIdSchema | | optional
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional


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

# SrcLangSchema

Queries language. If left empty each query's language will detected automatically, if not it is not explicitly set into the request body.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Queries language. If left empty each query&#x27;s language will detected automatically, if not it is not explicitly set into the request body. | must be one of ["it", "en", "fr", "de", "pt", "es", ] 

# DstLangSchema

Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["es", "de", "pt", "fr", "en", "it", ] 

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
200 | [ApiResponseFor200](#search_resumes_post.ApiResponseFor200) | Successful Response
415 | [ApiResponseFor415](#search_resumes_post.ApiResponseFor415) | Unsupported Media Type
400 | [ApiResponseFor400](#search_resumes_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#search_resumes_post.ApiResponseFor422) | Unprocessable Entity

#### search_resumes_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FoundDocsResponse**](../../models/FoundDocsResponse.md) |  | 


#### search_resumes_post.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_resumes_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_resumes_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

