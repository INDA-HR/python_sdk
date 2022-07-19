# inda_hr.UtilitiesApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_index_cache_delete**](UtilitiesApi.md#clear_index_cache_delete) | **DELETE** /hr/v2/index/{indexname}/cache/ | Clear Index Cache
[**health_status_get**](UtilitiesApi.md#health_status_get) | **GET** /hr/v2/ | Health Status


# **clear_index_cache_delete**
> IndexCacheDeletionResponse clear_index_cache_delete(indexname)

Clear Index Cache

 This method clears all standard and monitoring caches for given index. The *query parameters* allow to choose which caches should be cleared and to choose whether or not the method should wait to respond until the processing is completed.   The following caches can be cleared: + **Failed Documents**: Deletes all entries of failed documents cached for the index. + **Import statuses**: Deletes all entries of import statuses cached for the index. + **Tasks Queue**: Deletes tracking of all jobs scheduled to be performed on the index. WARNING: Does not delete the jobs themselves and does not prevent other jobs to be queued. + **Field data**: Deletes all field data on the index that are still cached. + **Queries Cache**: Deletes all queries performed on the index that are still cached. + **Requests Cache**: Deletes all requests performed on the index that are still cached.  *NOTE: Use only as a debug option!* 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import utilities_api
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
    indexname = "indexname_example" # str | 
    clean_failures = True # bool | Whether or not the document failures should be cleaned. (optional) if omitted the server will use the default value of True
    clean_imports = True # bool | Whether or not the import statuses should be cleaned. (optional) if omitted the server will use the default value of True
    clean_queues = True # bool | Whether or not the queue should be cleaned.It cannot stop running tasks or prevent new tasks to be queued. (optional) if omitted the server will use the default value of True
    clean_fielddata = True # bool | Whether or not the fields cache should be cleaned. (optional) if omitted the server will use the default value of True
    clean_queries = True # bool | Whether or not the queries cache should be cleaned. (optional) if omitted the server will use the default value of True
    clean_requests = True # bool | Whether or not the requests cache should be cleaned. (optional) if omitted the server will use the default value of True
    wait_for_completion = True # bool | Whether or not the method should wait to responduntil the processing is completed. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # Clear Index Cache
        api_response = api_instance.clear_index_cache_delete(indexname)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UtilitiesApi->clear_index_cache_delete: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Clear Index Cache
        api_response = api_instance.clear_index_cache_delete(indexname, clean_failures=clean_failures, clean_imports=clean_imports, clean_queues=clean_queues, clean_fielddata=clean_fielddata, clean_queries=clean_queries, clean_requests=clean_requests, wait_for_completion=wait_for_completion)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UtilitiesApi->clear_index_cache_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **clean_failures** | **bool**| Whether or not the document failures should be cleaned. | [optional] if omitted the server will use the default value of True
 **clean_imports** | **bool**| Whether or not the import statuses should be cleaned. | [optional] if omitted the server will use the default value of True
 **clean_queues** | **bool**| Whether or not the queue should be cleaned.It cannot stop running tasks or prevent new tasks to be queued. | [optional] if omitted the server will use the default value of True
 **clean_fielddata** | **bool**| Whether or not the fields cache should be cleaned. | [optional] if omitted the server will use the default value of True
 **clean_queries** | **bool**| Whether or not the queries cache should be cleaned. | [optional] if omitted the server will use the default value of True
 **clean_requests** | **bool**| Whether or not the requests cache should be cleaned. | [optional] if omitted the server will use the default value of True
 **wait_for_completion** | **bool**| Whether or not the method should wait to responduntil the processing is completed. | [optional] if omitted the server will use the default value of True

### Return type

[**IndexCacheDeletionResponse**](IndexCacheDeletionResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Cleared Elastic Cache And Monitoring Indices |  -  |
**500** | Internal Server Error |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_status_get**
> Check health_status_get()

Health Status

 This method checks whether the service is up and running.  Returns the *status* of the service: <code style='color: #333333; opacity: 0.9'>green</code>, <code style='color: #333333; opacity: 0.9'>yellow</code> or <code style='color: #333333; opacity: 0.9'>red</code>.  A <code style='color: #333333; opacity: 0.9'>yellow</code> status means that at least the 80% of the services are available, <code style='color: #333333; opacity: 0.9'>red</code> that something is definitely not working properly.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import utilities_api
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

### Return type

[**Check**](Check.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

