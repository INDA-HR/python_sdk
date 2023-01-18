<a name="__pageTop"></a>
# inda_hr.apis.tags.job_ad_knowledge_extraction_api.JobAdKnowledgeExtractionApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**extract_jobtitles_from_jobad_post**](#extract_jobtitles_from_jobad_post) | **post** /hr/v2/parse/jobad/jobtitles/ | Extract JobTitles from JobAd
[**extract_languages_from_jobad_post**](#extract_languages_from_jobad_post) | **post** /hr/v2/parse/jobad/languages/ | Extract Languages from JobAd
[**extract_skills_from_jobad_post**](#extract_skills_from_jobad_post) | **post** /hr/v2/parse/jobad/skills/ | Extract Skills from JobAd

# **extract_jobtitles_from_jobad_post**
<a name="extract_jobtitles_from_jobad_post"></a>
> JobAdJobTitlesResponse extract_jobtitles_from_jobad_post(job_ad_job_description_request)

Extract JobTitles from JobAd

 This method extract job titles that are semantically related with a job advert.  The input is a json containing the structure of the advert, as described in the schema below and in the example on the right.  The field *sections* in the body contains a list of documents, which correspond to distinct sections of the advert (e.g., company description, job description, requirements); in each document, the field *content* contains the text of the section, while the field *weight* (a number between <code style='color: #333333; opacity: 0.9'>0</code> and <code style='color: #333333; opacity: 0.9'>1</code>) can be used to give different weights to the different sections in the skill extraction (e.g., a section with the requirements is probably much more relevant for the skill extraction than a section with the company description); in the absence of the field *value*, the maximum value (i.e., *weight* = <code style='color: #333333; opacity: 0.9'>1</code>) will be assumed.  The field *header* contains the information about the job title. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_knowledge_extraction_api
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

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = JobAdJobDescriptionRequest(
        data=SlimData(
            job_title=JobTitleHeader(
                details=JobTitleHeaderDetails(
                    text_positions=[
                        TextPosition(
                            start=1,
                            end=1,
                        )
                    ],
                    raw_value="raw_value_example",
                    raw_values=[
                        TextDetails(
                            text_positions=[
                                TextPosition()
                            ],
                            raw_value="raw_value_example",
                        )
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
,
                ),
                position_description=Section(),
                position_requirements=Section(),
                additional_information=Section(),
            ),
        ),
        metadata=OptionalMetadata(
            language="it",
        ),
    )
    try:
        # Extract JobTitles from JobAd
        api_response = api_instance.extract_jobtitles_from_jobad_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_jobtitles_from_jobad_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'src_lang': "it",
        'dst_lang': "it",
        'size': 10,
        'min_score': 0.2,
    }
    body = JobAdJobDescriptionRequest(
        data=SlimData(
            job_title=JobTitleHeader(
                details=JobTitleHeaderDetails(
                    text_positions=[
                        TextPosition(
                            start=1,
                            end=1,
                        )
                    ],
                    raw_value="raw_value_example",
                    raw_values=[
                        TextDetails(
                            text_positions=[
                                TextPosition()
                            ],
                            raw_value="raw_value_example",
                        )
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
,
                ),
                position_description=Section(),
                position_requirements=Section(),
                additional_information=Section(),
            ),
        ),
        metadata=OptionalMetadata(
            language="it",
        ),
    )
    try:
        # Extract JobTitles from JobAd
        api_response = api_instance.extract_jobtitles_from_jobad_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_jobtitles_from_jobad_post: %s\n" % e)
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
[**JobAdJobDescriptionRequest**](../../models/JobAdJobDescriptionRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional
size | SizeSchema | | optional
min_score | MinScoreSchema | | optional


# SrcLangSchema

Job Description language. If left empty each section's language will detected automatically.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Job Description language. If left empty each section&#x27;s language will detected automatically. | must be one of ["it", "en", "es", "pt", "de", "fr", ] 

# DstLangSchema

Extracted entities destination language. If left empty is assumed to be equal to the Job Description language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Extracted entities destination language. If left empty is assumed to be equal to the Job Description language. | must be one of ["it", "en", "es", "pt", "de", "fr", ] 

# SizeSchema

Number of job titles to be returned, must be greater than <code style='color: #333333; opacity: 0.9'>0</code> and smaller or equal to <code style='color: #333333; opacity: 0.9'>20</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Number of job titles to be returned, must be greater than &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;0&lt;/code&gt; and smaller or equal to &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;20&lt;/code&gt;. | if omitted the server will use the default value of 10

# MinScoreSchema

Minimum score for the proposed job titles. The job titles with a score lower than this value will be neglected.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum score for the proposed job titles. The job titles with a score lower than this value will be neglected. | if omitted the server will use the default value of 0.2

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#extract_jobtitles_from_jobad_post.ApiResponseFor200) | Document Successfully Processed
422 | [ApiResponseFor422](#extract_jobtitles_from_jobad_post.ApiResponseFor422) | Validation Error

#### extract_jobtitles_from_jobad_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobAdJobTitlesResponse**](../../models/JobAdJobTitlesResponse.md) |  | 


#### extract_jobtitles_from_jobad_post.ApiResponseFor422
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

# **extract_languages_from_jobad_post**
<a name="extract_languages_from_jobad_post"></a>
> JobAdLanguagesResponse extract_languages_from_jobad_post(job_ad_job_description_request)

Extract Languages from JobAd

 This method extract job titles that are semantically related with a job advert.  The input is a json containing the structure of the advert, as described in the schema below and in the example on the right.  The field *sections* in the body contains a list of documents, which correspond to distinct sections of the advert (e.g., company description, job description, requirements); in each document, the field *content* contains the text of the section, while the field *weight* (a number between <code style='color: #333333; opacity: 0.9'>0</code> and <code style='color: #333333; opacity: 0.9'>1</code>) can be used to give different weights to the different sections in the skill extraction (e.g., a section with the requirements is probably much more relevant for the skill extraction than a section with the company description); in the absence of the field *value*, the maximum value (i.e., *weight* = <code style='color: #333333; opacity: 0.9'>1</code>) will be assumed.  The field *header* contains the information about the job title. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_knowledge_extraction_api
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

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = JobAdJobDescriptionRequest(
        data=SlimData(
            job_title=JobTitleHeader(
                details=JobTitleHeaderDetails(
                    text_positions=[
                        TextPosition(
                            start=1,
                            end=1,
                        )
                    ],
                    raw_value="raw_value_example",
                    raw_values=[
                        TextDetails(
                            text_positions=[
                                TextPosition()
                            ],
                            raw_value="raw_value_example",
                        )
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
,
                ),
                position_description=Section(),
                position_requirements=Section(),
                additional_information=Section(),
            ),
        ),
        metadata=OptionalMetadata(
            language="it",
        ),
    )
    try:
        # Extract Languages from JobAd
        api_response = api_instance.extract_languages_from_jobad_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_languages_from_jobad_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'src_lang': "it",
        'dst_lang': "it",
        'size': 10,
        'min_score': 0.2,
    }
    body = JobAdJobDescriptionRequest(
        data=SlimData(
            job_title=JobTitleHeader(
                details=JobTitleHeaderDetails(
                    text_positions=[
                        TextPosition(
                            start=1,
                            end=1,
                        )
                    ],
                    raw_value="raw_value_example",
                    raw_values=[
                        TextDetails(
                            text_positions=[
                                TextPosition()
                            ],
                            raw_value="raw_value_example",
                        )
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
,
                ),
                position_description=Section(),
                position_requirements=Section(),
                additional_information=Section(),
            ),
        ),
        metadata=OptionalMetadata(
            language="it",
        ),
    )
    try:
        # Extract Languages from JobAd
        api_response = api_instance.extract_languages_from_jobad_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_languages_from_jobad_post: %s\n" % e)
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
[**JobAdJobDescriptionRequest**](../../models/JobAdJobDescriptionRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional
size | SizeSchema | | optional
min_score | MinScoreSchema | | optional


# SrcLangSchema

Job Description language. If left empty each section's language will detected automatically.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Job Description language. If left empty each section&#x27;s language will detected automatically. | must be one of ["it", "en", "es", "pt", "de", "fr", ] 

# DstLangSchema

Extracted entities destination language. If left empty is assumed to be equal to the Job Description language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Extracted entities destination language. If left empty is assumed to be equal to the Job Description language. | must be one of ["it", "en", "es", "pt", "de", "fr", ] 

# SizeSchema

Number of languages to be returned, must be greater than <code style='color: #333333; opacity: 0.9'>0</code> and smaller or equal to <code style='color: #333333; opacity: 0.9'>20</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Number of languages to be returned, must be greater than &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;0&lt;/code&gt; and smaller or equal to &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;20&lt;/code&gt;. | if omitted the server will use the default value of 10

# MinScoreSchema

Minimum score for the proposed languages. The languages with a score lower than this value will be neglected.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum score for the proposed languages. The languages with a score lower than this value will be neglected. | if omitted the server will use the default value of 0.2

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#extract_languages_from_jobad_post.ApiResponseFor200) | Document Successfully Processed
422 | [ApiResponseFor422](#extract_languages_from_jobad_post.ApiResponseFor422) | Validation Error

#### extract_languages_from_jobad_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobAdLanguagesResponse**](../../models/JobAdLanguagesResponse.md) |  | 


#### extract_languages_from_jobad_post.ApiResponseFor422
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

# **extract_skills_from_jobad_post**
<a name="extract_skills_from_jobad_post"></a>
> JobAdSkillsResponse extract_skills_from_jobad_post(job_ad_job_description_request)

Extract Skills from JobAd

 This method extract job skills (both hard and soft skills) that are semantically related with a job advert.  The input is a json containing the structure of the advert, as described in the schema below and in the example on the right.  The field *sections* in the body contains a list of documents, which correspond to distinct sections of the advert (e.g., company description, job description, requirements); in each document, the field *content* contains the text of the section, while the field *weight* (a number between <code style='color: #333333; opacity: 0.9'>0</code> and <code style='color: #333333; opacity: 0.9'>1</code>) can be used to give different weights to the different sections in the skill extraction (e.g., a section with the requirements is probably much more relevant for the skill extraction than a section with the company description); in the absence of the field *value*, the maximum value (i.e., *weight* = <code style='color: #333333; opacity: 0.9'>1</code>) will be assumed.  The field *header* contains the information about the job title. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_knowledge_extraction_api
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

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = JobAdJobDescriptionRequest(
        data=SlimData(
            job_title=JobTitleHeader(
                details=JobTitleHeaderDetails(
                    text_positions=[
                        TextPosition(
                            start=1,
                            end=1,
                        )
                    ],
                    raw_value="raw_value_example",
                    raw_values=[
                        TextDetails(
                            text_positions=[
                                TextPosition()
                            ],
                            raw_value="raw_value_example",
                        )
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
,
                ),
                position_description=Section(),
                position_requirements=Section(),
                additional_information=Section(),
            ),
        ),
        metadata=OptionalMetadata(
            language="it",
        ),
    )
    try:
        # Extract Skills from JobAd
        api_response = api_instance.extract_skills_from_jobad_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_skills_from_jobad_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'src_lang': "it",
        'dst_lang': "it",
        'size': 10,
        'min_score': 0.2,
    }
    body = JobAdJobDescriptionRequest(
        data=SlimData(
            job_title=JobTitleHeader(
                details=JobTitleHeaderDetails(
                    text_positions=[
                        TextPosition(
                            start=1,
                            end=1,
                        )
                    ],
                    raw_value="raw_value_example",
                    raw_values=[
                        TextDetails(
                            text_positions=[
                                TextPosition()
                            ],
                            raw_value="raw_value_example",
                        )
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
,
                ),
                position_description=Section(),
                position_requirements=Section(),
                additional_information=Section(),
            ),
        ),
        metadata=OptionalMetadata(
            language="it",
        ),
    )
    try:
        # Extract Skills from JobAd
        api_response = api_instance.extract_skills_from_jobad_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdKnowledgeExtractionApi->extract_skills_from_jobad_post: %s\n" % e)
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
[**JobAdJobDescriptionRequest**](../../models/JobAdJobDescriptionRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional
size | SizeSchema | | optional
min_score | MinScoreSchema | | optional


# SrcLangSchema

Job Description language. If left empty each section's language will detected automatically.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Job Description language. If left empty each section&#x27;s language will detected automatically. | must be one of ["it", "en", "es", "pt", "de", "fr", ] 

# DstLangSchema

Extracted entities destination language. If left empty is assumed to be equal to the Job Description language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Extracted entities destination language. If left empty is assumed to be equal to the Job Description language. | must be one of ["it", "en", "es", "pt", "de", "fr", ] 

# SizeSchema

Number of skills to be returned, must be greater than <code style='color: #333333; opacity: 0.9'>0</code> and smaller or equal to <code style='color: #333333; opacity: 0.9'>20</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Number of skills to be returned, must be greater than &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;0&lt;/code&gt; and smaller or equal to &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;20&lt;/code&gt;. | if omitted the server will use the default value of 10

# MinScoreSchema

Minimum score for the proposed skills. The skills with a score lower than this value will be neglected.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum score for the proposed skills. The skills with a score lower than this value will be neglected. | if omitted the server will use the default value of 0.2

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#extract_skills_from_jobad_post.ApiResponseFor200) | Document Successfully Processed
422 | [ApiResponseFor422](#extract_skills_from_jobad_post.ApiResponseFor422) | Validation Error

#### extract_skills_from_jobad_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobAdSkillsResponse**](../../models/JobAdSkillsResponse.md) |  | 


#### extract_skills_from_jobad_post.ApiResponseFor422
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

