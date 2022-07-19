# inda_hr.MappingCareerCausewaysApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**career_recommendation_post**](MappingCareerCausewaysApi.md#career_recommendation_post) | **POST** /hr/v2/resume/career/occupation/recommendation/ | Career Recommendation
[**occupation_activities_comparison_post**](MappingCareerCausewaysApi.md#occupation_activities_comparison_post) | **POST** /hr/v2/resume/career/occupation/activities/comparison/ | Occupation Activities Comparison
[**occupation_skill_comparison_post**](MappingCareerCausewaysApi.md#occupation_skill_comparison_post) | **POST** /hr/v2/resume/career/occupation/skills/comparison/ | Occupation Skill Comparison
[**upskilling_simulator_post**](MappingCareerCausewaysApi.md#upskilling_simulator_post) | **POST** /hr/v2/resume/career/simulator/upskilling/ | Upskilling simulator


# **career_recommendation_post**
> TransitionRecommendations career_recommendation_post(career_transition_request)

Career Recommendation

 This method provides an ordered list of recommended jobs transition, given an origin occupation. First, the algorithm  calculates the ESCO occupation that best matches the input job title. The ESCO match is provided  only if the match score is higher than `min_score`.  Viability, salary, and automation risk define the transition recommendations, and the user can select them by the *TransitionType* field: - `viable`: the algorithm recommends all similar occupations, ordered by similarity. No other considerations are made. - `desirable`: the algorithm recommends all similar occupations that offer comparable or higher pay levels. - `safe_desirable`: the algorithm recommends the subset of roles that will likely reduce    a worker's exposure to automation risk among the `desirable` transition.   - `strictly_safe_desirable`: the algorithm recommends among the `desirable` transition, the subset of roles with    lower automation risk and higher prevalence of bottleneck tasks. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import mapping_career_causeways_api
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
    career_transition_request = CareerTransitionRequest(
        origin_occupation="origin_occupation_example",
        transition_type="viable",
    ) # CareerTransitionRequest | 
    lang = "it" # str | Output language. (optional) if omitted the server will use the default value of "it"
    min_score = 0.2 # float | Minimum similarity score for ESCO mapping. (optional) if omitted the server will use the default value of 0.2

    # example passing only required values which don't have defaults set
    try:
        # Career Recommendation
        api_response = api_instance.career_recommendation_post(career_transition_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->career_recommendation_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Career Recommendation
        api_response = api_instance.career_recommendation_post(career_transition_request, lang=lang, min_score=min_score)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->career_recommendation_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **career_transition_request** | [**CareerTransitionRequest**](CareerTransitionRequest.md)|  |
 **lang** | **str**| Output language. | [optional] if omitted the server will use the default value of "it"
 **min_score** | **float**| Minimum similarity score for ESCO mapping. | [optional] if omitted the server will use the default value of 0.2

### Return type

[**TransitionRecommendations**](TransitionRecommendations.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Processed |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **occupation_activities_comparison_post**
> WorkActivityComparison occupation_activities_comparison_post(work_activity_comparison_request)

Occupation Activities Comparison

 This method provides a detailed comparison of the principal activities of the origin and destination occupation.  For each activity, the method shows the gap between the two occupations.   The activity comparison is based n the skill ESCO level. It ranges from one to three,  and it is related to the specificity of the activity.   

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import mapping_career_causeways_api
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
    work_activity_comparison_request = WorkActivityComparisonRequest(
        origin_occupation="origin_occupation_example",
        destination_occupation="destination_occupation_example",
        esco_level=1.0,
    ) # WorkActivityComparisonRequest | 
    lang = "it" # str | Output language. (optional) if omitted the server will use the default value of "it"
    min_score = 0.2 # float | Minimum similarity score for ESCO mapping. (optional) if omitted the server will use the default value of 0.2

    # example passing only required values which don't have defaults set
    try:
        # Occupation Activities Comparison
        api_response = api_instance.occupation_activities_comparison_post(work_activity_comparison_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->occupation_activities_comparison_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Occupation Activities Comparison
        api_response = api_instance.occupation_activities_comparison_post(work_activity_comparison_request, lang=lang, min_score=min_score)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->occupation_activities_comparison_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_activity_comparison_request** | [**WorkActivityComparisonRequest**](WorkActivityComparisonRequest.md)|  |
 **lang** | **str**| Output language. | [optional] if omitted the server will use the default value of "it"
 **min_score** | **float**| Minimum similarity score for ESCO mapping. | [optional] if omitted the server will use the default value of 0.2

### Return type

[**WorkActivityComparison**](WorkActivityComparison.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Processed |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **occupation_skill_comparison_post**
> OccupationsSkillsComparison occupation_skill_comparison_post(occupation_skills_comparison_request)

Occupation Skill Comparison

 This method provides a detailed comparison of the skills of the origin and destination occupations.  Such comparison helps compare the skill gaps among the occupations. Each skill of the origin occupation  is mapped to the most similar skill of the destination occupation. The mapping is one to one.   Skills are split in: - `essential`: only the most relevant skills for such occupation are considered according to ESCO Classification; - `optional`: both essential and optional skills are considered according to ESCO Classification.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import mapping_career_causeways_api
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
    occupation_skills_comparison_request = OccupationSkillsComparisonRequest(
        origin_occupation="origin_occupation_example",
        destination_occupation="destination_occupation_example",
        skill_match="optional",
    ) # OccupationSkillsComparisonRequest | 
    lang = "it" # str | Output language. (optional) if omitted the server will use the default value of "it"
    min_score = 0.2 # float | Minimum similarity score for ESCO mapping. (optional) if omitted the server will use the default value of 0.2

    # example passing only required values which don't have defaults set
    try:
        # Occupation Skill Comparison
        api_response = api_instance.occupation_skill_comparison_post(occupation_skills_comparison_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->occupation_skill_comparison_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Occupation Skill Comparison
        api_response = api_instance.occupation_skill_comparison_post(occupation_skills_comparison_request, lang=lang, min_score=min_score)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->occupation_skill_comparison_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **occupation_skills_comparison_request** | [**OccupationSkillsComparisonRequest**](OccupationSkillsComparisonRequest.md)|  |
 **lang** | **str**| Output language. | [optional] if omitted the server will use the default value of "it"
 **min_score** | **float**| Minimum similarity score for ESCO mapping. | [optional] if omitted the server will use the default value of 0.2

### Return type

[**OccupationsSkillsComparison**](OccupationsSkillsComparison.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Processed |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upskilling_simulator_post**
> Upskilling upskilling_simulator_post(upskilling_request)

Upskilling simulator

 Learning and getting new skills usually leads to new job opportunities. Given an origin occupation and a list of acquired skills,  this method provides an updated ordered list of recommended jobs transition based on your occupation skills and your acquired skills.  First, the algorithm  calculates the ESCO occupation that best matches the input job title and ESCO skills that best fits the input skills list.  The ESCO match is provided  only if the match score is higher than `min_score`.    Viability, salary, and automation risk define the transition recommendations, and the user can select them by the *TransitionType* field: - `viable`: the algorithm recommends all similar occupations, ordered by similarity. No other considerations are made; - `desirable`: the algorithm recommends all similar occupations that offer comparable or higher pay levels; - `safe_desirable`: the algorithm recommends the subset of roles that will likely reduce     a worker's exposure to automation risk among the `desirable` transition;   - `strictly_safe_desirable`: the algorithm recommends among the `desirable` transition, the subset of roles with     lower automation risk and higher prevalence of bottleneck tasks. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import mapping_career_causeways_api
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
    upskilling_request = UpskillingRequest(
        origin_occupation="origin_occupation_example",
        transition_type="viable",
        skills=[
            "skills_example",
        ],
    ) # UpskillingRequest | 
    lang = "it" # str | Output language. (optional) if omitted the server will use the default value of "it"
    min_score = 0.2 # float | Minimum similarity score for ESCO mapping. (optional) if omitted the server will use the default value of 0.2

    # example passing only required values which don't have defaults set
    try:
        # Upskilling simulator
        api_response = api_instance.upskilling_simulator_post(upskilling_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->upskilling_simulator_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upskilling simulator
        api_response = api_instance.upskilling_simulator_post(upskilling_request, lang=lang, min_score=min_score)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling MappingCareerCausewaysApi->upskilling_simulator_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upskilling_request** | [**UpskillingRequest**](UpskillingRequest.md)|  |
 **lang** | **str**| Output language. | [optional] if omitted the server will use the default value of "it"
 **min_score** | **float**| Minimum similarity score for ESCO mapping. | [optional] if omitted the server will use the default value of 0.2

### Return type

[**Upskilling**](Upskilling.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Processed |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

