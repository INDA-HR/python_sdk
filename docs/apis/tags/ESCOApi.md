<a name="__pageTop"></a>
# inda_hr.apis.tags.esco_api.ESCOApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esco_occupations_hierarchy_get**](#esco_occupations_hierarchy_get) | **get** /hr/v2/occupations/similar/esco/hierarchy/ | ESCO Occupations Hierarchy
[**esco_skills_hierarchy_get**](#esco_skills_hierarchy_get) | **get** /hr/v2/skills/similar/esco/hierarchy/ | ESCO Skills Hierarchy
[**from_description_to_esco_occupations_post**](#from_description_to_esco_occupations_post) | **post** /hr/v2/occupations/description/match/esco/ | From description to ESCO Occupations
[**from_description_to_esco_skills_post**](#from_description_to_esco_skills_post) | **post** /hr/v2/skills/description/match/esco/ | From description to ESCO Skills
[**mapping_esco_get**](#mapping_esco_get) | **get** /hr/v2/occupations/mapping/esco/ | Mapping ESCO
[**mapping_isco_get**](#mapping_isco_get) | **get** /hr/v2/occupations/mapping/isco/ | Mapping ISCO
[**mapping_istat_cp2011_get**](#mapping_istat_cp2011_get) | **get** /hr/v2/occupations/mapping/istat/ | Mapping ISTAT-CP2011
[**mapping_onet_get**](#mapping_onet_get) | **get** /hr/v2/occupations/mapping/onet/ | Mapping O*NET
[**similar_esco_occupations_get**](#similar_esco_occupations_get) | **get** /hr/v2/occupations/similar/esco/ | Similar ESCO Occupations
[**similar_esco_skills_get**](#similar_esco_skills_get) | **get** /hr/v2/skills/similar/esco/ | Similar ESCO Skills

# **esco_occupations_hierarchy_get**
<a name="esco_occupations_hierarchy_get"></a>
> MostSimilarJobtitleResponseCategorized esco_occupations_hierarchy_get(query)

ESCO Occupations Hierarchy

 This method provides the most similar ESCO job title given a *jobtitle* (that could be a word or a sentence in several languages), its hierarchy classification according with ISCO classification, and the top three industries and job functions where the occupation is distributed.  More details about ESCO occupations hierarchy are showed [here](https://ec.europa.eu/esco/portal/occupation).  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import esco_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.most_similar_jobtitle_response_categorized import MostSimilarJobtitleResponseCategorized
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
    api_instance = esco_api.ESCOApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'query': "query_example",
    }
    try:
        # ESCO Occupations Hierarchy
        api_response = api_instance.esco_occupations_hierarchy_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->esco_occupations_hierarchy_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'query': "query_example",
        'dst_lang': "it",
    }
    try:
        # ESCO Occupations Hierarchy
        api_response = api_instance.esco_occupations_hierarchy_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->esco_occupations_hierarchy_get: %s\n" % e)
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
query | QuerySchema | | 
dst_lang | DstLangSchema | | optional


# QuerySchema

It could be any word or sentence in several languages.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | It could be any word or sentence in several languages. | 

# DstLangSchema

Language of the similar ESCO occupations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Language of the similar ESCO occupations. | must be one of ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv", ] if omitted the server will use the default value of "it"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#esco_occupations_hierarchy_get.ApiResponseFor200) | Successful Response
500 | [ApiResponseFor500](#esco_occupations_hierarchy_get.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#esco_occupations_hierarchy_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#esco_occupations_hierarchy_get.ApiResponseFor422) | Validation Error

#### esco_occupations_hierarchy_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MostSimilarJobtitleResponseCategorized**](../../models/MostSimilarJobtitleResponseCategorized.md) |  | 


#### esco_occupations_hierarchy_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### esco_occupations_hierarchy_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### esco_occupations_hierarchy_get.ApiResponseFor422
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

# **esco_skills_hierarchy_get**
<a name="esco_skills_hierarchy_get"></a>
> MostSimilarSkillResponseCategorized esco_skills_hierarchy_get(query)

ESCO Skills Hierarchy

 This method provides the most similar ESCO skills given a *query* (representing a skill) that could be a word or a sentence in several languages; also its hierarchy classification according with ESCO is returned.  More details about ESCO skills hierarchy are showed [here](https://ec.europa.eu/esco/portal/skill).  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import esco_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.most_similar_skill_response_categorized import MostSimilarSkillResponseCategorized
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
    api_instance = esco_api.ESCOApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'query': "query_example",
    }
    try:
        # ESCO Skills Hierarchy
        api_response = api_instance.esco_skills_hierarchy_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->esco_skills_hierarchy_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'query': "query_example",
        'dst_lang': "it",
    }
    try:
        # ESCO Skills Hierarchy
        api_response = api_instance.esco_skills_hierarchy_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->esco_skills_hierarchy_get: %s\n" % e)
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
query | QuerySchema | | 
dst_lang | DstLangSchema | | optional


# QuerySchema

A word or a brief sentence in several languages.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A word or a brief sentence in several languages. | 

# DstLangSchema

Language of the similar ESCO skills.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Language of the similar ESCO skills. | must be one of ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv", ] if omitted the server will use the default value of "it"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#esco_skills_hierarchy_get.ApiResponseFor200) | Successful Response
500 | [ApiResponseFor500](#esco_skills_hierarchy_get.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#esco_skills_hierarchy_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#esco_skills_hierarchy_get.ApiResponseFor422) | Validation Error

#### esco_skills_hierarchy_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MostSimilarSkillResponseCategorized**](../../models/MostSimilarSkillResponseCategorized.md) |  | 


#### esco_skills_hierarchy_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### esco_skills_hierarchy_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### esco_skills_hierarchy_get.ApiResponseFor422
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

# **from_description_to_esco_occupations_post**
<a name="from_description_to_esco_occupations_post"></a>
> EscoJobtitleResponse from_description_to_esco_occupations_post(description_input)

From description to ESCO Occupations

 This method provides the list of n most affine ESCO occupations given a sentence or a long description. For each returned occupation, the service provides also a list of the main related skills according to ESCO classification.  More details about ESCO occupations are showed [here](https://ec.europa.eu/esco/portal/occupation).  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import esco_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.description_input import DescriptionInput
from inda_hr.model.esco_jobtitle_response import EscoJobtitleResponse
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
    api_instance = esco_api.ESCOApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = DescriptionInput(
        description="description_example",
    )
    try:
        # From description to ESCO Occupations
        api_response = api_instance.from_description_to_esco_occupations_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->from_description_to_esco_occupations_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'dst_lang': "it",
        'size': 1,
        'min_score': 0.2,
    }
    body = DescriptionInput(
        description="description_example",
    )
    try:
        # From description to ESCO Occupations
        api_response = api_instance.from_description_to_esco_occupations_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->from_description_to_esco_occupations_post: %s\n" % e)
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
[**DescriptionInput**](../../models/DescriptionInput.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dst_lang | DstLangSchema | | optional
size | SizeSchema | | optional
min_score | MinScoreSchema | | optional


# DstLangSchema

Language of the similar ESCO occupations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Language of the similar ESCO occupations. | must be one of ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv", ] if omitted the server will use the default value of "it"

# SizeSchema

The maximum number of similar ESCO occupations retrieved by the algorithm.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of similar ESCO occupations retrieved by the algorithm. | if omitted the server will use the default value of 1

# MinScoreSchema

Minimum score of the similar ESCO occupations with respect to the job title queried by the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum score of the similar ESCO occupations with respect to the job title queried by the user. | if omitted the server will use the default value of 0.2

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#from_description_to_esco_occupations_post.ApiResponseFor200) | Successful Response
500 | [ApiResponseFor500](#from_description_to_esco_occupations_post.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#from_description_to_esco_occupations_post.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#from_description_to_esco_occupations_post.ApiResponseFor422) | Validation Error

#### from_description_to_esco_occupations_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EscoJobtitleResponse**](../../models/EscoJobtitleResponse.md) |  | 


#### from_description_to_esco_occupations_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### from_description_to_esco_occupations_post.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### from_description_to_esco_occupations_post.ApiResponseFor422
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

# **from_description_to_esco_skills_post**
<a name="from_description_to_esco_skills_post"></a>
> EscoSkillResponse from_description_to_esco_skills_post(description_input)

From description to ESCO Skills

 This method provides the list of n most affine ESCO skills given a sentence or a long description. For each returned skill, the service provides also a list of the main occupations where the skill is mandatory according to ESCO classification.  More details about ESCO skills are showed [here](https://ec.europa.eu/esco/portal/skill).  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import esco_api
from inda_hr.model.esco_skill_response import EscoSkillResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.description_input import DescriptionInput
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
    api_instance = esco_api.ESCOApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = DescriptionInput(
        description="description_example",
    )
    try:
        # From description to ESCO Skills
        api_response = api_instance.from_description_to_esco_skills_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->from_description_to_esco_skills_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'dst_lang': "it",
        'size': 1,
        'min_score': 0.2,
    }
    body = DescriptionInput(
        description="description_example",
    )
    try:
        # From description to ESCO Skills
        api_response = api_instance.from_description_to_esco_skills_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->from_description_to_esco_skills_post: %s\n" % e)
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
[**DescriptionInput**](../../models/DescriptionInput.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dst_lang | DstLangSchema | | optional
size | SizeSchema | | optional
min_score | MinScoreSchema | | optional


# DstLangSchema

Language of the similar ESCO skills.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Language of the similar ESCO skills. | must be one of ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv", ] if omitted the server will use the default value of "it"

# SizeSchema

The maximum number of similar ESCO skills retrieved by the algorithm.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of similar ESCO skills retrieved by the algorithm. | if omitted the server will use the default value of 1

# MinScoreSchema

Minimum score of the similar ESCO skills with respect to the skill queried by the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum score of the similar ESCO skills with respect to the skill queried by the user. | if omitted the server will use the default value of 0.2

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#from_description_to_esco_skills_post.ApiResponseFor200) | Successful Response
500 | [ApiResponseFor500](#from_description_to_esco_skills_post.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#from_description_to_esco_skills_post.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#from_description_to_esco_skills_post.ApiResponseFor422) | Validation Error

#### from_description_to_esco_skills_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EscoSkillResponse**](../../models/EscoSkillResponse.md) |  | 


#### from_description_to_esco_skills_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### from_description_to_esco_skills_post.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### from_description_to_esco_skills_post.ApiResponseFor422
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

# **mapping_esco_get**
<a name="mapping_esco_get"></a>
> ClassificationMappingEscoResponse mapping_esco_get(code)

Mapping ESCO

 This method provides the mapping from a [ESCO](https://ec.europa.eu/esco/portal) occupation code to: - [ISCO](https://www.ilo.org/public/english/bureau/stat/isco/) occupation codes; - [O*NET](https://www.onetonline.org/) occupation codes; - [ISTAT-CP2011](http://professioni.istat.it/cp2011/) occupation codes;  All requests are displayed in English. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import esco_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.classification_mapping_esco_response import ClassificationMappingEscoResponse
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
    api_instance = esco_api.ESCOApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'code': "code_example",
    }
    try:
        # Mapping ESCO
        api_response = api_instance.mapping_esco_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->mapping_esco_get: %s\n" % e)
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
code | CodeSchema | | 


# CodeSchema

[ESCO code](https://ec.europa.eu/esco/portal/occupation).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | [ESCO code](https://ec.europa.eu/esco/portal/occupation). | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#mapping_esco_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#mapping_esco_get.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#mapping_esco_get.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#mapping_esco_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#mapping_esco_get.ApiResponseFor422) | Validation Error

#### mapping_esco_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassificationMappingEscoResponse**](../../models/ClassificationMappingEscoResponse.md) |  | 


#### mapping_esco_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_esco_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_esco_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_esco_get.ApiResponseFor422
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

# **mapping_isco_get**
<a name="mapping_isco_get"></a>
> ClassificationMappingIscoResponse mapping_isco_get(code)

Mapping ISCO

 This method provides the mapping from a [ISCO](https://www.ilo.org/public/english/bureau/stat/isco/) occupation code to: - [ESCO](https://ec.europa.eu/esco/portal) occupation codes; - [O*NET](https://www.onetonline.org/) occupation codes; - [ISTAT-CP2011](http://professioni.istat.it/cp2011/) occupation codes;  All requests are displayed in English. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import esco_api
from inda_hr.model.classification_mapping_isco_response import ClassificationMappingIscoResponse
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
    api_instance = esco_api.ESCOApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'code': "code_example",
    }
    try:
        # Mapping ISCO
        api_response = api_instance.mapping_isco_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->mapping_isco_get: %s\n" % e)
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
code | CodeSchema | | 


# CodeSchema

[ISCO code](https://www.ilo.org/public/english/bureau/stat/isco/).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | [ISCO code](https://www.ilo.org/public/english/bureau/stat/isco/). | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#mapping_isco_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#mapping_isco_get.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#mapping_isco_get.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#mapping_isco_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#mapping_isco_get.ApiResponseFor422) | Validation Error

#### mapping_isco_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassificationMappingIscoResponse**](../../models/ClassificationMappingIscoResponse.md) |  | 


#### mapping_isco_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_isco_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_isco_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_isco_get.ApiResponseFor422
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

# **mapping_istat_cp2011_get**
<a name="mapping_istat_cp2011_get"></a>
> ClassificationMappingIstatResponse mapping_istat_cp2011_get(code)

Mapping ISTAT-CP2011

 This method provides the mapping from a [ISTAT-CP2011](http://professioni.istat.it/cp2011/) occupation code to: - [ESCO](https://ec.europa.eu/esco/portal) occupation codes; - [O*NET](https://www.onetonline.org/) occupation codes; - [ISCO](https://www.ilo.org/public/english/bureau/stat/isco/) occupation codes;  All requests are displayed in English. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import esco_api
from inda_hr.model.classification_mapping_istat_response import ClassificationMappingIstatResponse
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
    api_instance = esco_api.ESCOApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'code': "code_example",
    }
    try:
        # Mapping ISTAT-CP2011
        api_response = api_instance.mapping_istat_cp2011_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->mapping_istat_cp2011_get: %s\n" % e)
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
code | CodeSchema | | 


# CodeSchema

[ISTAT code](http://professioni.istat.it/cp2011/).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | [ISTAT code](http://professioni.istat.it/cp2011/). | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#mapping_istat_cp2011_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#mapping_istat_cp2011_get.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#mapping_istat_cp2011_get.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#mapping_istat_cp2011_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#mapping_istat_cp2011_get.ApiResponseFor422) | Validation Error

#### mapping_istat_cp2011_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassificationMappingIstatResponse**](../../models/ClassificationMappingIstatResponse.md) |  | 


#### mapping_istat_cp2011_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_istat_cp2011_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_istat_cp2011_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_istat_cp2011_get.ApiResponseFor422
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

# **mapping_onet_get**
<a name="mapping_onet_get"></a>
> ClassificationMappingOnetResponse mapping_onet_get(code)

Mapping O*NET

 This method provides the mapping from a [O*NET](https://www.onetonline.org/) occupation code to: - [ESCO](https://ec.europa.eu/esco/portal) occupation codes; - [ISTAT-CP2011](http://professioni.istat.it/cp2011/) occupation codes; - [ISCO](https://www.ilo.org/public/english/bureau/stat/isco/) occupation codes;  All requests are displayed in English. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import esco_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.classification_mapping_onet_response import ClassificationMappingOnetResponse
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
    api_instance = esco_api.ESCOApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'code': "code_example",
    }
    try:
        # Mapping O*NET
        api_response = api_instance.mapping_onet_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->mapping_onet_get: %s\n" % e)
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
code | CodeSchema | | 


# CodeSchema

[O*NET code](https://www.onetonline.org/).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | [O*NET code](https://www.onetonline.org/). | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#mapping_onet_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#mapping_onet_get.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#mapping_onet_get.ApiResponseFor400) | Bad Request
503 | [ApiResponseFor503](#mapping_onet_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#mapping_onet_get.ApiResponseFor422) | Validation Error

#### mapping_onet_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ClassificationMappingOnetResponse**](../../models/ClassificationMappingOnetResponse.md) |  | 


#### mapping_onet_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_onet_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_onet_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### mapping_onet_get.ApiResponseFor422
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

# **similar_esco_occupations_get**
<a name="similar_esco_occupations_get"></a>
> EscoJobtitleResponse similar_esco_occupations_get(query)

Similar ESCO Occupations

 This method provides the list of n most similar ESCO occupations given a *jobtitle*. For each returned occupation, the service provides also a list of the main related skills according to ESCO classification.  More details about ESCO occupations are showed [here](https://ec.europa.eu/esco/portal/occupation).  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import esco_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.esco_jobtitle_response import EscoJobtitleResponse
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
    api_instance = esco_api.ESCOApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'query': "query_example",
    }
    try:
        # Similar ESCO Occupations
        api_response = api_instance.similar_esco_occupations_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->similar_esco_occupations_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'query': "query_example",
        'dst_lang': "it",
        'size': 1,
        'min_score': 0.2,
    }
    try:
        # Similar ESCO Occupations
        api_response = api_instance.similar_esco_occupations_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->similar_esco_occupations_get: %s\n" % e)
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
query | QuerySchema | | 
dst_lang | DstLangSchema | | optional
size | SizeSchema | | optional
min_score | MinScoreSchema | | optional


# QuerySchema

A word or a brief sentence in several languages.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A word or a brief sentence in several languages. | 

# DstLangSchema

Language of the similar ESCO occupations.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Language of the similar ESCO occupations. | must be one of ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv", ] if omitted the server will use the default value of "it"

# SizeSchema

The maximum number of similar ESCO occupations retrieved by the algorithm.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of similar ESCO occupations retrieved by the algorithm. | if omitted the server will use the default value of 1

# MinScoreSchema

Minimum score of the similar ESCO occupations with respect to the job title queried by the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum score of the similar ESCO occupations with respect to the job title queried by the user. | if omitted the server will use the default value of 0.2

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#similar_esco_occupations_get.ApiResponseFor200) | Successful Response
500 | [ApiResponseFor500](#similar_esco_occupations_get.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#similar_esco_occupations_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#similar_esco_occupations_get.ApiResponseFor422) | Validation Error

#### similar_esco_occupations_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EscoJobtitleResponse**](../../models/EscoJobtitleResponse.md) |  | 


#### similar_esco_occupations_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### similar_esco_occupations_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### similar_esco_occupations_get.ApiResponseFor422
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

# **similar_esco_skills_get**
<a name="similar_esco_skills_get"></a>
> EscoSkillResponse similar_esco_skills_get(query)

Similar ESCO Skills

 This method provides the list of n most similar ESCO skills given a *skill*. For each returned skill, the service provides also a list of the main occupations where the skill is mandatory according to ESCO classification.  More details about ESCO skills are showed [here](https://ec.europa.eu/esco/portal/skill).  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import esco_api
from inda_hr.model.esco_skill_response import EscoSkillResponse
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
    api_instance = esco_api.ESCOApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'query': "query_example",
    }
    try:
        # Similar ESCO Skills
        api_response = api_instance.similar_esco_skills_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->similar_esco_skills_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'query': "query_example",
        'dst_lang': "it",
        'size': 1,
        'min_score': 0.2,
    }
    try:
        # Similar ESCO Skills
        api_response = api_instance.similar_esco_skills_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->similar_esco_skills_get: %s\n" % e)
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
query | QuerySchema | | 
dst_lang | DstLangSchema | | optional
size | SizeSchema | | optional
min_score | MinScoreSchema | | optional


# QuerySchema

A word or a brief sentence in several languages.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | A word or a brief sentence in several languages. | 

# DstLangSchema

Language of the similar ESCO skills.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Language of the similar ESCO skills. | must be one of ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv", ] if omitted the server will use the default value of "it"

# SizeSchema

The maximum number of similar ESCO skills retrieved by the algorithm.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | The maximum number of similar ESCO skills retrieved by the algorithm. | if omitted the server will use the default value of 1

# MinScoreSchema

Minimum score of the similar ESCO skills with respect to the skill queried by the user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum score of the similar ESCO skills with respect to the skill queried by the user. | if omitted the server will use the default value of 0.2

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#similar_esco_skills_get.ApiResponseFor200) | Successful Response
500 | [ApiResponseFor500](#similar_esco_skills_get.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#similar_esco_skills_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#similar_esco_skills_get.ApiResponseFor422) | Validation Error

#### similar_esco_skills_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EscoSkillResponse**](../../models/EscoSkillResponse.md) |  | 


#### similar_esco_skills_get.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### similar_esco_skills_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### similar_esco_skills_get.ApiResponseFor422
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

