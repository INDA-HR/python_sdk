<a name="__pageTop"></a>
# inda_hr.apis.tags.resume_management_api.ResumeManagementApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_resume_post**](#add_resume_post) | **post** /hr/v2/index/{indexname}/resume/ | Add Resume
[**delete_pic_delete**](#delete_pic_delete) | **delete** /hr/v2/index/{indexname}/resume/{resume_id}/pic/ | Delete Pic
[**delete_resume_delete**](#delete_resume_delete) | **delete** /hr/v2/index/{indexname}/resume/{resume_id}/ | Delete Resume
[**get_cv_get**](#get_cv_get) | **get** /hr/v2/index/{indexname}/resume/{resume_id}/document/ | Get CV
[**get_cv_text_get**](#get_cv_text_get) | **get** /hr/v2/index/{indexname}/resume/{resume_id}/text/ | Get CV Text
[**get_pic_get**](#get_pic_get) | **get** /hr/v2/index/{indexname}/resume/{resume_id}/pic/ | Get Pic
[**get_resume_get**](#get_resume_get) | **get** /hr/v2/index/{indexname}/resume/{resume_id}/ | Get Resume
[**patch_resume_patch**](#patch_resume_patch) | **patch** /hr/v2/index/{indexname}/resume/{resume_id}/ | Patch Resume
[**resume_status_get**](#resume_status_get) | **get** /hr/v2/index/{indexname}/resume/{resume_id}/status/ | Resume Status
[**update_pic_put**](#update_pic_put) | **put** /hr/v2/index/{indexname}/resume/{resume_id}/pic/ | Update Pic
[**update_resume_put**](#update_resume_put) | **put** /hr/v2/index/{indexname}/resume/{resume_id}/ | Update Resume

# **add_resume_post**
<a name="add_resume_post"></a>
> ItemIdResponse add_resume_post(indexnamefile_item_request)

Add Resume

 This method adds a resume to *indexname* and assigns it a *resume_id* (namely, a Unique Universal ID or UUID4).  On the right, we provide an example of input structure that corresponds to the result of the method [Parse Resume](https://api.inda.ai/hr/docs/v2/#operation/parse_resume__POST). However, the input structure is customizable. Further details can be found in the [Resume Model](https://api.inda.ai/hr/docs/v2/#tag/Resume) section.  Entities among skills, job (or position) titles and languages are automatically mapped by INDAto the adopted knowledge base, so that users can leverage on standardized values.Original values and entity IDs are available in *Details.RawValues* and *Details.Code*, respectively.Unrecognized items are ignored and not indexed, except for the *WorkExperiences.PositionTitle* entities.  This method adds the resume to be processed to the server's task queue and return immediately the *resume_id*. Note that the document may not successfully conclude the processing pipeline (e.g., it may be discarded because duplicate of one of the documents already present in the *indexname*), and thus it may not be actually added to the index.  In order to verify the resume status, the user can use the *resume_id* through the following methods: + [Resume Status](https://api.inda.ai/hr/docs/v2/#operation/resume_status__GET) + [Get Failures](https://api.inda.ai/hr/docs/v2/#operation/get_failures__GET)  For a synchronous approach, use the *sync* query parameter: if set to *true*, the resume is processed immediately. However, for standard usage in production environments, we recommend relying on the asynchronous strategy by ignoring  this parameter, in order to reduce the response times (due to the heterogeneity of resumes, the response time of each  resume processing can vary substantially among different documents).  Please note that, for user's convenience, the [API credits requests](https://api.inda.ai/hr/docs/v2/#tag/Credits-Management) assume that the  synchronous approach is named as *Add Resume Sync*, so that it can be easily distinguished from the asynchronous  *Add Resume*.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.item_id_response import ItemIdResponse
from inda_hr.model.file_item_request import FileItemRequest
from inda_hr.model.base_item_id_response import BaseItemIdResponse
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
    api_instance = resume_management_api.ResumeManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    body = FileItemRequest(
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
        attachments=ResumeRequestsAttachments(
            pic=Image(
                file_ext="file_ext_example",
                filename="filename_example",
                file=open('/path/to/file', 'rb'),
            ),
            cv=Document(
                file=open('/path/to/file', 'rb'),
                file_ext="file_ext_example",
                filename="filename_example",
            ),
        ),
    )
    try:
        # Add Resume
        api_response = api_instance.add_resume_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->add_resume_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'sync': False,
        'resume_id': "resume_id_example",
        'src_lang': "pt",
        'dst_lang': "pt",
    }
    body = FileItemRequest(
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
        attachments=ResumeRequestsAttachments(
            pic=Image(
                file_ext="file_ext_example",
                filename="filename_example",
                file=open('/path/to/file', 'rb'),
            ),
            cv=Document(
                file=open('/path/to/file', 'rb'),
                file_ext="file_ext_example",
                filename="filename_example",
            ),
        ),
    )
    try:
        # Add Resume
        api_response = api_instance.add_resume_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->add_resume_post: %s\n" % e)
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
[**FileItemRequest**](../../models/FileItemRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
sync | SyncSchema | | optional
resume_id | ResumeIdSchema | | optional
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional


# SyncSchema

Optional. Whether to wait for the resume processing or not.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Optional. Whether to wait for the resume processing or not. | if omitted the server will use the default value of False

# ResumeIdSchema

Optional. ID to use for the resume. Already existing IDs will cause a 409 error.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. ID to use for the resume. Already existing IDs will cause a 409 error. | 

# SrcLangSchema

Optional. Language in which the following *Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the detected *Attachment.CV.File* language is assumed as `src_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Language in which the following *Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the detected *Attachment.CV.File* language is assumed as &#x60;src_lang&#x60;. | must be one of ["pt", "it", "en", "de", "fr", "es", ] 

# DstLangSchema

Optional. Destination language in which the following *Data* entities are translated: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the input or detected `src_lang` is assumed as `dst_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Destination language in which the following *Data* entities are translated: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the input or detected &#x60;src_lang&#x60; is assumed as &#x60;dst_lang&#x60;. | must be one of ["pt", "it", "en", "de", "fr", "es", ] 

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
202 | [ApiResponseFor202](#add_resume_post.ApiResponseFor202) | Resume Successfully Queued
409 | [ApiResponseFor409](#add_resume_post.ApiResponseFor409) | Conflict
422 | [ApiResponseFor422](#add_resume_post.ApiResponseFor422) | Unprocessable Entity
415 | [ApiResponseFor415](#add_resume_post.ApiResponseFor415) | Unsupported Media Type
201 | [ApiResponseFor201](#add_resume_post.ApiResponseFor201) | Resume Successfully Added
200 | [ApiResponseFor200](#add_resume_post.ApiResponseFor200) | Resume Already Present

#### add_resume_post.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseItemIdResponse**](../../models/BaseItemIdResponse.md) |  | 


#### add_resume_post.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### add_resume_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### add_resume_post.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### add_resume_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseItemIdResponse**](../../models/BaseItemIdResponse.md) |  | 


#### add_resume_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ItemIdResponse**](../../models/ItemIdResponse.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_pic_delete**
<a name="delete_pic_delete"></a>
> DeleteItemResponse delete_pic_delete(indexnameresume_id)

Delete Pic

 This method deletes the profile picture associated with the resume *resume_id* and sets its profile picture to the default one. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_models_error_model import BaseModelsErrorModel
from inda_hr.model.delete_item_response import DeleteItemResponse
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
    api_instance = resume_management_api.ResumeManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    try:
        # Delete Pic
        api_response = api_instance.delete_pic_delete(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->delete_pic_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_pic_delete.ApiResponseFor200) | Picture Successfully Deleted.
404 | [ApiResponseFor404](#delete_pic_delete.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#delete_pic_delete.ApiResponseFor409) | Resume Currently Queued For Processing
422 | [ApiResponseFor422](#delete_pic_delete.ApiResponseFor422) | Resume Failed In Previous Task And Got Deleted

#### delete_pic_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteItemResponse**](../../models/DeleteItemResponse.md) |  | 


#### delete_pic_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### delete_pic_delete.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


#### delete_pic_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_resume_delete**
<a name="delete_resume_delete"></a>
> DeleteItemResponse delete_resume_delete(indexnameresume_id)

Delete Resume

 This method deletes the resume associated with *resume_id* from the index *indexname*. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_management_api
from inda_hr.model.base_models_error_model import BaseModelsErrorModel
from inda_hr.model.delete_item_response import DeleteItemResponse
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
    api_instance = resume_management_api.ResumeManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    try:
        # Delete Resume
        api_response = api_instance.delete_resume_delete(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->delete_resume_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_resume_delete.ApiResponseFor200) | Resume Successfully Deleted.
409 | [ApiResponseFor409](#delete_resume_delete.ApiResponseFor409) | Resume Currently Queued For Processing
422 | [ApiResponseFor422](#delete_resume_delete.ApiResponseFor422) | Resume Failed In Previous Task And Got Deleted

#### delete_resume_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteItemResponse**](../../models/DeleteItemResponse.md) |  | 


#### delete_resume_delete.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


#### delete_resume_delete.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_cv_get**
<a name="get_cv_get"></a>
> BinaryItemResponse get_cv_get(indexnameresume_id)

Get CV

 This method returns the Base64 encoding and the extension of the document associated  with the resume *resume_id*. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_models_error_model import BaseModelsErrorModel
from inda_hr.model.binary_item_response import BinaryItemResponse
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
    api_instance = resume_management_api.ResumeManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    try:
        # Get CV
        api_response = api_instance.get_cv_get(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->get_cv_get: %s\n" % e)
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
200 | [ApiResponseFor200](#get_cv_get.ApiResponseFor200) | Document Retrieved Successfully.
404 | [ApiResponseFor404](#get_cv_get.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#get_cv_get.ApiResponseFor409) | Resume Currently Queued For Processing
422 | [ApiResponseFor422](#get_cv_get.ApiResponseFor422) | Resume Failed In Previous Task And Got Deleted

#### get_cv_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BinaryItemResponse**](../../models/BinaryItemResponse.md) |  | 


#### get_cv_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_cv_get.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


#### get_cv_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_cv_text_get**
<a name="get_cv_text_get"></a>
> DocumentTextResponse get_cv_text_get(indexnameresume_id)

Get CV Text

 This method returns the text of the document associated with the resume *resume_id*. Note that this method merely returns the text, since the extraction has occurred during the add/update of the resume. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_models_error_model import BaseModelsErrorModel
from inda_hr.model.document_text_response import DocumentTextResponse
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
    api_instance = resume_management_api.ResumeManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    try:
        # Get CV Text
        api_response = api_instance.get_cv_text_get(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->get_cv_text_get: %s\n" % e)
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
200 | [ApiResponseFor200](#get_cv_text_get.ApiResponseFor200) | Text Retrieved Successfully.
404 | [ApiResponseFor404](#get_cv_text_get.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#get_cv_text_get.ApiResponseFor409) | Resume Currently Queued For Processing
422 | [ApiResponseFor422](#get_cv_text_get.ApiResponseFor422) | Resume Failed In Previous Task And Got Deleted

#### get_cv_text_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DocumentTextResponse**](../../models/DocumentTextResponse.md) |  | 


#### get_cv_text_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_cv_text_get.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


#### get_cv_text_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pic_get**
<a name="get_pic_get"></a>
> BinaryPicResponse get_pic_get(indexnameresume_id)

Get Pic

 This method returns the Base64 encoding and the extension of the profile picture associated with the resume *resume_id*. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.binary_pic_response import BinaryPicResponse
from inda_hr.model.base_models_error_model import BaseModelsErrorModel
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
    api_instance = resume_management_api.ResumeManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    try:
        # Get Pic
        api_response = api_instance.get_pic_get(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->get_pic_get: %s\n" % e)
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
200 | [ApiResponseFor200](#get_pic_get.ApiResponseFor200) | Picture Retrieved Successfully.
404 | [ApiResponseFor404](#get_pic_get.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#get_pic_get.ApiResponseFor409) | Resume Currently Queued For Processing
422 | [ApiResponseFor422](#get_pic_get.ApiResponseFor422) | Resume Failed In Previous Task And Got Deleted

#### get_pic_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BinaryPicResponse**](../../models/BinaryPicResponse.md) |  | 


#### get_pic_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_pic_get.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


#### get_pic_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_resume_get**
<a name="get_resume_get"></a>
> GetItemResponse get_resume_get(indexnameresume_id)

Get Resume

 This method returns the information related to the resume stored with id *resume_id* in the index *indexname*.  As reported in the schema below, the method has two different response schemas: + a *4xx* response is returned when the resume is still in the processing queue, if the processing failed, or if its *resume_id* has never been seen; + a *200* response is returned if the resume has been successfully processed and inserted in the index. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_models_error_model import BaseModelsErrorModel
from inda_hr.model.get_item_response import GetItemResponse
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
    api_instance = resume_management_api.ResumeManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    try:
        # Get Resume
        api_response = api_instance.get_resume_get(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->get_resume_get: %s\n" % e)
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
200 | [ApiResponseFor200](#get_resume_get.ApiResponseFor200) | Resume Retrieved Successfully
404 | [ApiResponseFor404](#get_resume_get.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#get_resume_get.ApiResponseFor409) | Resume Currently Queued For Processing
422 | [ApiResponseFor422](#get_resume_get.ApiResponseFor422) | Resume Failed In Previous Task And Got Deleted

#### get_resume_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetItemResponse**](../../models/GetItemResponse.md) |  | 


#### get_resume_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_resume_get.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


#### get_resume_get.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **patch_resume_patch**
<a name="patch_resume_patch"></a>
> PatchItemResponse patch_resume_patch(indexnameresume_idpatch_item_request)

Patch Resume

 This method updates the information related to the resume stored with id *resume_id*.  This method accepts an application/json body with the same structure as [Add Resume](https://api.inda.ai/hr/docs/v2/#operation/add_resume__POST), however in this case all fields are optional. Fields that contain differences between the corresponding original ones are substituted, while new fields are added. Bear in mind that lists are considered as singular value, therefore to modify an entry in a list it is necessary to insert the full list.  Note that this method only modifies the information; in order to change the attached file, please refer to the method [Update Resume](https://api.inda.ai/hr/docs/v2/#operation/update_resume__PUT).  Entities among skills, job (or position) titles and languages are automatically mapped by INDAto the adopted knowledge base, so that users can leverage on standardized values.Original values and entity IDs are available in *Details.RawValues* and *Details.Code*, respectively.Unrecognized items are ignored and not indexed, except for the *WorkExperiences.PositionTitle* entities.  Please note that, unlike the [Add Resume](https://api.inda.ai/hr/docs/v2/#operation/add_resume__POST), this function does not allowusers to set a `dst_lang`, as the one used at index time cannot be changed.It can be retrieved by accessing the *Metadata.Language* field. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_management_api
from inda_hr.model.patch_item_request import PatchItemRequest
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_models_error_model import BaseModelsErrorModel
from inda_hr.model.patch_item_response import PatchItemResponse
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
    api_instance = resume_management_api.ResumeManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
    }
    body = PatchItemRequest(
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
        attachments=OptionalCVAttachmentSlimDocument(
            cv=SlimDocument(
                filename="filename_example",
            ),
        ),
    )
    try:
        # Patch Resume
        api_response = api_instance.patch_resume_patch(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->patch_resume_patch: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
        'src_lang': "pt",
    }
    body = PatchItemRequest(
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
        attachments=OptionalCVAttachmentSlimDocument(
            cv=SlimDocument(
                filename="filename_example",
            ),
        ),
    )
    try:
        # Patch Resume
        api_response = api_instance.patch_resume_patch(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->patch_resume_patch: %s\n" % e)
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
[**PatchItemRequest**](../../models/PatchItemRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional


# SrcLangSchema

Optional. Language in which the following *Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the indexed *Attachment.CV.File* language is assumed as `src_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Language in which the following *Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the indexed *Attachment.CV.File* language is assumed as &#x60;src_lang&#x60;. | must be one of ["pt", "it", "en", "de", "fr", "es", ] 

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
200 | [ApiResponseFor200](#patch_resume_patch.ApiResponseFor200) | Resume Successfully Updated
404 | [ApiResponseFor404](#patch_resume_patch.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#patch_resume_patch.ApiResponseFor409) | Resume Currently Queued For Processing
422 | [ApiResponseFor422](#patch_resume_patch.ApiResponseFor422) | Resume Failed In Previous Task And Got Deleted

#### patch_resume_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchItemResponse**](../../models/PatchItemResponse.md) |  | 


#### patch_resume_patch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### patch_resume_patch.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


#### patch_resume_patch.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **resume_status_get**
<a name="resume_status_get"></a>
> ResumeResponsesStatus resume_status_get(indexnameresume_id)

Resume Status

 This method returns the status of a resume, which can be any of the following: + *Processing*: the resume is in INDA process queues; + *Available*: the resume is in the index and is available to the user; + *Duplicate*: the resume was a duplicate, refer to the indicated *DuplicateID* to retrieve the already  indexed one; + *Failed*: the processing of the input failed; + *Missing*: none of the previous; the *resume_id* may be wrong or corresponding to a deleted resume. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.resume_responses_status import ResumeResponsesStatus
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
    api_instance = resume_management_api.ResumeManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    try:
        # Resume Status
        api_response = api_instance.resume_status_get(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->resume_status_get: %s\n" % e)
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
200 | [ApiResponseFor200](#resume_status_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#resume_status_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#resume_status_get.ApiResponseFor422) | Validation Error

#### resume_status_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ResumeResponsesStatus**](../../models/ResumeResponsesStatus.md) |  | 


#### resume_status_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### resume_status_get.ApiResponseFor422
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

# **update_pic_put**
<a name="update_pic_put"></a>
> PatchItemResponse update_pic_put(indexnameresume_idupdate_pic_request)

Update Pic

 This method updates the profile picture associated with the resume *resume_id*.  The supported extensions are <code style='color: #333333; opacity: 0.9'>png</code>, <code style='color: #333333; opacity: 0.9'>jpg</code>, <code style='color: #333333; opacity: 0.9'>jpeg</code>. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_models_error_model import BaseModelsErrorModel
from inda_hr.model.patch_item_response import PatchItemResponse
from inda_hr.model.update_pic_request import UpdatePicRequest
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
    api_instance = resume_management_api.ResumeManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    body = UpdatePicRequest(
        attachments=PicAttachmentImage(
            pic=Image(
                file_ext="file_ext_example",
                filename="filename_example",
                file=open('/path/to/file', 'rb'),
            ),
        ),
    )
    try:
        # Update Pic
        api_response = api_instance.update_pic_put(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->update_pic_put: %s\n" % e)
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
[**UpdatePicRequest**](../../models/UpdatePicRequest.md) |  | 


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
200 | [ApiResponseFor200](#update_pic_put.ApiResponseFor200) | Picture Successfully Updated.
404 | [ApiResponseFor404](#update_pic_put.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#update_pic_put.ApiResponseFor409) | Resume Currently Queued For Processing
422 | [ApiResponseFor422](#update_pic_put.ApiResponseFor422) | Resume Failed In Previous Task And Got Deleted

#### update_pic_put.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchItemResponse**](../../models/PatchItemResponse.md) |  | 


#### update_pic_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### update_pic_put.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


#### update_pic_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_resume_put**
<a name="update_resume_put"></a>
> BaseItemIdResponse update_resume_put(indexnameresume_idupdate_item_request)

Update Resume

 This method updates both the information and the CV file (*Data.Attachments.CV.File*) related to the resume stored with  id *resume_id*.  This method manages to update the structured data in the same way [Patch Resume](https://api.inda.ai/hr/docs/v2/#operation/patch_resume__PATCH) does as well as  updating the corresponding CV file. It verifies if the file is duplicate with respect to the data already present into the *indexname*. If it finds a  possible duplicate with the same *resume_id* (if one is reuploading the same CV file) it proceeds updating the  structured data, skipping the file update, while it manages to completely delete the item *resume_id* if the file is  found on *indexname* but associated with a resume with different *resume_id*.  The method will enqueue the task and immediately return a response in an asynchronous fashion. In order to verify the  *resume_id* status one could rely on: + [Resume Status](https://api.inda.ai/hr/docs/v2/#operation/resume_status__GET) + [Get Failures](https://api.inda.ai/hr/docs/v2/#operation/get_failures__GET)  Entities among skills, job (or position) titles and languages are automatically mapped by INDAto the adopted knowledge base, so that users can leverage on standardized values.Original values and entity IDs are available in *Details.RawValues* and *Details.Code*, respectively.Unrecognized items are ignored and not indexed, except for the *WorkExperiences.PositionTitle* entities.  Please note that, unlike the [Add Resume](https://api.inda.ai/hr/docs/v2/#operation/add_resume__POST), this function does not allowusers to set a `dst_lang`, as the one used at index time cannot be changed.It can be retrieved by accessing the *Metadata.Language* field. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_models_error_model import BaseModelsErrorModel
from inda_hr.model.base_item_id_response import BaseItemIdResponse
from inda_hr.model.update_item_request import UpdateItemRequest
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
    api_instance = resume_management_api.ResumeManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
    }
    body = UpdateItemRequest(
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
        attachments=CVAttachmentDocument(
            cv=Document(
                file=open('/path/to/file', 'rb'),
                file_ext="file_ext_example",
                filename="filename_example",
            ),
        ),
    )
    try:
        # Update Resume
        api_response = api_instance.update_resume_put(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->update_resume_put: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
        'src_lang': "pt",
    }
    body = UpdateItemRequest(
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
        attachments=CVAttachmentDocument(
            cv=Document(
                file=open('/path/to/file', 'rb'),
                file_ext="file_ext_example",
                filename="filename_example",
            ),
        ),
    )
    try:
        # Update Resume
        api_response = api_instance.update_resume_put(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeManagementApi->update_resume_put: %s\n" % e)
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
[**UpdateItemRequest**](../../models/UpdateItemRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional


# SrcLangSchema

Optional. Language in which the following *Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the detected *Attachment.CV.File* language is assumed as `src_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Language in which the following *Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the detected *Attachment.CV.File* language is assumed as &#x60;src_lang&#x60;. | must be one of ["pt", "it", "en", "de", "fr", "es", ] 

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
202 | [ApiResponseFor202](#update_resume_put.ApiResponseFor202) | Resume Successfully Queued For Updating
400 | [ApiResponseFor400](#update_resume_put.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#update_resume_put.ApiResponseFor404) | Not Found
409 | [ApiResponseFor409](#update_resume_put.ApiResponseFor409) | Resume Currently Queued For Processing
422 | [ApiResponseFor422](#update_resume_put.ApiResponseFor422) | Resume Failed In Previous Task And Got Deleted

#### update_resume_put.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseItemIdResponse**](../../models/BaseItemIdResponse.md) |  | 


#### update_resume_put.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### update_resume_put.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### update_resume_put.ApiResponseFor409
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor409ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor409ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


#### update_resume_put.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseModelsErrorModel**](../../models/BaseModelsErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

