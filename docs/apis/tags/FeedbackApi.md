<a name="__pageTop"></a>
# inda_hr.apis.tags.feedback_api.FeedbackApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**info_extraction_feedback_post**](#info_extraction_feedback_post) | **post** /hr/v2/feedback/index/{indexname}/resume/{resume_id}/parse/data/ | Info Extraction Feedback
[**semantic_search_feedback_post**](#semantic_search_feedback_post) | **post** /hr/v2/feedback/index/{indexname}/resume/{resume_id}/search/semantic/ | Semantic Search Feedback

# **info_extraction_feedback_post**
<a name="info_extraction_feedback_post"></a>
> FeedbackResponse info_extraction_feedback_post(indexnameresume_idfeedback_info_item)

Info Extraction Feedback

 This method collects the feedback for the Information Extraction ([Parse Resume](https://api.inda.ai/hr/docs/v2/#operation/parse_resume__POST) method) on the document associated to *resume_id* on the index *indexname*.  Note that *resume_id* is generally the ID returned by the [Add Resume](https://api.inda.ai/hr/docs/v2/#operation/add_resume__POST) method. However, if the user does not make use of resume/index management services, he can still use the information extraction feedback simply by generating a *resume_id* (UUID4 format).  The method requires an application/json as content type body. This json is an object which contains two elements: + The first element *ParseResumeOutput* is the json provided by [Parse Resume](https://api.inda.ai/hr/docs/v2/#operation/parse_resume__POST) method + The second element *OutputCorrected* is a json with structure and content corresponding to the desired output for the Information Extraction.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import feedback_api
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.feedback_info_item import FeedbackInfoItem
from inda_hr.model.feedback_response import FeedbackResponse
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
    api_instance = feedback_api.FeedbackApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    body = FeedbackInfoItem(
        parse_resume_output=FeedbackExtractionItem(
            data=ResumeCommonData(
                job_title=OptionalResumeJobTitle(
                    details=OptionalResumeJobTitleDetails(
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
                        score=0.75,
                        code=ResumeJobTitleCode(
                            key="key_example",
                        ),
                    ),
                    value="value_example",
                ),
                personal_info=PersonalInfo(
                    person_name=ResumePersonNamePersonName(
                        prefix=ResumePersonNamePrefix(
                            details=BaseDetails(
,
                                raw_value="raw_value_example",
,
                                is_validated=False,
                                entity_type="entity_type_example",
                            ),
                            value="value_example",
                        ),
                        given_name=BaseModelsName(
                            details=BaseDetails(),
                            value="value_example",
                        ),
                        middle_names=[
                            BaseModelsName()
                        ],
                        family_name=BaseModelsName(),
                        suffix=ResumePersonNameSuffix(
                            details=BaseDetails(),
                            value="value_example",
                        ),
                        formatted_name=BaseModelsName(),
                    ),
                    birthdate=Date(
                        details=BaseDetails(),
                        value="1970-01-01",
                    ),
                    age=Age(
                        details=BaseDetails(),
                        value=1,
                    ),
                    nationalities=[
                        Nationality(
                            details=BaseDetails(),
                            value="value_example",
                        )
                    ],
                    citizenships=[
                        Citizenship(
                            details=BaseDetails(),
                            value="value_example",
                        )
                    ],
                    gender=Gender(
                        details=BaseDetails(),
                        value="value_example",
                    ),
                    disability=Disability(
                        disability_level_code=DisabilityLevelCode(
                            details=BaseDetails(),
                            value="value_example",
                        ),
                        disability_summary=Description(
                            details=BaseDetails(),
                            value="value_example",
                        ),
                    ),
                    protected_groups=[
                        ProtectedGroup(
                            details=BaseDetails(),
                            value="value_example",
                        )
                    ],
                    marital_status=MaritalStatus(
                        details=BaseDetails(),
                        value="value_example",
                    ),
                    number_of_children=NumberOfChildren(
                        details=BaseDetails(),
                        value=1,
                    ),
                ),
                contact_info=ResumeContactInfoContactInfo(
                    phone_numbers=[
                        ResumePhoneNumbersPhoneNumber(
                            number=ResumePhoneNumbersNumber(
                                details=BaseDetails(),
                                value=OptionalPhoneNumber(
                                    country_code="AW",
                                    country_dialling="country_dialling_example",
                                    dial_number="dial_number_example",
                                ),
                            ),
                            label=ResumePhoneNumbersPhoneLabel(
                                details=BaseDetails(),
                                value="value_example",
                            ),
                        )
                    ],
                    email_addresses=[
                        ResumeEmailAddressEmailAddress(
                            address=ResumeEmailAddressAddress(
                                details=BaseDetails(),
                                value="value_example",
                            ),
                            label=ResumeEmailAddressEmailLabel(
                                details=BaseDetails(),
                                value="value_example",
                            ),
                        )
                    ],
                    links=[
                        ResumeLinkLink(
                            url=ResumeLinkURL(
                                details=BaseDetails(),
                                value="value_example",
                            ),
                            label=ResumeLinkLinkLabel(
                                details=BaseDetails(),
                                value="value_example",
                            ),
                        )
                    ],
                ),
                person_location=PersonLocation(
                    current_location=ResumeLocationsLocation(
                        city=BaseModelsName(),
                        country=BaseModelsName(),
                        geo_coordinates=GeoCoordinates(
                            details=SlimBaseDetails(
                                is_validated=False,
                            ),
                            value=GeoLocation(
                                lat=-90.0,
                                lon=-180.0,
                            ),
                        ),
                        country_code=Text(
                            details=BaseDetails(),
                            value="value_example",
                        ),
,
,
                        county=BaseModelsName(),
                        region=BaseModelsName(),
                    ),
                    permanent_location=ResumeLocationsLocation(),
                ),
,
                education_experiences=[
                    EducationExperience(
                        duration=BaseDuration(
                            details=SlimBaseDetails(),
                            value=1,
                        ),
                        education_title=Text(),
                        field_of_study=Text(),
                        final_grade=FinalGrade(
                            details=BaseDetails(),
                            value=FinalGradeValue(
                                score_text="score_text_example",
                                score_numeric=1,
                            ),
                        ),
                        education_level_code=ResumeEducationExperiencesEducationLevelCode(
                            details=SlimBaseDetails(),
                            value=EducationLevelCodeValue(
                                eqf=1,
                            ),
                        ),
                        description=Description(),
                        start_date=Date(),
                        end_date=Date(),
                        ongoing=Ongoing(
                            details=SlimBaseDetails(),
                            value=True,
                        ),
                        location=ResumeLocationsLocation(),
                        organization=Organization(
                            organization_name=BaseModelsName(),
                            department=Text(),
                            location=ResumeLocationsLocation(),
                            link=ResumeLinkLink(),
                            id=ID(
                                details=OptionalEntityBaseDetails(
                                    is_validated=False,
                                    entity_type="entity_type_example",
                                ),
                                value="value_example",
                            ),
                        ),
                        courses=[
                            Text()
                        ],
                        id="id_example",
                    )
                ],
                work_experiences=[
                    WorkExperience(
                        seniority=BaseSeniority(
                            details=BaseDetails(),
                            value="value_example",
                        ),
                        duration=BaseDuration(),
                        position_title=OptionalResumeJobTitle(),
                        description=Description(),
                        start_date=Date(),
                        end_date=Date(),
                        ongoing=Ongoing(),
                        location=ResumeLocationsLocation(),
                        remote_working=RemoteWorking(
                            type=ResumeRemoteWorkingType(
                                details=BaseDetails(),
                                value="value_example",
                            ),
                            frequency=ResumeRemoteWorkingFrequencyRange(
                                details=BaseDetails(),
                                range=None,
                            ),
                        ),
                        employer=Organization(),
                        industries=[
                            ResumeWorkExperiencesIndustry(
                                details=IndustryDetails(
                                    is_validated=False,
                                ),
                                value="value_example",
                            )
                        ],
                        skills=[
                            OptionalResumeSkill(
                                details=OptionalResumeSkillDetails(
,
                                    raw_value="raw_value_example",
,
                                    is_validated=False,
                                    entity_type="entity_type_example",
                                    proficiency_level="proficiency_level_example",
                                    category="hard",
                                    code=ResumeSkillCode(
                                        key="key_example",
                                    ),
                                    score=0.75,
                                ),
                                value="value_example",
                            )
                        ],
                        id="id_example",
                    )
                ],
                cover_letter=Text(),
                references=[
                    Reference(
                        person_name=ResumePersonNamePersonName(),
                        contact_info=ResumeContactInfoContactInfo(),
                        description=Description(),
                    )
                ],
                profile_summary=ProfileSummary(
                    loyalty_score=ValidatedFloatValueModel(
                        details=SlimBaseDetails(),
                        value=3.14,
                    ),
                    work_experiences_count=ValidatedIntegerValueModel(
                        details=SlimBaseDetails(),
                        value=1,
                    ),
,
,
                    highest_seniority_level_code=SeniorityLevelCode(
                        details=BaseDetails(),
                        value="value_example",
                    ),
                    education_experiences_count=ValidatedIntegerValueModel(),
                    education_experiences_average_duration=ValidatedIntegerValueModel(),
                    education_experiences_total_duration=ValidatedIntegerValueModel(),
                    highest_education_title=HighestEducationTitle(
                        details=SlimBaseDetails(),
                        value="value_example",
                    ),
                    highest_education_level_code=ResumeEducationExperiencesEducationLevelCode(),
                    objective=Description(),
                    personal_description=Description(),
                ),
                skills=[
                    OptionalResumeSkill()
                ],
                job_titles=[
                    OptionalResumeJobTitle()
                ],
                languages=[
                    OptionalResumeLanguage(
                        details=OptionalResumeLanguageDetails(
,
                            raw_value="raw_value_example",
,
                            is_validated=False,
                            entity_type="entity_type_example",
                            proficiency_level="proficiency_level_example",
                            category="category_example",
                            code=ResumeLanguageCode(
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
                            is_primary=True,
                        ),
                        value="value_example",
                    )
                ],
                certifications=[
                    Certification(
                        certification_name=BaseModelsName(),
                        description=Description(),
                        first_issued_date=Date(),
                        issuing_authority=Organization(),
                        url=ResumeLinkURL(),
                    )
                ],
                publications=[
                    Publication(
                        title=Title(
                            details=BaseDetails(),
                            value="value_example",
                        ),
                        description=Description(),
                        doi=Text(),
                        year=Date(),
                        link=ResumeLinkLink(),
                    )
                ],
                awards=[
                    Award(
                        title=Title(),
                        description=Description(),
                        year=Date(),
                        awarder=Organization(),
                    )
                ],
                projects=[
                    Project(
                        project_name=BaseModelsName(),
                        description=Description(),
                        roles=[
                            Role(
                                details=BaseDetails(),
                                value="value_example",
                            )
                        ],
                        keywords=[
                            Keyword(
                                details=BaseDetails(),
                                value="value_example",
                            )
                        ],
                        start_date=Date(),
                        end_date=Date(),
                        ongoing=Ongoing(),
                        link=ResumeLinkLink(),
                    )
                ],
                achievements=[
                    Achievement(
                        title=Title(),
                        description=Description(),
                        year=Date(),
                        link=ResumeLinkLink(),
                    )
                ],
                patents=[
                    Patent(
                        patent_title=Title(),
                        patent_id=Text(),
                        patent_status=PatentStatus(
                            details=BaseDetails(),
                            value="value_example",
                        ),
                        description=Description(),
                        inventor_names=[
                            ResumePersonNamePersonName()
                        ],
                        issuing_authority=Organization(),
                    )
                ],
                hobbies_and_interests=[
                    Text()
                ],
                licenses=[
                    License(
                        license_type=LicenseType(
                            details=BaseDetails(),
                            value="value_example",
                        ),
                        license_type_code=DrivingLicenseTypeCode(
                            details=BaseDetails(),
                            value="value_example",
                        ),
                        first_issued_date=Date(),
                        expiry_date=Date(),
                    )
                ],
                volunteering=[
                    Event(
                        title=Title(),
                        start_date=Date(),
                        end_date=Date(),
                        ongoing=Ongoing(),
                        description=Description(),
                        location=ResumeLocationsLocation(),
                        link=ResumeLinkLink(),
                    )
                ],
                conference_and_seminars=[
                    Event()
                ],
                military_history=[
                    MilitaryService(
                        military_branch=Title(),
                        military_division=Title(),
                        starting_rank=Title(),
                        current_or_ending_rank=Title(),
                        location=ResumeLocationsLocation(),
                        start_date=Date(),
                        end_date=Date(),
                        ongoing=Ongoing(),
                    )
                ],
                others=[
                    Other(
                        title=Title(),
                        date=Date(),
                        description=Description(),
                        link=ResumeLinkLink(),
                    )
                ],
            ),
            attachments=FeedbackAttachments(
                pic=ImageMetadata(
                    file_ext="file_ext_example",
                    filename="filename_example",
                ),
                cv=ParseResumeDocument(
                    plain_text="plain_text_example",
                    language="it",
                    filename="filename_example",
                    file_ext="file_ext_example",
                ),
            ),
        ),
        output_corrected=FeedbackBaseItem(
            data=FeedbackData(
                job_title=OptionalResumeJobTitle(),
                personal_info=PersonalInfo(),
                contact_info=ResumeContactInfoContactInfo(),
                person_location=PersonLocation(),
                headline=Text(),
,
,
                cover_letter=Text(),
,
                profile_summary=ProfileSummary(),
,
,
                languages=[
                    FeedbackLanguage(
                        value=None,
                    )
                ],
,
,
,
,
,
,
,
,
,
,
,
,
                education_experience=[
                    FeedbackEducationExperience(
                        duration=BaseDuration(),
                        education_title=FeedbackEducationTitle(
                            details=BaseDetails(),
,
                        ),
                        field_of_study=FeedbackFieldOfStudy(
                            details=BaseDetails(),
,
                        ),
                        final_grade=FinalGrade(),
                        education_level_code=ResumeEducationExperiencesEducationLevelCode(),
                        description=Description(),
                        start_date=Date(),
                        end_date=Date(),
                        ongoing=Ongoing(),
                        location=ResumeLocationsLocation(),
                        organization=FeedbackOrganization(
                            organization_name=FeedbackOrganizationName(
                                details=BaseDetails(),
,
                            ),
                            department=Text(),
                            location=ResumeLocationsLocation(),
                            link=ResumeLinkLink(),
                            id=ID(),
                        ),
,
                        id="id_example",
                    )
                ],
                work_experience=[
                    FeedbackWorkExperience(
                        seniority=BaseSeniority(),
                        duration=BaseDuration(),
                        position_title=FeedbackJobTitle(
                            details=OptionalResumeJobTitleDetails(),
,
                        ),
                        description=Description(),
                        start_date=Date(),
                        end_date=Date(),
                        ongoing=Ongoing(),
                        location=ResumeLocationsLocation(),
                        remote_working=RemoteWorking(),
                        employer=Organization(),
,
,
                        id="id_example",
                    )
                ],
            ),
            attachments=FeedbackAttachments(),
        ),
    )
    try:
        # Info Extraction Feedback
        api_response = api_instance.info_extraction_feedback_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling FeedbackApi->info_extraction_feedback_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
[**FeedbackInfoItem**](../../models/FeedbackInfoItem.md) |  | 


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
200 | [ApiResponseFor200](#info_extraction_feedback_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#info_extraction_feedback_post.ApiResponseFor422) | Validation Error

#### info_extraction_feedback_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FeedbackResponse**](../../models/FeedbackResponse.md) |  | 


#### info_extraction_feedback_post.ApiResponseFor422
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

# **semantic_search_feedback_post**
<a name="semantic_search_feedback_post"></a>
> FeedbackResponse semantic_search_feedback_post(indexnameresume_idsemantic_feedback_request)

Semantic Search Feedback

 This method collects the feedback the Semantic Search ([Search Resumes](https://api.inda.ai/hr/docs/v2/#operation/search_resumes__POST) method) on the document associated to *resume_id* on the index *indexname*. Note that *resume_id* is the ID returned by the [Add Resume](https://api.inda.ai/hr/docs/v2/#operation/add_resume__POST) method.  The method requires an application/json as content type body. This json is an object which contains the following elements (see also the schema below and the example on the right): + A list of *QueryTerms* and *Weights* used to perform the [Search Resumes](https://api.inda.ai/hr/docs/v2/#operation/search_resumes__POST). + The rank of the item in the [Search Resumes](https://api.inda.ai/hr/docs/v2/#operation/search_resumes__POST) output. + The feedback field: The allowed values are <code style='color: #333333; opacity: 0.9'>0</code>, <code style='color: #333333; opacity: 0.9'>1</code>, and <code style='color: #333333; opacity: 0.9'>-1</code>. <code style='color: #333333; opacity: 0.9'>0</code> indicates that the rank is agreeable (i.e., it is not far from the rank expected by the user); <code style='color: #333333; opacity: 0.9'>1</code> indicates that the rank should have been significantly larger; <code style='color: #333333; opacity: 0.9'>-1</code> indicates that the rank should have been significantly smaller. + Optionally, the outcome of the [Search Resumes Evidence](https://api.inda.ai/hr/docs/v2/#operation/search_resumes_evidence__POST) call might be provided to improve log readability. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import feedback_api
from inda_hr.model.semantic_feedback_request import SemanticFeedbackRequest
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.feedback_response import FeedbackResponse
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
    api_instance = feedback_api.FeedbackApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    body = SemanticFeedbackRequest(
        terms=[
            WeightedQueryTerm(
                term="term_example",
                language="it",
                weight=1.0,
            )
        ],
        rank=0.0,
        feedback=-1,
        evidence=[
            SearchTerm(
                score=3.14,
                term="term_example",
            )
        ],
    )
    try:
        # Semantic Search Feedback
        api_response = api_instance.semantic_search_feedback_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling FeedbackApi->semantic_search_feedback_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
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
[**SemanticFeedbackRequest**](../../models/SemanticFeedbackRequest.md) |  | 


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
200 | [ApiResponseFor200](#semantic_search_feedback_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#semantic_search_feedback_post.ApiResponseFor422) | Validation Error

#### semantic_search_feedback_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FeedbackResponse**](../../models/FeedbackResponse.md) |  | 


#### semantic_search_feedback_post.ApiResponseFor422
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

