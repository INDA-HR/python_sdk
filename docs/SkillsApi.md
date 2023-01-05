# inda_hr.SkillsApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**similar_skills_get**](SkillsApi.md#similar_skills_get) | **GET** /hr/v2/skills/similar/semantic/ | Similar Skills
[**skills_classification_post**](SkillsApi.md#skills_classification_post) | **POST** /hr/v2/skills/classification/ | Skills Classification


# **similar_skills_get**
> SimilarEntitiesResponse similar_skills_get(query)

Similar Skills

 This method returns the *size* most similar skills found in the knowledge base with respect to the input *skill*.  The similarity of each result to the input skill is rated with a score between <code style='color: #333333; opacity: 0.9'>0</code> (minimum similarity) and <code style='color: #333333; opacity: 0.9'>1</code> (maximum similarity). This method can be used to perform a *keyword expansion*: expanding a skill with its synonyms or semantically similar skills may be useful, for instance, to improve a job description or to perform a more flexible search with respect to a traditional word match or boolean search system.  This method returns a dictionary with keys *Hits* (the number of skills returned) and *Out*, which is a list of dictionaries with two keys: the first key (*Term*) contains the proposed skill, while the second one (*Score*)  contains its similarity score, as described above. The parameter *min_score* set the threshold for the similarity score, below which the output skills are discarded; its default value is <code style='color: #333333; opacity: 0.9'>0.5</code>.  Note that the number of retrieved similar skills may be smaller than *size* when the minimum score is larger than zero or when the searched skill is particularly uncommon.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import skills_api
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
    query = "query_example" # str | Input skill to be analyzed
    size = 5 # int | Number of similar skills to return. (optional) if omitted the server will use the default value of 5
    min_score = 0.5 # float | Minimum pertinence score. (optional) if omitted the server will use the default value of 0.5
    src_lang = "it" # str | Optional. Language of the input skills.If missing, the detected language is assumed as `src_lang`. (optional)
    dst_lang = "it" # str | Optional. Language of the input skills.If missing, the detected language is assumed as `src_lang`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Similar Skills
        api_response = api_instance.similar_skills_get(query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling SkillsApi->similar_skills_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Similar Skills
        api_response = api_instance.similar_skills_get(query, size=size, min_score=min_score, src_lang=src_lang, dst_lang=dst_lang)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling SkillsApi->similar_skills_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Input skill to be analyzed |
 **size** | **int**| Number of similar skills to return. | [optional] if omitted the server will use the default value of 5
 **min_score** | **float**| Minimum pertinence score. | [optional] if omitted the server will use the default value of 0.5
 **src_lang** | **str**| Optional. Language of the input skills.If missing, the detected language is assumed as &#x60;src_lang&#x60;. | [optional]
 **dst_lang** | **str**| Optional. Language of the input skills.If missing, the detected language is assumed as &#x60;src_lang&#x60;. | [optional]

### Return type

[**SimilarEntitiesResponse**](SimilarEntitiesResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request Successfully Processed |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **skills_classification_post**
> SkillsClassificationResponse skills_classification_post(skills_classification_request)

Skills Classification

 This method returns a label associated to each given skill among the following: <code style='color: #333333; opacity: 0.9'>hard</code>, <code style='color: #333333; opacity: 0.9'>IT</code>, <code style='color: #333333; opacity: 0.9'>soft</code> and <code style='color: #333333; opacity: 0.9'>language</code>.  The request is structured according two main fields: *lang* and *skills*.  The *lang* field allows users to set the main language to which the skills to classify belong.  The *skills* field is merely the list of terms for which users want to find the closest category among the aforementioned ones. Please note that if a term is not recognized as a skill, it will be absent from the response.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import skills_api
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
    skills_classification_request = SkillsClassificationRequest(
        skills=[
            "skills_example",
        ],
    ) # SkillsClassificationRequest | 
    src_lang = "it" # str | Language of the input skills. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Skills Classification
        api_response = api_instance.skills_classification_post(skills_classification_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling SkillsApi->skills_classification_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Skills Classification
        api_response = api_instance.skills_classification_post(skills_classification_request, src_lang=src_lang)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling SkillsApi->skills_classification_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skills_classification_request** | [**SkillsClassificationRequest**](SkillsClassificationRequest.md)|  |
 **src_lang** | **str**| Language of the input skills. | [optional]

### Return type

[**SkillsClassificationResponse**](SkillsClassificationResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request Successfully Processed |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

