<a name="__pageTop"></a>
# inda_hr.apis.tags.job_ad_management_api.JobAdManagementApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_jobad_post**](#add_jobad_post) | **post** /hr/v2/index/{indexname}/jobad/ | Add JobAd
[**delete_jobad_delete**](#delete_jobad_delete) | **delete** /hr/v2/index/{indexname}/jobad/{jobad_id}/ | Delete JobAd
[**get_jobad_get**](#get_jobad_get) | **get** /hr/v2/index/{indexname}/jobad/{jobad_id}/ | Get JobAd
[**get_jobads_get**](#get_jobads_get) | **get** /hr/v2/index/{indexname}/jobads/ | Get JobAds
[**patch_jobad_patch**](#patch_jobad_patch) | **patch** /hr/v2/index/{indexname}/jobad/{jobad_id}/ | Patch JobAd

# **add_jobad_post**
<a name="add_jobad_post"></a>
> JobAdIDResponse add_jobad_post(indexnamejob_ad_request)

Add JobAd

 This method adds a job advertisement to *indexname* and assigns it a *JobAdID* (namely, a Unique Universal ID or UUID4). This method requires an application/json as content type body.  On the right, we provide an example of input structure; further details are available in dedicated sections.  Note that it is mandatory for users to have previously added information about the employer through the  [Add Company](https://api.inda.ai/hr/docs/v2/#operation/add_company__POST) method; the returned *ID* is the required *EmployerID* of job advertisement data. Obviously, one may skip this step if employer company data already exists.  Furthermore, also *Skills* is a required field, since it is necessary to perform the  [Match Resume](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST).  Users may leverage the [Extract Skills from JobAd](https://api.inda.ai/hr/docs/v2/#operation/extract_skills_from_jobad__POST) method and allow INDA to automatically extract skills by analyzing the job advertisement data. It is **highly recommended** to validate the retrieved skills before injecting them to *Add JobAd* requests.  Entities among skills, job titles and languages are automatically mapped by INDAto the adopted knowledge base, so that users can leverage on standardized values.Original values and entity IDs are available in *Details.RawValues* and *Details.Code*, respectively.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.job_ad_id_response import JobAdIDResponse
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.job_ad_request import JobAdRequest
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
    api_instance = job_ad_management_api.JobAdManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    body = JobAdRequest(
        data=JobadCommonData(
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
            employer_id="employer_id_example",
            contact_info=[
                JobadContactInfoContactInfo(
                    person_name=JobadContactInfoPersonName(
                        prefix=JobadContactInfoPrefix(
                            value="value_example",
                        ),
                        given_name=JobadContactInfoName(
                            value="value_example",
                        ),
                        middle_names=[
                            JobadContactInfoName()
                        ],
                        family_name=JobadContactInfoName(),
                        suffix=JobadContactInfoSuffix(
                            value="value_example",
                        ),
                        formatted_name=JobadContactInfoName(),
                    ),
                    phone_numbers=[
                        JobadPhoneNumbersPhoneNumber(
                            number=JobadPhoneNumbersNumber(
                                value=OptionalPhoneNumber(
                                    country_code="AW",
                                    country_dialling="country_dialling_example",
                                    dial_number="dial_number_example",
                                ),
                            ),
                            label=JobadPhoneNumbersPhoneLabel(
                                value="value_example",
                            ),
                        )
                    ],
                    email_addresses=[
                        JobadEmailAddressEmailAddress(
                            address=JobadEmailAddressAddress(
                                value="value_example",
                            ),
                            label=JobadEmailAddressEmailLabel(
                                value="value_example",
                            ),
                        )
                    ],
                    links=[
                        JobadLinkLink(
                            url=JobadLinkURL(
                                value="value_example",
                            ),
                            label=JobadLinkLinkLabel(
                                value="value_example",
                            ),
                        )
                    ],
                )
            ],
            job_locations=[
                BaseLocationsLocation(
                    city=BaseBenefitsValueModelStrictStr(),
                    country=BaseBenefitsValueModelStrictStr(),
                    geo_coordinates=ValueModelGeoLocation(
                        value=GeoLocation(
                            lat=-90.0,
                            lon=-180.0,
                        ),
                    ),
                    country_code=BaseBenefitsValueModelStrictStr(),
                    postal_code=BaseBenefitsValueModelStrictStr(),
                    street_address=BaseBenefitsValueModelStrictStr(),
                    county=BaseBenefitsValueModelStrictStr(),
                    region=BaseBenefitsValueModelStrictStr(),
                )
            ],
            relocation_preferences=RelocationPreferences(
                details=RelocationBoolBaseModel(
                    is_possible=True,
                    is_mandatory=True,
                    is_all_expenses_paid=True,
                ),
                relocation_date=RangeDatetime(
                    range=None,
                ),
            ),
            remote_working=JobAdRemoteWorking(
                type=JobAdRemoteWorkingType(
                    details=BoolBaseModel(
                        is_possible=True,
                        is_mandatory=True,
                    ),
                    value="value_example",
                ),
                frequency=None,
            ),
            experience=Experience(
                duration=OptionalRequiredAndPreferredDurationRange(
                    required=DurationRange(
                        range=None,
                    ),
                    preferred=DurationRange(),
                ),
                seniority=OptionalRequiredAndPreferredSeniorityValue(
                    required=SeniorityValue(
                        value="value_example",
                    ),
,
                ),
            ),
            education=OptionalRequiredAndPreferredEducation(
                required=Education(
                    title=EducationTitle(
                        value="value_example",
                    ),
                    education_level_code=JobadEducationEducationLevelCode(
                        value=EducationLevelCodeValue(
                            eqf=1,
                        ),
                    ),
                    fields=[
                        BaseBenefitsValueModelStrictStr()
                    ],
                ),
                preferred=Education(),
            ),
            skills=None,
            languages=OptionalRequiredAndPreferredConListLanguages(
                required=[
                    OptionalJobAdLanguage(
                        details=OptionalJobAdLanguageDetails(
,
                            raw_value="raw_value_example",
,
                            is_validated=False,
                            entity_type="entity_type_example",
                            proficiency_level="proficiency_level_example",
                            category="category_example",
                            code=JobAdLanguageCode(
                                key="key_example",
                            ),
                            language_code="language_code_example",
                            proficiency_level_code=ProficiencyLevelCode(
                                cefr=CEFRLevels(
                                    overall="A1",
                                    writing="A1",
                                    reading="A1",
                                    speaking="A1",
                                    listening="A1",
                                    spoken_interaction="A1",
                                    spoken_production="A1",
                                ),
                            ),
                        ),
                        value="value_example",
                    )
                ],
                preferred=[
                    OptionalJobAdLanguage()
                ],
            ),
            related_job_titles=[
                OptionalJobAdJobTitle(
                    details=OptionalJobAdJobTitleDetails(
,
                        raw_value="raw_value_example",
,
                        is_validated=False,
                        entity_type="entity_type_example",
                        proficiency_level="proficiency_level_example",
                        category="category_example",
                        code=JobAdJobTitleCode(),
                        weight=0.75,
                    ),
                    value="value_example",
                )
            ],
            employment=JobTitleEmployment(
                code=BaseBenefitsValueModelStrictStr(),
                category=BaseBenefitsValueModelStrictStr(),
                type=EmploymentType(
                    value="value_example",
                ),
                industries=[
                    BaseEmploymentsIndustry(
                        value="value_example",
                    )
                ],
                functional_areas=[
                    BaseBenefitsValueModelStrictStr()
                ],
                activities=[
                    Activity(
                        value="value_example",
                        tags=[
                            "tags_example"
                        ],
                    )
                ],
            ),
            contract=JobAdContract(
                type=ContractType(
                    value="value_example",
                ),
                duration=ValueModelInt(
                    value=1,
                ),
                start_date=ValueModelDatetime(
                    value="1970-01-01T00:00:00.00Z",
                ),
,
            ),
            publisher=Publisher(
                name=BaseBenefitsValueModelStrictStr(),
                category=BaseBenefitsValueModelStrictStr(),
                link=JobadLinkLink(),
            ),
            job_shift=JobShift(
                details=BoolBaseModel(),
                type=JobShiftType(
                    value="DAY_SHIFT",
                ),
                frequency=None,
            ),
            number_of_openings=ValueModelInt(),
            link=JobadLinkLink(),
            advertisement_sites=[
                JobadLinkLink()
            ],
            salary=JobAdSalary(
                amount=RangeFloat(
                    range=None,
                ),
                currency=Currency(
                    value="value_example",
                ),
                frequency=Frequency(
                    value="YEARLY",
                ),
                type=BaseSalariesType(
                    value="GROSS",
                ),
            ),
            benefits=[
                JobAdBenefit(
                    value="value_example",
                )
            ],
            expiration_date=ValueModelDatetime(),
            status=JobadCommonValueModelStr(
                value="value_example",
            ),
        ),
        metadata=RequestMetadata(
            language="pt",
        ),
    )
    try:
        # Add JobAd
        api_response = api_instance.add_jobad_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->add_jobad_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'src_lang': "pt",
        'dst_lang': "pt",
        'jobad_id': "jobad_id_example",
    }
    body = JobAdRequest(
        data=JobadCommonData(
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
            employer_id="employer_id_example",
            contact_info=[
                JobadContactInfoContactInfo(
                    person_name=JobadContactInfoPersonName(
                        prefix=JobadContactInfoPrefix(
                            value="value_example",
                        ),
                        given_name=JobadContactInfoName(
                            value="value_example",
                        ),
                        middle_names=[
                            JobadContactInfoName()
                        ],
                        family_name=JobadContactInfoName(),
                        suffix=JobadContactInfoSuffix(
                            value="value_example",
                        ),
                        formatted_name=JobadContactInfoName(),
                    ),
                    phone_numbers=[
                        JobadPhoneNumbersPhoneNumber(
                            number=JobadPhoneNumbersNumber(
                                value=OptionalPhoneNumber(
                                    country_code="AW",
                                    country_dialling="country_dialling_example",
                                    dial_number="dial_number_example",
                                ),
                            ),
                            label=JobadPhoneNumbersPhoneLabel(
                                value="value_example",
                            ),
                        )
                    ],
                    email_addresses=[
                        JobadEmailAddressEmailAddress(
                            address=JobadEmailAddressAddress(
                                value="value_example",
                            ),
                            label=JobadEmailAddressEmailLabel(
                                value="value_example",
                            ),
                        )
                    ],
                    links=[
                        JobadLinkLink(
                            url=JobadLinkURL(
                                value="value_example",
                            ),
                            label=JobadLinkLinkLabel(
                                value="value_example",
                            ),
                        )
                    ],
                )
            ],
            job_locations=[
                BaseLocationsLocation(
                    city=BaseBenefitsValueModelStrictStr(),
                    country=BaseBenefitsValueModelStrictStr(),
                    geo_coordinates=ValueModelGeoLocation(
                        value=GeoLocation(
                            lat=-90.0,
                            lon=-180.0,
                        ),
                    ),
                    country_code=BaseBenefitsValueModelStrictStr(),
                    postal_code=BaseBenefitsValueModelStrictStr(),
                    street_address=BaseBenefitsValueModelStrictStr(),
                    county=BaseBenefitsValueModelStrictStr(),
                    region=BaseBenefitsValueModelStrictStr(),
                )
            ],
            relocation_preferences=RelocationPreferences(
                details=RelocationBoolBaseModel(
                    is_possible=True,
                    is_mandatory=True,
                    is_all_expenses_paid=True,
                ),
                relocation_date=RangeDatetime(
                    range=None,
                ),
            ),
            remote_working=JobAdRemoteWorking(
                type=JobAdRemoteWorkingType(
                    details=BoolBaseModel(
                        is_possible=True,
                        is_mandatory=True,
                    ),
                    value="value_example",
                ),
                frequency=None,
            ),
            experience=Experience(
                duration=OptionalRequiredAndPreferredDurationRange(
                    required=DurationRange(
                        range=None,
                    ),
                    preferred=DurationRange(),
                ),
                seniority=OptionalRequiredAndPreferredSeniorityValue(
                    required=SeniorityValue(
                        value="value_example",
                    ),
,
                ),
            ),
            education=OptionalRequiredAndPreferredEducation(
                required=Education(
                    title=EducationTitle(
                        value="value_example",
                    ),
                    education_level_code=JobadEducationEducationLevelCode(
                        value=EducationLevelCodeValue(
                            eqf=1,
                        ),
                    ),
                    fields=[
                        BaseBenefitsValueModelStrictStr()
                    ],
                ),
                preferred=Education(),
            ),
            skills=None,
            languages=OptionalRequiredAndPreferredConListLanguages(
                required=[
                    OptionalJobAdLanguage(
                        details=OptionalJobAdLanguageDetails(
,
                            raw_value="raw_value_example",
,
                            is_validated=False,
                            entity_type="entity_type_example",
                            proficiency_level="proficiency_level_example",
                            category="category_example",
                            code=JobAdLanguageCode(
                                key="key_example",
                            ),
                            language_code="language_code_example",
                            proficiency_level_code=ProficiencyLevelCode(
                                cefr=CEFRLevels(
                                    overall="A1",
                                    writing="A1",
                                    reading="A1",
                                    speaking="A1",
                                    listening="A1",
                                    spoken_interaction="A1",
                                    spoken_production="A1",
                                ),
                            ),
                        ),
                        value="value_example",
                    )
                ],
                preferred=[
                    OptionalJobAdLanguage()
                ],
            ),
            related_job_titles=[
                OptionalJobAdJobTitle(
                    details=OptionalJobAdJobTitleDetails(
,
                        raw_value="raw_value_example",
,
                        is_validated=False,
                        entity_type="entity_type_example",
                        proficiency_level="proficiency_level_example",
                        category="category_example",
                        code=JobAdJobTitleCode(),
                        weight=0.75,
                    ),
                    value="value_example",
                )
            ],
            employment=JobTitleEmployment(
                code=BaseBenefitsValueModelStrictStr(),
                category=BaseBenefitsValueModelStrictStr(),
                type=EmploymentType(
                    value="value_example",
                ),
                industries=[
                    BaseEmploymentsIndustry(
                        value="value_example",
                    )
                ],
                functional_areas=[
                    BaseBenefitsValueModelStrictStr()
                ],
                activities=[
                    Activity(
                        value="value_example",
                        tags=[
                            "tags_example"
                        ],
                    )
                ],
            ),
            contract=JobAdContract(
                type=ContractType(
                    value="value_example",
                ),
                duration=ValueModelInt(
                    value=1,
                ),
                start_date=ValueModelDatetime(
                    value="1970-01-01T00:00:00.00Z",
                ),
,
            ),
            publisher=Publisher(
                name=BaseBenefitsValueModelStrictStr(),
                category=BaseBenefitsValueModelStrictStr(),
                link=JobadLinkLink(),
            ),
            job_shift=JobShift(
                details=BoolBaseModel(),
                type=JobShiftType(
                    value="DAY_SHIFT",
                ),
                frequency=None,
            ),
            number_of_openings=ValueModelInt(),
            link=JobadLinkLink(),
            advertisement_sites=[
                JobadLinkLink()
            ],
            salary=JobAdSalary(
                amount=RangeFloat(
                    range=None,
                ),
                currency=Currency(
                    value="value_example",
                ),
                frequency=Frequency(
                    value="YEARLY",
                ),
                type=BaseSalariesType(
                    value="GROSS",
                ),
            ),
            benefits=[
                JobAdBenefit(
                    value="value_example",
                )
            ],
            expiration_date=ValueModelDatetime(),
            status=JobadCommonValueModelStr(
                value="value_example",
            ),
        ),
        metadata=RequestMetadata(
            language="pt",
        ),
    )
    try:
        # Add JobAd
        api_response = api_instance.add_jobad_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->add_jobad_post: %s\n" % e)
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
[**JobAdRequest**](../../models/JobAdRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional
jobad_id | JobadIdSchema | | optional


# SrcLangSchema

Job Description language. If left empty each section's language will detected automatically.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Job Description language. If left empty each section&#x27;s language will detected automatically. | must be one of ["pt", "it", "en", "de", "fr", "es", ] 

# DstLangSchema

Extracted entities destination language. If left empty is assumed to be equal to the Job Description language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Extracted entities destination language. If left empty is assumed to be equal to the Job Description language. | must be one of ["pt", "it", "en", "de", "fr", "es", ] 

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#add_jobad_post.ApiResponseFor201) | JobAd Successfully Added
400 | [ApiResponseFor400](#add_jobad_post.ApiResponseFor400) | Bad Request
409 | [ApiResponseFor409](#add_jobad_post.ApiResponseFor409) | Conflict
404 | [ApiResponseFor404](#add_jobad_post.ApiResponseFor404) | Not Found
200 | [ApiResponseFor200](#add_jobad_post.ApiResponseFor200) | JobAd Already Present
422 | [ApiResponseFor422](#add_jobad_post.ApiResponseFor422) | Validation Error

#### add_jobad_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobAdIDResponse**](../../models/JobAdIDResponse.md) |  | 


#### add_jobad_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### add_jobad_post.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### add_jobad_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### add_jobad_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**JobAdIDResponse**](../../models/JobAdIDResponse.md) |  | 


#### add_jobad_post.ApiResponseFor422
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

# **delete_jobad_delete**
<a name="delete_jobad_delete"></a>
> DeleteJobAdResponse delete_jobad_delete(indexnamejobad_id)

Delete JobAd

 This method removes the job advertisement associated with *jobad_id* from the index *indexname*.  Note that when a job advertisement is deleted, the same happens to all its related applications.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.delete_job_ad_response import DeleteJobAdResponse
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
    api_instance = job_ad_management_api.JobAdManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': "jobad_id_example",
    }
    try:
        # Delete JobAd
        api_response = api_instance.delete_jobad_delete(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->delete_jobad_delete: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 
jobad_id | JobadIdSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_jobad_delete.ApiResponseFor200) | JobAd Successfully Deleted.
404 | [ApiResponseFor404](#delete_jobad_delete.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#delete_jobad_delete.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#delete_jobad_delete.ApiResponseFor422) | Validation Error

#### delete_jobad_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteJobAdResponse**](../../models/DeleteJobAdResponse.md) |  | 


#### delete_jobad_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### delete_jobad_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### delete_jobad_delete.ApiResponseFor422
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

# **get_jobad_get**
<a name="get_jobad_get"></a>
> GetJobAdResponse get_jobad_get(indexnamejobad_id)

Get JobAd

 This method returns the information related to the job advertisement stored with id *jobad_id* in the index *indexname*.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.get_job_ad_response import GetJobAdResponse
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
    api_instance = job_ad_management_api.JobAdManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': "jobad_id_example",
    }
    try:
        # Get JobAd
        api_response = api_instance.get_jobad_get(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->get_jobad_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 
jobad_id | JobadIdSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_jobad_get.ApiResponseFor200) | JobAd Successfully Retrieved
404 | [ApiResponseFor404](#get_jobad_get.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#get_jobad_get.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#get_jobad_get.ApiResponseFor422) | Validation Error

#### get_jobad_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetJobAdResponse**](../../models/GetJobAdResponse.md) |  | 


#### get_jobad_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_jobad_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_jobad_get.ApiResponseFor422
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

# **get_jobads_get**
<a name="get_jobads_get"></a>
> GetJobAdsResponse get_jobads_get(indexname)

Get JobAds

 This method returns a list of UUID4 associated to the job advertisements stored in the index *indexname*.  Query parameters are used to specify the *offset* and *size* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored; in order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  The use of caching is highly recommended to improve the performances.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.get_job_ads_response import GetJobAdsResponse
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
    api_instance = job_ad_management_api.JobAdManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    try:
        # Get JobAds
        api_response = api_instance.get_jobads_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->get_jobads_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'cache': True,
        'cache_time': 300,
        'offset': 0,
        'search_id': "search_id_example",
        'size': 50,
    }
    try:
        # Get JobAds
        api_response = api_instance.get_jobads_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->get_jobads_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
cache | CacheSchema | | optional
cache_time | CacheTimeSchema | | optional
offset | OffsetSchema | | optional
search_id | SearchIdSchema | | optional
size | SizeSchema | | optional


# CacheSchema

Optional. Whether the search results should be cached or not.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Optional. Whether the search results should be cached or not. | if omitted the server will use the default value of True

# CacheTimeSchema

Optional. Seconds.Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>false</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Seconds.Ignored if *cache* is &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;false&lt;/code&gt;. | if omitted the server will use the default value of 300

# OffsetSchema

Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to skip. Ignored if *cache* is &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;true&lt;/code&gt;. | if omitted the server will use the default value of 0

# SearchIdSchema

Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. Other query parameters are uselesswhen *SearchID* is used.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. Other query parameters are uselesswhen *SearchID* is used. | 

# SizeSchema

Optional. Number of documents to return.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to return. | if omitted the server will use the default value of 50

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_jobads_get.ApiResponseFor200) | JobAds Successfully Retrieved
404 | [ApiResponseFor404](#get_jobads_get.ApiResponseFor404) | Not Found
415 | [ApiResponseFor415](#get_jobads_get.ApiResponseFor415) | Unsupported Media Type
422 | [ApiResponseFor422](#get_jobads_get.ApiResponseFor422) | Validation Error

#### get_jobads_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetJobAdsResponse**](../../models/GetJobAdsResponse.md) |  | 


#### get_jobads_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_jobads_get.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_jobads_get.ApiResponseFor422
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

# **patch_jobad_patch**
<a name="patch_jobad_patch"></a>
> PatchJobAdResponse patch_jobad_patch(indexnamejobad_idpatch_job_ad_request)

Patch JobAd

 This method updates the information related to the job advertisement stored with id *job_ad_id*.  This method accepts an application/json body with the same structure as [Add JobAd](https://api.inda.ai/hr/docs/v2/#operation/add_jobad__POST), however in this case all fields are optional.  Fields that contain differences between the corresponding original ones are substituted, while new fields are added. Bear in mind that lists are considered as singular value, therefore to modify an entry in a list it is necessary to insert the full list.  Entities among skills, job titles and languages are automatically mapped by INDAto the adopted knowledge base, so that users can leverage on standardized values.Original values and entity IDs are available in *Details.RawValues* and *Details.Code*, respectively.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.patch_job_ad_response import PatchJobAdResponse
from inda_hr.model.patch_job_ad_request import PatchJobAdRequest
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
    api_instance = job_ad_management_api.JobAdManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': "jobad_id_example",
    }
    query_params = {
    }
    body = PatchJobAdRequest(
        data=JobadCommonOptionalData(
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
            employer_id="employer_id_example",
            contact_info=[
                JobadContactInfoContactInfo(
                    person_name=JobadContactInfoPersonName(
                        prefix=JobadContactInfoPrefix(
                            value="value_example",
                        ),
                        given_name=JobadContactInfoName(
                            value="value_example",
                        ),
                        middle_names=[
                            JobadContactInfoName()
                        ],
                        family_name=JobadContactInfoName(),
                        suffix=JobadContactInfoSuffix(
                            value="value_example",
                        ),
                        formatted_name=JobadContactInfoName(),
                    ),
                    phone_numbers=[
                        JobadPhoneNumbersPhoneNumber(
                            number=JobadPhoneNumbersNumber(
                                value=OptionalPhoneNumber(
                                    country_code="AW",
                                    country_dialling="country_dialling_example",
                                    dial_number="dial_number_example",
                                ),
                            ),
                            label=JobadPhoneNumbersPhoneLabel(
                                value="value_example",
                            ),
                        )
                    ],
                    email_addresses=[
                        JobadEmailAddressEmailAddress(
                            address=JobadEmailAddressAddress(
                                value="value_example",
                            ),
                            label=JobadEmailAddressEmailLabel(
                                value="value_example",
                            ),
                        )
                    ],
                    links=[
                        JobadLinkLink(
                            url=JobadLinkURL(
                                value="value_example",
                            ),
                            label=JobadLinkLinkLabel(
                                value="value_example",
                            ),
                        )
                    ],
                )
            ],
            job_locations=[
                BaseLocationsLocation(
                    city=BaseBenefitsValueModelStrictStr(),
                    country=BaseBenefitsValueModelStrictStr(),
                    geo_coordinates=ValueModelGeoLocation(
                        value=GeoLocation(
                            lat=-90.0,
                            lon=-180.0,
                        ),
                    ),
                    country_code=BaseBenefitsValueModelStrictStr(),
                    postal_code=BaseBenefitsValueModelStrictStr(),
                    street_address=BaseBenefitsValueModelStrictStr(),
                    county=BaseBenefitsValueModelStrictStr(),
                    region=BaseBenefitsValueModelStrictStr(),
                )
            ],
            relocation_preferences=RelocationPreferences(
                details=RelocationBoolBaseModel(
                    is_possible=True,
                    is_mandatory=True,
                    is_all_expenses_paid=True,
                ),
                relocation_date=RangeDatetime(
                    range=None,
                ),
            ),
            remote_working=JobAdRemoteWorking(
                type=JobAdRemoteWorkingType(
                    details=BoolBaseModel(
                        is_possible=True,
                        is_mandatory=True,
                    ),
                    value="value_example",
                ),
                frequency=None,
            ),
            experience=Experience(
                duration=OptionalRequiredAndPreferredDurationRange(
                    required=DurationRange(
                        range=None,
                    ),
                    preferred=DurationRange(),
                ),
                seniority=OptionalRequiredAndPreferredSeniorityValue(
                    required=SeniorityValue(
                        value="value_example",
                    ),
,
                ),
            ),
            education=OptionalRequiredAndPreferredEducation(
                required=Education(
                    title=EducationTitle(
                        value="value_example",
                    ),
                    education_level_code=JobadEducationEducationLevelCode(
                        value=EducationLevelCodeValue(
                            eqf=1,
                        ),
                    ),
                    fields=[
                        BaseBenefitsValueModelStrictStr()
                    ],
                ),
                preferred=Education(),
            ),
            skills=None,
            languages=OptionalRequiredAndPreferredConListLanguages(
                required=[
                    OptionalJobAdLanguage(
                        details=OptionalJobAdLanguageDetails(
,
                            raw_value="raw_value_example",
,
                            is_validated=False,
                            entity_type="entity_type_example",
                            proficiency_level="proficiency_level_example",
                            category="category_example",
                            code=JobAdLanguageCode(
                                key="key_example",
                            ),
                            language_code="language_code_example",
                            proficiency_level_code=ProficiencyLevelCode(
                                cefr=CEFRLevels(
                                    overall="A1",
                                    writing="A1",
                                    reading="A1",
                                    speaking="A1",
                                    listening="A1",
                                    spoken_interaction="A1",
                                    spoken_production="A1",
                                ),
                            ),
                        ),
                        value="value_example",
                    )
                ],
                preferred=[
                    OptionalJobAdLanguage()
                ],
            ),
            related_job_titles=[
                OptionalJobAdJobTitle(
                    details=OptionalJobAdJobTitleDetails(
,
                        raw_value="raw_value_example",
,
                        is_validated=False,
                        entity_type="entity_type_example",
                        proficiency_level="proficiency_level_example",
                        category="category_example",
                        code=JobAdJobTitleCode(),
                        weight=0.75,
                    ),
                    value="value_example",
                )
            ],
            employment=JobTitleEmployment(
                code=BaseBenefitsValueModelStrictStr(),
                category=BaseBenefitsValueModelStrictStr(),
                type=EmploymentType(
                    value="value_example",
                ),
                industries=[
                    BaseEmploymentsIndustry(
                        value="value_example",
                    )
                ],
                functional_areas=[
                    BaseBenefitsValueModelStrictStr()
                ],
                activities=[
                    Activity(
                        value="value_example",
                        tags=[
                            "tags_example"
                        ],
                    )
                ],
            ),
            contract=JobAdContract(
                type=ContractType(
                    value="value_example",
                ),
                duration=ValueModelInt(
                    value=1,
                ),
                start_date=ValueModelDatetime(
                    value="1970-01-01T00:00:00.00Z",
                ),
,
            ),
            publisher=Publisher(
                name=BaseBenefitsValueModelStrictStr(),
                category=BaseBenefitsValueModelStrictStr(),
                link=JobadLinkLink(),
            ),
            job_shift=JobShift(
                details=BoolBaseModel(),
                type=JobShiftType(
                    value="DAY_SHIFT",
                ),
                frequency=None,
            ),
            number_of_openings=ValueModelInt(),
            link=JobadLinkLink(),
            advertisement_sites=[
                JobadLinkLink()
            ],
            salary=JobAdSalary(
                amount=RangeFloat(
                    range=None,
                ),
                currency=Currency(
                    value="value_example",
                ),
                frequency=Frequency(
                    value="YEARLY",
                ),
                type=BaseSalariesType(
                    value="GROSS",
                ),
            ),
            benefits=[
                JobAdBenefit(
                    value="value_example",
                )
            ],
            expiration_date=ValueModelDatetime(),
            status=JobadCommonValueModelStr(
                value="value_example",
            ),
        ),
        metadata=RequestMetadata(
            language="pt",
        ),
    )
    try:
        # Patch JobAd
        api_response = api_instance.patch_jobad_patch(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->patch_jobad_patch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': "jobad_id_example",
    }
    query_params = {
        'src_lang': "pt",
    }
    body = PatchJobAdRequest(
        data=JobadCommonOptionalData(
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
            employer_id="employer_id_example",
            contact_info=[
                JobadContactInfoContactInfo(
                    person_name=JobadContactInfoPersonName(
                        prefix=JobadContactInfoPrefix(
                            value="value_example",
                        ),
                        given_name=JobadContactInfoName(
                            value="value_example",
                        ),
                        middle_names=[
                            JobadContactInfoName()
                        ],
                        family_name=JobadContactInfoName(),
                        suffix=JobadContactInfoSuffix(
                            value="value_example",
                        ),
                        formatted_name=JobadContactInfoName(),
                    ),
                    phone_numbers=[
                        JobadPhoneNumbersPhoneNumber(
                            number=JobadPhoneNumbersNumber(
                                value=OptionalPhoneNumber(
                                    country_code="AW",
                                    country_dialling="country_dialling_example",
                                    dial_number="dial_number_example",
                                ),
                            ),
                            label=JobadPhoneNumbersPhoneLabel(
                                value="value_example",
                            ),
                        )
                    ],
                    email_addresses=[
                        JobadEmailAddressEmailAddress(
                            address=JobadEmailAddressAddress(
                                value="value_example",
                            ),
                            label=JobadEmailAddressEmailLabel(
                                value="value_example",
                            ),
                        )
                    ],
                    links=[
                        JobadLinkLink(
                            url=JobadLinkURL(
                                value="value_example",
                            ),
                            label=JobadLinkLinkLabel(
                                value="value_example",
                            ),
                        )
                    ],
                )
            ],
            job_locations=[
                BaseLocationsLocation(
                    city=BaseBenefitsValueModelStrictStr(),
                    country=BaseBenefitsValueModelStrictStr(),
                    geo_coordinates=ValueModelGeoLocation(
                        value=GeoLocation(
                            lat=-90.0,
                            lon=-180.0,
                        ),
                    ),
                    country_code=BaseBenefitsValueModelStrictStr(),
                    postal_code=BaseBenefitsValueModelStrictStr(),
                    street_address=BaseBenefitsValueModelStrictStr(),
                    county=BaseBenefitsValueModelStrictStr(),
                    region=BaseBenefitsValueModelStrictStr(),
                )
            ],
            relocation_preferences=RelocationPreferences(
                details=RelocationBoolBaseModel(
                    is_possible=True,
                    is_mandatory=True,
                    is_all_expenses_paid=True,
                ),
                relocation_date=RangeDatetime(
                    range=None,
                ),
            ),
            remote_working=JobAdRemoteWorking(
                type=JobAdRemoteWorkingType(
                    details=BoolBaseModel(
                        is_possible=True,
                        is_mandatory=True,
                    ),
                    value="value_example",
                ),
                frequency=None,
            ),
            experience=Experience(
                duration=OptionalRequiredAndPreferredDurationRange(
                    required=DurationRange(
                        range=None,
                    ),
                    preferred=DurationRange(),
                ),
                seniority=OptionalRequiredAndPreferredSeniorityValue(
                    required=SeniorityValue(
                        value="value_example",
                    ),
,
                ),
            ),
            education=OptionalRequiredAndPreferredEducation(
                required=Education(
                    title=EducationTitle(
                        value="value_example",
                    ),
                    education_level_code=JobadEducationEducationLevelCode(
                        value=EducationLevelCodeValue(
                            eqf=1,
                        ),
                    ),
                    fields=[
                        BaseBenefitsValueModelStrictStr()
                    ],
                ),
                preferred=Education(),
            ),
            skills=None,
            languages=OptionalRequiredAndPreferredConListLanguages(
                required=[
                    OptionalJobAdLanguage(
                        details=OptionalJobAdLanguageDetails(
,
                            raw_value="raw_value_example",
,
                            is_validated=False,
                            entity_type="entity_type_example",
                            proficiency_level="proficiency_level_example",
                            category="category_example",
                            code=JobAdLanguageCode(
                                key="key_example",
                            ),
                            language_code="language_code_example",
                            proficiency_level_code=ProficiencyLevelCode(
                                cefr=CEFRLevels(
                                    overall="A1",
                                    writing="A1",
                                    reading="A1",
                                    speaking="A1",
                                    listening="A1",
                                    spoken_interaction="A1",
                                    spoken_production="A1",
                                ),
                            ),
                        ),
                        value="value_example",
                    )
                ],
                preferred=[
                    OptionalJobAdLanguage()
                ],
            ),
            related_job_titles=[
                OptionalJobAdJobTitle(
                    details=OptionalJobAdJobTitleDetails(
,
                        raw_value="raw_value_example",
,
                        is_validated=False,
                        entity_type="entity_type_example",
                        proficiency_level="proficiency_level_example",
                        category="category_example",
                        code=JobAdJobTitleCode(),
                        weight=0.75,
                    ),
                    value="value_example",
                )
            ],
            employment=JobTitleEmployment(
                code=BaseBenefitsValueModelStrictStr(),
                category=BaseBenefitsValueModelStrictStr(),
                type=EmploymentType(
                    value="value_example",
                ),
                industries=[
                    BaseEmploymentsIndustry(
                        value="value_example",
                    )
                ],
                functional_areas=[
                    BaseBenefitsValueModelStrictStr()
                ],
                activities=[
                    Activity(
                        value="value_example",
                        tags=[
                            "tags_example"
                        ],
                    )
                ],
            ),
            contract=JobAdContract(
                type=ContractType(
                    value="value_example",
                ),
                duration=ValueModelInt(
                    value=1,
                ),
                start_date=ValueModelDatetime(
                    value="1970-01-01T00:00:00.00Z",
                ),
,
            ),
            publisher=Publisher(
                name=BaseBenefitsValueModelStrictStr(),
                category=BaseBenefitsValueModelStrictStr(),
                link=JobadLinkLink(),
            ),
            job_shift=JobShift(
                details=BoolBaseModel(),
                type=JobShiftType(
                    value="DAY_SHIFT",
                ),
                frequency=None,
            ),
            number_of_openings=ValueModelInt(),
            link=JobadLinkLink(),
            advertisement_sites=[
                JobadLinkLink()
            ],
            salary=JobAdSalary(
                amount=RangeFloat(
                    range=None,
                ),
                currency=Currency(
                    value="value_example",
                ),
                frequency=Frequency(
                    value="YEARLY",
                ),
                type=BaseSalariesType(
                    value="GROSS",
                ),
            ),
            benefits=[
                JobAdBenefit(
                    value="value_example",
                )
            ],
            expiration_date=ValueModelDatetime(),
            status=JobadCommonValueModelStr(
                value="value_example",
            ),
        ),
        metadata=RequestMetadata(
            language="pt",
        ),
    )
    try:
        # Patch JobAd
        api_response = api_instance.patch_jobad_patch(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->patch_jobad_patch: %s\n" % e)
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
[**PatchJobAdRequest**](../../models/PatchJobAdRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional


# SrcLangSchema

Job Description language. If left empty each section's language will detected automatically.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Job Description language. If left empty each section&#x27;s language will detected automatically. | must be one of ["pt", "it", "en", "de", "fr", "es", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 
jobad_id | JobadIdSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#patch_jobad_patch.ApiResponseFor200) | JobAd Successfully Updated
404 | [ApiResponseFor404](#patch_jobad_patch.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#patch_jobad_patch.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#patch_jobad_patch.ApiResponseFor422) | Validation Error

#### patch_jobad_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchJobAdResponse**](../../models/PatchJobAdResponse.md) |  | 


#### patch_jobad_patch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### patch_jobad_patch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### patch_jobad_patch.ApiResponseFor422
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

