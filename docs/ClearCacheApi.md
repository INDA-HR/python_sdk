# inda_hr.ClearCacheApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_search_results_delete**](ClearCacheApi.md#clear_search_results_delete) | **DELETE** /hr/v2/index/{indexname}/resumes/search/scroll/ | Clear Search Results


# **clear_search_results_delete**
> CacheDeletion clear_search_results_delete(indexname, search_id)

Clear Search Results

 This method deletes the *SearchID* and the cache previously (and eventually) created by all those API calls that have a *SearchID* key in their response. They include: + [Full-Text Search on Resumes](https://api.inda.ai/hr/docs/v2/#operation/full-text_search_on_resumes__POST) + [Full-Text Search on JobAds](https://api.inda.ai/hr/docs/v2/#operation/full-text_search_on_jobads__POST) + [Search Resumes](https://api.inda.ai/hr/docs/v2/#operation/search_resumes__POST) + [Search Applicants](https://api.inda.ai/hr/docs/v2/#operation/search_applicants__POST) + [Search Applications](https://api.inda.ai/hr/docs/v2/#operation/search_applications__POST) + [Get JobAds](https://api.inda.ai/hr/docs/v2/#operation/get_jobads__GET) + [Get Applicants](https://api.inda.ai/hr/docs/v2/#operation/get_applicants__GET) + [Get Applications](https://api.inda.ai/hr/docs/v2/#operation/get_applications__GET)  When a user leaves a search page linked to INDA API, it is a good practice to delete the search cache using this method.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import clear_cache_api
from inda_hr.model.cache_deletion import CacheDeletion
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
    api_instance = clear_cache_api.ClearCacheApi(api_client)
    indexname = "indexname_example" # str | 
    search_id = "search_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Clear Search Results
        api_response = api_instance.clear_search_results_delete(indexname, search_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ClearCacheApi->clear_search_results_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **search_id** | **str**|  |

### Return type

[**CacheDeletion**](CacheDeletion.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scroll ID Successfully Deleted |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

