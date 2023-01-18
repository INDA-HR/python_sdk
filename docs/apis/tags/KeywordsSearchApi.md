<a name="__pageTop"></a>
# inda_hr.apis.tags.keywords_search_api.KeywordsSearchApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**keywords_autocomplete_get**](#keywords_autocomplete_get) | **get** /hr/v2/keywords/search/autocomplete/ | Keywords Autocomplete
[**similar_words_in_resume_post**](#similar_words_in_resume_post) | **post** /hr/v2/index/{indexname}/resume/{resume_id}/keywords/search/semantic/ | Similar Words in Resume
[**similar_words_post**](#similar_words_post) | **post** /hr/v2/keywords/search/semantic/ | Similar Words

# **keywords_autocomplete_get**
<a name="keywords_autocomplete_get"></a>
> AutocompleteResponse keywords_autocomplete_get(term)

Keywords Autocomplete

This method performs token autocompletion, based on a INDA dictionary, i.e., a large dictionary specialized to recruiting domain. An example of application is to improve the user experience of a recruiter who is writing search keywords for candidate screening.  The *term* to be completed (see *query parameters* below) must contain at least *2* characters. The output contains a list of possible complete terms sorted with respect to the frequency in INDA dictionary (the list is associated with the key *candidates*, as shown in the example on the right).

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import keywords_search_api
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

    # example passing only required values which don't have defaults set
    query_params = {
        'term': "term_example",
    }
    try:
        # Keywords Autocomplete
        api_response = api_instance.keywords_autocomplete_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling KeywordsSearchApi->keywords_autocomplete_get: %s\n" % e)
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


# TermSchema

Token to be completed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Token to be completed | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#keywords_autocomplete_get.ApiResponseFor200) | Successfully Found Autocomplete Candidates
404 | [ApiResponseFor404](#keywords_autocomplete_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#keywords_autocomplete_get.ApiResponseFor422) | Validation Error

#### keywords_autocomplete_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AutocompleteResponse**](../../models/AutocompleteResponse.md) |  | 


#### keywords_autocomplete_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### keywords_autocomplete_get.ApiResponseFor422
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

# **similar_words_in_resume_post**
<a name="similar_words_in_resume_post"></a>
> KeywordsResponse similar_words_in_resume_post(indexnameresume_idsimilar_words_query)

Similar Words in Resume

This method works as the method [Similar Words](https://api.inda.ai/hr/docs/v2/#operation/similar_words__POST), but it is restricted to the words contained in the resume *resume_id*.  It could be used, for instance, to inspect a document found via [Search Resumes](https://api.inda.ai/hr/docs/v2/#operation/search_resumes__POST) in order to have better insights on the most similar words in the document to each query term used.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import keywords_search_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
    }
    body = SimilarWordsQuery(
        query_terms=[
            QueryTerm(
                term="term_example",
                language="it",
            )
        ],
    )
    try:
        # Similar Words in Resume
        api_response = api_instance.similar_words_in_resume_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling KeywordsSearchApi->similar_words_in_resume_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
        'size': 3,
        'src_lang': "it",
    }
    body = SimilarWordsQuery(
        query_terms=[
            QueryTerm(
                term="term_example",
                language="it",
            )
        ],
    )
    try:
        # Similar Words in Resume
        api_response = api_instance.similar_words_in_resume_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling KeywordsSearchApi->similar_words_in_resume_post: %s\n" % e)
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
[**SimilarWordsQuery**](../../models/SimilarWordsQuery.md) |  | 


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
200 | [ApiResponseFor200](#similar_words_in_resume_post.ApiResponseFor200) | Keywords Search Successful
400 | [ApiResponseFor400](#similar_words_in_resume_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#similar_words_in_resume_post.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#similar_words_in_resume_post.ApiResponseFor422) | Unprocessable Entity

#### similar_words_in_resume_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**KeywordsResponse**](../../models/KeywordsResponse.md) |  | 


#### similar_words_in_resume_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### similar_words_in_resume_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### similar_words_in_resume_post.ApiResponseFor422
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

# **similar_words_post**
<a name="similar_words_post"></a>
> KeywordsResponse similar_words_post(similar_words_query)

Similar Words

Given a list of *query* terms, this method returns, for each term, the *size* most similar words found in vocabulary. The similarity of each result to the corresponding query term is rated with a score between <code style='color: #333333; opacity: 0.9'>0</code> (minimum similarity) and <code style='color: #333333; opacity: 0.9'>1</code> (maximum similarity).  This method can be used to perform a **keyword expansion**: expanding a query word with its synonyms or semantically similar words allows a more flexible search with respect to a traditional word match or boolean search system. Note that each element of *query terms* is considered independently from the others.  This method returns a dictionary with keys *Hits* (the number of *query terms* found in vocabulary), *OutOfVocabulary* (the number of query terms not found in vocabulary), and *Out*, which is a list of dictionaries with two keys: the first key (*Query*) contains the query term, while the second one (*Results*) contains a list of dictionaries, one for each similar word. Each dictionary contains the word retrieved (*Term*) and its *Score* representing the similarity with the searched word, ranging from <code style='color: #333333; opacity: 0.9'>0</code> (minimum similarity) to <code style='color: #333333; opacity: 0.9'>1</code> (maximum similarity).  If all searched words are out of vocabulary, an error is raised.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import keywords_search_api
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

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = SimilarWordsQuery(
        query_terms=[
            QueryTerm(
                term="term_example",
                language="it",
            )
        ],
    )
    try:
        # Similar Words
        api_response = api_instance.similar_words_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling KeywordsSearchApi->similar_words_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'size': 3,
        'src_lang': "it",
    }
    body = SimilarWordsQuery(
        query_terms=[
            QueryTerm(
                term="term_example",
                language="it",
            )
        ],
    )
    try:
        # Similar Words
        api_response = api_instance.similar_words_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling KeywordsSearchApi->similar_words_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SimilarWordsQuery**](../../models/SimilarWordsQuery.md) |  | 


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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#similar_words_post.ApiResponseFor200) | Keyword Search Successful
400 | [ApiResponseFor400](#similar_words_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#similar_words_post.ApiResponseFor422) | Unprocessable Entity

#### similar_words_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**KeywordsResponse**](../../models/KeywordsResponse.md) |  | 


#### similar_words_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### similar_words_post.ApiResponseFor422
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

