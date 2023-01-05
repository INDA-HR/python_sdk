# inda_hr.JobAdKnowledgeExtractionApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_jobtitles_from_jobad_post**](JobAdKnowledgeExtractionApi.md#extract_jobtitles_from_jobad_post) | **POST** /hr/v2/parse/jobad/jobtitles/ | Extract JobTitles from JobAd
[**extract_languages_from_jobad_post**](JobAdKnowledgeExtractionApi.md#extract_languages_from_jobad_post) | **POST** /hr/v2/parse/jobad/languages/ | Extract Languages from JobAd
[**extract_skills_from_jobad_post**](JobAdKnowledgeExtractionApi.md#extract_skills_from_jobad_post) | **POST** /hr/v2/parse/jobad/skills/ | Extract Skills from JobAd


# **extract_jobtitles_from_jobad_post**
> JobAdJobTitlesResponse extract_jobtitles_from_jobad_post(job_ad_job_description_request)

Extract JobTitles from JobAd

 This method extract job titles that are semantically related with a job advert.  The input is a json containing the structure of the advert, as described in the schema below and in the example on the right.  The field *sections* in the body contains a list of documents, which correspond to distinct sections of the advert (e.g., company description, job description, requirements); in each document, the field *content* contains the text of the section, while the field *weight* (a number between <code style='color: #333333; opacity: 0.9'>0</code> and <code style='color: #333333; opacity: 0.9'>1</code>) can be used to give different weights to the different sections in the skill extraction (e.g., a section with the requirements is probably much more relevant for the skill extraction than a section with the company description); in the absence of the field *value*, the maximum value (i.e., *weight* = <code style='color: #333333; opacity: 0.9'>1</code>) will be assumed.  The field *header* contains the information about the job title. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_knowledge_extraction_api
from inda_hr.model.job_ad_job_description_request import JobAdJobDescriptionRequest
from inda_hr.model.job_ad_job_titles_response import JobAdJobTitlesResponse
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
    api_instance = job_ad_knowledge_extraction_api.JobAdKnowledgeExtractionApi(api_client)
    job_ad_job_description_request = JobAdJobDescriptionRequest(
        data=SlimData(
            job_title=JobTitleHeader(
                details=JobTitleHeaderDetails(
                    text_positions=[
                        TextPosition(
                            start=1,
                            end=1,
                        ),
                    ],
                    raw_value="raw_value_example",
                    raw_values=[
                        TextDetails(
                            text_positions=[
                                TextPosition(
                                    start=1,
                                    end=1,
                                ),
                            ],
                            raw_value="raw_value_example",
                        ),
                    ],
                    is_validated=False,
                    entity_type="entity_type_example",
                    proficiency_level="proficiency_level_example",
                    category="category_example",
                    code=JobAdJobTitleCode(
                        key="key_example",
                    ),
                    weight=0.8,
                ),
                value="value_example",
            ),
            job_description=JobDescription(
                company_description=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
                position_description=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
                position_requirements=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
                additional_information=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
            ),
        ),
        metadata=OptionalMetadata(
            language="it",
        ),
    ) # JobAdJobDescriptionRequest | 
    src_lang = "it" # str | Job Description language. If left empty each section's language will detected automatically. (optional)
    dst_lang = "it" # str | Extracted entities destination language. If left empty is assumed to be equal to the Job Description language. (optional)
    size = 10 # int | Number of job titles to be returned, must be greater than <code style='color: #333333; opacity: 0.9'>0</code> and smaller or equal to <code style='color: #333333; opacity: 0.9'>20</code>. (optional) if omitted the server will use the default value of 10
    min_score = 0.2 # float | Minimum score for the proposed job titles. The job titles with a score lower than this value will be neglected. (optional) if omitted the server will use the default value of 0.2

    # example passing only required values which don't have defaults set
    try:
        # Extract JobTitles from JobAd
        api_response = api_instance.extract_jobtitles_from_jobad_post(job_ad_job_description_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_jobtitles_from_jobad_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Extract JobTitles from JobAd
        api_response = api_instance.extract_jobtitles_from_jobad_post(job_ad_job_description_request, src_lang=src_lang, dst_lang=dst_lang, size=size, min_score=min_score)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_jobtitles_from_jobad_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_ad_job_description_request** | [**JobAdJobDescriptionRequest**](JobAdJobDescriptionRequest.md)|  |
 **src_lang** | **str**| Job Description language. If left empty each section&#39;s language will detected automatically. | [optional]
 **dst_lang** | **str**| Extracted entities destination language. If left empty is assumed to be equal to the Job Description language. | [optional]
 **size** | **int**| Number of job titles to be returned, must be greater than &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;0&lt;/code&gt; and smaller or equal to &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;20&lt;/code&gt;. | [optional] if omitted the server will use the default value of 10
 **min_score** | **float**| Minimum score for the proposed job titles. The job titles with a score lower than this value will be neglected. | [optional] if omitted the server will use the default value of 0.2

### Return type

[**JobAdJobTitlesResponse**](JobAdJobTitlesResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document Successfully Processed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_languages_from_jobad_post**
> JobAdLanguagesResponse extract_languages_from_jobad_post(job_ad_job_description_request)

Extract Languages from JobAd

 This method extract job titles that are semantically related with a job advert.  The input is a json containing the structure of the advert, as described in the schema below and in the example on the right.  The field *sections* in the body contains a list of documents, which correspond to distinct sections of the advert (e.g., company description, job description, requirements); in each document, the field *content* contains the text of the section, while the field *weight* (a number between <code style='color: #333333; opacity: 0.9'>0</code> and <code style='color: #333333; opacity: 0.9'>1</code>) can be used to give different weights to the different sections in the skill extraction (e.g., a section with the requirements is probably much more relevant for the skill extraction than a section with the company description); in the absence of the field *value*, the maximum value (i.e., *weight* = <code style='color: #333333; opacity: 0.9'>1</code>) will be assumed.  The field *header* contains the information about the job title. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_knowledge_extraction_api
from inda_hr.model.job_ad_job_description_request import JobAdJobDescriptionRequest
from inda_hr.model.job_ad_languages_response import JobAdLanguagesResponse
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
    api_instance = job_ad_knowledge_extraction_api.JobAdKnowledgeExtractionApi(api_client)
    job_ad_job_description_request = JobAdJobDescriptionRequest(
        data=SlimData(
            job_title=JobTitleHeader(
                details=JobTitleHeaderDetails(
                    text_positions=[
                        TextPosition(
                            start=1,
                            end=1,
                        ),
                    ],
                    raw_value="raw_value_example",
                    raw_values=[
                        TextDetails(
                            text_positions=[
                                TextPosition(
                                    start=1,
                                    end=1,
                                ),
                            ],
                            raw_value="raw_value_example",
                        ),
                    ],
                    is_validated=False,
                    entity_type="entity_type_example",
                    proficiency_level="proficiency_level_example",
                    category="category_example",
                    code=JobAdJobTitleCode(
                        key="key_example",
                    ),
                    weight=0.8,
                ),
                value="value_example",
            ),
            job_description=JobDescription(
                company_description=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
                position_description=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
                position_requirements=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
                additional_information=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
            ),
        ),
        metadata=OptionalMetadata(
            language="it",
        ),
    ) # JobAdJobDescriptionRequest | 
    src_lang = "it" # str | Job Description language. If left empty each section's language will detected automatically. (optional)
    dst_lang = "it" # str | Extracted entities destination language. If left empty is assumed to be equal to the Job Description language. (optional)
    size = 10 # int | Number of languages to be returned, must be greater than <code style='color: #333333; opacity: 0.9'>0</code> and smaller or equal to <code style='color: #333333; opacity: 0.9'>20</code>. (optional) if omitted the server will use the default value of 10
    min_score = 0.2 # float | Minimum score for the proposed languages. The languages with a score lower than this value will be neglected. (optional) if omitted the server will use the default value of 0.2

    # example passing only required values which don't have defaults set
    try:
        # Extract Languages from JobAd
        api_response = api_instance.extract_languages_from_jobad_post(job_ad_job_description_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_languages_from_jobad_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Extract Languages from JobAd
        api_response = api_instance.extract_languages_from_jobad_post(job_ad_job_description_request, src_lang=src_lang, dst_lang=dst_lang, size=size, min_score=min_score)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_languages_from_jobad_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_ad_job_description_request** | [**JobAdJobDescriptionRequest**](JobAdJobDescriptionRequest.md)|  |
 **src_lang** | **str**| Job Description language. If left empty each section&#39;s language will detected automatically. | [optional]
 **dst_lang** | **str**| Extracted entities destination language. If left empty is assumed to be equal to the Job Description language. | [optional]
 **size** | **int**| Number of languages to be returned, must be greater than &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;0&lt;/code&gt; and smaller or equal to &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;20&lt;/code&gt;. | [optional] if omitted the server will use the default value of 10
 **min_score** | **float**| Minimum score for the proposed languages. The languages with a score lower than this value will be neglected. | [optional] if omitted the server will use the default value of 0.2

### Return type

[**JobAdLanguagesResponse**](JobAdLanguagesResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document Successfully Processed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extract_skills_from_jobad_post**
> JobAdSkillsResponse extract_skills_from_jobad_post(job_ad_job_description_request)

Extract Skills from JobAd

 This method extract job skills (both hard and soft skills) that are semantically related with a job advert.  The input is a json containing the structure of the advert, as described in the schema below and in the example on the right.  The field *sections* in the body contains a list of documents, which correspond to distinct sections of the advert (e.g., company description, job description, requirements); in each document, the field *content* contains the text of the section, while the field *weight* (a number between <code style='color: #333333; opacity: 0.9'>0</code> and <code style='color: #333333; opacity: 0.9'>1</code>) can be used to give different weights to the different sections in the skill extraction (e.g., a section with the requirements is probably much more relevant for the skill extraction than a section with the company description); in the absence of the field *value*, the maximum value (i.e., *weight* = <code style='color: #333333; opacity: 0.9'>1</code>) will be assumed.  The field *header* contains the information about the job title. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_knowledge_extraction_api
from inda_hr.model.job_ad_job_description_request import JobAdJobDescriptionRequest
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.job_ad_skills_response import JobAdSkillsResponse
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
    api_instance = job_ad_knowledge_extraction_api.JobAdKnowledgeExtractionApi(api_client)
    job_ad_job_description_request = JobAdJobDescriptionRequest(
        data=SlimData(
            job_title=JobTitleHeader(
                details=JobTitleHeaderDetails(
                    text_positions=[
                        TextPosition(
                            start=1,
                            end=1,
                        ),
                    ],
                    raw_value="raw_value_example",
                    raw_values=[
                        TextDetails(
                            text_positions=[
                                TextPosition(
                                    start=1,
                                    end=1,
                                ),
                            ],
                            raw_value="raw_value_example",
                        ),
                    ],
                    is_validated=False,
                    entity_type="entity_type_example",
                    proficiency_level="proficiency_level_example",
                    category="category_example",
                    code=JobAdJobTitleCode(
                        key="key_example",
                    ),
                    weight=0.8,
                ),
                value="value_example",
            ),
            job_description=JobDescription(
                company_description=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
                position_description=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
                position_requirements=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
                additional_information=Section(
                    details=SectionDetails(
                        language="de",
                        weight=0.8,
                    ),
                    title=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ),
            ),
        ),
        metadata=OptionalMetadata(
            language="it",
        ),
    ) # JobAdJobDescriptionRequest | 
    src_lang = "it" # str | Job Description language. If left empty each section's language will detected automatically. (optional)
    dst_lang = "it" # str | Extracted entities destination language. If left empty is assumed to be equal to the Job Description language. (optional)
    size = 10 # int | Number of skills to be returned, must be greater than <code style='color: #333333; opacity: 0.9'>0</code> and smaller or equal to <code style='color: #333333; opacity: 0.9'>20</code>. (optional) if omitted the server will use the default value of 10
    min_score = 0.2 # float | Minimum score for the proposed skills. The skills with a score lower than this value will be neglected. (optional) if omitted the server will use the default value of 0.2

    # example passing only required values which don't have defaults set
    try:
        # Extract Skills from JobAd
        api_response = api_instance.extract_skills_from_jobad_post(job_ad_job_description_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_skills_from_jobad_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Extract Skills from JobAd
        api_response = api_instance.extract_skills_from_jobad_post(job_ad_job_description_request, src_lang=src_lang, dst_lang=dst_lang, size=size, min_score=min_score)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_skills_from_jobad_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_ad_job_description_request** | [**JobAdJobDescriptionRequest**](JobAdJobDescriptionRequest.md)|  |
 **src_lang** | **str**| Job Description language. If left empty each section&#39;s language will detected automatically. | [optional]
 **dst_lang** | **str**| Extracted entities destination language. If left empty is assumed to be equal to the Job Description language. | [optional]
 **size** | **int**| Number of skills to be returned, must be greater than &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;0&lt;/code&gt; and smaller or equal to &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;20&lt;/code&gt;. | [optional] if omitted the server will use the default value of 10
 **min_score** | **float**| Minimum score for the proposed skills. The skills with a score lower than this value will be neglected. | [optional] if omitted the server will use the default value of 0.2

### Return type

[**JobAdSkillsResponse**](JobAdSkillsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document Successfully Processed |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

