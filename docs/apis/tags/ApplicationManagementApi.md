<a name="__pageTop"></a>
# inda_hr.apis.tags.application_management_api.ApplicationManagementApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_application_post**](#add_application_post) | **post** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/ | Add Application
[**add_application_stage_post**](#add_application_stage_post) | **post** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/hiring-pipeline/stage/ | Add Application Stage
[**application_status_get**](#application_status_get) | **get** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/status/ | Application Status
[**apply_post**](#apply_post) | **post** /hr/v2/index/{indexname}/jobad/{jobad_id}/apply/ | Apply
[**delete_applicants_delete**](#delete_applicants_delete) | **delete** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resumes/ | Delete Applicants
[**delete_application_delete**](#delete_application_delete) | **delete** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/ | Delete Application
[**delete_application_stage_delete**](#delete_application_stage_delete) | **delete** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/hiring-pipeline/stage/ | Delete Application Stage
[**delete_applications_delete**](#delete_applications_delete) | **delete** /hr/v2/index/{indexname}/resume/{resume_id}/applications/jobads/ | Delete Applications
[**get_applicants_get**](#get_applicants_get) | **get** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resumes/ | Get Applicants
[**get_application_get**](#get_application_get) | **get** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/ | Get Application
[**get_applications_get**](#get_applications_get) | **get** /hr/v2/index/{indexname}/resume/{resume_id}/applications/jobads/ | Get Applications
[**patch_application_patch**](#patch_application_patch) | **patch** /hr/v2/index/{indexname}/jobad/{jobad_id}/applications/resume/{resume_id}/ | Patch Application

# **add_application_post**
<a name="add_application_post"></a>
> ApplicationIDResponse add_application_post(indexnamejobad_idresume_id)

Add Application

 This method stores on *indexname* the application made by the applicant *resume_id* to the job advertisement *jobad_id*.  It is assumed that both the resume and the job advertisement involved have been previously added to *indexname* by  the appropriate methods.  On the right, we provide an example of input structure; further details are available in dedicated sections.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
        'resume_id': "resume_id_example",
    }
    try:
        # Add Application
        api_response = api_instance.add_application_post(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->add_application_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
        'resume_id': "resume_id_example",
    }
    body = BaseApplicationRequest(
        data=ApplicationCommonData(
            objective=BaseBenefitsValueModelStrictStr(
                value="value_example",
            ),
,
            desired_employment=ResumeEmployment(
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
                        value="1970-01-01T00:00:00.00Z",
                    ),
,
                )
            ],
            desired_salary=ResumeSalary(
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
            desired_benefits=[
                ResumeBenefit(
                    value="value_example",
                )
            ],
            desired_locations=[
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
            job_shift=JobShift(
                details=BoolBaseModel(),
                type=JobShiftType(
                    value="DAY_SHIFT",
                ),
                frequency=None,
            ),
            origin_links=[
                JobadLinkLink(
                    url=JobadLinkURL(
                        value="value_example",
                    ),
                    label=JobadLinkLinkLabel(
                        value="value_example",
                    ),
                )
            ],
        ),
        hiring_details=HiringDetails(
            application_date="1970-01-01",
            hiring_date="1970-01-01",
            hiring_pipeline=[
                HiringPipelineStage(
                    date="1970-01-01T00:00:00.00Z",
                    description="description_example",
                    status="APPLIED",
                )
            ],
        ),
    )
    try:
        # Add Application
        api_response = api_instance.add_application_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->add_application_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
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
[**BaseApplicationRequest**](../../models/BaseApplicationRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 
jobad_id | JobadIdSchema | | 
resume_id | ResumeIdSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["auto", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", ] 

# any_of_1

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
201 | [ApiResponseFor201](#add_application_post.ApiResponseFor201) | Application Successfully Added
400 | [ApiResponseFor400](#add_application_post.ApiResponseFor400) | Bad Request
200 | [ApiResponseFor200](#add_application_post.ApiResponseFor200) | Application Already Present
422 | [ApiResponseFor422](#add_application_post.ApiResponseFor422) | Validation Error

#### add_application_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationIDResponse**](../../models/ApplicationIDResponse.md) |  | 


#### add_application_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### add_application_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationIDResponse**](../../models/ApplicationIDResponse.md) |  | 


#### add_application_post.ApiResponseFor422
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

# **add_application_stage_post**
<a name="add_application_stage_post"></a>
> ApplicationIDResponse add_application_stage_post(indexnameresume_idjobad_idapplication_status_request)

Add Application Stage

 This method updates the applicant hiring pipeline by adding a new stage according to the requested values.  The supported stages for the hiring pipelines are: <code style='color: #333333; opacity: 0.9'>APPLIED</code>, <code style='color: #333333; opacity: 0.9'>SOURCED</code>, <code style='color: #333333; opacity: 0.9'>SCREEN</code>, <code style='color: #333333; opacity: 0.9'>INTERVIEW</code>, <code style='color: #333333; opacity: 0.9'>EVALUATION</code>, <code style='color: #333333; opacity: 0.9'>OFFER</code>, <code style='color: #333333; opacity: 0.9'>HIRED</code>, <code style='color: #333333; opacity: 0.9'>DISQUALIFIED</code>.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
        'jobad_id': None,
    }
    body = ApplicationStatusRequest(
        date="1970-01-01T00:00:00.00Z",
        description="description_example",
        status="APPLIED",
    )
    try:
        # Add Application Stage
        api_response = api_instance.add_application_stage_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->add_application_stage_post: %s\n" % e)
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
[**ApplicationStatusRequest**](../../models/ApplicationStatusRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 
resume_id | ResumeIdSchema | | 
jobad_id | JobadIdSchema | | 

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

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["auto", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", ] 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#add_application_stage_post.ApiResponseFor201) | Hiring Pipeline Stage Successfully Added
400 | [ApiResponseFor400](#add_application_stage_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#add_application_stage_post.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#add_application_stage_post.ApiResponseFor422) | Validation Error

#### add_application_stage_post.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationIDResponse**](../../models/ApplicationIDResponse.md) |  | 


#### add_application_stage_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### add_application_stage_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### add_application_stage_post.ApiResponseFor422
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

# **application_status_get**
<a name="application_status_get"></a>
> ApplicationResponsesStatus application_status_get(indexnamejobad_idresume_id)

Application Status

 This method returns the status of an application, which can be any of the following: + *Processing*: the application is in INDA process queue; + *Available*: the application is in the index and is available to the user; + *Duplicate*: the application was a duplicate, refer to the indicated pair  (*ResumeID*, *JobAdID*) to retrieve the already indexed one; + *Failed*: the processing of the input failed; + *Missing*: none of the previous; the pair (*ResumeID*, *JobAdID*) may be wrong or corresponding to a deleted application. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
        'resume_id': "resume_id_example",
    }
    try:
        # Application Status
        api_response = api_instance.application_status_get(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->application_status_get: %s\n" % e)
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
resume_id | ResumeIdSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["auto", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", ] 

# any_of_1

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
200 | [ApiResponseFor200](#application_status_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#application_status_get.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#application_status_get.ApiResponseFor422) | Validation Error

#### application_status_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationResponsesStatus**](../../models/ApplicationResponsesStatus.md) |  | 


#### application_status_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### application_status_get.ApiResponseFor422
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

# **apply_post**
<a name="apply_post"></a>
> ApplicationIDResponse apply_post(indexnamejobad_idapply_item_request)

Apply

 This method adds a candidate resume to *indexname* and registers their application to *jobad_id*.  In an asynchronous fashion, the resume to be processed is added to the server's task queue and the assigned *ResumeID*  is returned immediately; when its processing is successfully completed and the resume is effectively added to  *indexname*, the pipeline continues with the candidate request to apply to the job advertisement identified by  *jobad_id*.  Under the hood, this method performs: + [Add Resume](https://api.inda.ai/hr/docs/v2/#operation/add_resume__POST)  + [Add Application](https://api.inda.ai/hr/docs/v2/#operation/add_application__POST)  Note that the document may not successfully conclude the processing pipeline (e.g., it may be discarded because duplicate of one of the documents already present in the *indexname*), and thus it may not be actually added to the index. The same may happen while processing the application request.  In order to verify the resume and the application status, the user can use the *ResumeID* and the *JobAdID* through  the following methods: + [Resume Status](https://api.inda.ai/hr/docs/v2/#operation/resume_status__GET) + [Application Status](https://api.inda.ai/hr/docs/v2/#operation/application_status__GET) + [Get Failures](https://api.inda.ai/hr/docs/v2/#operation/get_failures__GET)  On the right, we provide an example of input structure; further details are available in dedicated sections.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
    }
    query_params = {
    }
    body = ApplyItemRequest(
        application=BaseApplicationRequest(
            data=ApplicationCommonData(
                objective=BaseBenefitsValueModelStrictStr(
                    value="value_example",
                ),
,
                desired_employment=ResumeEmployment(
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
                            value="1970-01-01T00:00:00.00Z",
                        ),
,
                    )
                ],
                desired_salary=ResumeSalary(
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
                desired_benefits=[
                    ResumeBenefit(
                        value="value_example",
                    )
                ],
                desired_locations=[
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
                job_shift=JobShift(
                    details=BoolBaseModel(),
                    type=JobShiftType(
                        value="DAY_SHIFT",
                    ),
                    frequency=None,
                ),
                origin_links=[
                    JobadLinkLink(
                        url=JobadLinkURL(
                            value="value_example",
                        ),
                        label=JobadLinkLinkLabel(
                            value="value_example",
                        ),
                    )
                ],
            ),
            hiring_details=HiringDetails(
                application_date="1970-01-01",
                hiring_date="1970-01-01",
                hiring_pipeline=[
                    HiringPipelineStage(
                        date="1970-01-01T00:00:00.00Z",
                        description="description_example",
                        status="APPLIED",
                    )
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
                            value=GeoLocation(),
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
,
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
        ),
    )
    try:
        # Apply
        api_response = api_instance.apply_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->apply_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
    }
    query_params = {
        'resume_id': "resume_id_example",
        'src_lang': "pt",
        'dst_lang': "pt",
    }
    body = ApplyItemRequest(
        application=BaseApplicationRequest(
            data=ApplicationCommonData(
                objective=BaseBenefitsValueModelStrictStr(
                    value="value_example",
                ),
,
                desired_employment=ResumeEmployment(
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
                            value="1970-01-01T00:00:00.00Z",
                        ),
,
                    )
                ],
                desired_salary=ResumeSalary(
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
                desired_benefits=[
                    ResumeBenefit(
                        value="value_example",
                    )
                ],
                desired_locations=[
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
                job_shift=JobShift(
                    details=BoolBaseModel(),
                    type=JobShiftType(
                        value="DAY_SHIFT",
                    ),
                    frequency=None,
                ),
                origin_links=[
                    JobadLinkLink(
                        url=JobadLinkURL(
                            value="value_example",
                        ),
                        label=JobadLinkLinkLabel(
                            value="value_example",
                        ),
                    )
                ],
            ),
            hiring_details=HiringDetails(
                application_date="1970-01-01",
                hiring_date="1970-01-01",
                hiring_pipeline=[
                    HiringPipelineStage(
                        date="1970-01-01T00:00:00.00Z",
                        description="description_example",
                        status="APPLIED",
                    )
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
                            value=GeoLocation(),
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
,
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
        ),
    )
    try:
        # Apply
        api_response = api_instance.apply_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->apply_post: %s\n" % e)
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
[**ApplyItemRequest**](../../models/ApplyItemRequest.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
resume_id | ResumeIdSchema | | optional
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional


# ResumeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# SrcLangSchema

Optional. Language in which the following *Resume.Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the detected *Attachment.CV.File* language is assumed as `src_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Language in which the following *Resume.Data* entities are expressed: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the detected *Attachment.CV.File* language is assumed as &#x60;src_lang&#x60;. | must be one of ["pt", "it", "en", "de", "fr", "es", ] 

# DstLangSchema

Optional. Destination language in which the following *Resume.Data* entities are translated: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the input or detected `src_lang` is assumed as `dst_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Destination language in which the following *Resume.Data* entities are translated: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the input or detected &#x60;src_lang&#x60; is assumed as &#x60;dst_lang&#x60;. | must be one of ["pt", "it", "en", "de", "fr", "es", ] 

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
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["auto", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", ] 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
202 | [ApiResponseFor202](#apply_post.ApiResponseFor202) | Application Successfully Queued
422 | [ApiResponseFor422](#apply_post.ApiResponseFor422) | Validation Error

#### apply_post.ApiResponseFor202
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor202ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor202ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationIDResponse**](../../models/ApplicationIDResponse.md) |  | 


#### apply_post.ApiResponseFor422
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

# **delete_applicants_delete**
<a name="delete_applicants_delete"></a>
> DeleteCandidatesResponse delete_applicants_delete(indexnamejobad_id)

Delete Applicants

 This method removes all the applicants associated with *jobad_id* from the index *indexname*.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
    }
    try:
        # Delete Applicants
        api_response = api_instance.delete_applicants_delete(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->delete_applicants_delete: %s\n" % e)
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
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["auto", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", ] 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#delete_applicants_delete.ApiResponseFor200) | Applicants Successfully Deleted
404 | [ApiResponseFor404](#delete_applicants_delete.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#delete_applicants_delete.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#delete_applicants_delete.ApiResponseFor422) | Validation Error

#### delete_applicants_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteCandidatesResponse**](../../models/DeleteCandidatesResponse.md) |  | 


#### delete_applicants_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### delete_applicants_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### delete_applicants_delete.ApiResponseFor422
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

# **delete_application_delete**
<a name="delete_application_delete"></a>
> DeleteApplicationResponse delete_application_delete(indexnamejobad_idresume_id)

Delete Application

 This method removes the application associated with *jobad_id* and *resume_id* from the index *indexname*.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
        'resume_id': "resume_id_example",
    }
    try:
        # Delete Application
        api_response = api_instance.delete_application_delete(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->delete_application_delete: %s\n" % e)
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
resume_id | ResumeIdSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["auto", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", ] 

# any_of_1

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
200 | [ApiResponseFor200](#delete_application_delete.ApiResponseFor200) | Application Successfully Deleted
404 | [ApiResponseFor404](#delete_application_delete.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#delete_application_delete.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#delete_application_delete.ApiResponseFor422) | Validation Error

#### delete_application_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteApplicationResponse**](../../models/DeleteApplicationResponse.md) |  | 


#### delete_application_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### delete_application_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### delete_application_delete.ApiResponseFor422
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

# **delete_application_stage_delete**
<a name="delete_application_stage_delete"></a>
> ApplicationIDResponse delete_application_stage_delete(indexnamejobad_idresume_idstatus)

Delete Application Stage

 This method updates the applicant hiring pipeline by deleting a previously stored stage according to the requested  values.  The supported stages for the hiring pipelines are: <code style='color: #333333; opacity: 0.9'>APPLIED</code>, <code style='color: #333333; opacity: 0.9'>SOURCED</code>, <code style='color: #333333; opacity: 0.9'>SCREEN</code>, <code style='color: #333333; opacity: 0.9'>INTERVIEW</code>, <code style='color: #333333; opacity: 0.9'>EVALUATION</code>, <code style='color: #333333; opacity: 0.9'>OFFER</code>, <code style='color: #333333; opacity: 0.9'>HIRED</code>, <code style='color: #333333; opacity: 0.9'>DISQUALIFIED</code>.  Note that all the stages matching *status* and *date* (if present) query parameters will be removed from the  hiring pipeline.   

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
        'resume_id': "resume_id_example",
    }
    query_params = {
        'status': "APPLIED",
    }
    try:
        # Delete Application Stage
        api_response = api_instance.delete_application_stage_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->delete_application_stage_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
        'resume_id': "resume_id_example",
    }
    query_params = {
        'status': "APPLIED",
        'date': "1970-01-01T00:00:00.00Z",
    }
    try:
        # Delete Application Stage
        api_response = api_instance.delete_application_stage_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->delete_application_stage_delete: %s\n" % e)
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
status | StatusSchema | | 
date | DateSchema | | optional


# StatusSchema

The status describes the hiring pipeline level. The statuses are: <code style='color: #333333; opacity: 0.9'>APPLIED</code>, <code style='color: #333333; opacity: 0.9'>SOURCED</code>, <code style='color: #333333; opacity: 0.9'>SCREEN</code>, <code style='color: #333333; opacity: 0.9'>INTERVIEW</code>, <code style='color: #333333; opacity: 0.9'>EVALUATION</code>, <code style='color: #333333; opacity: 0.9'>OFFER</code>, <code style='color: #333333; opacity: 0.9'>HIRED</code>, <code style='color: #333333; opacity: 0.9'>DISQUALIFIED</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The status describes the hiring pipeline level. The statuses are: &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;APPLIED&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;SOURCED&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;SCREEN&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;INTERVIEW&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;EVALUATION&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;OFFER&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;HIRED&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;DISQUALIFIED&lt;/code&gt;. | must be one of ["APPLIED", "SOURCED", "SCREEN", "INTERVIEW", "EVALUATION", "OFFER", "HIRED", "DISQUALIFIED", ] 

# DateSchema

The date in which the status changed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str, datetime,  | str,  | The date in which the status changed. | value must conform to RFC-3339 date-time

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 
jobad_id | JobadIdSchema | | 
resume_id | ResumeIdSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["auto", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", ] 

# any_of_1

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
200 | [ApiResponseFor200](#delete_application_stage_delete.ApiResponseFor200) | Hiring Pipeline Stage Successfully Updated
400 | [ApiResponseFor400](#delete_application_stage_delete.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#delete_application_stage_delete.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#delete_application_stage_delete.ApiResponseFor422) | Validation Error

#### delete_application_stage_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ApplicationIDResponse**](../../models/ApplicationIDResponse.md) |  | 


#### delete_application_stage_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### delete_application_stage_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### delete_application_stage_delete.ApiResponseFor422
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

# **delete_applications_delete**
<a name="delete_applications_delete"></a>
> DeleteApplicationsResponse delete_applications_delete(indexnameresume_id)

Delete Applications

 This method removes all the applications associated with *resume_id* from the index *indexname*.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    try:
        # Delete Applications
        api_response = api_instance.delete_applications_delete(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->delete_applications_delete: %s\n" % e)
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
200 | [ApiResponseFor200](#delete_applications_delete.ApiResponseFor200) | Applications Successfully Deleted
404 | [ApiResponseFor404](#delete_applications_delete.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#delete_applications_delete.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#delete_applications_delete.ApiResponseFor422) | Validation Error

#### delete_applications_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DeleteApplicationsResponse**](../../models/DeleteApplicationsResponse.md) |  | 


#### delete_applications_delete.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### delete_applications_delete.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### delete_applications_delete.ApiResponseFor422
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

# **get_applicants_get**
<a name="get_applicants_get"></a>
> GetCandidatesResponse get_applicants_get(indexnamejobad_id)

Get Applicants

 This method returns a list of UUID4 associated to applicants of the job advertisement with id *jobad_id* stored in the index *indexname*.  Query parameters are used to specify the *offset* and *size* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored; in order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  The use of caching is highly recommended to improve the performances.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
    }
    query_params = {
    }
    try:
        # Get Applicants
        api_response = api_instance.get_applicants_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->get_applicants_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
    }
    query_params = {
        'cache': True,
        'cache_time': 300,
        'offset': 0,
        'search_id': "search_id_example",
        'size': 50,
    }
    try:
        # Get Applicants
        api_response = api_instance.get_applicants_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->get_applicants_get: %s\n" % e)
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

Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. | 

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
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["auto", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", ] 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_applicants_get.ApiResponseFor200) | Resumes Successfully Retrieved
404 | [ApiResponseFor404](#get_applicants_get.ApiResponseFor404) | Not Found
415 | [ApiResponseFor415](#get_applicants_get.ApiResponseFor415) | Unsupported Media Type
400 | [ApiResponseFor400](#get_applicants_get.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#get_applicants_get.ApiResponseFor422) | Validation Error

#### get_applicants_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetCandidatesResponse**](../../models/GetCandidatesResponse.md) |  | 


#### get_applicants_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_applicants_get.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_applicants_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_applicants_get.ApiResponseFor422
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

# **get_application_get**
<a name="get_application_get"></a>
> GetApplicationResponse get_application_get(indexnameresume_idjobad_id)

Get Application

 This method returns the information related to the application stored with ids *resume_id* and *jobad_id* in the index *indexname*.  As reported in the schema below, the method has two different response schemas: + a *Status* response is returned when the application or the related [resume](https://api.inda.ai/hr/docs/v2/#tag/Resume-Management) is still in the processing queue, if the processing failed, or if the requested application has never been stored (e.g., resume processing failed when using [Apply](https://api.inda.ai/hr/docs/v2/#operation/apply__POST) method); + a *GetApplicationResponse* response is returned if the application has been successfully processed and inserted in the index. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
        'jobad_id': None,
    }
    try:
        # Get Application
        api_response = api_instance.get_application_get(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->get_application_get: %s\n" % e)
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
jobad_id | JobadIdSchema | | 

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

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["auto", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", ] 

# any_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_application_get.ApiResponseFor200) | Application Successfully Retrieved
404 | [ApiResponseFor404](#get_application_get.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#get_application_get.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#get_application_get.ApiResponseFor422) | Validation Error

#### get_application_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetApplicationResponse**](../../models/GetApplicationResponse.md) |  | 


#### get_application_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_application_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_application_get.ApiResponseFor422
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

# **get_applications_get**
<a name="get_applications_get"></a>
> GetApplicationsResponse get_applications_get(indexnameresume_id)

Get Applications

 This method returns a list of UUID4 associated to those job advertisements that have the resume of id *resume_id* as applicant. Both resumes and job advertisements are stored in the *index* indexname.  Query parameters are used to specify the *offset* and *size* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored; in order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  The use of caching is highly recommended to improve the performances.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
    }
    try:
        # Get Applications
        api_response = api_instance.get_applications_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->get_applications_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
        'cache': True,
        'cache_time': 300,
        'offset': 0,
        'search_id': "search_id_example",
        'size': 50,
    }
    try:
        # Get Applications
        api_response = api_instance.get_applications_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->get_applications_get: %s\n" % e)
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

Optional. Seconds.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Seconds. | if omitted the server will use the default value of 300

# OffsetSchema

Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Optional. Number of documents to skip. Ignored if *cache* is &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;true&lt;/code&gt;. | if omitted the server will use the default value of 0

# SearchIdSchema

Both the initial search request and each subsequent scroll request returns a *search_id*. The *search_id* may or may not  change between requests; however, only the most recently received *search_id* should be used.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Both the initial search request and each subsequent scroll request returns a *search_id*. The *search_id* may or may not  change between requests; however, only the most recently received *search_id* should be used. | 

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
200 | [ApiResponseFor200](#get_applications_get.ApiResponseFor200) | Applications Successfully Retrieved
404 | [ApiResponseFor404](#get_applications_get.ApiResponseFor404) | Not Found
415 | [ApiResponseFor415](#get_applications_get.ApiResponseFor415) | Unsupported Media Type
400 | [ApiResponseFor400](#get_applications_get.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#get_applications_get.ApiResponseFor422) | Validation Error

#### get_applications_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetApplicationsResponse**](../../models/GetApplicationsResponse.md) |  | 


#### get_applications_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_applications_get.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_applications_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_applications_get.ApiResponseFor422
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

# **patch_application_patch**
<a name="patch_application_patch"></a>
> PatchApplicationResponse patch_application_patch(indexnamejobad_idresume_idpatch_application_request)

Patch Application

 This method updates the information related to the application stored with id *resume_id* and *jobad_id*.  This method accepts an application/json body with the same structure as [Add Application](https://api.inda.ai/hr/docs/v2/#operation/add_application__POST) however in this case all fields are optional. Fields that contain differences between the corresponding original ones are substituted, while new fields are added. Bear in mind that lists are considered as singular value, therefore to modify an entry in a list it is necessary to insert the full list.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import application_management_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'jobad_id': None,
        'resume_id': "resume_id_example",
    }
    body = PatchApplicationRequest(
        data=ApplicationCommonOptionalData(
            objective=BaseBenefitsValueModelStrictStr(
                value="value_example",
            ),
,
            desired_employment=ResumeEmployment(
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
                        value="1970-01-01T00:00:00.00Z",
                    ),
,
                )
            ],
            desired_salary=OptionalResumeSalary(
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
            desired_benefits=[
                ResumeBenefit(
                    value="value_example",
                )
            ],
            desired_locations=[
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
            job_shift=OptionalJobShift(
                details=BoolBaseModel(),
                type=OptionalJobShiftType(
                    value="value_example",
                ),
                frequency=None,
            ),
            origin_links=[
                JobadLinkLink(
                    url=JobadLinkURL(
                        value="value_example",
                    ),
                    label=JobadLinkLinkLabel(
                        value="value_example",
                    ),
                )
            ],
        ),
    )
    try:
        # Patch Application
        api_response = api_instance.patch_application_patch(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ApplicationManagementApi->patch_application_patch: %s\n" % e)
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
[**PatchApplicationRequest**](../../models/PatchApplicationRequest.md) |  | 


### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 
jobad_id | JobadIdSchema | | 
resume_id | ResumeIdSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# JobadIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### anyOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[any_of_0](#any_of_0) | str,  | str,  |  | must be one of ["auto", ] 
[any_of_1](#any_of_1) | str,  | str,  |  | 

# any_of_0

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["auto", ] 

# any_of_1

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
200 | [ApiResponseFor200](#patch_application_patch.ApiResponseFor200) | Application Successfully Updated
400 | [ApiResponseFor400](#patch_application_patch.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#patch_application_patch.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#patch_application_patch.ApiResponseFor422) | Validation Error

#### patch_application_patch.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**PatchApplicationResponse**](../../models/PatchApplicationResponse.md) |  | 


#### patch_application_patch.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### patch_application_patch.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### patch_application_patch.ApiResponseFor422
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

