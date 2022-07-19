# inda_hr.JobAdSearchApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**full_text_search_on_jobads_post**](JobAdSearchApi.md#full_text_search_on_jobads_post) | **POST** /hr/v2/index/{indexname}/jobads/search/full-text/ | Full-Text Search on JobAds
[**search_applications_post**](JobAdSearchApi.md#search_applications_post) | **POST** /hr/v2/index/{indexname}/resume/{resume_id}/applications/jobads/search/ | Search Applications


# **full_text_search_on_jobads_post**
> FoundJobAdsResponse full_text_search_on_jobads_post(indexname)

Full-Text Search on JobAds

 This is the most common way to search a text document through the job advertisements stored in the index *indexname*.  This function takes as input a list of objects containing the terms you wish to search for, please consider that tokens (individual words) grouped together in the same *QueryTerms* element will be queried separately in an **OR** clause, whereas different *QueryTerms* elements will be joined by an **AND** clause. To put it in words, the query will retrieve documents that match at least one word from each element in *QueryTerms*.  This behaviour can be modified in one of two ways:  + The **default_operator** query parameter, which defaults to OR, can be set to AND in order to only find documents that contain ALL of the tokens in a given *query_terms* element. + The **\"** (double quotes) operator, which can be used to wrap strings made up of multiple tokens in order to find documents that contain those words exactly in the order they are presented (sentence match). Remember to escape double quotes in your JSON inputs with a backslash.  Each *QueryTerms* element can be negated with the parameter **Exclude** set to *true*. This is equivalent to setting it in a **NOT** clause.  It's also possible to use wildcards to perform jolly searches, the supported wildcards are:  + \\*: Can be used to match any number of characters in the middle (ad\\*ment) or at the end (doc\\*) of a word. + ?: Can be used to match a single character in any position (?xample).  All queries are case-insensitive and have some amount of fuzziness by default, meaning that typos and character transpositions will be included in the matches. Additionally, filters can be added to form boolean queries on indexed fields. For a comprehensive list and explanation of filters, see the [*Query Filters*](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) section, the structure is the same.  Query parameters are used to specify the *offset* and *size* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored; in order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  The use of caching is highly recommended to improve the performances.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_search_api
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
    indexname = "indexname_example" # str | 
    default_operator = "OR" # str | Optional. Change this to *AND* if you wish documents to match ALLof the tokens in a single query_terms element. (optional) if omitted the server will use the default value of "OR"
    cache = True # bool | Optional. Whether the search results should be cached or not. (optional) if omitted the server will use the default value of True
    cache_time = 300 # int | Optional. Seconds. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>false</code>. (optional) if omitted the server will use the default value of 300
    size = 50 # int | Optional. Number of documents to return. (optional) if omitted the server will use the default value of 50
    offset = 0 # int | Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>. (optional) if omitted the server will use the default value of 0
    min_score = 0 # float | Optional. Minimum pertinence score. (optional) if omitted the server will use the default value of 0
    search_id = "search_id_example" # str | Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. (optional)
    job_ad_full_text_search = JobAdFullTextSearch(
        query_terms=[
            JobadRequestsSimpleTerm(
                term="term_example",
                exclude=False,
            ),
        ],
        query_filters=QueryFilters(
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
    ) # JobAdFullTextSearch |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Full-Text Search on JobAds
        api_response = api_instance.full_text_search_on_jobads_post(indexname)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdSearchApi->full_text_search_on_jobads_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Full-Text Search on JobAds
        api_response = api_instance.full_text_search_on_jobads_post(indexname, default_operator=default_operator, cache=cache, cache_time=cache_time, size=size, offset=offset, min_score=min_score, search_id=search_id, job_ad_full_text_search=job_ad_full_text_search)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdSearchApi->full_text_search_on_jobads_post: %s\n" % e)
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
 **job_ad_full_text_search** | [**JobAdFullTextSearch**](JobAdFullTextSearch.md)|  | [optional]

### Return type

[**FoundJobAdsResponse**](FoundJobAdsResponse.md)

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

# **search_applications_post**
> FoundJobAdsResponse search_applications_post(indexname, resume_id)

Search Applications

  This method is meant to return those job advertisements that the resume of ID *resume_id* have applied to, if they respect the given query.  Users may specify [query filters](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) to apply on both [Applications](https://api.inda.ai/hr/docs/v2/#tag/Application-Management) and [JobAds](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Management) indexed fields.  Query parameters are used to specify the *cache_time* and *size* of the search. The method will automatically cache each search for *cache_time* seconds. In order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_search_api
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
    indexname = "indexname_example" # str | 
    resume_id = "resume_id_example" # str | 
    cache_time = 300 # int | Optional. Seconds. (optional) if omitted the server will use the default value of 300
    size = 50 # int | Optional. Number of documents to return. (optional) if omitted the server will use the default value of 50
    search_id = "search_id_example" # str | Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. (optional)
    job_ad_search_query = JobAdSearchQuery(
        query_filters=BaseJobAdSearchQuery(
            application=QueryFilters(
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
            job_ad=QueryFilters(
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
    ) # JobAdSearchQuery |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Search Applications
        api_response = api_instance.search_applications_post(indexname, resume_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdSearchApi->search_applications_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Applications
        api_response = api_instance.search_applications_post(indexname, resume_id, cache_time=cache_time, size=size, search_id=search_id, job_ad_search_query=job_ad_search_query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdSearchApi->search_applications_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **resume_id** | **str**|  |
 **cache_time** | **int**| Optional. Seconds. | [optional] if omitted the server will use the default value of 300
 **size** | **int**| Optional. Number of documents to return. | [optional] if omitted the server will use the default value of 50
 **search_id** | **str**| Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. | [optional]
 **job_ad_search_query** | [**JobAdSearchQuery**](JobAdSearchQuery.md)|  | [optional]

### Return type

[**FoundJobAdsResponse**](FoundJobAdsResponse.md)

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

