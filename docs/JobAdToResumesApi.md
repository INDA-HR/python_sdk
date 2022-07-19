# inda_hr.JobAdToResumesApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**match_resumes_evidence_from_indexed_jobad_post**](JobAdToResumesApi.md#match_resumes_evidence_from_indexed_jobad_post) | **POST** /hr/v2/index/{indexname}/resumes/matching/jobad/{jobad_id}/evidence/ | Match Resumes Evidence from indexed JobAd
[**match_resumes_evidence_post**](JobAdToResumesApi.md#match_resumes_evidence_post) | **POST** /hr/v2/index/{indexname}/resumes/matching/jobad/evidence/ | Match Resumes Evidence
[**match_resumes_from_indexed_jobad_post**](JobAdToResumesApi.md#match_resumes_from_indexed_jobad_post) | **POST** /hr/v2/index/{indexname}/resumes/matching/jobad/{jobad_id}/ | Match Resumes from indexed JobAd
[**match_resumes_post**](JobAdToResumesApi.md#match_resumes_post) | **POST** /hr/v2/index/{indexname}/resumes/matching/jobad/ | Match Resumes


# **match_resumes_evidence_from_indexed_jobad_post**
> MatchResumeEvidenceResponse match_resumes_evidence_from_indexed_jobad_post(indexname, jobad_id, base_resume_matching_evidence_query)

Match Resumes Evidence from indexed JobAd

 This method can be used for a registerd job advert; it is analogous to the The [Match Resume Evidence](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_evidence__POST) method, but it takes in input the ID of the job advert instead of its JSON.  Please refer to the [Match Resumes Evidence](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_evidence__POST) description for further details on the method and on its output. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_to_resumes_api
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
    indexname = "indexname_example" # str | 
    jobad_id = "jobad_id_example" # str | 
    base_resume_matching_evidence_query = BaseResumeMatchingEvidenceQuery(
        resume_ids=[
            "resume_ids_example",
        ],
    ) # BaseResumeMatchingEvidenceQuery | 

    # example passing only required values which don't have defaults set
    try:
        # Match Resumes Evidence from indexed JobAd
        api_response = api_instance.match_resumes_evidence_from_indexed_jobad_post(indexname, jobad_id, base_resume_matching_evidence_query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_evidence_from_indexed_jobad_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **str**|  |
 **base_resume_matching_evidence_query** | [**BaseResumeMatchingEvidenceQuery**](BaseResumeMatchingEvidenceQuery.md)|  |

### Return type

[**MatchResumeEvidenceResponse**](MatchResumeEvidenceResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching Evidence completed |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_resumes_evidence_post**
> MatchResumeEvidenceResponse match_resumes_evidence_post(indexname, resume_matching_evidence_query)

Match Resumes Evidence

 This method provides details about the score of a list of resumes according to the matching with a given job advert.  The method should be used after the call of [Match Resumes](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST) or [Match Resumes from indexed JobAd](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_from_indexed_jobad__POST), on a *ResumeID* or a set of *ResumeID*s returned by one of these methods, in order to obtain the evidence of the matching score.  The relevant information for the matching evidence is the same described in the [Match Resumes](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST) method.  For each *ResumeID*, the method returns + A global matching score between all the job titles specified in the job advert and the resume job titles + A detail for each job title in the job advert, containing a matching score for this specified job title and a list of entities found in the resumes which are semantically related to the specified job title + A global matching scores between the required skills specified in the job advert and the resume skills + A detail for each required skill in the job advert, containing a matching score for this specified skill and a list of entities found in the resumes which are semantically related to the specified skill + An analogous information for the preferred skills specified in the job advert, if present. + A matching score between the [EQF level](https://en.wikipedia.org/wiki/European_Qualifications_Framework) of the candidate and the required and preferred EQF (if any) + A matching score between the experience of the candidate and the required and preferred experience (if any)  Any *ResumeID* not corresponding to an available resume in the index *indexname* will be ignored.  Note that the [Match Resumes Evidence from indexed JobAd](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_evidence_from_indexed_jobad__POST), method can be used for a job advert which has been already indexed. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_to_resumes_api
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
    indexname = "indexname_example" # str | 
    resume_matching_evidence_query = ResumeMatchingEvidenceQuery(
        resume_ids=[
            "resume_ids_example",
        ],
        job_ad=MatchingJobAdDocument(
            data=JobAdMatchingData(
                job_title=JobTitleHeader(
                    details=JobTitleHeaderDetails(
                        language="pt",
                        weight=0.8,
                        category="category_example",
                    ),
                    value="value_example",
                ),
                job_description=JobDescription(
                    company_description=Section(
                        details=SectionDetails(
                            language="pt",
                            weight=0.8,
                        ),
                        title=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        content=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                    position_description=Section(
                        details=SectionDetails(
                            language="pt",
                            weight=0.8,
                        ),
                        title=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        content=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                    position_requirements=Section(
                        details=SectionDetails(
                            language="pt",
                            weight=0.8,
                        ),
                        title=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        content=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                    additional_information=Section(
                        details=SectionDetails(
                            language="pt",
                            weight=0.8,
                        ),
                        title=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        content=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
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
                                JobadContactInfoName(
                                    value="value_example",
                                ),
                            ],
                            family_name=JobadContactInfoName(
                                value="value_example",
                            ),
                            suffix=JobadContactInfoSuffix(
                                value="value_example",
                            ),
                            formatted_name=JobadContactInfoName(
                                value="value_example",
                            ),
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
                            ),
                        ],
                        email_addresses=[
                            JobadEmailAddressEmailAddress(
                                address=JobadEmailAddressAddress(
                                    value="value_example",
                                ),
                                label=JobadEmailAddressEmailLabel(
                                    value="value_example",
                                ),
                            ),
                        ],
                        links=[
                            JobadLinkLink(
                                url=JobadLinkURL(
                                    value="value_example",
                                ),
                                label=JobadLinkLinkLabel(
                                    value="value_example",
                                ),
                            ),
                        ],
                    ),
                ],
                job_locations=[
                    BaseLocationsLocation(
                        city=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        country=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        geo_coordinates=ValueModelGeoLocation(
                            value=GeoLocation(
                                lat=-90.0,
                                lon=-180.0,
                            ),
                        ),
                        country_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        postal_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        street_address=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        county=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        region=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                ],
                relocation_preferences=RelocationPreferences(
                    details=RelocationBoolBaseModel(
                        is_possible=True,
                        is_mandatory=True,
                        is_all_expenses_paid=True,
                    ),
                    relocation_date=None,
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
                    duration=OptionalRequiredAndPreferredUnionDurationValueDurationRange(
                        required=None,
                        preferred=None,
                    ),
                    seniority=OptionalRequiredAndPreferredSeniorityValue(
                        required=SeniorityValue(
                            value="value_example",
                        ),
                        preferred=SeniorityValue(
                            value="value_example",
                        ),
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
                            BaseEmploymentsValueModelStrictStr(
                                value="value_example",
                            ),
                        ],
                    ),
                    preferred=Education(
                        title=EducationTitle(
                            value="value_example",
                        ),
                        education_level_code=JobadEducationEducationLevelCode(
                            value=EducationLevelCodeValue(
                                eqf=1,
                            ),
                        ),
                        fields=[
                            BaseEmploymentsValueModelStrictStr(
                                value="value_example",
                            ),
                        ],
                    ),
                ),
                skills=None,
                languages=OptionalRequiredAndPreferredListJobAdLanguage(
                    required=[
                        JobAdLanguage(
                            details=JobAdLanguageDetails(
                                proficiency_level="proficiency_level_example",
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
                        ),
                    ],
                    preferred=[
                        JobAdLanguage(
                            details=JobAdLanguageDetails(
                                proficiency_level="proficiency_level_example",
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
                        ),
                    ],
                ),
                related_job_titles=[
                    OptionalJobAdJobTitle(
                        details=OptionalJobAdJobTitleDetails(
                            category="category_example",
                            weight=0.75,
                        ),
                        value="value_example",
                    ),
                ],
                employment=JobTitleEmployment(
                    code=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    category=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    type=EmploymentType(
                        value="value_example",
                    ),
                    industries=[
                        BaseEmploymentsIndustry(
                            value="value_example",
                        ),
                    ],
                    functional_areas=[
                        BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ],
                    activities=[
                        Activity(
                            value="value_example",
                            tags=[
                                "tags_example",
                            ],
                        ),
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
                        value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                    end_date=ValueModelDatetime(
                        value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ),
                publisher=Publisher(
                    name=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    category=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    link=JobadLinkLink(
                        url=JobadLinkURL(
                            value="value_example",
                        ),
                        label=JobadLinkLinkLabel(
                            value="value_example",
                        ),
                    ),
                ),
                job_shift=JobShift(
                    details=BoolBaseModel(
                        is_possible=True,
                        is_mandatory=True,
                    ),
                    type=JobShiftType(
                        value="DAY_SHIFT",
                    ),
                    frequency=None,
                ),
                number_of_openings=ValueModelInt(
                    value=1,
                ),
                link=JobadLinkLink(
                    url=JobadLinkURL(
                        value="value_example",
                    ),
                    label=JobadLinkLinkLabel(
                        value="value_example",
                    ),
                ),
                advertisement_sites=[
                    JobadLinkLink(
                        url=JobadLinkURL(
                            value="value_example",
                        ),
                        label=JobadLinkLinkLabel(
                            value="value_example",
                        ),
                    ),
                ],
                salary=JobAdSalary(
                    currency=Currency(
                        value="value_example",
                    ),
                    frequency=Frequency(
                        value="YEARLY",
                    ),
                    type=BaseSalariesType(
                        value="GROSS",
                    ),
                    amount=None,
                ),
                benefits=[
                    JobAdBenefit(
                        value="value_example",
                    ),
                ],
                expiration_date=ValueModelDatetime(
                    value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ),
            metadata=MatchingJobadMatchingPublicMetadata(
                language="it",
            ),
        ),
    ) # ResumeMatchingEvidenceQuery | 

    # example passing only required values which don't have defaults set
    try:
        # Match Resumes Evidence
        api_response = api_instance.match_resumes_evidence_post(indexname, resume_matching_evidence_query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_evidence_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **resume_matching_evidence_query** | [**ResumeMatchingEvidenceQuery**](ResumeMatchingEvidenceQuery.md)|  |

### Return type

[**MatchResumeEvidenceResponse**](MatchResumeEvidenceResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching Evidence completed |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_resumes_from_indexed_jobad_post**
> SearchResumeMatchResponse match_resumes_from_indexed_jobad_post(indexname, jobad_id, base_resume_matching_query)

Match Resumes from indexed JobAd

 This method performs a search among the resumes in index *indexname* to find the best matching for a given job advert.  The method can be used for any job advert which has been already added in the index. Note that, unless the parameter *only_applicants* is set to <code style='color: #333333; opacity: 0.9'>false</code>, only the resumes registered to the job advert will be considered in the search.  Note also that the [Match Resumes](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST) method should be used for a job advert which has not not yet been indexed.  Please refer to the [Match Resumes](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST) method for details on the relevant information used for the matching, on the suggested filters, and on the output.  The [Match Resumes Evidence from indexed JobAd](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_evidence_from_indexed_jobad__POST) method can be used to obtain the evidence of the matching score. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_to_resumes_api
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
    indexname = "indexname_example" # str | 
    jobad_id = "jobad_id_example" # str | 
    base_resume_matching_query = BaseResumeMatchingQuery(
        query_filters=QueryFilters(
            should=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            must_not=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            filter=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
        ),
    ) # BaseResumeMatchingQuery | 
    size = 20 # int | Optional. Number of documents to return. (optional) if omitted the server will use the default value of 20
    min_score = 0 # float | Optional. Minimum pertinence score. (optional) if omitted the server will use the default value of 0
    resume_langs = [
        "es",
    ] # [str] | Languages of the Resumes. Defaults to the JobAd language. (optional)
    only_applicants = True # bool | If true, it narrows the search to the resumes registered to the job advert. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Match Resumes from indexed JobAd
        api_response = api_instance.match_resumes_from_indexed_jobad_post(indexname, jobad_id, base_resume_matching_query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_from_indexed_jobad_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Match Resumes from indexed JobAd
        api_response = api_instance.match_resumes_from_indexed_jobad_post(indexname, jobad_id, base_resume_matching_query, size=size, min_score=min_score, resume_langs=resume_langs, only_applicants=only_applicants)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_from_indexed_jobad_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **str**|  |
 **base_resume_matching_query** | [**BaseResumeMatchingQuery**](BaseResumeMatchingQuery.md)|  |
 **size** | **int**| Optional. Number of documents to return. | [optional] if omitted the server will use the default value of 20
 **min_score** | **float**| Optional. Minimum pertinence score. | [optional] if omitted the server will use the default value of 0
 **resume_langs** | **[str]**| Languages of the Resumes. Defaults to the JobAd language. | [optional]
 **only_applicants** | **bool**| If true, it narrows the search to the resumes registered to the job advert. | [optional] if omitted the server will use the default value of True

### Return type

[**SearchResumeMatchResponse**](SearchResumeMatchResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching completed |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_resumes_post**
> SearchResumeMatchResponse match_resumes_post(indexname, resume_matching_query)

Match Resumes

 This method performs a search among the resumes in index *indexname* to find the best matchings for a given job advert.  The method should be used after the json of the job advert has been completely formed, but before the job advert is added in the index. We strongly recommend the use of the method [Match Resumes from indexed JobAd](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_from_indexed_jobad__POST),  for a job advert which has been already indexed, as it allows to focus on the resumes who registered to the  job advert.   Note also that the [JobAd Knowledge Extraction](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Knowledge-Extraction) methods can be used to enrich the job advert JSON with relevant information. The following information is particularly relevant and should be present in the job advert to obtain an accurate matching:  + The main job title  + Related job titles (if any)  + The required skills  + The preferred skills (if any)  Other relevant information -- e.g., required and preferred duration, required and preferred [EQF level](https://en.wikipedia.org/wiki/European_Qualifications_Framework)  -- is retrieved from the job advert JSON and contributes to the pertinence score of each resume, provided that the index contains a sufficient number of resumes with that information.  Optionally, a list of [*query filters*](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) (*QueryFilters*) can be provided to narrow the query. We strongly encourage use of query filters to reduce computation time and improve the result accuracy. For instance, the following filters may be used: + Filter on the last update date (*Metadata.LastModified*) + Filter on the [EQF level](https://en.wikipedia.org/wiki/European_Qualifications_Framework) (*Data.ProfileSummary.HighestEducationLevelCode.Value.EQF*) + Filter on the duration (*Data.ProfileSummary.WorkExperiencesTotalDuration.Value*) + Filter on the applicant address, if this is a relevant information  The Mandatory requirements specified within the *JobAd* (subfields of a *required* field) narrow the search to the suitable resumes, provided that the index contains a sufficient number of candidates with the information required to filter; if a requirement specified in the *JobAd* involves the same field associated to a filter specified in *QueryFilters*, the latter overrides the former.   Furthermore, in order to tackle the bias problem, INDA automatically ignores specific fields (such as name, gender, age and nationality) during the initial processing of each resume data. We are constantly working on reduce the bias in original data so that INDA results may be as fair as possible.   The method returns a list of JSON documents, each of which contains a resume that represents a job advert applicant; the resumes are sorted according to a pertinence score (*Score*) determined on the basis of the matching level in terms of the relevant information discussed above that are specified in the job advert. Please refer to the response sample on the right for further details on the output.  The [Match Resumes Evidence](https://api.inda.ai/hr/docs/v2/#operation/match_resumes_evidence__POST) method can be used to obtain the evidence of the matching score.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_to_resumes_api
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
    indexname = "indexname_example" # str | 
    resume_matching_query = ResumeMatchingQuery(
        query_filters=QueryFilters(
            should=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            must_not=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            filter=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
        ),
        job_ad=MatchingJobAdDocument(
            data=JobAdMatchingData(
                job_title=JobTitleHeader(
                    details=JobTitleHeaderDetails(
                        language="pt",
                        weight=0.8,
                        category="category_example",
                    ),
                    value="value_example",
                ),
                job_description=JobDescription(
                    company_description=Section(
                        details=SectionDetails(
                            language="pt",
                            weight=0.8,
                        ),
                        title=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        content=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                    position_description=Section(
                        details=SectionDetails(
                            language="pt",
                            weight=0.8,
                        ),
                        title=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        content=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                    position_requirements=Section(
                        details=SectionDetails(
                            language="pt",
                            weight=0.8,
                        ),
                        title=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        content=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                    additional_information=Section(
                        details=SectionDetails(
                            language="pt",
                            weight=0.8,
                        ),
                        title=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        content=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
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
                                JobadContactInfoName(
                                    value="value_example",
                                ),
                            ],
                            family_name=JobadContactInfoName(
                                value="value_example",
                            ),
                            suffix=JobadContactInfoSuffix(
                                value="value_example",
                            ),
                            formatted_name=JobadContactInfoName(
                                value="value_example",
                            ),
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
                            ),
                        ],
                        email_addresses=[
                            JobadEmailAddressEmailAddress(
                                address=JobadEmailAddressAddress(
                                    value="value_example",
                                ),
                                label=JobadEmailAddressEmailLabel(
                                    value="value_example",
                                ),
                            ),
                        ],
                        links=[
                            JobadLinkLink(
                                url=JobadLinkURL(
                                    value="value_example",
                                ),
                                label=JobadLinkLinkLabel(
                                    value="value_example",
                                ),
                            ),
                        ],
                    ),
                ],
                job_locations=[
                    BaseLocationsLocation(
                        city=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        country=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        geo_coordinates=ValueModelGeoLocation(
                            value=GeoLocation(
                                lat=-90.0,
                                lon=-180.0,
                            ),
                        ),
                        country_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        postal_code=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        street_address=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        county=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                        region=BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ),
                ],
                relocation_preferences=RelocationPreferences(
                    details=RelocationBoolBaseModel(
                        is_possible=True,
                        is_mandatory=True,
                        is_all_expenses_paid=True,
                    ),
                    relocation_date=None,
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
                    duration=OptionalRequiredAndPreferredUnionDurationValueDurationRange(
                        required=None,
                        preferred=None,
                    ),
                    seniority=OptionalRequiredAndPreferredSeniorityValue(
                        required=SeniorityValue(
                            value="value_example",
                        ),
                        preferred=SeniorityValue(
                            value="value_example",
                        ),
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
                            BaseEmploymentsValueModelStrictStr(
                                value="value_example",
                            ),
                        ],
                    ),
                    preferred=Education(
                        title=EducationTitle(
                            value="value_example",
                        ),
                        education_level_code=JobadEducationEducationLevelCode(
                            value=EducationLevelCodeValue(
                                eqf=1,
                            ),
                        ),
                        fields=[
                            BaseEmploymentsValueModelStrictStr(
                                value="value_example",
                            ),
                        ],
                    ),
                ),
                skills=None,
                languages=OptionalRequiredAndPreferredListJobAdLanguage(
                    required=[
                        JobAdLanguage(
                            details=JobAdLanguageDetails(
                                proficiency_level="proficiency_level_example",
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
                        ),
                    ],
                    preferred=[
                        JobAdLanguage(
                            details=JobAdLanguageDetails(
                                proficiency_level="proficiency_level_example",
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
                        ),
                    ],
                ),
                related_job_titles=[
                    OptionalJobAdJobTitle(
                        details=OptionalJobAdJobTitleDetails(
                            category="category_example",
                            weight=0.75,
                        ),
                        value="value_example",
                    ),
                ],
                employment=JobTitleEmployment(
                    code=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    category=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    type=EmploymentType(
                        value="value_example",
                    ),
                    industries=[
                        BaseEmploymentsIndustry(
                            value="value_example",
                        ),
                    ],
                    functional_areas=[
                        BaseEmploymentsValueModelStrictStr(
                            value="value_example",
                        ),
                    ],
                    activities=[
                        Activity(
                            value="value_example",
                            tags=[
                                "tags_example",
                            ],
                        ),
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
                        value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                    end_date=ValueModelDatetime(
                        value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    ),
                ),
                publisher=Publisher(
                    name=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    category=BaseEmploymentsValueModelStrictStr(
                        value="value_example",
                    ),
                    link=JobadLinkLink(
                        url=JobadLinkURL(
                            value="value_example",
                        ),
                        label=JobadLinkLinkLabel(
                            value="value_example",
                        ),
                    ),
                ),
                job_shift=JobShift(
                    details=BoolBaseModel(
                        is_possible=True,
                        is_mandatory=True,
                    ),
                    type=JobShiftType(
                        value="DAY_SHIFT",
                    ),
                    frequency=None,
                ),
                number_of_openings=ValueModelInt(
                    value=1,
                ),
                link=JobadLinkLink(
                    url=JobadLinkURL(
                        value="value_example",
                    ),
                    label=JobadLinkLinkLabel(
                        value="value_example",
                    ),
                ),
                advertisement_sites=[
                    JobadLinkLink(
                        url=JobadLinkURL(
                            value="value_example",
                        ),
                        label=JobadLinkLinkLabel(
                            value="value_example",
                        ),
                    ),
                ],
                salary=JobAdSalary(
                    currency=Currency(
                        value="value_example",
                    ),
                    frequency=Frequency(
                        value="YEARLY",
                    ),
                    type=BaseSalariesType(
                        value="GROSS",
                    ),
                    amount=None,
                ),
                benefits=[
                    JobAdBenefit(
                        value="value_example",
                    ),
                ],
                expiration_date=ValueModelDatetime(
                    value=dateutil_parser('1970-01-01T00:00:00.00Z'),
                ),
            ),
            metadata=MatchingJobadMatchingPublicMetadata(
                language="it",
            ),
        ),
    ) # ResumeMatchingQuery | 
    size = 20 # int | Optional. Number of documents to return. (optional) if omitted the server will use the default value of 20
    min_score = 0 # float | Optional. Minimum pertinence score. (optional) if omitted the server will use the default value of 0
    resume_langs = [
        "es",
    ] # [str] | Languages of the Resumes. Defaults to the JobAd language. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Match Resumes
        api_response = api_instance.match_resumes_post(indexname, resume_matching_query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Match Resumes
        api_response = api_instance.match_resumes_post(indexname, resume_matching_query, size=size, min_score=min_score, resume_langs=resume_langs)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdToResumesApi->match_resumes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **resume_matching_query** | [**ResumeMatchingQuery**](ResumeMatchingQuery.md)|  |
 **size** | **int**| Optional. Number of documents to return. | [optional] if omitted the server will use the default value of 20
 **min_score** | **float**| Optional. Minimum pertinence score. | [optional] if omitted the server will use the default value of 0
 **resume_langs** | **[str]**| Languages of the Resumes. Defaults to the JobAd language. | [optional]

### Return type

[**SearchResumeMatchResponse**](SearchResumeMatchResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Matching completed |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

