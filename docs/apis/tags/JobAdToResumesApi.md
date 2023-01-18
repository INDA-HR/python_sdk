<a name="__pageTop"></a>
# inda_hr.apis.tags.job_ad_to_resumes_api.JobAdToResumesApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**match_resumes_evidence_from_indexed_jobad_post**](#match_resumes_evidence_from_indexed_jobad_post) | **post** /hr/v2/index/{indexname}/resumes/matching/jobad/{jobad_id}/evidence/ | Match Resumes Evidence from indexed JobAd
[**match_resumes_evidence_post**](#match_resumes_evidence_post) | **post** /hr/v2/index/{indexname}/resumes/matching/jobad/evidence/ | Match Resumes Evidence
[**match_resumes_from_indexed_jobad_post**](#match_resumes_from_indexed_jobad_post) | **post** /hr/v2/index/{indexname}/resumes/matching/jobad/{jobad_id}/ | Match Resumes from indexed JobAd
[**match_resumes_post**](#match_resumes_post) | **post** /hr/v2/index/{indexname}/resumes/matching/jobad/ | Match Resumes

# **match_resumes_evidence_from_indexed_jobad_post**
<a name="match_resumes_evidence_from_indexed_jobad_post"></a>
> MatchResumeEvidenceResponse match_resumes_evidence_from_indexed_jobad_post(indexnamejobad_idbase_resume_matching_evidence_query)

Match Resumes Evidence from indexed JobAd

This method can be used for a registerd job advert; it is analogous to the The [Match Resume Evidence](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_evidence__POST) method, but it takes in input the ID of the job advert instead of its JSON.  Please refer to the [Match Resumes Evidence](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_evidence__POST) description for further details on the method and on its output.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_to_resumes_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.match_resume_evidence_response import MatchResumeEvidenceResponse
from inda_hr.model.base_resume_matching_evidence_query import BaseResumeMatchingEvidenceQuery
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
    api_instance = job_ad_to_resumes_api.JobAdToResumesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': "jobad_id_example",
    }
    body = BaseResumeMatchingEvidenceQuery(
        resume_ids=[
            "resume_ids_example"
        ],
    )
    try:
        # Match Resumes Evidence from indexed JobAd
        api_response = api_instance.match_resumes_evidence_from_indexed_jobad_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_evidence_from_indexed_jobad_post: %s\n" % e)
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
[**BaseResumeMatchingEvidenceQuery**](../../models/BaseResumeMatchingEvidenceQuery.md) |  | 


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
200 | [ApiResponseFor200](#match_resumes_evidence_from_indexed_jobad_post.ApiResponseFor200) | Matching Evidence completed
400 | [ApiResponseFor400](#match_resumes_evidence_from_indexed_jobad_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#match_resumes_evidence_from_indexed_jobad_post.ApiResponseFor422) | Validation Error

#### match_resumes_evidence_from_indexed_jobad_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MatchResumeEvidenceResponse**](../../models/MatchResumeEvidenceResponse.md) |  | 


#### match_resumes_evidence_from_indexed_jobad_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### match_resumes_evidence_from_indexed_jobad_post.ApiResponseFor422
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

# **match_resumes_evidence_post**
<a name="match_resumes_evidence_post"></a>
> MatchResumeEvidenceResponse match_resumes_evidence_post(indexnameresume_matching_evidence_query)

Match Resumes Evidence

This method provides details about the score of a list of resumes according to the matching with a given job advert.  The method should be used after the call of [Match Resumes](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST) or [Match Resumes from indexed JobAd](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_from_indexed_jobad__POST), on a *ResumeID* or a set of *ResumeID*s returned by one of these methods, in order to obtain the evidence of the matching score.  The relevant information for the matching evidence is the same described in the [Match Resumes](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST) method.  For each resume *ID*, the method returns: + a matching score between the [EQF level](https://en.wikipedia.org/wiki/European_Qualifications_Framework) of the candidate and the job advert's required and preferred EQF (if any); + a matching score between the total duration of the candidate's work experiences and the job advert's required and preferred experience durations (if any); + a matching score between the candidate's seniority and the job advert's required and preferred seniorities (if any); + a detail for each skill in the resume, containing the relative matching score with respect to the job advert; + a detail for each job title in the resume, containing the relative matching score with respect to the job advert.  Each aforementioned matching score has to be considered as an affinity score between job advert's and candidate's data, which contributes to the final [Match Resumes](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST) response's <code style='color: #333333; opacity: 0.9'>Score</code>.  Any *ResumeID* not corresponding to an available resume in the index *indexname* will be ignored.  Note that the [Match Resumes Evidence from indexed JobAd](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_evidence_from_indexed_jobad__POST), method can be used for a job advert which has been already indexed.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_to_resumes_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.resume_matching_evidence_query import ResumeMatchingEvidenceQuery
from inda_hr.model.match_resume_evidence_response import MatchResumeEvidenceResponse
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
    api_instance = job_ad_to_resumes_api.JobAdToResumesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    body = ResumeMatchingEvidenceQuery(
        resume_ids=[
            "resume_ids_example"
        ],
        job_ad=JobAd(
            data=JobAdMatchingData(
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
            metadata=MatchingJobadMatchingPublicMetadata(
                language="it",
            ),
        ),
    )
    try:
        # Match Resumes Evidence
        api_response = api_instance.match_resumes_evidence_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_evidence_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'src_lang': "es",
    }
    body = ResumeMatchingEvidenceQuery(
        resume_ids=[
            "resume_ids_example"
        ],
        job_ad=JobAd(
            data=JobAdMatchingData(
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
            metadata=MatchingJobadMatchingPublicMetadata(
                language="it",
            ),
        ),
    )
    try:
        # Match Resumes Evidence
        api_response = api_instance.match_resumes_evidence_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_evidence_post: %s\n" % e)
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
[**ResumeMatchingEvidenceQuery**](../../models/ResumeMatchingEvidenceQuery.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional


# SrcLangSchema

Job Description language. If left empty each section's language will be detected automatically.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Job Description language. If left empty each section&#x27;s language will be detected automatically. | must be one of ["es", "de", "pt", "fr", "en", "it", ] 

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
200 | [ApiResponseFor200](#match_resumes_evidence_post.ApiResponseFor200) | Matching Evidence completed
400 | [ApiResponseFor400](#match_resumes_evidence_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#match_resumes_evidence_post.ApiResponseFor422) | Validation Error

#### match_resumes_evidence_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MatchResumeEvidenceResponse**](../../models/MatchResumeEvidenceResponse.md) |  | 


#### match_resumes_evidence_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### match_resumes_evidence_post.ApiResponseFor422
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

# **match_resumes_from_indexed_jobad_post**
<a name="match_resumes_from_indexed_jobad_post"></a>
> SearchResumeMatchResponse match_resumes_from_indexed_jobad_post(indexnamejobad_idbase_resume_matching_query)

Match Resumes from indexed JobAd

This method performs a search among the resumes in index *indexname* to find the best matching for a given job advert.  The method can be used for any job advert which has been already added in the index. Note that, unless the parameter *only_applicants* is set to <code style='color: #333333; opacity: 0.9'>false</code>, only the resumes registered to the job advert will be considered in the search.  Note also that the [Match Resumes](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST) method should be used for a job advert which has not not yet been indexed.  Please refer to the [Match Resumes](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST) method for details on the relevant information used for the matching, on the suggested filters, and on the output.  The [Match Resumes Evidence from indexed JobAd](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_evidence_from_indexed_jobad__POST) method can be used to obtain the evidence of the matching score.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_to_resumes_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.search_resume_match_response import SearchResumeMatchResponse
from inda_hr.model.base_resume_matching_query import BaseResumeMatchingQuery
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
    api_instance = job_ad_to_resumes_api.JobAdToResumesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': "jobad_id_example",
    }
    query_params = {
    }
    body = BaseResumeMatchingQuery(
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
        # Match Resumes from indexed JobAd
        api_response = api_instance.match_resumes_from_indexed_jobad_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_from_indexed_jobad_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': "jobad_id_example",
    }
    query_params = {
        'size': 20,
        'offset': 0,
        'min_score': 0,
        'dst_lang': [
        "es"
    ],
        'resume_langs': [
        "es"
    ],
        'only_applicants': False,
        'exclude_applicants': False,
    }
    body = BaseResumeMatchingQuery(
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
        # Match Resumes from indexed JobAd
        api_response = api_instance.match_resumes_from_indexed_jobad_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_from_indexed_jobad_post: %s\n" % e)
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
[**BaseResumeMatchingQuery**](../../models/BaseResumeMatchingQuery.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
size | SizeSchema | | optional
offset | OffsetSchema | | optional
min_score | MinScoreSchema | | optional
dst_lang | DstLangSchema | | optional
resume_langs | ResumeLangsSchema | | optional
only_applicants | OnlyApplicantsSchema | | optional
exclude_applicants | ExcludeApplicantsSchema | | optional


# SizeSchema

Optional. Number of documents to return.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to return. | if omitted the server will use the default value of 20

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

# ResumeLangsSchema

DEPRECATED: use <code style='color: #333333; opacity: 0.9'>dst_langs</code> instead. Results languages. If left empty then the results will not be filtered by language.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | DEPRECATED: use &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;dst_langs&lt;/code&gt; instead. Results languages. If left empty then the results will not be filtered by language. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["es", "de", "pt", "fr", "en", "it", ] 

# OnlyApplicantsSchema

If true, it narrows the search to the resumes registered to the job advert.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | If true, it narrows the search to the resumes registered to the job advert. | if omitted the server will use the default value of False

# ExcludeApplicantsSchema

If true, it excludes the resumes registered to the job advert from the search results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | If true, it excludes the resumes registered to the job advert from the search results. | if omitted the server will use the default value of False

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
200 | [ApiResponseFor200](#match_resumes_from_indexed_jobad_post.ApiResponseFor200) | Matching completed
400 | [ApiResponseFor400](#match_resumes_from_indexed_jobad_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#match_resumes_from_indexed_jobad_post.ApiResponseFor422) | Validation Error

#### match_resumes_from_indexed_jobad_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchResumeMatchResponse**](../../models/SearchResumeMatchResponse.md) |  | 


#### match_resumes_from_indexed_jobad_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### match_resumes_from_indexed_jobad_post.ApiResponseFor422
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

# **match_resumes_post**
<a name="match_resumes_post"></a>
> SearchResumeMatchResponse match_resumes_post(indexnameresume_matching_query)

Match Resumes

This method performs a search among the resumes in index *indexname* to find the best matchings for a given job advert.  The method should be used after the json of the job advert has been completely formed, but before the job advert is added in the index. We strongly recommend the use of the method [Match Resumes from indexed JobAd](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_from_indexed_jobad__POST),  for a job advert which has been already indexed, as it allows to focus on the resumes who registered to the  job advert.   Note also that the [JobAd Knowledge Extraction](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Knowledge-Extraction) methods can be used to enrich the job advert JSON with relevant information. The following information is particularly relevant and should be present in the job advert to obtain an accurate matching:  + The main job title  + Related job titles (if any)  + The required skills  + The preferred skills (if any)  Other relevant information -- e.g., required and preferred duration, required and preferred [EQF level](https://en.wikipedia.org/wiki/European_Qualifications_Framework)  -- is retrieved from the job advert JSON and contributes to the pertinence score of each resume, provided that the index contains a sufficient number of resumes with that information.  Optionally, a list of [*query filters*](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) (*QueryFilters*) can be provided to narrow the query. We strongly encourage use of query filters to reduce computation time and improve the result accuracy. For instance, the following filters may be used: + Filter on the last update date (*Metadata.LastModified*) + Filter on the [EQF level](https://en.wikipedia.org/wiki/European_Qualifications_Framework) (*Data.ProfileSummary.HighestEducationLevelCode.Value.EQF*) + Filter on the duration (*Data.ProfileSummary.WorkExperiencesTotalDuration.Value*) + Filter on the applicant address, if this is a relevant information  The Mandatory requirements specified within the *JobAd* (subfields of a *required* field) narrow the search to the suitable resumes, provided that the index contains a sufficient number of candidates with the information required to filter; if a requirement specified in the *JobAd* involves the same field associated to a filter specified in *QueryFilters*, the latter overrides the former.   Furthermore, in order to tackle the bias problem, INDA automatically ignores specific fields (such as name, gender, age and nationality) during the initial processing of each resume data. We are constantly working on reduce the bias in original data so that INDA results may be as fair as possible.   The method returns a list of JSON documents, each of which contains a resume that represents a job advert applicant; the resumes are sorted according to a pertinence score (*Score*) determined on the basis of the matching level in terms of the relevant information discussed above that are specified in the job advert. Please refer to the response sample on the right for further details on the output.  The [Match Resumes Evidence](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_evidence__POST) method can be used to obtain the evidence of the matching score.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import job_ad_to_resumes_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.search_resume_match_response import SearchResumeMatchResponse
from inda_hr.model.resume_matching_query import ResumeMatchingQuery
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
    api_instance = job_ad_to_resumes_api.JobAdToResumesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    body = ResumeMatchingQuery(
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
        job_ad=JobAd(
            data=JobAdMatchingData(
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
            metadata=MatchingJobadMatchingPublicMetadata(
                language="it",
            ),
        ),
    )
    try:
        # Match Resumes
        api_response = api_instance.match_resumes_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'size': 20,
        'offset': 0,
        'min_score': 0,
        'src_lang': "es",
        'dst_lang': [
        "es"
    ],
        'resume_langs': [
        "es"
    ],
    }
    body = ResumeMatchingQuery(
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
        job_ad=JobAd(
            data=JobAdMatchingData(
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
            metadata=MatchingJobadMatchingPublicMetadata(
                language="it",
            ),
        ),
    )
    try:
        # Match Resumes
        api_response = api_instance.match_resumes_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_post: %s\n" % e)
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
[**ResumeMatchingQuery**](../../models/ResumeMatchingQuery.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
size | SizeSchema | | optional
offset | OffsetSchema | | optional
min_score | MinScoreSchema | | optional
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional
resume_langs | ResumeLangsSchema | | optional


# SizeSchema

Optional. Number of documents to return.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to return. | if omitted the server will use the default value of 20

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

Job Description language. If left empty each section's language will be detected automatically.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Job Description language. If left empty each section&#x27;s language will be detected automatically. | must be one of ["es", "de", "pt", "fr", "en", "it", ] 

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

# ResumeLangsSchema

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
200 | [ApiResponseFor200](#match_resumes_post.ApiResponseFor200) | Matching completed
400 | [ApiResponseFor400](#match_resumes_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#match_resumes_post.ApiResponseFor422) | Validation Error

#### match_resumes_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SearchResumeMatchResponse**](../../models/SearchResumeMatchResponse.md) |  | 


#### match_resumes_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### match_resumes_post.ApiResponseFor422
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

