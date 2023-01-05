# inda_hr.ResumeSearchApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**full_text_search_on_resumes_post**](ResumeSearchApi.md#full_text_search_on_resumes_post) | **POST** /hr/v2/index/{indexname}/resumes/search/full-text/ | Full-Text Search on Resumes
[**search_applicants_post**](ResumeSearchApi.md#search_applicants_post) | **POST** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resumes/search/ | Search Applicants
[**search_resumes_evidence_post**](ResumeSearchApi.md#search_resumes_evidence_post) | **POST** /hr/v2/index/{indexname}/resumes/search/semantic/evidence/ | Search Resumes Evidence
[**search_resumes_post**](ResumeSearchApi.md#search_resumes_post) | **POST** /hr/v2/index/{indexname}/resumes/search/semantic/ | Search Resumes


# **full_text_search_on_resumes_post**
> FoundDocsResponse full_text_search_on_resumes_post(indexname)

Full-Text Search on Resumes

This is the most common way to search a text document through the resumes stored in the index *indexname*. This function takes as input a list of objects containing the terms you wish to search for, please consider that tokens (individual words) grouped together in the same *QueryTerms* element will be queried separately in an **OR** clause, whereas different *QueryTerms* elements will be joined by an **AND** clause. To put it in words, the query will retrieve documents that match at least one word from each element in *QueryTerms*.  This behaviour can be modified in one of two ways:  + The **default_operator** query parameter, which defaults to OR, can be set to AND in order to only find documents that contain ALL of the tokens in a given *QueryTerms* element. + The **\"** (double quotes) operator, which can be used to wrap strings made up of multiple tokens in order to find documents that contain those words exactly in the order they are presented (sentence match). Remember to escape double quotes in your JSON inputs with a backslash.  Each *QueryTerms* element can be negated with the parameter **Exclude** set to *true*. This is equivalent to setting it in a **NOT** clause.  It's also possible to use wildcards to perform jolly searches, the supported wildcards are:  + \\*: Can be used to match any number of characters in the middle (ad\\*ment) or at the end (doc\\*) of a word. + ?: Can be used to match a single character in any position (?xample).  All queries are case-insensitive and have some amount of fuzziness by default, meaning that typos and character transpositions will be included in the matches. Additionally, filters can be added to form boolean queries on indexed fields. For a comprehensive list and explanation of filters, see the [*Query Filters*](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) section, the structure is the same.  The method returns a list of JSON documents, each of which contains a resume; the resumes are sorted according to a **pertinence score** determined by their relevance to the used query terms.  Query parameters are used to specify the *offset*, *size* and *min_score* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored because it's meant navigate the entire search response (in chunks of size *size*) through the *search_id*. The use of caching is highly recommended to improve the performance. Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import resume_search_api
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
    indexname = "indexname_example" # str | 
    default_operator = "OR" # str | Optional. Change this to *AND* if you wish documents to match ALLof the tokens in a single query_terms element. (optional) if omitted the server will use the default value of "OR"
    cache = True # bool | Optional. Whether the search results should be cached or not. (optional) if omitted the server will use the default value of True
    cache_time = 300 # int | Optional. Seconds. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>false</code>. (optional) if omitted the server will use the default value of 300
    size = 50 # int | Optional. Number of documents to return. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>. (optional) if omitted the server will use the default value of 0
    min_score = 0 # float | Optional. Minimum pertinence score. (optional) if omitted the server will use the default value of 0
    search_id = "search_id_example" # str | Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. (optional)
    traditional_docs_search_query = TraditionalDocsSearchQuery(
        query_terms=[
            SemanticCommonSimpleTerm(
                term="term_example",
                exclude=False,
            ),
        ],
        query_filters=QueryFilters(
            must=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            should=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            must_not=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            filter=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
        ),
    ) # TraditionalDocsSearchQuery |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Full-Text Search on Resumes
        api_response = api_instance.full_text_search_on_resumes_post(indexname)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->full_text_search_on_resumes_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Full-Text Search on Resumes
        api_response = api_instance.full_text_search_on_resumes_post(indexname, default_operator=default_operator, cache=cache, cache_time=cache_time, size=size, offset=offset, min_score=min_score, search_id=search_id, traditional_docs_search_query=traditional_docs_search_query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->full_text_search_on_resumes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **default_operator** | **str**| Optional. Change this to *AND* if you wish documents to match ALLof the tokens in a single query_terms element. | [optional] if omitted the server will use the default value of "OR"
 **cache** | **bool**| Optional. Whether the search results should be cached or not. | [optional] if omitted the server will use the default value of True
 **cache_time** | **int**| Optional. Seconds. Ignored if *cache* is &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;false&lt;/code&gt;. | [optional] if omitted the server will use the default value of 300
 **size** | **int**| Optional. Number of documents to return. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| Optional. Number of documents to skip. Ignored if *cache* is &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;true&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **min_score** | **float**| Optional. Minimum pertinence score. | [optional] if omitted the server will use the default value of 0
 **search_id** | **str**| Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. | [optional]
 **traditional_docs_search_query** | [**TraditionalDocsSearchQuery**](TraditionalDocsSearchQuery.md)|  | [optional]

### Return type

[**FoundDocsResponse**](FoundDocsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**415** | Unsupported Media Type |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_applicants_post**
> FoundCandidatesResponse search_applicants_post(indexname, jobad_id)

Search Applicants

This method is meant to return those applicants (i.e., resumes) of the job advert with ID *jobad_id* that respect the given query.  Users may specify [query filters](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) to apply on both [Applications](https://api.inda.ai/hr/docs/v2/#tag/Application-Management) and [Resumes](https://api.inda.ai/hr/docs/v2/#tag/Resume-Management) indexed fields.  Query parameters are used to specify the *cache_time* and *size* of the search. The method will automatically cache each search for *cache_time* seconds. In order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import resume_search_api
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
    indexname = "indexname_example" # str | 
    jobad_id = JobadId(None) # JobadId | 
    cache_time = 300 # int | Optional. Seconds. (optional) if omitted the server will use the default value of 300
    size = 50 # int | Optional. Number of documents to return. (optional) if omitted the server will use the default value of 50
    search_id = "search_id_example" # str | Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. (optional)
    candidate_search_query = CandidateSearchQuery(
        query_filters=BaseCandidateSearchQuery(
            application=QueryFilters(
                must=[
                    FilterField(
                        field="field_example",
                        type="type_example",
                        value={},
                    ),
                ],
                should=[
                    FilterField(
                        field="field_example",
                        type="type_example",
                        value={},
                    ),
                ],
                must_not=[
                    FilterField(
                        field="field_example",
                        type="type_example",
                        value={},
                    ),
                ],
                filter=[
                    FilterField(
                        field="field_example",
                        type="type_example",
                        value={},
                    ),
                ],
            ),
            resume=QueryFilters(
                must=[
                    FilterField(
                        field="field_example",
                        type="type_example",
                        value={},
                    ),
                ],
                should=[
                    FilterField(
                        field="field_example",
                        type="type_example",
                        value={},
                    ),
                ],
                must_not=[
                    FilterField(
                        field="field_example",
                        type="type_example",
                        value={},
                    ),
                ],
                filter=[
                    FilterField(
                        field="field_example",
                        type="type_example",
                        value={},
                    ),
                ],
            ),
        ),
    ) # CandidateSearchQuery |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Applicants
        api_response = api_instance.search_applicants_post(indexname, jobad_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_applicants_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Applicants
        api_response = api_instance.search_applicants_post(indexname, jobad_id, cache_time=cache_time, size=size, search_id=search_id, candidate_search_query=candidate_search_query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_applicants_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **JobadId**|  |
 **cache_time** | **int**| Optional. Seconds. | [optional] if omitted the server will use the default value of 300
 **size** | **int**| Optional. Number of documents to return. | [optional] if omitted the server will use the default value of 50
 **search_id** | **str**| Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. | [optional]
 **candidate_search_query** | [**CandidateSearchQuery**](CandidateSearchQuery.md)|  | [optional]

### Return type

[**FoundCandidatesResponse**](FoundCandidatesResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_resumes_evidence_post**
> [SearchEvidence] search_resumes_evidence_post(indexname, evidence_request)

Search Resumes Evidence

Provides evidence for [Search Resumes](https://api.inda.ai/hr/docs/v2/#operation/search_resumes__POST) by returning the *size* most relevant words in each resume *resume_id* (listed into the list *resume_ids*) with respect to the *QueryTerms*. Note that -- unlike in the Related Words methods ([Similar Words](https://api.inda.ai/hr/docs/v2/#operation/similar_words__POST) and [Similar Words In Doc](https://api.inda.ai/hr/docs/v2/#operation/similar_words_in_resume__POST)) -- the elements of *QueryTerms* are combined together. Hence, the output minimizes the distance from all query terms simultaneously.  It returns a list of objects each containing the resume *resume_id* (*ID*) and a list of *Terms*.  Any *resume_id* not corresponding to an available resume in the index *indexname* will be ignored.

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import resume_search_api
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
    indexname = "indexname_example" # str | 
    evidence_request = EvidenceRequest(
        query_terms=[
            WeightedQueryTerm(
                term="term_example",
                language="it",
                weight=1.0,
            ),
        ],
        resume_ids=[
            "resume_ids_example",
        ],
    ) # EvidenceRequest | 
    size = 3 # int | Number of elements to be returned, must be greater than <code style='color: #333333; opacity: 0.9'>0</code> and smaller or equal to <code style='color: #333333; opacity: 0.9'>5</code>. (optional) if omitted the server will use the default value of 3
    src_lang = "it" # str | Queries language. If left empty each query's language will detected automatically, if not it is not explicitly set into the request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Resumes Evidence
        api_response = api_instance.search_resumes_evidence_post(indexname, evidence_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_resumes_evidence_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Resumes Evidence
        api_response = api_instance.search_resumes_evidence_post(indexname, evidence_request, size=size, src_lang=src_lang)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_resumes_evidence_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **evidence_request** | [**EvidenceRequest**](EvidenceRequest.md)|  |
 **size** | **int**| Number of elements to be returned, must be greater than &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;0&lt;/code&gt; and smaller or equal to &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;5&lt;/code&gt;. | [optional] if omitted the server will use the default value of 3
 **src_lang** | **str**| Queries language. If left empty each query&#39;s language will detected automatically, if not it is not explicitly set into the request body. | [optional]

### Return type

[**[SearchEvidence]**](SearchEvidence.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Found Evidence |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_resumes_post**
> FoundDocsResponse search_resumes_post(indexname)

Search Resumes

This method performs a semantic search of resumes in index *indexname* according to the given query.  Compared with traditional search engines, *INDA Semantic Search* enables users to search in a pool of resumes in a more flexible way: search results are not limited to term matches but they include all resumes that are semantically close to the query.  Furthermore, in order to tackle the bias problem, INDA automatically ignores specific fields (such as name, gender, age and nationality) during the initial processing of each candidate data. We are constantly working on reduce the bias in original data so that INDA results may be as fair as possible.  The semantic search can be complemented with a traditional filter-based search through the [filters](https://api.inda.ai/hr/docs/v2/#tag/Search) built inside the *QueryFilters* field.  The desired query must be specified in the application/json content type body (see the example on the right). The elements of *QueryTerms* are mandatory and each of them must be associated with a weight between <code style='color: #333333; opacity: 0.9'>0</code> and <code style='color: #333333; opacity: 0.9'>1</code>, which determines the importance of the term in the search.  The method returns a list of JSON documents, each of which contains a resume; the resumes are sorted according to a **pertinence score** determined on the basis of their semantic similarity with the query terms. Note that each resume is evaluated based on the semantic similarity with respect to all query terms (where each query term is weighted according to its *weight*).  Query parameters are used to specify the *offset*, *size* and *min_score* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored because to navigate the entire search response (in chunks of size *size*) through the *search_id*. The use of caching is highly recommended to improve the performance. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Please consider to use the [Semantic Search Feedback](https://api.inda.ai/hr/docs/v2/#operation/semantic_search_feedback__POST) to evaluate the provided ranking  of resumes. It is very useful to improve our algorithms' performances.

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import resume_search_api
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
    indexname = "indexname_example" # str | 
    cache = True # bool | Optional. Whether the search results should be cached or not. (optional) if omitted the server will use the default value of True
    cache_time = 300 # int | Optional. Seconds. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>false</code>. (optional) if omitted the server will use the default value of 300
    size = 50 # int | Optional. Number of documents to return. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>. (optional) if omitted the server will use the default value of 0
    min_score = 0 # float | Optional. Minimum pertinence score. (optional) if omitted the server will use the default value of 0
    search_id = "search_id_example" # str | Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. (optional)
    src_lang = "it" # str | Queries language. If left empty each query's language will detected automatically, if not it is not explicitly set into the request body. (optional)
    dst_lang = [
        "es",
    ] # [str] | Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results. (optional)
    docs_search_query = DocsSearchQuery(
        query_terms=[
            WeightedQueryTerm(
                term="term_example",
                language="it",
                weight=1.0,
            ),
        ],
        query_filters=QueryFilters(
            must=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            should=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            must_not=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            filter=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
        ),
    ) # DocsSearchQuery |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Resumes
        api_response = api_instance.search_resumes_post(indexname)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_resumes_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Resumes
        api_response = api_instance.search_resumes_post(indexname, cache=cache, cache_time=cache_time, size=size, offset=offset, min_score=min_score, search_id=search_id, src_lang=src_lang, dst_lang=dst_lang, docs_search_query=docs_search_query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeSearchApi->search_resumes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **cache** | **bool**| Optional. Whether the search results should be cached or not. | [optional] if omitted the server will use the default value of True
 **cache_time** | **int**| Optional. Seconds. Ignored if *cache* is &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;false&lt;/code&gt;. | [optional] if omitted the server will use the default value of 300
 **size** | **int**| Optional. Number of documents to return. | [optional] if omitted the server will use the default value of 50
 **offset** | **int**| Optional. Number of documents to skip. Ignored if *cache* is &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;true&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **min_score** | **float**| Optional. Minimum pertinence score. | [optional] if omitted the server will use the default value of 0
 **search_id** | **str**| Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. | [optional]
 **src_lang** | **str**| Queries language. If left empty each query&#39;s language will detected automatically, if not it is not explicitly set into the request body. | [optional]
 **dst_lang** | **[str]**| Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results. | [optional]
 **docs_search_query** | [**DocsSearchQuery**](DocsSearchQuery.md)|  | [optional]

### Return type

[**FoundDocsResponse**](FoundDocsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**415** | Unsupported Media Type |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

