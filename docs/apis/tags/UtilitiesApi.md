<a name="__pageTop"></a>
# inda_hr.apis.tags.utilities_api.UtilitiesApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_index_cache_delete**](#clear_index_cache_delete) | **delete** /hr/v2/index/{indexname}/cache/ | Clear Index Cache
[**health_status_get**](#health_status_get) | **get** /hr/v2/ | Health Status

# **clear_index_cache_delete**
<a name="clear_index_cache_delete"></a>
> IndexCacheDeletionResponse clear_index_cache_delete(indexname)

Clear Index Cache

 This method clears all standard and monitoring caches for given index. The *query parameters* allow to choose which caches should be cleared and to choose whether or not the method should wait to respond until the processing is completed.   The following caches can be cleared: + **Failed Documents**: Deletes all entries of failed documents cached for the index. + **Import statuses**: Deletes all entries of import statuses cached for the index. + **Tasks Queue**: Deletes tracking of all jobs scheduled to be performed on the index. WARNING: Does not delete the jobs themselves and does not prevent other jobs to be queued. + **Field data**: Deletes all field data on the index that are still cached. + **Queries Cache**: Deletes all queries performed on the index that are still cached. + **Requests Cache**: Deletes all requests performed on the index that are still cached.  *NOTE: Use only as a debug option!* 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import utilities_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.index_cache_deletion_response import IndexCacheDeletionResponse
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
    api_instance = utilities_api.UtilitiesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    try:
        # Clear Index Cache
        api_response = api_instance.clear_index_cache_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UtilitiesApi->clear_index_cache_delete: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'clean_failures': True,
        'clean_imports': True,
        'clean_queues': True,
        'clean_fielddata': True,
        'clean_queries': True,
        'clean_requests': True,
        'wait_for_completion': True,
    }
    try:
        # Clear Index Cache
        api_response = api_instance.clear_index_cache_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UtilitiesApi->clear_index_cache_delete: %s\n" % e)
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
clean_failures | CleanFailuresSchema | | optional
clean_imports | CleanImportsSchema | | optional
clean_queues | CleanQueuesSchema | | optional
clean_fielddata | CleanFielddataSchema | | optional
clean_queries | CleanQueriesSchema | | optional
clean_requests | CleanRequestsSchema | | optional
wait_for_completion | WaitForCompletionSchema | | optional


# CleanFailuresSchema

Whether or not the document failures should be cleaned.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Whether or not the document failures should be cleaned. | if omitted the server will use the default value of True

# CleanImportsSchema

Whether or not the import statuses should be cleaned.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Whether or not the import statuses should be cleaned. | if omitted the server will use the default value of True

# CleanQueuesSchema

Whether or not the queue should be cleaned.It cannot stop running tasks or prevent new tasks to be queued.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Whether or not the queue should be cleaned.It cannot stop running tasks or prevent new tasks to be queued. | if omitted the server will use the default value of True

# CleanFielddataSchema

Whether or not the fields cache should be cleaned.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Whether or not the fields cache should be cleaned. | if omitted the server will use the default value of True

# CleanQueriesSchema

Whether or not the queries cache should be cleaned.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Whether or not the queries cache should be cleaned. | if omitted the server will use the default value of True

# CleanRequestsSchema

Whether or not the requests cache should be cleaned.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Whether or not the requests cache should be cleaned. | if omitted the server will use the default value of True

# WaitForCompletionSchema

Whether or not the method should wait to responduntil the processing is completed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Whether or not the method should wait to responduntil the processing is completed. | if omitted the server will use the default value of True

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
200 | [ApiResponseFor200](#clear_index_cache_delete.ApiResponseFor200) | Successfully Cleared Elastic Cache And Monitoring Indices
500 | [ApiResponseFor500](#clear_index_cache_delete.ApiResponseFor500) | Internal Server Error
422 | [ApiResponseFor422](#clear_index_cache_delete.ApiResponseFor422) | Validation Error

#### clear_index_cache_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IndexCacheDeletionResponse**](../../models/IndexCacheDeletionResponse.md) |  | 


#### clear_index_cache_delete.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### clear_index_cache_delete.ApiResponseFor422
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

# **health_status_get**
<a name="health_status_get"></a>
> Check health_status_get()

Health Status

This method checks whether the service is up and running.  Returns the *status* of the service: <code style='color: #333333; opacity: 0.9'>green</code>, <code style='color: #333333; opacity: 0.9'>yellow</code> or <code style='color: #333333; opacity: 0.9'>red</code>.  A <code style='color: #333333; opacity: 0.9'>yellow</code> status means that at least the 80% of the services are available, <code style='color: #333333; opacity: 0.9'>red</code> that something is definitely not working properly.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import utilities_api
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.check import Check
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
    api_instance = utilities_api.UtilitiesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Health Status
        api_response = api_instance.health_status_get()
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UtilitiesApi->health_status_get: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#health_status_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#health_status_get.ApiResponseFor422) | Validation Error

#### health_status_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Check**](../../models/Check.md) |  | 


#### health_status_get.ApiResponseFor422
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

