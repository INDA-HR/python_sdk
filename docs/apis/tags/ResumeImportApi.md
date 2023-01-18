<a name="__pageTop"></a>
# inda_hr.apis.tags.resume_import_api.ResumeImportApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**aws_import_post**](#aws_import_post) | **post** /hr/v2/index/{indexname}/resumes/import/aws/ | AWS Import
[**import_status_get**](#import_status_get) | **get** /hr/v2/index/{indexname}/resumes/import/aws/status/ | Import Status

# **aws_import_post**
<a name="aws_import_post"></a>
> ImportResponse aws_import_post(indexnamedocs_import_item_request)

AWS Import

 This method imports a collection of *Files* from a *Bucket* on Amazon S3 Storage Service into the INDA index  *indexname*.  *Intervieweb* customers do not need any  *Credentials*, because their files are already in the [Inrecruiting](https://www.in-recruiting.com/en/) cloud. For other users, we strongly recommend creating *ad-hoc credentials* with *read-only* rights. These credentials will not be stored by us anyway in any form.  The array of *Files* should contain a collection of resumes. Each file must have an *URL*, which is the file path inside the *Bucket*, an *InternalID* (i.e., an unique identifier used by the user internal system), and a *Resume*, which contains all the structured data to be imported in INDA. The *Resume* field has the same structure used in [Add Resume](https://api.inda.ai/hr/docs/v2/#operation/add_resume__POST), without the fields *Attachments.CV.File* (the file binary) and  *Attachments.CV.FileExt* (the file extension). The *Resume* data in the request will not be validated in input, but rather later during the request preprocessing.  The list of documents in the response accounts for documents that were successfully validated and downloaded from the *Bucket*. Note that these documents will be processed in the background before they can be uploaded to *indexname* and this may cause some small changes in the list of documents actually uploaded.  The response contains (*i*) a *Stats* field which provides a brief overview of the number of *Sent* and *Queued* documents, (*ii*) a list of queued *Resumes* with an INDA *ResumeID* and its user *InternalID*, and (*iii*) a list of *Errors* raised during the preprocessing stage.  In order to obtain updated information on the import progress and on the failures that might happen during the import process, the user can use the *import_id* through the following methods: + [Get Failures](https://api.inda.ai/hr/docs/v2/#operation/get_failures__GET) + [Import Status](https://api.inda.ai/hr/docs/v2/#operation/import_status__GET) 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_import_api
from inda_hr.model.import_response import ImportResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.docs_import_item_request import DocsImportItemRequest
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
    api_instance = resume_import_api.ResumeImportApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    body = DocsImportItemRequest(
        bucket="bucket_example",
        files=[
            DocsBucketItem(
                resume=DocsImportResume(
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
                    metadata=Metadata(
                        language="fr",
                    ),
                    attachments=DocsImportAttachments(
                        pic=Image(
                            file_ext="file_ext_example",
                            filename="filename_example",
                            file=open('/path/to/file', 'rb'),
                        ),
                        cv=OptionalResumeAttachmentLanguage(
                            language="fr",
                        ),
                    ),
                ),
                url="url_example",
                internal_id=None,
            )
        ],
        credentials=AwsCredentials(
            region_name="region_name_example",
            awsid="awsid_example",
            aws_key="aws_key_example",
        ),
    )
    try:
        # AWS Import
        api_response = api_instance.aws_import_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeImportApi->aws_import_post: %s\n" % e)
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
[**DocsImportItemRequest**](../../models/DocsImportItemRequest.md) |  | 


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
202 | [ApiResponseFor202](#aws_import_post.ApiResponseFor202) | Import Successfully Queued
403 | [ApiResponseFor403](#aws_import_post.ApiResponseFor403) | Forbidden
404 | [ApiResponseFor404](#aws_import_post.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#aws_import_post.ApiResponseFor422) | Validation Error

#### aws_import_post.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImportResponse**](../../models/ImportResponse.md) |  | 


#### aws_import_post.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### aws_import_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### aws_import_post.ApiResponseFor422
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

# **import_status_get**
<a name="import_status_get"></a>
> ImportStatus import_status_get(indexnameimport_id)

Import Status

 This method returns the status of the import corresponding to the *import_id* indicated as query parameter (see the schema below). The status value may be one of the following: + *Pending*: the import is in INDA process queues; + *Running*: the import has begun; INDA is processeing the associated resumes; + *Completed*: the import is finished. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_import_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.import_status import ImportStatus
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
    api_instance = resume_import_api.ResumeImportApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'import_id': "import_id_example",
    }
    try:
        # Import Status
        api_response = api_instance.import_status_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeImportApi->import_status_get: %s\n" % e)
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
import_id | ImportIdSchema | | 


# ImportIdSchema

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
200 | [ApiResponseFor200](#import_status_get.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#import_status_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#import_status_get.ApiResponseFor404) | Not Found
503 | [ApiResponseFor503](#import_status_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#import_status_get.ApiResponseFor422) | Validation Error

#### import_status_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ImportStatus**](../../models/ImportStatus.md) |  | 


#### import_status_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### import_status_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### import_status_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### import_status_get.ApiResponseFor422
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

