<a name="__pageTop"></a>
# inda_hr.apis.tags.failures_api.FailuresApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_failures_get**](#get_failures_get) | **get** /hr/v2/index/{indexname}/failures/ | Get Failures

# **get_failures_get**
<a name="get_failures_get"></a>
> IndexedDocumentFailuresResponse get_failures_get(indexname)

Get Failures

 This method returns a list of documents that failed to be uploaded to *indexname*.  Note that the optional query parameters (see the schema below) allow to narrow the search to a specific item or import.  Users may also indicate a *doc_type* of interest, and retrieve just the failed documents of that type.   Allowed values for the *doc_type* parameter are: + <code style='color: #333333; opacity: 0.9'>resume</code> for [resumes](https://api.inda.ai/hr/docs/v2/#tag/Resume-Management); + <code style='color: #333333; opacity: 0.9'>job-ad</code> for [job adverts](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Management); + <code style='color: #333333; opacity: 0.9'>application</code> for [applications](https://api.inda.ai/hr/docs/v2/#tag/Application-Management).  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import failures_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.indexed_document_failures_response import IndexedDocumentFailuresResponse
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
    api_instance = failures_api.FailuresApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    try:
        # Get Failures
        api_response = api_instance.get_failures_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling FailuresApi->get_failures_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'import_id': "import_id_example",
        'resume_id': "resume_id_example",
        'jobad_id': "jobad_id_example",
        'doc_type': "resume",
    }
    try:
        # Get Failures
        api_response = api_instance.get_failures_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling FailuresApi->get_failures_get: %s\n" % e)
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
import_id | ImportIdSchema | | optional
resume_id | ResumeIdSchema | | optional
jobad_id | JobadIdSchema | | optional
doc_type | DocTypeSchema | | optional


# ImportIdSchema

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
str,  | str,  |  | 

# DocTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | must be one of ["resume", "job-ad", "application", ] 

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
200 | [ApiResponseFor200](#get_failures_get.ApiResponseFor200) | Failures Successfully Retrieved
404 | [ApiResponseFor404](#get_failures_get.ApiResponseFor404) | Not Found
503 | [ApiResponseFor503](#get_failures_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#get_failures_get.ApiResponseFor422) | Validation Error

#### get_failures_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IndexedDocumentFailuresResponse**](../../models/IndexedDocumentFailuresResponse.md) |  | 


#### get_failures_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_failures_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### get_failures_get.ApiResponseFor422
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

