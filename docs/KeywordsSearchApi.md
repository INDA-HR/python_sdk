# inda_hr.KeywordsSearchApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keywords_autocomplete_get**](KeywordsSearchApi.md#keywords_autocomplete_get) | **GET** /hr/v2/keywords/search/autocomplete/ | Keywords Autocomplete
[**similar_words_in_resume_post**](KeywordsSearchApi.md#similar_words_in_resume_post) | **POST** /hr/v2/index/{indexname}/resume/{resume_id}/keywords/search/semantic/ | Similar Words in Resume
[**similar_words_post**](KeywordsSearchApi.md#similar_words_post) | **POST** /hr/v2/keywords/search/semantic/ | Similar Words


# **keywords_autocomplete_get**
> AutocompleteResponse keywords_autocomplete_get(term)

Keywords Autocomplete

This method performs token autocompletion, based on a INDA dictionary, i.e., a large dictionary specialized to recruiting domain. An example of application is to improve the user experience of a recruiter who is writing search keywords for candidate screening.  The *term* to be completed (see *query parameters* below) must contain at least *2* characters. The output contains a list of possible complete terms sorted with respect to the frequency in INDA dictionary (the list is associated with the key *candidates*, as shown in the example on the right).

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import keywords_search_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.autocomplete_response import AutocompleteResponse
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
    api_instance = keywords_search_api.KeywordsSearchApi(api_client)
    term = "term_example" # str | Token to be completed

    # example passing only required values which don't have defaults set
    try:
        # Keywords Autocomplete
        api_response = api_instance.keywords_autocomplete_get(term)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling KeywordsSearchApi->keywords_autocomplete_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Token to be completed |

### Return type

[**AutocompleteResponse**](AutocompleteResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Found Autocomplete Candidates |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **similar_words_in_resume_post**
> KeywordsResponse similar_words_in_resume_post(indexname, resume_id, similar_words_query)

Similar Words in Resume

This method works as the method [Similar Words](https://api.inda.ai/hr/docs/v2/#operation/similar_words__POST), but it is restricted to the words contained in the resume *resume_id*.  It could be used, for instance, to inspect a document found via [Search Resumes](https://api.inda.ai/hr/docs/v2/#operation/search_resumes__POST) in order to have better insights on the most similar words in the document to each query term used.

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import keywords_search_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.similar_words_query import SimilarWordsQuery
from inda_hr.model.keywords_response import KeywordsResponse
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
    api_instance = keywords_search_api.KeywordsSearchApi(api_client)
    indexname = "indexname_example" # str | 
    resume_id = "resume_id_example" # str | 
    similar_words_query = SimilarWordsQuery(
        query_terms=[
            QueryTerm(
                term="term_example",
                language="it",
            ),
        ],
    ) # SimilarWordsQuery | 
    size = 3 # int | Number of elements to be returned, must be greater than <code style='color: #333333; opacity: 0.9'>0</code> and smaller or equal to <code style='color: #333333; opacity: 0.9'>5</code>. (optional) if omitted the server will use the default value of 3
    src_lang = "it" # str | Queries language. If left empty each query's language will detected automatically, if not it is not explicitly set into the request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Similar Words in Resume
        api_response = api_instance.similar_words_in_resume_post(indexname, resume_id, similar_words_query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling KeywordsSearchApi->similar_words_in_resume_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Similar Words in Resume
        api_response = api_instance.similar_words_in_resume_post(indexname, resume_id, similar_words_query, size=size, src_lang=src_lang)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling KeywordsSearchApi->similar_words_in_resume_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **resume_id** | **str**|  |
 **similar_words_query** | [**SimilarWordsQuery**](SimilarWordsQuery.md)|  |
 **size** | **int**| Number of elements to be returned, must be greater than &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;0&lt;/code&gt; and smaller or equal to &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;5&lt;/code&gt;. | [optional] if omitted the server will use the default value of 3
 **src_lang** | **str**| Queries language. If left empty each query&#39;s language will detected automatically, if not it is not explicitly set into the request body. | [optional]

### Return type

[**KeywordsResponse**](KeywordsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Keywords Search Successful |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **similar_words_post**
> KeywordsResponse similar_words_post(similar_words_query)

Similar Words

Given a list of *query* terms, this method returns, for each term, the *size* most similar words found in vocabulary. The similarity of each result to the corresponding query term is rated with a score between <code style='color: #333333; opacity: 0.9'>0</code> (minimum similarity) and <code style='color: #333333; opacity: 0.9'>1</code> (maximum similarity).  This method can be used to perform a **keyword expansion**: expanding a query word with its synonyms or semantically similar words allows a more flexible search with respect to a traditional word match or boolean search system. Note that each element of *query terms* is considered independently from the others.  This method returns a dictionary with keys *Hits* (the number of *query terms* found in vocabulary), *OutOfVocabulary* (the number of query terms not found in vocabulary), and *Out*, which is a list of dictionaries with two keys: the first key (*Query*) contains the query term, while the second one (*Results*) contains a list of dictionaries, one for each similar word. Each dictionary contains the word retrieved (*Term*) and its *Score* representing the similarity with the searched word, ranging from <code style='color: #333333; opacity: 0.9'>0</code> (minimum similarity) to <code style='color: #333333; opacity: 0.9'>1</code> (maximum similarity).  If all searched words are out of vocabulary, an error is raised.

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import keywords_search_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.similar_words_query import SimilarWordsQuery
from inda_hr.model.keywords_response import KeywordsResponse
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
    api_instance = keywords_search_api.KeywordsSearchApi(api_client)
    similar_words_query = SimilarWordsQuery(
        query_terms=[
            QueryTerm(
                term="term_example",
                language="it",
            ),
        ],
    ) # SimilarWordsQuery | 
    size = 3 # int | Number of elements to be returned, must be greater than <code style='color: #333333; opacity: 0.9'>0</code> and smaller or equal to <code style='color: #333333; opacity: 0.9'>5</code>. (optional) if omitted the server will use the default value of 3
    src_lang = "it" # str | Queries language. If left empty each query's language will detected automatically, if not it is not explicitly set into the request body. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Similar Words
        api_response = api_instance.similar_words_post(similar_words_query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling KeywordsSearchApi->similar_words_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Similar Words
        api_response = api_instance.similar_words_post(similar_words_query, size=size, src_lang=src_lang)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling KeywordsSearchApi->similar_words_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **similar_words_query** | [**SimilarWordsQuery**](SimilarWordsQuery.md)|  |
 **size** | **int**| Number of elements to be returned, must be greater than &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;0&lt;/code&gt; and smaller or equal to &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;5&lt;/code&gt;. | [optional] if omitted the server will use the default value of 3
 **src_lang** | **str**| Queries language. If left empty each query&#39;s language will detected automatically, if not it is not explicitly set into the request body. | [optional]

### Return type

[**KeywordsResponse**](KeywordsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Keyword Search Successful |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

