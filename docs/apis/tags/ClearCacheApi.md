<a name="__pageTop"></a>
# inda_hr.apis.tags.clear_cache_api.ClearCacheApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_search_results_delete**](#clear_search_results_delete) | **delete** /hr/v2/index/{indexname}/resumes/search/scroll/ | Clear Search Results

# **clear_search_results_delete**
<a name="clear_search_results_delete"></a>
> CacheDeletion clear_search_results_delete(indexnamesearch_id)

Clear Search Results

This method deletes the *SearchID* and the cache previously (and eventually) created by all those API calls that have a *SearchID* key in their response. They include: + [Full-Text Search on Resumes](https://api.inda.ai/hr/docs/v2/#operation/full-text_search_on_resumes__POST) + [Full-Text Search on JobAds](https://api.inda.ai/hr/docs/v2/#operation/full-text_search_on_jobads__POST) + [Search Resumes](https://api.inda.ai/hr/docs/v2/#operation/search_resumes__POST) + [Search Applicants](https://api.inda.ai/hr/docs/v2/#operation/search_applicants__POST) + [Search Applications](https://api.inda.ai/hr/docs/v2/#operation/search_applications__POST) + [Get JobAds](https://api.inda.ai/hr/docs/v2/#operation/get_jobads__GET) + [Get Applicants](https://api.inda.ai/hr/docs/v2/#operation/get_applicants__GET) + [Get Applications](https://api.inda.ai/hr/docs/v2/#operation/get_applications__GET)  When a user leaves a search page linked to INDA API, it is a good practice to delete the search cache using this method.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import clear_cache_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'search_id': "search_id_example",
    }
    try:
        # Clear Search Results
        api_response = api_instance.clear_search_results_delete(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ClearCacheApi->clear_search_results_delete: %s\n" % e)
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
search_id | SearchIdSchema | | 


# SearchIdSchema

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
200 | [ApiResponseFor200](#clear_search_results_delete.ApiResponseFor200) | Scroll ID Successfully Deleted
422 | [ApiResponseFor422](#clear_search_results_delete.ApiResponseFor422) | Validation Error

#### clear_search_results_delete.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CacheDeletion**](../../models/CacheDeletion.md) |  | 


#### clear_search_results_delete.ApiResponseFor422
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

