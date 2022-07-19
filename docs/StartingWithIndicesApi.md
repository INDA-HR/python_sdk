# inda_hr.StartingWithIndicesApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**most_recent_resumes_get**](StartingWithIndicesApi.md#most_recent_resumes_get) | **GET** /hr/v2/index/{indexname}/resumes/latest/ | Most Recent Resumes
[**stats_index_get**](StartingWithIndicesApi.md#stats_index_get) | **GET** /hr/v2/index/{indexname}/stats/ | Stats Index


# **most_recent_resumes_get**
> MostRecentResponse most_recent_resumes_get(indexname)

Most Recent Resumes

 Returns the *size* documents into the index *indexname* sorted by the field *sort_by* in the order *sort_order*. In the response, *Hits* indicates the number of documents retrieved, while *Total* indicates the number of documents in the index. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import starting_with_indices_api
from inda_hr.model.most_recent_response import MostRecentResponse
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
    api_instance = starting_with_indices_api.StartingWithIndicesApi(api_client)
    indexname = "indexname_example" # str | 
    sort_by = "CreationDate" # str | The field the results will be sorted by. Available options: <code style='color: #333333; opacity: 0.9'>\"CreationDate\"</code>, <code style='color: #333333; opacity: 0.9'>\"LastModified\"</code> (optional) if omitted the server will use the default value of "CreationDate"
    sort_order = "desc" # str | The sort_order option can have the following values: <code style='color: #333333; opacity: 0.9'>\"asc\"</code>, <code style='color: #333333; opacity: 0.9'>\"desc\"</code>. The former will sort in ascending order, the latter in descending order. (optional) if omitted the server will use the default value of "desc"
    size = 20 # int | Number of resumes to be returned (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    try:
        # Most Recent Resumes
        api_response = api_instance.most_recent_resumes_get(indexname)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StartingWithIndicesApi->most_recent_resumes_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Most Recent Resumes
        api_response = api_instance.most_recent_resumes_get(indexname, sort_by=sort_by, sort_order=sort_order, size=size)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StartingWithIndicesApi->most_recent_resumes_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **sort_by** | **str**| The field the results will be sorted by. Available options: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;\&quot;CreationDate\&quot;&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;\&quot;LastModified\&quot;&lt;/code&gt; | [optional] if omitted the server will use the default value of "CreationDate"
 **sort_order** | **str**| The sort_order option can have the following values: &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;\&quot;asc\&quot;&lt;/code&gt;, &lt;code style&#x3D;&#39;color: #333333; opacity: 0.9&#39;&gt;\&quot;desc\&quot;&lt;/code&gt;. The former will sort in ascending order, the latter in descending order. | [optional] if omitted the server will use the default value of "desc"
 **size** | **int**| Number of resumes to be returned | [optional] if omitted the server will use the default value of 20

### Return type

[**MostRecentResponse**](MostRecentResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stats_index_get**
> StatsIndex stats_index_get(indexname)

Stats Index

  This method returns the number of documents present in *indexname*,  grouped by document types. To fetch information about a specific document type, please use the *doc_type* query parameter; allowed values are: + <code style='color: #333333; opacity: 0.9'>resume</code> for [resumes](https://api.inda.ai/hr/docs/v2/#tag/Resume-Management); + <code style='color: #333333; opacity: 0.9'>job-ad</code> for [job adverts](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Management); + <code style='color: #333333; opacity: 0.9'>application</code> for [applications](https://api.inda.ai/hr/docs/v2/#tag/Application-Management). 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import starting_with_indices_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.stats_index import StatsIndex
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
    api_instance = starting_with_indices_api.StartingWithIndicesApi(api_client)
    indexname = "indexname_example" # str | 
    doc_type = "resume" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Stats Index
        api_response = api_instance.stats_index_get(indexname)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StartingWithIndicesApi->stats_index_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stats Index
        api_response = api_instance.stats_index_get(indexname, doc_type=doc_type)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StartingWithIndicesApi->stats_index_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **doc_type** | **str**|  | [optional]

### Return type

[**StatsIndex**](StatsIndex.md)

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
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

