# inda_hr.ESCOApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**esco_occupations_hierarchy_get**](ESCOApi.md#esco_occupations_hierarchy_get) | **GET** /hr/v2/occupations/similar/esco/hierarchy/ | ESCO Occupations Hierarchy
[**esco_skills_hierarchy_get**](ESCOApi.md#esco_skills_hierarchy_get) | **GET** /hr/v2/skills/similar/esco/hierarchy/ | ESCO Skills Hierarchy
[**from_description_to_esco_occupations_post**](ESCOApi.md#from_description_to_esco_occupations_post) | **POST** /hr/v2/occupations/description/match/esco/ | From description to ESCO Occupations
[**from_description_to_esco_skills_post**](ESCOApi.md#from_description_to_esco_skills_post) | **POST** /hr/v2/skills/description/match/esco/ | From description to ESCO Skills
[**mapping_esco_get**](ESCOApi.md#mapping_esco_get) | **GET** /hr/v2/occupations/mapping/esco/ | Mapping ESCO
[**mapping_isco_get**](ESCOApi.md#mapping_isco_get) | **GET** /hr/v2/occupations/mapping/isco/ | Mapping ISCO
[**mapping_istat_cp2011_get**](ESCOApi.md#mapping_istat_cp2011_get) | **GET** /hr/v2/occupations/mapping/istat/ | Mapping ISTAT-CP2011
[**mapping_onet_get**](ESCOApi.md#mapping_onet_get) | **GET** /hr/v2/occupations/mapping/onet/ | Mapping O*NET
[**similar_esco_occupations_get**](ESCOApi.md#similar_esco_occupations_get) | **GET** /hr/v2/occupations/similar/esco/ | Similar ESCO Occupations
[**similar_esco_skills_get**](ESCOApi.md#similar_esco_skills_get) | **GET** /hr/v2/skills/similar/esco/ | Similar ESCO Skills


# **esco_occupations_hierarchy_get**
> MostSimilarJobtitleResponseCategorized esco_occupations_hierarchy_get(query)

ESCO Occupations Hierarchy

 This method provides the most similar ESCO job title given a *jobtitle* (that could be a word or a sentence in several languages), its hierarchy classification according with ISCO classification, and the top three industries and job functions where the occupation is distributed.  More details about ESCO occupations hierarchy are showed [here](https://ec.europa.eu/esco/portal/occupation).  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import esco_api
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
    query = "query_example" # str | It could be any word or sentence in several languages.
    dst_lang = "it" # str | Language of the similar ESCO occupations. (optional) if omitted the server will use the default value of "it"

    # example passing only required values which don't have defaults set
    try:
        # ESCO Occupations Hierarchy
        api_response = api_instance.esco_occupations_hierarchy_get(query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->esco_occupations_hierarchy_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ESCO Occupations Hierarchy
        api_response = api_instance.esco_occupations_hierarchy_get(query, dst_lang=dst_lang)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->esco_occupations_hierarchy_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| It could be any word or sentence in several languages. |
 **dst_lang** | **str**| Language of the similar ESCO occupations. | [optional] if omitted the server will use the default value of "it"

### Return type

[**MostSimilarJobtitleResponseCategorized**](MostSimilarJobtitleResponseCategorized.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **esco_skills_hierarchy_get**
> MostSimilarSkillResponseCategorized esco_skills_hierarchy_get(query)

ESCO Skills Hierarchy

 This method provides the most similar ESCO skills given a *query* (representing a skill) that could be a word or a sentence in several languages; also its hierarchy classification according with ESCO is returned.  More details about ESCO skills hierarchy are showed [here](https://ec.europa.eu/esco/portal/skill).  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import esco_api
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
    query = "query_example" # str | A word or a brief sentence in several languages.
    dst_lang = "it" # str | Language of the similar ESCO skills. (optional) if omitted the server will use the default value of "it"

    # example passing only required values which don't have defaults set
    try:
        # ESCO Skills Hierarchy
        api_response = api_instance.esco_skills_hierarchy_get(query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->esco_skills_hierarchy_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ESCO Skills Hierarchy
        api_response = api_instance.esco_skills_hierarchy_get(query, dst_lang=dst_lang)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->esco_skills_hierarchy_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| A word or a brief sentence in several languages. |
 **dst_lang** | **str**| Language of the similar ESCO skills. | [optional] if omitted the server will use the default value of "it"

### Return type

[**MostSimilarSkillResponseCategorized**](MostSimilarSkillResponseCategorized.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **from_description_to_esco_occupations_post**
> EscoJobtitleResponse from_description_to_esco_occupations_post(description_input)

From description to ESCO Occupations

 This method provides the list of n most affine ESCO occupations given a sentence or a long description. For each returned occupation, the service provides also a list of the main related skills according to ESCO classification.  More details about ESCO occupations are showed [here](https://ec.europa.eu/esco/portal/occupation).  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import esco_api
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
    description_input = DescriptionInput(
        description="description_example",
    ) # DescriptionInput | 
    dst_lang = "it" # str | Language of the similar ESCO occupations. (optional) if omitted the server will use the default value of "it"
    size = 1 # int | The maximum number of similar ESCO occupations retrieved by the algorithm. (optional) if omitted the server will use the default value of 1
    min_score = 0.2 # float | Minimum score of the similar ESCO occupations with respect to the job title queried by the user. (optional) if omitted the server will use the default value of 0.2

    # example passing only required values which don't have defaults set
    try:
        # From description to ESCO Occupations
        api_response = api_instance.from_description_to_esco_occupations_post(description_input)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->from_description_to_esco_occupations_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # From description to ESCO Occupations
        api_response = api_instance.from_description_to_esco_occupations_post(description_input, dst_lang=dst_lang, size=size, min_score=min_score)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->from_description_to_esco_occupations_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description_input** | [**DescriptionInput**](DescriptionInput.md)|  |
 **dst_lang** | **str**| Language of the similar ESCO occupations. | [optional] if omitted the server will use the default value of "it"
 **size** | **int**| The maximum number of similar ESCO occupations retrieved by the algorithm. | [optional] if omitted the server will use the default value of 1
 **min_score** | **float**| Minimum score of the similar ESCO occupations with respect to the job title queried by the user. | [optional] if omitted the server will use the default value of 0.2

### Return type

[**EscoJobtitleResponse**](EscoJobtitleResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **from_description_to_esco_skills_post**
> EscoSkillResponse from_description_to_esco_skills_post(description_input)

From description to ESCO Skills

 This method provides the list of n most affine ESCO skills given a sentence or a long description. For each returned skill, the service provides also a list of the main occupations where the skill is mandatory according to ESCO classification.  More details about ESCO skills are showed [here](https://ec.europa.eu/esco/portal/skill).  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import esco_api
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
    description_input = DescriptionInput(
        description="description_example",
    ) # DescriptionInput | 
    dst_lang = "it" # str | Language of the similar ESCO skills. (optional) if omitted the server will use the default value of "it"
    size = 1 # int | The maximum number of similar ESCO skills retrieved by the algorithm. (optional) if omitted the server will use the default value of 1
    min_score = 0.2 # float | Minimum score of the similar ESCO skills with respect to the skill queried by the user. (optional) if omitted the server will use the default value of 0.2

    # example passing only required values which don't have defaults set
    try:
        # From description to ESCO Skills
        api_response = api_instance.from_description_to_esco_skills_post(description_input)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->from_description_to_esco_skills_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # From description to ESCO Skills
        api_response = api_instance.from_description_to_esco_skills_post(description_input, dst_lang=dst_lang, size=size, min_score=min_score)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->from_description_to_esco_skills_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **description_input** | [**DescriptionInput**](DescriptionInput.md)|  |
 **dst_lang** | **str**| Language of the similar ESCO skills. | [optional] if omitted the server will use the default value of "it"
 **size** | **int**| The maximum number of similar ESCO skills retrieved by the algorithm. | [optional] if omitted the server will use the default value of 1
 **min_score** | **float**| Minimum score of the similar ESCO skills with respect to the skill queried by the user. | [optional] if omitted the server will use the default value of 0.2

### Return type

[**EscoSkillResponse**](EscoSkillResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mapping_esco_get**
> ClassificationMappingEscoResponse mapping_esco_get(code)

Mapping ESCO

 This method provides the mapping from a [ESCO](https://ec.europa.eu/esco/portal) occupation code to: - [ISCO](https://www.ilo.org/public/english/bureau/stat/isco/) occupation codes; - [O*NET](https://www.onetonline.org/) occupation codes; - [ISTAT-CP2011](http://professioni.istat.it/cp2011/) occupation codes;  All requests are displayed in English. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import esco_api
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
    code = "code_example" # str | [ESCO code](https://ec.europa.eu/esco/portal/occupation).

    # example passing only required values which don't have defaults set
    try:
        # Mapping ESCO
        api_response = api_instance.mapping_esco_get(code)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->mapping_esco_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| [ESCO code](https://ec.europa.eu/esco/portal/occupation). |

### Return type

[**ClassificationMappingEscoResponse**](ClassificationMappingEscoResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mapping_isco_get**
> ClassificationMappingIscoResponse mapping_isco_get(code)

Mapping ISCO

 This method provides the mapping from a [ISCO](https://www.ilo.org/public/english/bureau/stat/isco/) occupation code to: - [ESCO](https://ec.europa.eu/esco/portal) occupation codes; - [O*NET](https://www.onetonline.org/) occupation codes; - [ISTAT-CP2011](http://professioni.istat.it/cp2011/) occupation codes;  All requests are displayed in English. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import esco_api
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
    code = "code_example" # str | [ISCO code](https://www.ilo.org/public/english/bureau/stat/isco/).

    # example passing only required values which don't have defaults set
    try:
        # Mapping ISCO
        api_response = api_instance.mapping_isco_get(code)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->mapping_isco_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| [ISCO code](https://www.ilo.org/public/english/bureau/stat/isco/). |

### Return type

[**ClassificationMappingIscoResponse**](ClassificationMappingIscoResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mapping_istat_cp2011_get**
> ClassificationMappingIstatResponse mapping_istat_cp2011_get(code)

Mapping ISTAT-CP2011

 This method provides the mapping from a [ISTAT-CP2011](http://professioni.istat.it/cp2011/) occupation code to: - [ESCO](https://ec.europa.eu/esco/portal) occupation codes; - [O*NET](https://www.onetonline.org/) occupation codes; - [ISCO](https://www.ilo.org/public/english/bureau/stat/isco/) occupation codes;  All requests are displayed in English. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import esco_api
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
    code = "code_example" # str | [ISTAT code](http://professioni.istat.it/cp2011/).

    # example passing only required values which don't have defaults set
    try:
        # Mapping ISTAT-CP2011
        api_response = api_instance.mapping_istat_cp2011_get(code)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->mapping_istat_cp2011_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| [ISTAT code](http://professioni.istat.it/cp2011/). |

### Return type

[**ClassificationMappingIstatResponse**](ClassificationMappingIstatResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mapping_onet_get**
> ClassificationMappingOnetResponse mapping_onet_get(code)

Mapping O*NET

 This method provides the mapping from a [O*NET](https://www.onetonline.org/) occupation code to: - [ESCO](https://ec.europa.eu/esco/portal) occupation codes; - [ISTAT-CP2011](http://professioni.istat.it/cp2011/) occupation codes; - [ISCO](https://www.ilo.org/public/english/bureau/stat/isco/) occupation codes;  All requests are displayed in English. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import esco_api
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
    code = "code_example" # str | [O*NET code](https://www.onetonline.org/).

    # example passing only required values which don't have defaults set
    try:
        # Mapping O*NET
        api_response = api_instance.mapping_onet_get(code)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->mapping_onet_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| [O*NET code](https://www.onetonline.org/). |

### Return type

[**ClassificationMappingOnetResponse**](ClassificationMappingOnetResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **similar_esco_occupations_get**
> EscoJobtitleResponse similar_esco_occupations_get(query)

Similar ESCO Occupations

 This method provides the list of n most similar ESCO occupations given a *jobtitle*. For each returned occupation, the service provides also a list of the main related skills according to ESCO classification.  More details about ESCO occupations are showed [here](https://ec.europa.eu/esco/portal/occupation).  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import esco_api
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
    query = "query_example" # str | A word or a brief sentence in several languages.
    dst_lang = "it" # str | Language of the similar ESCO occupations. (optional) if omitted the server will use the default value of "it"
    size = 1 # int | The maximum number of similar ESCO occupations retrieved by the algorithm. (optional) if omitted the server will use the default value of 1
    min_score = 0.2 # float | Minimum score of the similar ESCO occupations with respect to the job title queried by the user. (optional) if omitted the server will use the default value of 0.2

    # example passing only required values which don't have defaults set
    try:
        # Similar ESCO Occupations
        api_response = api_instance.similar_esco_occupations_get(query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->similar_esco_occupations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Similar ESCO Occupations
        api_response = api_instance.similar_esco_occupations_get(query, dst_lang=dst_lang, size=size, min_score=min_score)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->similar_esco_occupations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| A word or a brief sentence in several languages. |
 **dst_lang** | **str**| Language of the similar ESCO occupations. | [optional] if omitted the server will use the default value of "it"
 **size** | **int**| The maximum number of similar ESCO occupations retrieved by the algorithm. | [optional] if omitted the server will use the default value of 1
 **min_score** | **float**| Minimum score of the similar ESCO occupations with respect to the job title queried by the user. | [optional] if omitted the server will use the default value of 0.2

### Return type

[**EscoJobtitleResponse**](EscoJobtitleResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **similar_esco_skills_get**
> EscoSkillResponse similar_esco_skills_get(query)

Similar ESCO Skills

 This method provides the list of n most similar ESCO skills given a *skill*. For each returned skill, the service provides also a list of the main occupations where the skill is mandatory according to ESCO classification.  More details about ESCO skills are showed [here](https://ec.europa.eu/esco/portal/skill).  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import esco_api
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
    query = "query_example" # str | A word or a brief sentence in several languages.
    dst_lang = "it" # str | Language of the similar ESCO skills. (optional) if omitted the server will use the default value of "it"
    size = 1 # int | The maximum number of similar ESCO skills retrieved by the algorithm. (optional) if omitted the server will use the default value of 1
    min_score = 0.2 # float | Minimum score of the similar ESCO skills with respect to the skill queried by the user. (optional) if omitted the server will use the default value of 0.2

    # example passing only required values which don't have defaults set
    try:
        # Similar ESCO Skills
        api_response = api_instance.similar_esco_skills_get(query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->similar_esco_skills_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Similar ESCO Skills
        api_response = api_instance.similar_esco_skills_get(query, dst_lang=dst_lang, size=size, min_score=min_score)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ESCOApi->similar_esco_skills_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| A word or a brief sentence in several languages. |
 **dst_lang** | **str**| Language of the similar ESCO skills. | [optional] if omitted the server will use the default value of "it"
 **size** | **int**| The maximum number of similar ESCO skills retrieved by the algorithm. | [optional] if omitted the server will use the default value of 1
 **min_score** | **float**| Minimum score of the similar ESCO skills with respect to the skill queried by the user. | [optional] if omitted the server will use the default value of 0.2

### Return type

[**EscoSkillResponse**](EscoSkillResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

