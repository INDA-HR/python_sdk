<a name="__pageTop"></a>
# inda_hr.apis.tags.skills_api.SkillsApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**similar_skills_get**](#similar_skills_get) | **get** /hr/v2/skills/similar/semantic/ | Similar Skills
[**skills_classification_post**](#skills_classification_post) | **post** /hr/v2/skills/classification/ | Skills Classification

# **similar_skills_get**
<a name="similar_skills_get"></a>
> SimilarEntitiesResponse similar_skills_get(query)

Similar Skills

 This method returns the *size* most similar skills found in the knowledge base with respect to the input *skill*.  The similarity of each result to the input skill is rated with a score between <code style='color: #333333; opacity: 0.9'>0</code> (minimum similarity) and <code style='color: #333333; opacity: 0.9'>1</code> (maximum similarity). This method can be used to perform a *keyword expansion*: expanding a skill with its synonyms or semantically similar skills may be useful, for instance, to improve a job description or to perform a more flexible search with respect to a traditional word match or boolean search system.  This method returns a dictionary with keys *Hits* (the number of skills returned) and *Out*, which is a list of dictionaries with two keys: the first key (*Term*) contains the proposed skill, while the second one (*Score*)  contains its similarity score, as described above. The parameter *min_score* set the threshold for the similarity score, below which the output skills are discarded; its default value is <code style='color: #333333; opacity: 0.9'>0.5</code>.  Note that the number of retrieved similar skills may be smaller than *size* when the minimum score is larger than zero or when the searched skill is particularly uncommon.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import skills_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.similar_entities_response import SimilarEntitiesResponse
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
    api_instance = skills_api.SkillsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'query': "query_example",
    }
    try:
        # Similar Skills
        api_response = api_instance.similar_skills_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling SkillsApi->similar_skills_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'size': 5,
        'min_score': 0.5,
        'query': "query_example",
        'src_lang': "it",
        'dst_lang': "it",
    }
    try:
        # Similar Skills
        api_response = api_instance.similar_skills_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling SkillsApi->similar_skills_get: %s\n" % e)
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
size | SizeSchema | | optional
min_score | MinScoreSchema | | optional
query | QuerySchema | | 
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional


# SizeSchema

Number of similar skills to return.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Number of similar skills to return. | if omitted the server will use the default value of 5

# MinScoreSchema

Minimum pertinence score.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum pertinence score. | if omitted the server will use the default value of 0.5

# QuerySchema

Input skill to be analyzed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Input skill to be analyzed | 

# SrcLangSchema

Optional. Language of the input skills.If missing, the detected language is assumed as `src_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Language of the input skills.If missing, the detected language is assumed as &#x60;src_lang&#x60;. | must be one of ["it", "en", "es", "pt", "de", "fr", ] 

# DstLangSchema

Optional. Language of the input skills.If missing, the detected language is assumed as `src_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Language of the input skills.If missing, the detected language is assumed as &#x60;src_lang&#x60;. | must be one of ["it", "en", "es", "pt", "de", "fr", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#similar_skills_get.ApiResponseFor200) | Request Successfully Processed
400 | [ApiResponseFor400](#similar_skills_get.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#similar_skills_get.ApiResponseFor422) | Validation Error

#### similar_skills_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SimilarEntitiesResponse**](../../models/SimilarEntitiesResponse.md) |  | 


#### similar_skills_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### similar_skills_get.ApiResponseFor422
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

# **skills_classification_post**
<a name="skills_classification_post"></a>
> SkillsClassificationResponse skills_classification_post(skills_classification_request)

Skills Classification

 This method returns a label associated to each given skill among the following: <code style='color: #333333; opacity: 0.9'>hard</code>, <code style='color: #333333; opacity: 0.9'>IT</code>, <code style='color: #333333; opacity: 0.9'>soft</code> and <code style='color: #333333; opacity: 0.9'>language</code>.  The request is structured according two main fields: *lang* and *skills*.  The *lang* field allows users to set the main language to which the skills to classify belong.  The *skills* field is merely the list of terms for which users want to find the closest category among the aforementioned ones. Please note that if a term is not recognized as a skill, it will be absent from the response.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import skills_api
from inda_hr.model.skills_classification_request import SkillsClassificationRequest
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.skills_classification_response import SkillsClassificationResponse
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
    api_instance = skills_api.SkillsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = SkillsClassificationRequest(
        skills=[
            "skills_example"
        ],
    )
    try:
        # Skills Classification
        api_response = api_instance.skills_classification_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling SkillsApi->skills_classification_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'src_lang': "it",
    }
    body = SkillsClassificationRequest(
        skills=[
            "skills_example"
        ],
    )
    try:
        # Skills Classification
        api_response = api_instance.skills_classification_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling SkillsApi->skills_classification_post: %s\n" % e)
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
[**SkillsClassificationRequest**](../../models/SkillsClassificationRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional


# SrcLangSchema

Language of the input skills.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Language of the input skills. | must be one of ["it", "en", "es", "pt", "de", "fr", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#skills_classification_post.ApiResponseFor200) | Request Successfully Processed
400 | [ApiResponseFor400](#skills_classification_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#skills_classification_post.ApiResponseFor422) | Validation Error

#### skills_classification_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SkillsClassificationResponse**](../../models/SkillsClassificationResponse.md) |  | 


#### skills_classification_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### skills_classification_post.ApiResponseFor422
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

