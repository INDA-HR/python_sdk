# inda_hr.ApplicationManagementApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_application_post**](ApplicationManagementApi.md#add_application_post) | **POST** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/ | Add Application
[**add_application_stage_post**](ApplicationManagementApi.md#add_application_stage_post) | **POST** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/hiring-pipeline/stage/ | Add Application Stage
[**application_status_get**](ApplicationManagementApi.md#application_status_get) | **GET** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/status/ | Application Status
[**apply_post**](ApplicationManagementApi.md#apply_post) | **POST** /hr/v2/index/{indexname}/jobad/{jobad_id}/apply/ | Apply
[**delete_applicants_delete**](ApplicationManagementApi.md#delete_applicants_delete) | **DELETE** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resumes/ | Delete Applicants
[**delete_application_delete**](ApplicationManagementApi.md#delete_application_delete) | **DELETE** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/ | Delete Application
[**delete_application_stage_delete**](ApplicationManagementApi.md#delete_application_stage_delete) | **DELETE** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/hiring-pipeline/stage/ | Delete Application Stage
[**delete_applications_delete**](ApplicationManagementApi.md#delete_applications_delete) | **DELETE** /hr/v2/index/{indexname}/resume/{resume_id}/applications/jobads/ | Delete Applications
[**get_applicants_get**](ApplicationManagementApi.md#get_applicants_get) | **GET** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resumes/ | Get Applicants
[**get_application_get**](ApplicationManagementApi.md#get_application_get) | **GET** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/ | Get Application
[**get_applications_get**](ApplicationManagementApi.md#get_applications_get) | **GET** /hr/v2/index/{indexname}/resume/{resume_id}/applications/jobads/ | Get Applications
[**patch_application_patch**](ApplicationManagementApi.md#patch_application_patch) | **PATCH** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/ | Patch Application


# **add_application_post**
> ApplicationIDResponse add_application_post(indexname, jobad_id, resume_id)

Add Application

 This method stores on *indexname* the application made by the applicant *resume_id* to the job advertisement *jobad_id*.  It is assumed that both the resume and the job advertisement involved have been previously added to *indexname* by  the appropriate methods.  On the right, we provide an example of input structure; further details are available in dedicated sections.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_application_request import BaseApplicationRequest
from inda_hr.model.application_id_response import ApplicationIDResponse
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    jobad_id = JobadId(None) # JobadId | 
    resume_id = "resume_id_example" # str | 
    base_application_request = BaseApplicationRequest(
        data=ApplicationCommonData(
            objective=BaseBenefitsValueModelStrictStr(
                value="value_example",
            ),
            professional_summary=BaseBenefitsValueModelStrictStr(
                value="value_example",
            ),
            desired_employment=ResumeEmployment(
                code=BaseBenefitsValueModelStrictStr(
                    value="value_example",
                ),
                category=BaseBenefitsValueModelStrictStr(
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
                    BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ],
            ),
            desired_contracts=[
                ResumeContract(
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
            ],
            desired_salary=ResumeSalary(
                amount=RangeFloat(
                    range=Range(None),
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
            desired_benefits=[
                ResumeBenefit(
                    value="value_example",
                ),
            ],
            desired_locations=[
                BaseLocationsLocation(
                    city=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    country=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    geo_coordinates=ValueModelGeoLocation(
                        value=GeoLocation(
                            lat=-90.0,
                            lon=-180.0,
                        ),
                    ),
                    country_code=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    postal_code=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    street_address=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    county=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    region=BaseBenefitsValueModelStrictStr(
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
                relocation_date=RangeDatetime(
                    range=Range1(None),
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
                frequency=Frequency1(None),
            ),
            job_shift=JobShift(
                details=BoolBaseModel(
                    is_possible=True,
                    is_mandatory=True,
                ),
                type=JobShiftType(
                    value="DAY_SHIFT",
                ),
                frequency=Frequency2(None),
            ),
            origin_links=[
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
        hiring_details=HiringDetails(
            application_date=dateutil_parser('1970-01-01').date(),
            hiring_date=dateutil_parser('1970-01-01').date(),
            hiring_pipeline=[
                HiringPipelineStage(
                    date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                    description="description_example",
                    status="APPLIED",
                ),
            ],
        ),
    ) # BaseApplicationRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add Application
        api_response = api_instance.add_application_post(indexname, jobad_id, resume_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->add_application_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add Application
        api_response = api_instance.add_application_post(indexname, jobad_id, resume_id, base_application_request=base_application_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->add_application_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **JobadId**|  |
 **resume_id** | **str**|  |
 **base_application_request** | [**BaseApplicationRequest**](BaseApplicationRequest.md)|  | [optional]

### Return type

[**ApplicationIDResponse**](ApplicationIDResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Application Successfully Added |  -  |
**400** | Bad Request |  -  |
**200** | Application Already Present |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_application_stage_post**
> ApplicationIDResponse add_application_stage_post(indexname, resume_id, jobad_id, application_status_request)

Add Application Stage

 This method updates the applicant hiring pipeline by adding a new stage according to the requested values.  The supported stages for the hiring pipelines are: <code style='color: #333333; opacity: 0.9'>APPLIED</code>, <code style='color: #333333; opacity: 0.9'>SOURCED</code>, <code style='color: #333333; opacity: 0.9'>SCREEN</code>, <code style='color: #333333; opacity: 0.9'>INTERVIEW</code>, <code style='color: #333333; opacity: 0.9'>EVALUATION</code>, <code style='color: #333333; opacity: 0.9'>OFFER</code>, <code style='color: #333333; opacity: 0.9'>HIRED</code>, <code style='color: #333333; opacity: 0.9'>DISQUALIFIED</code>.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.application_status_request import ApplicationStatusRequest
from inda_hr.model.application_id_response import ApplicationIDResponse
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    resume_id = "resume_id_example" # str | 
    jobad_id = JobadId(None) # JobadId | 
    application_status_request = ApplicationStatusRequest(
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        description="description_example",
        status="APPLIED",
    ) # ApplicationStatusRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Add Application Stage
        api_response = api_instance.add_application_stage_post(indexname, resume_id, jobad_id, application_status_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->add_application_stage_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **resume_id** | **str**|  |
 **jobad_id** | **JobadId**|  |
 **application_status_request** | [**ApplicationStatusRequest**](ApplicationStatusRequest.md)|  |

### Return type

[**ApplicationIDResponse**](ApplicationIDResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Hiring Pipeline Stage Successfully Added |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **application_status_get**
> ApplicationResponsesStatus application_status_get(indexname, jobad_id, resume_id)

Application Status

 This method returns the status of an application, which can be any of the following: + *Processing*: the application is in INDA process queue; + *Available*: the application is in the index and is available to the user; + *Duplicate*: the application was a duplicate, refer to the indicated pair  (*ResumeID*, *JobAdID*) to retrieve the already indexed one; + *Failed*: the processing of the input failed; + *Missing*: none of the previous; the pair (*ResumeID*, *JobAdID*) may be wrong or corresponding to a deleted application. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.application_responses_status import ApplicationResponsesStatus
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    jobad_id = JobadId(None) # JobadId | 
    resume_id = "resume_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Application Status
        api_response = api_instance.application_status_get(indexname, jobad_id, resume_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->application_status_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **JobadId**|  |
 **resume_id** | **str**|  |

### Return type

[**ApplicationResponsesStatus**](ApplicationResponsesStatus.md)

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **apply_post**
> ApplicationIDResponse apply_post(indexname, jobad_id, apply_item_request)

Apply

 This method adds a candidate resume to *indexname* and registers their application to *jobad_id*.  In an asynchronous fashion, the resume to be processed is added to the server's task queue and the assigned *ResumeID*  is returned immediately; when its processing is successfully completed and the resume is effectively added to  *indexname*, the pipeline continues with the candidate request to apply to the job advertisement identified by  *jobad_id*.  Under the hood, this method performs: + [Add Resume](https://api.inda.ai/hr/docs/v2/#operation/add_resume__POST)  + [Add Application](https://api.inda.ai/hr/docs/v2/#operation/add_application__POST)  Note that the document may not successfully conclude the processing pipeline (e.g., it may be discarded because duplicate of one of the documents already present in the *indexname*), and thus it may not be actually added to the index. The same may happen while processing the application request.  In order to verify the resume and the application status, the user can use the *ResumeID* and the *JobAdID* through  the following methods: + [Resume Status](https://api.inda.ai/hr/docs/v2/#operation/resume_status__GET) + [Application Status](https://api.inda.ai/hr/docs/v2/#operation/application_status__GET) + [Get Failures](https://api.inda.ai/hr/docs/v2/#operation/get_failures__GET)  On the right, we provide an example of input structure; further details are available in dedicated sections.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.apply_item_request import ApplyItemRequest
from inda_hr.model.application_id_response import ApplicationIDResponse
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    jobad_id = JobadId(None) # JobadId | 
    apply_item_request = ApplyItemRequest(
        application=BaseApplicationRequest(
            data=ApplicationCommonData(
                objective=BaseBenefitsValueModelStrictStr(
                    value="value_example",
                ),
                professional_summary=BaseBenefitsValueModelStrictStr(
                    value="value_example",
                ),
                desired_employment=ResumeEmployment(
                    code=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    category=BaseBenefitsValueModelStrictStr(
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
                        BaseBenefitsValueModelStrictStr(
                            value="value_example",
                        ),
                    ],
                ),
                desired_contracts=[
                    ResumeContract(
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
                ],
                desired_salary=ResumeSalary(
                    amount=RangeFloat(
                        range=Range(None),
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
                desired_benefits=[
                    ResumeBenefit(
                        value="value_example",
                    ),
                ],
                desired_locations=[
                    BaseLocationsLocation(
                        city=BaseBenefitsValueModelStrictStr(
                            value="value_example",
                        ),
                        country=BaseBenefitsValueModelStrictStr(
                            value="value_example",
                        ),
                        geo_coordinates=ValueModelGeoLocation(
                            value=GeoLocation(
                                lat=-90.0,
                                lon=-180.0,
                            ),
                        ),
                        country_code=BaseBenefitsValueModelStrictStr(
                            value="value_example",
                        ),
                        postal_code=BaseBenefitsValueModelStrictStr(
                            value="value_example",
                        ),
                        street_address=BaseBenefitsValueModelStrictStr(
                            value="value_example",
                        ),
                        county=BaseBenefitsValueModelStrictStr(
                            value="value_example",
                        ),
                        region=BaseBenefitsValueModelStrictStr(
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
                    relocation_date=RangeDatetime(
                        range=Range1(None),
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
                    frequency=Frequency1(None),
                ),
                job_shift=JobShift(
                    details=BoolBaseModel(
                        is_possible=True,
                        is_mandatory=True,
                    ),
                    type=JobShiftType(
                        value="DAY_SHIFT",
                    ),
                    frequency=Frequency2(None),
                ),
                origin_links=[
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
            hiring_details=HiringDetails(
                application_date=dateutil_parser('1970-01-01').date(),
                hiring_date=dateutil_parser('1970-01-01').date(),
                hiring_pipeline=[
                    HiringPipelineStage(
                        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        description="description_example",
                        status="APPLIED",
                    ),
                ],
            ),
        ),
        resume=FileItemRequest(
            data=ResumeCommonData(
                job_title=OptionalResumeJobTitle(
                    details=OptionalResumeJobTitleDetails(
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
                            ),
                            value="value_example",
                        ),
                        given_name=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        middle_names=[
                            BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ],
                        family_name=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        suffix=ResumePersonNameSuffix(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        formatted_name=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                    ),
                    birthdate=Date(
                        details=BaseDetails(
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
                        ),
                        value=dateutil_parser('1970-01-01').date(),
                    ),
                    age=Age(
                        details=BaseDetails(
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
                        ),
                        value=1,
                    ),
                    nationalities=[
                        Nationality(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                    ],
                    citizenships=[
                        Citizenship(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                    ],
                    gender=Gender(
                        details=BaseDetails(
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
                        ),
                        value="value_example",
                    ),
                    disability=Disability(
                        disability_level_code=DisabilityLevelCode(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        disability_summary=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                    ),
                    protected_groups=[
                        ProtectedGroup(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                    ],
                    marital_status=MaritalStatus(
                        details=BaseDetails(
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
                        ),
                        value="value_example",
                    ),
                    number_of_children=NumberOfChildren(
                        details=BaseDetails(
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
                        ),
                        value=1,
                    ),
                ),
                contact_info=ResumeContactInfoContactInfo(
                    phone_numbers=[
                        ResumePhoneNumbersPhoneNumber(
                            number=ResumePhoneNumbersNumber(
                                details=BaseDetails(
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
                                ),
                                value=OptionalPhoneNumber(
                                    country_code="AW",
                                    country_dialling="country_dialling_example",
                                    dial_number="dial_number_example",
                                ),
                            ),
                            label=ResumePhoneNumbersPhoneLabel(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                    ],
                    email_addresses=[
                        ResumeEmailAddressEmailAddress(
                            address=ResumeEmailAddressAddress(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            label=ResumeEmailAddressEmailLabel(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                    ],
                    links=[
                        ResumeLinkLink(
                            url=ResumeLinkURL(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            label=ResumeLinkLinkLabel(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                    ],
                ),
                person_location=PersonLocation(
                    current_location=ResumeLocationsLocation(
                        city=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        country=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
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
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        postal_code=Text(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        street_address=Text(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        county=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        region=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                    ),
                    permanent_location=ResumeLocationsLocation(
                        city=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        country=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
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
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        postal_code=Text(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        street_address=Text(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        county=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        region=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                    ),
                ),
                headline=Text(
                    details=BaseDetails(
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
                    ),
                    value="value_example",
                ),
                education_experiences=[
                    EducationExperience(
                        duration=BaseDuration(
                            details=SlimBaseDetails(
                                is_validated=False,
                            ),
                            value=1,
                        ),
                        education_title=Text(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        field_of_study=Text(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        final_grade=FinalGrade(
                            details=BaseDetails(
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
                            ),
                            value=FinalGradeValue(
                                score_text="score_text_example",
                                score_numeric=1,
                            ),
                        ),
                        education_level_code=ResumeEducationExperiencesEducationLevelCode(
                            details=SlimBaseDetails(
                                is_validated=False,
                            ),
                            value=EducationLevelCodeValue(
                                eqf=1,
                            ),
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        start_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        end_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        ongoing=Ongoing(
                            details=SlimBaseDetails(
                                is_validated=False,
                            ),
                            value=True,
                        ),
                        location=ResumeLocationsLocation(
                            city=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            country=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
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
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            postal_code=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            street_address=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            county=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            region=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                        organization=Organization(
                            organization_name=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            department=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            location=ResumeLocationsLocation(
                                city=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                country=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
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
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                postal_code=Text(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                street_address=Text(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                county=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                region=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ),
                            link=ResumeLinkLink(
                                url=ResumeLinkURL(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                label=ResumeLinkLinkLabel(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ),
                            id=ID(
                                details=OptionalEntityBaseDetails(
                                    is_validated=False,
                                    entity_type="entity_type_example",
                                ),
                                value="value_example",
                            ),
                        ),
                        courses=[
                            Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ],
                        id="id_example",
                    ),
                ],
                work_experiences=[
                    WorkExperience(
                        seniority=BaseSeniority(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        duration=BaseDuration(
                            details=SlimBaseDetails(
                                is_validated=False,
                            ),
                            value=1,
                        ),
                        position_title=OptionalResumeJobTitle(
                            details=OptionalResumeJobTitleDetails(
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
                                score=0.75,
                                code=ResumeJobTitleCode(
                                    key="key_example",
                                ),
                            ),
                            value="value_example",
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        start_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        end_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        ongoing=Ongoing(
                            details=SlimBaseDetails(
                                is_validated=False,
                            ),
                            value=True,
                        ),
                        location=ResumeLocationsLocation(
                            city=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            country=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
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
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            postal_code=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            street_address=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            county=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            region=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                        remote_working=RemoteWorking(
                            type=ResumeRemoteWorkingType(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            frequency=ResumeRemoteWorkingFrequencyRange(
                                details=BaseDetails(
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
                                ),
                                range=Range(None),
                            ),
                        ),
                        employer=Organization(
                            organization_name=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            department=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            location=ResumeLocationsLocation(
                                city=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                country=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
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
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                postal_code=Text(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                street_address=Text(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                county=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                region=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ),
                            link=ResumeLinkLink(
                                url=ResumeLinkURL(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                label=ResumeLinkLinkLabel(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ),
                            id=ID(
                                details=OptionalEntityBaseDetails(
                                    is_validated=False,
                                    entity_type="entity_type_example",
                                ),
                                value="value_example",
                            ),
                        ),
                        industries=[
                            ResumeWorkExperiencesIndustry(
                                details=IndustryDetails(
                                    is_validated=False,
                                ),
                                value="value_example",
                            ),
                        ],
                        skills=[
                            OptionalResumeSkill(
                                details=OptionalResumeSkillDetails(
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
                                    category="hard",
                                    code=ResumeSkillCode(
                                        key="key_example",
                                    ),
                                    score=0.75,
                                ),
                                value="value_example",
                            ),
                        ],
                        id="id_example",
                    ),
                ],
                cover_letter=Text(
                    details=BaseDetails(
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
                    ),
                    value="value_example",
                ),
                references=[
                    Reference(
                        person_name=ResumePersonNamePersonName(
                            prefix=ResumePersonNamePrefix(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            given_name=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            middle_names=[
                                BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ],
                            family_name=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            suffix=ResumePersonNameSuffix(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            formatted_name=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                        contact_info=ResumeContactInfoContactInfo(
                            phone_numbers=[
                                ResumePhoneNumbersPhoneNumber(
                                    number=ResumePhoneNumbersNumber(
                                        details=BaseDetails(
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
                                        ),
                                        value=OptionalPhoneNumber(
                                            country_code="AW",
                                            country_dialling="country_dialling_example",
                                            dial_number="dial_number_example",
                                        ),
                                    ),
                                    label=ResumePhoneNumbersPhoneLabel(
                                        details=BaseDetails(
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
                                        ),
                                        value="value_example",
                                    ),
                                ),
                            ],
                            email_addresses=[
                                ResumeEmailAddressEmailAddress(
                                    address=ResumeEmailAddressAddress(
                                        details=BaseDetails(
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
                                        ),
                                        value="value_example",
                                    ),
                                    label=ResumeEmailAddressEmailLabel(
                                        details=BaseDetails(
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
                                        ),
                                        value="value_example",
                                    ),
                                ),
                            ],
                            links=[
                                ResumeLinkLink(
                                    url=ResumeLinkURL(
                                        details=BaseDetails(
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
                                        ),
                                        value="value_example",
                                    ),
                                    label=ResumeLinkLinkLabel(
                                        details=BaseDetails(
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
                                        ),
                                        value="value_example",
                                    ),
                                ),
                            ],
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                    ),
                ],
                profile_summary=ProfileSummary(
                    loyalty_score=ValidatedFloatValueModel(
                        details=SlimBaseDetails(
                            is_validated=False,
                        ),
                        value=3.14,
                    ),
                    work_experiences_count=ValidatedIntegerValueModel(
                        details=SlimBaseDetails(
                            is_validated=False,
                        ),
                        value=1,
                    ),
                    work_experiences_average_duration=ValidatedIntegerValueModel(
                        details=SlimBaseDetails(
                            is_validated=False,
                        ),
                        value=1,
                    ),
                    work_experiences_total_duration=ValidatedIntegerValueModel(
                        details=SlimBaseDetails(
                            is_validated=False,
                        ),
                        value=1,
                    ),
                    highest_seniority_level_code=SeniorityLevelCode(
                        details=BaseDetails(
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
                        ),
                        value="value_example",
                    ),
                    education_experiences_count=ValidatedIntegerValueModel(
                        details=SlimBaseDetails(
                            is_validated=False,
                        ),
                        value=1,
                    ),
                    education_experiences_average_duration=ValidatedIntegerValueModel(
                        details=SlimBaseDetails(
                            is_validated=False,
                        ),
                        value=1,
                    ),
                    education_experiences_total_duration=ValidatedIntegerValueModel(
                        details=SlimBaseDetails(
                            is_validated=False,
                        ),
                        value=1,
                    ),
                    highest_education_title=HighestEducationTitle(
                        details=SlimBaseDetails(
                            is_validated=False,
                        ),
                        value="value_example",
                    ),
                    highest_education_level_code=ResumeEducationExperiencesEducationLevelCode(
                        details=SlimBaseDetails(
                            is_validated=False,
                        ),
                        value=EducationLevelCodeValue(
                            eqf=1,
                        ),
                    ),
                    objective=Description(
                        details=BaseDetails(
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
                        ),
                        value="value_example",
                    ),
                    personal_description=Description(
                        details=BaseDetails(
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
                        ),
                        value="value_example",
                    ),
                ),
                skills=[
                    OptionalResumeSkill(
                        details=OptionalResumeSkillDetails(
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
                            category="hard",
                            code=ResumeSkillCode(
                                key="key_example",
                            ),
                            score=0.75,
                        ),
                        value="value_example",
                    ),
                ],
                job_titles=[
                    OptionalResumeJobTitle(
                        details=OptionalResumeJobTitleDetails(
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
                            score=0.75,
                            code=ResumeJobTitleCode(
                                key="key_example",
                            ),
                        ),
                        value="value_example",
                    ),
                ],
                languages=[
                    OptionalResumeLanguage(
                        details=OptionalResumeLanguageDetails(
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
                    ),
                ],
                certifications=[
                    Certification(
                        certification_name=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        first_issued_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        issuing_authority=Organization(
                            organization_name=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            department=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            location=ResumeLocationsLocation(
                                city=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                country=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
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
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                postal_code=Text(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                street_address=Text(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                county=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                region=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ),
                            link=ResumeLinkLink(
                                url=ResumeLinkURL(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                label=ResumeLinkLinkLabel(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ),
                            id=ID(
                                details=OptionalEntityBaseDetails(
                                    is_validated=False,
                                    entity_type="entity_type_example",
                                ),
                                value="value_example",
                            ),
                        ),
                        url=ResumeLinkURL(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                    ),
                ],
                publications=[
                    Publication(
                        title=Title(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        doi=Text(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        year=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        link=ResumeLinkLink(
                            url=ResumeLinkURL(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            label=ResumeLinkLinkLabel(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                    ),
                ],
                awards=[
                    Award(
                        title=Title(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        year=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        awarder=Organization(
                            organization_name=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            department=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            location=ResumeLocationsLocation(
                                city=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                country=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
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
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                postal_code=Text(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                street_address=Text(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                county=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                region=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ),
                            link=ResumeLinkLink(
                                url=ResumeLinkURL(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                label=ResumeLinkLinkLabel(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ),
                            id=ID(
                                details=OptionalEntityBaseDetails(
                                    is_validated=False,
                                    entity_type="entity_type_example",
                                ),
                                value="value_example",
                            ),
                        ),
                    ),
                ],
                projects=[
                    Project(
                        project_name=BaseModelsName(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        roles=[
                            Role(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ],
                        keywords=[
                            Keyword(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ],
                        start_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        end_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        ongoing=Ongoing(
                            details=SlimBaseDetails(
                                is_validated=False,
                            ),
                            value=True,
                        ),
                        link=ResumeLinkLink(
                            url=ResumeLinkURL(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            label=ResumeLinkLinkLabel(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                    ),
                ],
                achievements=[
                    Achievement(
                        title=Title(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        year=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        link=ResumeLinkLink(
                            url=ResumeLinkURL(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            label=ResumeLinkLinkLabel(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                    ),
                ],
                patents=[
                    Patent(
                        patent_title=Title(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        patent_id=Text(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        patent_status=PatentStatus(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        inventor_names=[
                            ResumePersonNamePersonName(
                                prefix=ResumePersonNamePrefix(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                given_name=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                middle_names=[
                                    BaseModelsName(
                                        details=BaseDetails(
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
                                        ),
                                        value="value_example",
                                    ),
                                ],
                                family_name=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                suffix=ResumePersonNameSuffix(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                formatted_name=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ),
                        ],
                        issuing_authority=Organization(
                            organization_name=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            department=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            location=ResumeLocationsLocation(
                                city=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                country=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
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
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                postal_code=Text(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                street_address=Text(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                county=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                region=BaseModelsName(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ),
                            link=ResumeLinkLink(
                                url=ResumeLinkURL(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                                label=ResumeLinkLinkLabel(
                                    details=BaseDetails(
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
                                    ),
                                    value="value_example",
                                ),
                            ),
                            id=ID(
                                details=OptionalEntityBaseDetails(
                                    is_validated=False,
                                    entity_type="entity_type_example",
                                ),
                                value="value_example",
                            ),
                        ),
                    ),
                ],
                hobbies_and_interests=[
                    Text(
                        details=BaseDetails(
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
                        ),
                        value="value_example",
                    ),
                ],
                licenses=[
                    License(
                        license_type=LicenseType(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        license_type_code=DrivingLicenseTypeCode(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        first_issued_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        expiry_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                    ),
                ],
                volunteering=[
                    Event(
                        title=Title(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        start_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        end_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        ongoing=Ongoing(
                            details=SlimBaseDetails(
                                is_validated=False,
                            ),
                            value=True,
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        location=ResumeLocationsLocation(
                            city=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            country=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
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
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            postal_code=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            street_address=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            county=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            region=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                        link=ResumeLinkLink(
                            url=ResumeLinkURL(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            label=ResumeLinkLinkLabel(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                    ),
                ],
                conference_and_seminars=[
                    Event(
                        title=Title(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        start_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        end_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        ongoing=Ongoing(
                            details=SlimBaseDetails(
                                is_validated=False,
                            ),
                            value=True,
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        location=ResumeLocationsLocation(
                            city=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            country=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
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
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            postal_code=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            street_address=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            county=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            region=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                        link=ResumeLinkLink(
                            url=ResumeLinkURL(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            label=ResumeLinkLinkLabel(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                    ),
                ],
                military_history=[
                    MilitaryService(
                        military_branch=Title(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        military_division=Title(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        starting_rank=Title(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        current_or_ending_rank=Title(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        location=ResumeLocationsLocation(
                            city=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            country=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
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
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            postal_code=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            street_address=Text(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            county=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            region=BaseModelsName(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                        start_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        end_date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        ongoing=Ongoing(
                            details=SlimBaseDetails(
                                is_validated=False,
                            ),
                            value=True,
                        ),
                    ),
                ],
                others=[
                    Other(
                        title=Title(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        date=Date(
                            details=BaseDetails(
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
                            ),
                            value=dateutil_parser('1970-01-01').date(),
                        ),
                        description=Description(
                            details=BaseDetails(
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
                            ),
                            value="value_example",
                        ),
                        link=ResumeLinkLink(
                            url=ResumeLinkURL(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                            label=ResumeLinkLinkLabel(
                                details=BaseDetails(
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
                                ),
                                value="value_example",
                            ),
                        ),
                    ),
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
        ),
    ) # ApplyItemRequest | 
    resume_id = "resume_id_example" # str |  (optional)
    src_lang = "pt" # str | Optional. Language in which the following *Resume.Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the detected *Attachment.CV.File* language is assumed as `src_lang`. (optional)
    dst_lang = "pt" # str | Optional. Destination language in which the following *Resume.Data* entities are translated: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the input or detected `src_lang` is assumed as `dst_lang`. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Apply
        api_response = api_instance.apply_post(indexname, jobad_id, apply_item_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->apply_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Apply
        api_response = api_instance.apply_post(indexname, jobad_id, apply_item_request, resume_id=resume_id, src_lang=src_lang, dst_lang=dst_lang)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->apply_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **JobadId**|  |
 **apply_item_request** | [**ApplyItemRequest**](ApplyItemRequest.md)|  |
 **resume_id** | **str**|  | [optional]
 **src_lang** | **str**| Optional. Language in which the following *Resume.Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the detected *Attachment.CV.File* language is assumed as &#x60;src_lang&#x60;. | [optional]
 **dst_lang** | **str**| Optional. Destination language in which the following *Resume.Data* entities are translated: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the input or detected &#x60;src_lang&#x60; is assumed as &#x60;dst_lang&#x60;. | [optional]

### Return type

[**ApplicationIDResponse**](ApplicationIDResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Application Successfully Queued |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_applicants_delete**
> DeleteCandidatesResponse delete_applicants_delete(indexname, jobad_id)

Delete Applicants

 This method removes all the applicants associated with *jobad_id* from the index *indexname*.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.delete_candidates_response import DeleteCandidatesResponse
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    jobad_id = JobadId(None) # JobadId | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Applicants
        api_response = api_instance.delete_applicants_delete(indexname, jobad_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->delete_applicants_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **JobadId**|  |

### Return type

[**DeleteCandidatesResponse**](DeleteCandidatesResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applicants Successfully Deleted |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_delete**
> DeleteApplicationResponse delete_application_delete(indexname, jobad_id, resume_id)

Delete Application

 This method removes the application associated with *jobad_id* and *resume_id* from the index *indexname*.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.delete_application_response import DeleteApplicationResponse
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    jobad_id = JobadId(None) # JobadId | 
    resume_id = "resume_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Application
        api_response = api_instance.delete_application_delete(indexname, jobad_id, resume_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->delete_application_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **JobadId**|  |
 **resume_id** | **str**|  |

### Return type

[**DeleteApplicationResponse**](DeleteApplicationResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application Successfully Deleted |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_application_stage_delete**
> ApplicationIDResponse delete_application_stage_delete(indexname, jobad_id, resume_id, status)

Delete Application Stage

 This method updates the applicant hiring pipeline by deleting a previously stored stage according to the requested  values.  The supported stages for the hiring pipelines are: <code style='color: #333333; opacity: 0.9'>APPLIED</code>, <code style='color: #333333; opacity: 0.9'>SOURCED</code>, <code style='color: #333333; opacity: 0.9'>SCREEN</code>, <code style='color: #333333; opacity: 0.9'>INTERVIEW</code>, <code style='color: #333333; opacity: 0.9'>EVALUATION</code>, <code style='color: #333333; opacity: 0.9'>OFFER</code>, <code style='color: #333333; opacity: 0.9'>HIRED</code>, <code style='color: #333333; opacity: 0.9'>DISQUALIFIED</code>.  Note that all the stages matching *status* and *date* (if present) query parameters will be removed from the  hiring pipeline.   

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.application_id_response import ApplicationIDResponse
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    jobad_id = JobadId(None) # JobadId | 
    resume_id = "resume_id_example" # str | 
    status = "APPLIED" # str | The status describes the hiring pipeline level. The statuses are: <code style='color: #333333; opacity: 0.9'>APPLIED</code>, <code style='color: #333333; opacity: 0.9'>SOURCED</code>, <code style='color: #333333; opacity: 0.9'>SCREEN</code>, <code style='color: #333333; opacity: 0.9'>INTERVIEW</code>, <code style='color: #333333; opacity: 0.9'>EVALUATION</code>, <code style='color: #333333; opacity: 0.9'>OFFER</code>, <code style='color: #333333; opacity: 0.9'>HIRED</code>, <code style='color: #333333; opacity: 0.9'>DISQUALIFIED</code>.
    date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | The date in which the status changed. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete Application Stage
        api_response = api_instance.delete_application_stage_delete(indexname, jobad_id, resume_id, status)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->delete_application_stage_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete Application Stage
        api_response = api_instance.delete_application_stage_delete(indexname, jobad_id, resume_id, status, date=date)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->delete_application_stage_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **JobadId**|  |
 **resume_id** | **str**|  |
 **status** | **str**| The status describes the hiring pipeline level. The statuses are: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;APPLIED&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;SOURCED&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;SCREEN&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;INTERVIEW&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;EVALUATION&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;OFFER&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;HIRED&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;DISQUALIFIED&lt;/code&gt;. |
 **date** | **datetime**| The date in which the status changed. | [optional]

### Return type

[**ApplicationIDResponse**](ApplicationIDResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hiring Pipeline Stage Successfully Updated |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_applications_delete**
> DeleteApplicationsResponse delete_applications_delete(indexname, resume_id)

Delete Applications

 This method removes all the applications associated with *resume_id* from the index *indexname*.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.delete_applications_response import DeleteApplicationsResponse
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    resume_id = "resume_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete Applications
        api_response = api_instance.delete_applications_delete(indexname, resume_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->delete_applications_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **resume_id** | **str**|  |

### Return type

[**DeleteApplicationsResponse**](DeleteApplicationsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applications Successfully Deleted |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applicants_get**
> GetCandidatesResponse get_applicants_get(indexname, jobad_id)

Get Applicants

 This method returns a list of UUID4 associated to applicants of the job advertisement with id *jobad_id* stored in the index *indexname*.  Query parameters are used to specify the *offset* and *size* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored; in order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  The use of caching is highly recommended to improve the performances.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.get_candidates_response import GetCandidatesResponse
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    jobad_id = JobadId(None) # JobadId | 
    cache = True # bool | Optional. Whether the search results should be cached or not. (optional) if omitted the server will use the default value of True
    cache_time = 300 # int | Optional. Seconds.Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>false</code>. (optional) if omitted the server will use the default value of 300
    offset = 0 # int | Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>. (optional) if omitted the server will use the default value of 0
    search_id = "search_id_example" # str | Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. (optional)
    size = 50 # int | Optional. Number of documents to return. (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Applicants
        api_response = api_instance.get_applicants_get(indexname, jobad_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->get_applicants_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Applicants
        api_response = api_instance.get_applicants_get(indexname, jobad_id, cache=cache, cache_time=cache_time, offset=offset, search_id=search_id, size=size)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->get_applicants_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **JobadId**|  |
 **cache** | **bool**| Optional. Whether the search results should be cached or not. | [optional] if omitted the server will use the default value of True
 **cache_time** | **int**| Optional. Seconds.Ignored if *cache* is &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;false&lt;/code&gt;. | [optional] if omitted the server will use the default value of 300
 **offset** | **int**| Optional. Number of documents to skip. Ignored if *cache* is &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;true&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **search_id** | **str**| Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. | [optional]
 **size** | **int**| Optional. Number of documents to return. | [optional] if omitted the server will use the default value of 50

### Return type

[**GetCandidatesResponse**](GetCandidatesResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resumes Successfully Retrieved |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_application_get**
> GetApplicationResponse get_application_get(indexname, resume_id, jobad_id)

Get Application

 This method returns the information related to the application stored with ids *resume_id* and *jobad_id* in the index *indexname*.  As reported in the schema below, the method has two different response schemas: + a *Status* response is returned when the application or the related [resume](https://api.inda.ai/hr/docs/v2/#tag/Resume-Management) is still in the processing queue, if the processing failed, or if the requested application has never been stored (e.g., resume processing failed when using [Apply](https://api.inda.ai/hr/docs/v2/#operation/apply__POST) method); + a *GetApplicationResponse* response is returned if the application has been successfully processed and inserted in the index. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.get_application_response import GetApplicationResponse
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    resume_id = "resume_id_example" # str | 
    jobad_id = JobadId(None) # JobadId | 

    # example passing only required values which don't have defaults set
    try:
        # Get Application
        api_response = api_instance.get_application_get(indexname, resume_id, jobad_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->get_application_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **resume_id** | **str**|  |
 **jobad_id** | **JobadId**|  |

### Return type

[**GetApplicationResponse**](GetApplicationResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application Successfully Retrieved |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_applications_get**
> GetApplicationsResponse get_applications_get(indexname, resume_id)

Get Applications

 This method returns a list of UUID4 associated to those job advertisements that have the resume of id *resume_id* as applicant. Both resumes and job advertisements are stored in the *index* indexname.  Query parameters are used to specify the *offset* and *size* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored; in order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  The use of caching is highly recommended to improve the performances.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.get_applications_response import GetApplicationsResponse
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    resume_id = "resume_id_example" # str | 
    cache = True # bool | Optional. Whether the search results should be cached or not. (optional) if omitted the server will use the default value of True
    cache_time = 300 # int | Optional. Seconds. (optional) if omitted the server will use the default value of 300
    offset = 0 # int | Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>. (optional) if omitted the server will use the default value of 0
    search_id = "search_id_example" # str | Both the initial search request and each subsequent scroll request returns a *search_id*. The *search_id* may or may not  change between requests; however, only the most recently received *search_id* should be used. (optional)
    size = 50 # int | Optional. Number of documents to return. (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get Applications
        api_response = api_instance.get_applications_get(indexname, resume_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->get_applications_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Applications
        api_response = api_instance.get_applications_get(indexname, resume_id, cache=cache, cache_time=cache_time, offset=offset, search_id=search_id, size=size)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->get_applications_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **resume_id** | **str**|  |
 **cache** | **bool**| Optional. Whether the search results should be cached or not. | [optional] if omitted the server will use the default value of True
 **cache_time** | **int**| Optional. Seconds. | [optional] if omitted the server will use the default value of 300
 **offset** | **int**| Optional. Number of documents to skip. Ignored if *cache* is &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;true&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **search_id** | **str**| Both the initial search request and each subsequent scroll request returns a *search_id*. The *search_id* may or may not  change between requests; however, only the most recently received *search_id* should be used. | [optional]
 **size** | **int**| Optional. Number of documents to return. | [optional] if omitted the server will use the default value of 50

### Return type

[**GetApplicationsResponse**](GetApplicationsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Applications Successfully Retrieved |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_application_patch**
> PatchApplicationResponse patch_application_patch(indexname, jobad_id, resume_id, patch_application_request)

Patch Application

 This method updates the information related to the application stored with id *resume_id* and *jobad_id*.  This method accepts an application/json body with the same structure as [Add Application](https://api.inda.ai/hr/docs/v2/#operation/add_application__POST) however in this case all fields are optional. Fields that contain differences between the corresponding original ones are substituted, while new fields are added. Bear in mind that lists are considered as singular value, therefore to modify an entry in a list it is necessary to insert the full list.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import application_management_api
from inda_hr.model.patch_application_response import PatchApplicationResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.patch_application_request import PatchApplicationRequest
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
    api_instance = application_management_api.ApplicationManagementApi(api_client)
    indexname = "indexname_example" # str | 
    jobad_id = JobadId(None) # JobadId | 
    resume_id = "resume_id_example" # str | 
    patch_application_request = PatchApplicationRequest(
        data=ApplicationCommonOptionalData(
            objective=BaseBenefitsValueModelStrictStr(
                value="value_example",
            ),
            professional_summary=BaseBenefitsValueModelStrictStr(
                value="value_example",
            ),
            desired_employment=ResumeEmployment(
                code=BaseBenefitsValueModelStrictStr(
                    value="value_example",
                ),
                category=BaseBenefitsValueModelStrictStr(
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
                    BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                ],
            ),
            desired_contracts=[
                OptionalResumeContract(
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
            ],
            desired_salary=OptionalResumeSalary(
                amount=RangeFloat(
                    range=Range(None),
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
            desired_benefits=[
                ResumeBenefit(
                    value="value_example",
                ),
            ],
            desired_locations=[
                BaseLocationsLocation(
                    city=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    country=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    geo_coordinates=ValueModelGeoLocation(
                        value=GeoLocation(
                            lat=-90.0,
                            lon=-180.0,
                        ),
                    ),
                    country_code=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    postal_code=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    street_address=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    county=BaseBenefitsValueModelStrictStr(
                        value="value_example",
                    ),
                    region=BaseBenefitsValueModelStrictStr(
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
                relocation_date=RangeDatetime(
                    range=Range1(None),
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
                frequency=Frequency1(None),
            ),
            job_shift=OptionalJobShift(
                details=BoolBaseModel(
                    is_possible=True,
                    is_mandatory=True,
                ),
                type=OptionalJobShiftType(
                    value="value_example",
                ),
                frequency=Frequency2(None),
            ),
            origin_links=[
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
    ) # PatchApplicationRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Patch Application
        api_response = api_instance.patch_application_patch(indexname, jobad_id, resume_id, patch_application_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->patch_application_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **JobadId**|  |
 **resume_id** | **str**|  |
 **patch_application_request** | [**PatchApplicationRequest**](PatchApplicationRequest.md)|  |

### Return type

[**PatchApplicationResponse**](PatchApplicationResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Application Successfully Updated |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

