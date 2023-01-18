<a name="__pageTop"></a>
# inda_hr.apis.tags.mapping_career_causeways_api.MappingCareerCausewaysApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**career_recommendation_post**](#career_recommendation_post) | **post** /hr/v2/resume/career/occupation/recommendation/ | Career Recommendation
[**occupation_activities_comparison_post**](#occupation_activities_comparison_post) | **post** /hr/v2/resume/career/occupation/activities/comparison/ | Occupation Activities Comparison
[**occupation_skill_comparison_post**](#occupation_skill_comparison_post) | **post** /hr/v2/resume/career/occupation/skills/comparison/ | Occupation Skill Comparison
[**upskilling_simulator_post**](#upskilling_simulator_post) | **post** /hr/v2/resume/career/simulator/upskilling/ | Upskilling simulator

# **career_recommendation_post**
<a name="career_recommendation_post"></a>
> TransitionRecommendations career_recommendation_post(career_transition_request)

Career Recommendation

This method provides an ordered list of recommended jobs transition, given an origin occupation. First, the algorithm  calculates the ESCO occupation that best matches the input job title. The ESCO match is provided  only if the match score is higher than `min_score`.  Viability, salary, and automation risk define the transition recommendations, and the user can select them by the *TransitionType* field: - `viable`: the algorithm recommends all similar occupations, ordered by similarity. No other considerations are made. - `desirable`: the algorithm recommends all similar occupations that offer comparable or higher pay levels. - `safe_desirable`: the algorithm recommends the subset of roles that will likely reduce    a worker's exposure to automation risk among the `desirable` transition.   - `strictly_safe_desirable`: the algorithm recommends among the `desirable` transition, the subset of roles with    lower automation risk and higher prevalence of bottleneck tasks.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import mapping_career_causeways_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.transition_recommendations import TransitionRecommendations
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.career_transition_request import CareerTransitionRequest
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
    api_instance = mapping_career_causeways_api.MappingCareerCausewaysApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = CareerTransitionRequest(
        origin_occupation="origin_occupation_example",
        transition_type="viable",
    )
    try:
        # Career Recommendation
        api_response = api_instance.career_recommendation_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->career_recommendation_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'dst_lang': "it",
        'min_score': 0.2,
    }
    body = CareerTransitionRequest(
        origin_occupation="origin_occupation_example",
        transition_type="viable",
    )
    try:
        # Career Recommendation
        api_response = api_instance.career_recommendation_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->career_recommendation_post: %s\n" % e)
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
[**CareerTransitionRequest**](../../models/CareerTransitionRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dst_lang | DstLangSchema | | optional
min_score | MinScoreSchema | | optional


# DstLangSchema

Output language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Output language. | must be one of ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv", ] if omitted the server will use the default value of "it"

# MinScoreSchema

Minimum similarity score for ESCO mapping.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum similarity score for ESCO mapping. | if omitted the server will use the default value of 0.2

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#career_recommendation_post.ApiResponseFor200) | Successfully Processed
500 | [ApiResponseFor500](#career_recommendation_post.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#career_recommendation_post.ApiResponseFor503) | Service Unavailable
400 | [ApiResponseFor400](#career_recommendation_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#career_recommendation_post.ApiResponseFor422) | Validation Error

#### career_recommendation_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TransitionRecommendations**](../../models/TransitionRecommendations.md) |  | 


#### career_recommendation_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### career_recommendation_post.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### career_recommendation_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### career_recommendation_post.ApiResponseFor422
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

# **occupation_activities_comparison_post**
<a name="occupation_activities_comparison_post"></a>
> WorkActivityComparison occupation_activities_comparison_post(work_activity_comparison_request)

Occupation Activities Comparison

This method provides a detailed comparison of the principal activities of the origin and destination occupation.  For each activity, the method shows the gap between the two occupations.   The activity comparison is based n the skill ESCO level. It ranges from one to three,  and it is related to the specificity of the activity.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import mapping_career_causeways_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.work_activity_comparison import WorkActivityComparison
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.work_activity_comparison_request import WorkActivityComparisonRequest
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
    api_instance = mapping_career_causeways_api.MappingCareerCausewaysApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = WorkActivityComparisonRequest(
        origin_occupation="origin_occupation_example",
        destination_occupation="destination_occupation_example",
        esco_level=1.0,
    )
    try:
        # Occupation Activities Comparison
        api_response = api_instance.occupation_activities_comparison_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->occupation_activities_comparison_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'dst_lang': "it",
        'min_score': 0.2,
    }
    body = WorkActivityComparisonRequest(
        origin_occupation="origin_occupation_example",
        destination_occupation="destination_occupation_example",
        esco_level=1.0,
    )
    try:
        # Occupation Activities Comparison
        api_response = api_instance.occupation_activities_comparison_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->occupation_activities_comparison_post: %s\n" % e)
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
[**WorkActivityComparisonRequest**](../../models/WorkActivityComparisonRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dst_lang | DstLangSchema | | optional
min_score | MinScoreSchema | | optional


# DstLangSchema

Output language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Output language. | must be one of ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv", ] if omitted the server will use the default value of "it"

# MinScoreSchema

Minimum similarity score for ESCO mapping.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum similarity score for ESCO mapping. | if omitted the server will use the default value of 0.2

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#occupation_activities_comparison_post.ApiResponseFor200) | Successfully Processed
500 | [ApiResponseFor500](#occupation_activities_comparison_post.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#occupation_activities_comparison_post.ApiResponseFor503) | Service Unavailable
400 | [ApiResponseFor400](#occupation_activities_comparison_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#occupation_activities_comparison_post.ApiResponseFor422) | Validation Error

#### occupation_activities_comparison_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**WorkActivityComparison**](../../models/WorkActivityComparison.md) |  | 


#### occupation_activities_comparison_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### occupation_activities_comparison_post.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### occupation_activities_comparison_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### occupation_activities_comparison_post.ApiResponseFor422
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

# **occupation_skill_comparison_post**
<a name="occupation_skill_comparison_post"></a>
> OccupationsSkillsComparison occupation_skill_comparison_post(occupation_skills_comparison_request)

Occupation Skill Comparison

This method provides a detailed comparison of the skills of the origin and destination occupations.  Such comparison helps compare the skill gaps among the occupations. Each skill of the origin occupation  is mapped to the most similar skill of the destination occupation. The mapping is one to one.   Skills are split in: - `essential`: only the most relevant skills for such occupation are considered according to ESCO Classification; - `optional`: both essential and optional skills are considered according to ESCO Classification.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import mapping_career_causeways_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.occupations_skills_comparison import OccupationsSkillsComparison
from inda_hr.model.occupation_skills_comparison_request import OccupationSkillsComparisonRequest
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
    api_instance = mapping_career_causeways_api.MappingCareerCausewaysApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = OccupationSkillsComparisonRequest(
        origin_occupation="origin_occupation_example",
        destination_occupation="destination_occupation_example",
        skill_match="optional",
    )
    try:
        # Occupation Skill Comparison
        api_response = api_instance.occupation_skill_comparison_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->occupation_skill_comparison_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'dst_lang': "it",
        'min_score': 0.2,
    }
    body = OccupationSkillsComparisonRequest(
        origin_occupation="origin_occupation_example",
        destination_occupation="destination_occupation_example",
        skill_match="optional",
    )
    try:
        # Occupation Skill Comparison
        api_response = api_instance.occupation_skill_comparison_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->occupation_skill_comparison_post: %s\n" % e)
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
[**OccupationSkillsComparisonRequest**](../../models/OccupationSkillsComparisonRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dst_lang | DstLangSchema | | optional
min_score | MinScoreSchema | | optional


# DstLangSchema

Output language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Output language. | must be one of ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv", ] if omitted the server will use the default value of "it"

# MinScoreSchema

Minimum similarity score for ESCO mapping.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum similarity score for ESCO mapping. | if omitted the server will use the default value of 0.2

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#occupation_skill_comparison_post.ApiResponseFor200) | Successfully Processed
500 | [ApiResponseFor500](#occupation_skill_comparison_post.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#occupation_skill_comparison_post.ApiResponseFor503) | Service Unavailable
400 | [ApiResponseFor400](#occupation_skill_comparison_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#occupation_skill_comparison_post.ApiResponseFor422) | Validation Error

#### occupation_skill_comparison_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**OccupationsSkillsComparison**](../../models/OccupationsSkillsComparison.md) |  | 


#### occupation_skill_comparison_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### occupation_skill_comparison_post.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### occupation_skill_comparison_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### occupation_skill_comparison_post.ApiResponseFor422
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

# **upskilling_simulator_post**
<a name="upskilling_simulator_post"></a>
> Upskilling upskilling_simulator_post(upskilling_request)

Upskilling simulator

Learning and getting new skills usually leads to new job opportunities. Given an origin occupation and a list of acquired skills,  this method provides an updated ordered list of recommended jobs transition based on your occupation skills and your acquired skills.  First, the algorithm  calculates the ESCO occupation that best matches the input job title and ESCO skills that best fits the input skills list.  The ESCO match is provided  only if the match score is higher than `min_score`.    Viability, salary, and automation risk define the transition recommendations, and the user can select them by the *TransitionType* field: - `viable`: the algorithm recommends all similar occupations, ordered by similarity. No other considerations are made; - `desirable`: the algorithm recommends all similar occupations that offer comparable or higher pay levels; - `safe_desirable`: the algorithm recommends the subset of roles that will likely reduce     a worker's exposure to automation risk among the `desirable` transition;   - `strictly_safe_desirable`: the algorithm recommends among the `desirable` transition, the subset of roles with     lower automation risk and higher prevalence of bottleneck tasks.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import mapping_career_causeways_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.upskilling_request import UpskillingRequest
from inda_hr.model.upskilling import Upskilling
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
    api_instance = mapping_career_causeways_api.MappingCareerCausewaysApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = UpskillingRequest(
        origin_occupation="origin_occupation_example",
        transition_type="viable",
        skills=[
            "skills_example"
        ],
    )
    try:
        # Upskilling simulator
        api_response = api_instance.upskilling_simulator_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->upskilling_simulator_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'dst_lang': "it",
        'min_score': 0.2,
    }
    body = UpskillingRequest(
        origin_occupation="origin_occupation_example",
        transition_type="viable",
        skills=[
            "skills_example"
        ],
    )
    try:
        # Upskilling simulator
        api_response = api_instance.upskilling_simulator_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->upskilling_simulator_post: %s\n" % e)
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
[**UpskillingRequest**](../../models/UpskillingRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
dst_lang | DstLangSchema | | optional
min_score | MinScoreSchema | | optional


# DstLangSchema

Output language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Output language. | must be one of ["bg", "cs", "da", "de", "el", "en", "es", "et", "fi", "fr", "hr", "hu", "it", "lt", "lv", "nl", "pl", "pt", "ro", "sk", "sl", "sv", ] if omitted the server will use the default value of "it"

# MinScoreSchema

Minimum similarity score for ESCO mapping.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum similarity score for ESCO mapping. | if omitted the server will use the default value of 0.2

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#upskilling_simulator_post.ApiResponseFor200) | Successfully Processed
500 | [ApiResponseFor500](#upskilling_simulator_post.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#upskilling_simulator_post.ApiResponseFor503) | Service Unavailable
400 | [ApiResponseFor400](#upskilling_simulator_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#upskilling_simulator_post.ApiResponseFor422) | Validation Error

#### upskilling_simulator_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Upskilling**](../../models/Upskilling.md) |  | 


#### upskilling_simulator_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### upskilling_simulator_post.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### upskilling_simulator_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### upskilling_simulator_post.ApiResponseFor422
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

