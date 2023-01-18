<a name="__pageTop"></a>
# inda_hr.apis.tags.resume_to_job_ads_api.ResumeToJobAdsApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**match_jobads_evidence_from_indexed_resume_post**](#match_jobads_evidence_from_indexed_resume_post) | **post** /hr/v2/index/{indexname}/jobads/matching/resume/{resume_id}/evidence/ | Match JobAds Evidence from indexed Resume
[**match_jobads_evidence_post**](#match_jobads_evidence_post) | **post** /hr/v2/index/{indexname}/jobads/matching/resume/evidence/ | Match JobAds Evidence
[**match_jobads_from_indexed_resume_post**](#match_jobads_from_indexed_resume_post) | **post** /hr/v2/index/{indexname}/jobads/matching/resume/{resume_id}/ | Match JobAds from indexed Resume
[**match_jobads_post**](#match_jobads_post) | **post** /hr/v2/index/{indexname}/jobads/matching/resume/ | Match JobAds

# **match_jobads_evidence_from_indexed_resume_post**
<a name="match_jobads_evidence_from_indexed_resume_post"></a>
> MatchJobAdEvidenceResponse match_jobads_evidence_from_indexed_resume_post(indexnameresume_idbase_jobad_matching_evidence_query)

Match JobAds Evidence from indexed Resume

This method can be used for a registered resume; it is analogous to the The [Match JobAds Evidence](https://api.inda.ai/hr/docs/v2/#operation/match_jobads_evidence__POST) method, but it takes in input the ID of the resume instead of its JSON.  Please refer to the [Match JobAds Evidence](https://api.inda.ai/hr/docs/v2/#operation/match_jobads_evidence__POST) description for further details on the method and on its output.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_to_job_ads_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_jobad_matching_evidence_query import BaseJobadMatchingEvidenceQuery
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.match_job_ad_evidence_response import MatchJobAdEvidenceResponse
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
    api_instance = resume_to_job_ads_api.ResumeToJobAdsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    body = BaseJobadMatchingEvidenceQuery(
        job_ad_ids=[
            "job_ad_ids_example"
        ],
    )
    try:
        # Match JobAds Evidence from indexed Resume
        api_response = api_instance.match_jobads_evidence_from_indexed_resume_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeToJobAdsApi->match_jobads_evidence_from_indexed_resume_post: %s\n" % e)
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
[**BaseJobadMatchingEvidenceQuery**](../../models/BaseJobadMatchingEvidenceQuery.md) |  | 


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
200 | [ApiResponseFor200](#match_jobads_evidence_from_indexed_resume_post.ApiResponseFor200) | Matching Evidence completed
400 | [ApiResponseFor400](#match_jobads_evidence_from_indexed_resume_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#match_jobads_evidence_from_indexed_resume_post.ApiResponseFor422) | Validation Error

#### match_jobads_evidence_from_indexed_resume_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MatchJobAdEvidenceResponse**](../../models/MatchJobAdEvidenceResponse.md) |  | 


#### match_jobads_evidence_from_indexed_resume_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### match_jobads_evidence_from_indexed_resume_post.ApiResponseFor422
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

# **match_jobads_evidence_post**
<a name="match_jobads_evidence_post"></a>
> MatchJobAdEvidenceResponse match_jobads_evidence_post(indexnamejobad_matching_evidence_query)

Match JobAds Evidence

This method provides details about the score of a list of job adverts according to the matching with a given resume.  The method should be used after the call of [Match JobAds](https://api.inda.ai/hr/docs/v2/#operation/match_jobads__POST) or [Match JobAds from indexed Resume](https://api.inda.ai/hr/docs/v2/#operation/match_jobads_from_indexed_resume__POST), on a *JobadID* or a set of *JobadID*s returned by one of these methods, in order to obtain the evidence of the matching score.  The relevant information for the matching evidence is the same described in the [Match JobAds](https://api.inda.ai/hr/docs/v2/#operation/match_jobads__POST) method.  For each job advert *ID*, the method returns: + a matching score between the job advert's required and preferred [EQF level](https://en.wikipedia.org/wiki/European_Qualifications_Framework) and the candidate's one (if any); + a matching score between the job advert's required and preferred experience durations and the total duration of the candidate's work experiences (if any); + a matching score between the job advert's required and preferred seniorities and the candidate's seniority (if any); + a detail for each skill in the job advert, containing the relative matching score with respect to the resume; + a detail for each job title in the job advert, containing the relative matching score with respect to the resume.  Each aforementioned matching score has to be considered as an affinity score between job advert's and candidate's data, which contributes to the final [Match JobAds](https://api.inda.ai/hr/docs/v2/#operation/match_jobads__POST) response's <code style='color: #333333; opacity: 0.9'>Score</code>.  Any *JobAdID* not corresponding to an available job advert in the index *indexname* will be ignored.  Note that the [Match JobAds Evidence from indexed Resume](https://api.inda.ai/hr/docs/v2/#operation/match_jobads_evidence_from_indexed_resume__POST), method can be used for a resume which has been already indexed.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_to_job_ads_api
from inda_hr.model.jobad_matching_evidence_query import JobadMatchingEvidenceQuery
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.match_job_ad_evidence_response import MatchJobAdEvidenceResponse
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
    api_instance = resume_to_job_ads_api.ResumeToJobAdsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    body = JobadMatchingEvidenceQuery(
        job_ad_ids=[
            "job_ad_ids_example"
        ],
        resume=Resume(
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
            metadata=MatchingResumeMatchingPublicMetadata(
                language="it",
            ),
            attachments=MatchingDocumentAttachmentV6(
                cv=DocumentV5(
                    plain_text="plain_text_example",
                    language="es",
                    filename="filename_example",
                    file_ext="file_ext_example",
                ),
            ),
        ),
    )
    try:
        # Match JobAds Evidence
        api_response = api_instance.match_jobads_evidence_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeToJobAdsApi->match_jobads_evidence_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'src_lang': "es",
    }
    body = JobadMatchingEvidenceQuery(
        job_ad_ids=[
            "job_ad_ids_example"
        ],
        resume=Resume(
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
            metadata=MatchingResumeMatchingPublicMetadata(
                language="it",
            ),
            attachments=MatchingDocumentAttachmentV6(
                cv=DocumentV5(
                    plain_text="plain_text_example",
                    language="es",
                    filename="filename_example",
                    file_ext="file_ext_example",
                ),
            ),
        ),
    )
    try:
        # Match JobAds Evidence
        api_response = api_instance.match_jobads_evidence_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeToJobAdsApi->match_jobads_evidence_post: %s\n" % e)
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
[**JobadMatchingEvidenceQuery**](../../models/JobadMatchingEvidenceQuery.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional


# SrcLangSchema

Optional. Language in which the following *Resume.Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the detected *Attachment.CV.PlainText* language is assumed as `src_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Language in which the following *Resume.Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the detected *Attachment.CV.PlainText* language is assumed as &#x60;src_lang&#x60;. | must be one of ["es", "de", "pt", "fr", "en", "it", ] 

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
200 | [ApiResponseFor200](#match_jobads_evidence_post.ApiResponseFor200) | Matching Evidence completed
400 | [ApiResponseFor400](#match_jobads_evidence_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#match_jobads_evidence_post.ApiResponseFor422) | Validation Error

#### match_jobads_evidence_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MatchJobAdEvidenceResponse**](../../models/MatchJobAdEvidenceResponse.md) |  | 


#### match_jobads_evidence_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### match_jobads_evidence_post.ApiResponseFor422
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

# **match_jobads_from_indexed_resume_post**
<a name="match_jobads_from_indexed_resume_post"></a>
> SearchJobAdMatchResponse match_jobads_from_indexed_resume_post(indexnameresume_idbase_jobad_matching_query)

Match JobAds from indexed Resume

This method performs a search among the job adverts in index *indexname* to find the best matches for a given resume already registered in INDA. To perform the search starting from the resume of a candidate not yet registered in INDA, please use the [Match JobAds](https://api.inda.ai/hr/docs/v2/#operation/match_jobads__POST), method.  The method can be used, for instance, in the career page in order to guide the candidate to the best matching with their resume. The method can also be used -- via scheduled execution over a pool of resumes -- to generate for each applicant a feed of  suggested job positions which are relevant for them, in order to improve candidate engagement.  Skills and job titles are particularly relevant and should be present in the resume to obtain an accurate matching. Other relevant information -- e.g., experience duration, [EQF level](https://en.wikipedia.org/wiki/European_Qualifications_Framework)  -- is retrieved from the resume and contributes to the pertinence score of each job adverts, provided that the index contains a sufficient number of job adverts with that information.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_to_job_ads_api
from inda_hr.model.base_jobad_matching_query import BaseJobadMatchingQuery
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.search_job_ad_match_response import SearchJobAdMatchResponse
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
    api_instance = resume_to_job_ads_api.ResumeToJobAdsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
    }
    body = BaseJobadMatchingQuery(
        query_filters=QueryFilters(
            must=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value=dict(),
                )
            ],
            should=[
                FilterField()
            ],
            must_not=[
                FilterField()
            ],
            filter=[
                FilterField()
            ],
        ),
    )
    try:
        # Match JobAds from indexed Resume
        api_response = api_instance.match_jobads_from_indexed_resume_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeToJobAdsApi->match_jobads_from_indexed_resume_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
        'size': 5,
        'offset': 0,
        'min_score': 0,
        'dst_lang': [
        "es"
    ],
        'jobad_langs': [
        "es"
    ],
    }
    body = BaseJobadMatchingQuery(
        query_filters=QueryFilters(
            must=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value=dict(),
                )
            ],
            should=[
                FilterField()
            ],
            must_not=[
                FilterField()
            ],
            filter=[
                FilterField()
            ],
        ),
    )
    try:
        # Match JobAds from indexed Resume
        api_response = api_instance.match_jobads_from_indexed_resume_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeToJobAdsApi->match_jobads_from_indexed_resume_post: %s\n" % e)
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
[**BaseJobadMatchingQuery**](../../models/BaseJobadMatchingQuery.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
size | SizeSchema | | optional
offset | OffsetSchema | | optional
min_score | MinScoreSchema | | optional
dst_lang | DstLangSchema | | optional
jobad_langs | JobadLangsSchema | | optional


# SizeSchema

Optional. Number of documents to return.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to return. | if omitted the server will use the default value of 5

# OffsetSchema

Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to skip. Ignored if *cache* is &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;true&lt;/code&gt;. | if omitted the server will use the default value of 0

# MinScoreSchema

Optional. Minimum pertinence score.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Optional. Minimum pertinence score. | if omitted the server will use the default value of 0

# DstLangSchema

Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["es", "de", "pt", "fr", "en", "it", ] 

# JobadLangsSchema

DEPRECATED: use <code style='color: #333333; opacity: 0.9'>dst_langs</code> instead. Results languages. If left empty then the results will not be filtered by language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: use &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;dst_langs&lt;/code&gt; instead. Results languages. If left empty then the results will not be filtered by language. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["es", "de", "pt", "fr", "en", "it", ] 

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
200 | [ApiResponseFor200](#match_jobads_from_indexed_resume_post.ApiResponseFor200) | Matching completed
400 | [ApiResponseFor400](#match_jobads_from_indexed_resume_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#match_jobads_from_indexed_resume_post.ApiResponseFor422) | Validation Error

#### match_jobads_from_indexed_resume_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchJobAdMatchResponse**](../../models/SearchJobAdMatchResponse.md) |  | 


#### match_jobads_from_indexed_resume_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### match_jobads_from_indexed_resume_post.ApiResponseFor422
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

# **match_jobads_post**
<a name="match_jobads_post"></a>
> SearchJobAdMatchResponse match_jobads_post(indexnamejobad_matching_query)

Match JobAds

This method performs a search among the job adverts in index *indexname* to find the best matches for a given resume. To perform the search starting from a resume already registered in INDA, we suggest to use the [Match JobAds from indexed Resume](https://api.inda.ai/hr/docs/v2/#operation/match_jobads_from_indexed_resume__POST), method.  The method can be used, for instance, in the career page in order to guide the candidate to the best matching with their resume. The method can also be used -- via scheduled execution over a pool of resumes -- to generate for each candidate a feed of  suggested job positions which are relevant for them, in order to improve candidate engagement.  Skills and job titles are particularly relevant and should be present in the resume to obtain an accurate matching. Other relevant information -- e.g., experience duration, [EQF level](https://en.wikipedia.org/wiki/European_Qualifications_Framework)  -- is retrieved from the resume and contributes to the pertinence score of each job adverts, provided that the index contains a sufficient number of job adverts with that information.  Optionally, a list of [*query filters*](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) (*QueryFilters*) can be provided to narrow the query. We strongly encourage use of query_filters to reduce computation time and improve the result accuracy.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_to_job_ads_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.jobad_matching_query import JobadMatchingQuery
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.search_job_ad_match_response import SearchJobAdMatchResponse
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
    api_instance = resume_to_job_ads_api.ResumeToJobAdsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    body = JobadMatchingQuery(
        query_filters=QueryFilters(
            must=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value=dict(),
                )
            ],
            should=[
                FilterField()
            ],
            must_not=[
                FilterField()
            ],
            filter=[
                FilterField()
            ],
        ),
        resume=Resume(
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
            metadata=MatchingResumeMatchingPublicMetadata(
                language="it",
            ),
            attachments=MatchingDocumentAttachmentV6(
                cv=DocumentV5(
                    plain_text="plain_text_example",
                    language="es",
                    filename="filename_example",
                    file_ext="file_ext_example",
                ),
            ),
        ),
    )
    try:
        # Match JobAds
        api_response = api_instance.match_jobads_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeToJobAdsApi->match_jobads_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'size': 5,
        'offset': 0,
        'min_score': 0,
        'src_lang': "es",
        'dst_lang': [
        "es"
    ],
        'jobad_langs': [
        "es"
    ],
    }
    body = JobadMatchingQuery(
        query_filters=QueryFilters(
            must=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value=dict(),
                )
            ],
            should=[
                FilterField()
            ],
            must_not=[
                FilterField()
            ],
            filter=[
                FilterField()
            ],
        ),
        resume=Resume(
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
            metadata=MatchingResumeMatchingPublicMetadata(
                language="it",
            ),
            attachments=MatchingDocumentAttachmentV6(
                cv=DocumentV5(
                    plain_text="plain_text_example",
                    language="es",
                    filename="filename_example",
                    file_ext="file_ext_example",
                ),
            ),
        ),
    )
    try:
        # Match JobAds
        api_response = api_instance.match_jobads_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeToJobAdsApi->match_jobads_post: %s\n" % e)
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
[**JobadMatchingQuery**](../../models/JobadMatchingQuery.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
size | SizeSchema | | optional
offset | OffsetSchema | | optional
min_score | MinScoreSchema | | optional
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional
jobad_langs | JobadLangsSchema | | optional


# SizeSchema

Optional. Number of documents to return.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to return. | if omitted the server will use the default value of 5

# OffsetSchema

Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to skip. Ignored if *cache* is &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;true&lt;/code&gt;. | if omitted the server will use the default value of 0

# MinScoreSchema

Optional. Minimum pertinence score.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Optional. Minimum pertinence score. | if omitted the server will use the default value of 0

# SrcLangSchema

Job Description language. If left empty each section's language will detected automatically.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Job Description language. If left empty each section&#x27;s language will detected automatically. | must be one of ["es", "de", "pt", "fr", "en", "it", ] 

# DstLangSchema

Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["es", "de", "pt", "fr", "en", "it", ] 

# JobadLangsSchema

DEPRECATED: use <code style='color: #333333; opacity: 0.9'>dst_langs</code> instead. Results languages. If left empty then the results will not be filtered by language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: use &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;dst_langs&lt;/code&gt; instead. Results languages. If left empty then the results will not be filtered by language. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["es", "de", "pt", "fr", "en", "it", ] 

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
200 | [ApiResponseFor200](#match_jobads_post.ApiResponseFor200) | Matching completed
400 | [ApiResponseFor400](#match_jobads_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#match_jobads_post.ApiResponseFor422) | Validation Error

#### match_jobads_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchJobAdMatchResponse**](../../models/SearchJobAdMatchResponse.md) |  | 


#### match_jobads_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### match_jobads_post.ApiResponseFor422
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

