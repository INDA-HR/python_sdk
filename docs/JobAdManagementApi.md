# inda_hr.JobAdManagementApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_jobad_post**](JobAdManagementApi.md#add_jobad_post) | **POST** /hr/v2/index/{indexname}/jobad/ | Add JobAd
[**delete_jobad_delete**](JobAdManagementApi.md#delete_jobad_delete) | **DELETE** /hr/v2/index/{indexname}/jobad/{jobad_id}/ | Delete JobAd
[**get_jobad_get**](JobAdManagementApi.md#get_jobad_get) | **GET** /hr/v2/index/{indexname}/jobad/{jobad_id}/ | Get JobAd
[**get_jobads_get**](JobAdManagementApi.md#get_jobads_get) | **GET** /hr/v2/index/{indexname}/jobads/ | Get JobAds
[**patch_jobad_patch**](JobAdManagementApi.md#patch_jobad_patch) | **PATCH** /hr/v2/index/{indexname}/jobad/{jobad_id}/ | Patch JobAd


# **add_jobad_post**
> JobAdIDResponse add_jobad_post(indexname, job_ad_request)

Add JobAd

 This method adds a job advertisement to *indexname* and assigns it a *JobAdID* (namely, a Unique Universal ID or UUID4). This method requires an application/json as content type body.  On the right, we provide an example of input structure; further details are available in dedicated sections.  Note that it is mandatory for users to have previously added information about the employer through the  [Add Company](https://api.inda.ai/hr/docs/v2/#operation/add_company__POST) method; the returned *ID* is the required *EmployerID* of job advertisement data. Obviously, one may skip this step if employer company data already exists.  Furthermore, also *Skills* is a required field, since it is necessary to perform the  [Match Resume](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST).  Users may leverage the [Extract Skills from JobAd](https://api.inda.ai/hr/docs/v2/#operation/extract_skills_from_jobad__POST) method and allow INDA to automatically extract skills by analyzing the job advertisement data. It is **highly recommended** to validate the retrieved skills before injecting them to *Add JobAd* requests.   

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_management_api
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
    indexname = "indexname_example" # str | 
    job_ad_request = JobAdRequest(
        data=JobadCommonData(
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
        metadata=JobadRequestsMetadata(
            language="it",
        ),
    ) # JobAdRequest | 
    jobad_id = "jobad_id_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add JobAd
        api_response = api_instance.add_jobad_post(indexname, job_ad_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->add_jobad_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add JobAd
        api_response = api_instance.add_jobad_post(indexname, job_ad_request, jobad_id=jobad_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->add_jobad_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **job_ad_request** | [**JobAdRequest**](JobAdRequest.md)|  |
 **jobad_id** | **str**|  | [optional]

### Return type

[**JobAdIDResponse**](JobAdIDResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | JobAd Successfully Added |  -  |
**400** | Bad Request |  -  |
**409** | Conflict |  -  |
**404** | Not Found |  -  |
**200** | JobAd Already Present |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_jobad_delete**
> DeleteJobAdResponse delete_jobad_delete(indexname, jobad_id)

Delete JobAd

 This method removes the job advertisement associated with *jobad_id* from the index *indexname*.  Note that when a job advertisement is deleted, the same happens to all its related applications.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_management_api
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
    indexname = "indexname_example" # str | 
    jobad_id = "jobad_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete JobAd
        api_response = api_instance.delete_jobad_delete(indexname, jobad_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->delete_jobad_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **str**|  |

### Return type

[**DeleteJobAdResponse**](DeleteJobAdResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JobAd Successfully Deleted. |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobad_get**
> GetJobAdResponse get_jobad_get(indexname, jobad_id)

Get JobAd

 This method returns the information related to the job advertisement stored with id *jobad_id* in the index *indexname*.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_management_api
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
    indexname = "indexname_example" # str | 
    jobad_id = "jobad_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get JobAd
        api_response = api_instance.get_jobad_get(indexname, jobad_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->get_jobad_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **str**|  |

### Return type

[**GetJobAdResponse**](GetJobAdResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JobAd Successfully Retrieved |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_jobads_get**
> GetJobAdsResponse get_jobads_get(indexname)

Get JobAds

 This method returns a list of UUID4 associated to the job advertisements stored in the index *indexname*.  Query parameters are used to specify the *offset* and *size* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored; in order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  The use of caching is highly recommended to improve the performances.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_management_api
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
    indexname = "indexname_example" # str | 
    cache = True # bool | Optional. Whether the search results should be cached or not. (optional) if omitted the server will use the default value of True
    cache_time = 300 # int | Optional. Seconds.Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>false</code>. (optional) if omitted the server will use the default value of 300
    offset = 0 # int | Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>. (optional) if omitted the server will use the default value of 0
    search_id = "search_id_example" # str | Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. Other query parameters are uselesswhen *SearchID* is used. (optional)
    size = 50 # int | Optional. Number of documents to return. (optional) if omitted the server will use the default value of 50

    # example passing only required values which don't have defaults set
    try:
        # Get JobAds
        api_response = api_instance.get_jobads_get(indexname)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->get_jobads_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get JobAds
        api_response = api_instance.get_jobads_get(indexname, cache=cache, cache_time=cache_time, offset=offset, search_id=search_id, size=size)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->get_jobads_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **cache** | **bool**| Optional. Whether the search results should be cached or not. | [optional] if omitted the server will use the default value of True
 **cache_time** | **int**| Optional. Seconds.Ignored if *cache* is &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;false&lt;/code&gt;. | [optional] if omitted the server will use the default value of 300
 **offset** | **int**| Optional. Number of documents to skip. Ignored if *cache* is &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;true&lt;/code&gt;. | [optional] if omitted the server will use the default value of 0
 **search_id** | **str**| Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. Other query parameters are uselesswhen *SearchID* is used. | [optional]
 **size** | **int**| Optional. Number of documents to return. | [optional] if omitted the server will use the default value of 50

### Return type

[**GetJobAdsResponse**](GetJobAdsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JobAds Successfully Retrieved |  -  |
**404** | Not Found |  -  |
**415** | Unsupported Media Type |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_jobad_patch**
> PatchJobAdResponse patch_jobad_patch(indexname, jobad_id, patch_job_ad_request)

Patch JobAd

 This method updates the information related to the job advertisement stored with id *job_ad_id*.  This method accepts an application/json body with the same structure as [Add JobAd](https://api.inda.ai/hr/docs/v2/#operation/add_jobad__POST), however in this case all fields are optional.  Fields that contain differences between the corresponding original ones are substituted, while new fields are added. Bear in mind that lists are considered as singular value, therefore to modify an entry in a list it is necessary to insert the full list.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import job_ad_management_api
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
    indexname = "indexname_example" # str | 
    jobad_id = "jobad_id_example" # str | 
    patch_job_ad_request = PatchJobAdRequest(
        data=JobadCommonOptionalData(
            job_title=JobTitleHeader(
                details=JobTitleHeaderDetails(
                    language="pt",
                    weight=0.8,
                    category="category_example",
                ),
                value="value_example",
            ),
            job_description=OptionalJobDescription(
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
                position_description=OptionalSection(
                    details=SectionDetails(
                        language="pt",
                        weight=0.8,
                    ),
                    title=JobadSectionsValueModelStrictStr(
                        value="value_example",
                    ),
                    content=JobadSectionsValueModelStrictStr(
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
            skills=OptionalRequiredAndPreferredConstrainedListValue(
                required=[
                    OptionalJobAdSkill(
                        details=OptionalJobAdSkillDetails(
                            proficiency_level="proficiency_level_example",
                            category="hard",
                            weight=0.75,
                        ),
                        value="value_example",
                    ),
                ],
                preferred=[
                    OptionalJobAdSkill(
                        details=OptionalJobAdSkillDetails(
                            proficiency_level="proficiency_level_example",
                            category="hard",
                            weight=0.75,
                        ),
                        value="value_example",
                    ),
                ],
            ),
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
            contract=OptionalJobAdContract(
                type="type_example",
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
            publisher=OptionalPublisher(
                name=JobadSectionsValueModelStrictStr(
                    value="value_example",
                ),
                category=JobadSectionsValueModelStrictStr(
                    value="value_example",
                ),
                link=OptionalLink(
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
            link=OptionalLink(
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
            salary=OptionalJobAdSalary(
                currency=Currency(
                    value="value_example",
                ),
                frequency=OptionalFrequency(
                    value="value_example",
                ),
                type=OptionalType(
                    value="value_example",
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
        metadata=OptionalMetadata(
            language="es",
        ),
    ) # PatchJobAdRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Patch JobAd
        api_response = api_instance.patch_jobad_patch(indexname, jobad_id, patch_job_ad_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling JobAdManagementApi->patch_jobad_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **jobad_id** | **str**|  |
 **patch_job_ad_request** | [**PatchJobAdRequest**](PatchJobAdRequest.md)|  |

### Return type

[**PatchJobAdResponse**](PatchJobAdResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | JobAd Successfully Updated |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

