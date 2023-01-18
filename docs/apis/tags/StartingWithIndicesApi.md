<a name="__pageTop"></a>
# inda_hr.apis.tags.starting_with_indices_api.StartingWithIndicesApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**most_recent_resumes_get**](#most_recent_resumes_get) | **get** /hr/v2/index/{indexname}/resumes/latest/ | Most Recent Resumes
[**stats_index_get**](#stats_index_get) | **get** /hr/v2/index/{indexname}/stats/ | Stats Index

# **most_recent_resumes_get**
<a name="most_recent_resumes_get"></a>
> MostRecentResponse most_recent_resumes_get(indexname)

Most Recent Resumes

 Returns the *size* documents into the index *indexname* sorted by the field *sort_by* in the order *sort_order*. In the response, *Hits* indicates the number of documents retrieved, while *Total* indicates the number of documents in the index. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import starting_with_indices_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    try:
        # Most Recent Resumes
        api_response = api_instance.most_recent_resumes_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StartingWithIndicesApi->most_recent_resumes_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'sort_by': "CreationDate",
        'sort_order': "desc",
        'size': 20,
    }
    try:
        # Most Recent Resumes
        api_response = api_instance.most_recent_resumes_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StartingWithIndicesApi->most_recent_resumes_get: %s\n" % e)
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
sort_by | SortBySchema | | optional
sort_order | SortOrderSchema | | optional
size | SizeSchema | | optional


# SortBySchema

The field the results will be sorted by. Available options: <code style='color: #333333; opacity: 0.9'>\"CreationDate\"</code>, <code style='color: #333333; opacity: 0.9'>\"LastModified\"</code>

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The field the results will be sorted by. Available options: &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;\&quot;CreationDate\&quot;&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;\&quot;LastModified\&quot;&lt;/code&gt; | must be one of ["CreationDate", "LastModified", ] if omitted the server will use the default value of "CreationDate"

# SortOrderSchema

The sort_order option can have the following values: <code style='color: #333333; opacity: 0.9'>\"asc\"</code>, <code style='color: #333333; opacity: 0.9'>\"desc\"</code>. The former will sort in ascending order, the latter in descending order.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | The sort_order option can have the following values: &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;\&quot;asc\&quot;&lt;/code&gt;, &lt;code style&#x3D;&#x27;color: #333333; opacity: 0.9&#x27;&gt;\&quot;desc\&quot;&lt;/code&gt;. The former will sort in ascending order, the latter in descending order. | must be one of ["desc", "asc", ] if omitted the server will use the default value of "desc"

# SizeSchema

Number of resumes to be returned

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Number of resumes to be returned | if omitted the server will use the default value of 20

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
200 | [ApiResponseFor200](#most_recent_resumes_get.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#most_recent_resumes_get.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#most_recent_resumes_get.ApiResponseFor404) | Not Found
503 | [ApiResponseFor503](#most_recent_resumes_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#most_recent_resumes_get.ApiResponseFor422) | Validation Error

#### most_recent_resumes_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MostRecentResponse**](../../models/MostRecentResponse.md) |  | 


#### most_recent_resumes_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### most_recent_resumes_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### most_recent_resumes_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### most_recent_resumes_get.ApiResponseFor422
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

# **stats_index_get**
<a name="stats_index_get"></a>
> StatsIndex stats_index_get(indexname)

Stats Index

  This method returns the number of documents present in *indexname*,  grouped by document types. To fetch information about a specific document type, please use the *doc_type* query parameter; allowed values are: + <code style='color: #333333; opacity: 0.9'>resume</code> for [resumes](https://api.inda.ai/hr/docs/v2/#tag/Resume-Management); + <code style='color: #333333; opacity: 0.9'>job-ad</code> for [job adverts](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Management); + <code style='color: #333333; opacity: 0.9'>application</code> for [applications](https://api.inda.ai/hr/docs/v2/#tag/Application-Management). 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import starting_with_indices_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
    }
    try:
        # Stats Index
        api_response = api_instance.stats_index_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StartingWithIndicesApi->stats_index_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
    }
    query_params = {
        'doc_type': "resume",
    }
    try:
        # Stats Index
        api_response = api_instance.stats_index_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling StartingWithIndicesApi->stats_index_get: %s\n" % e)
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
doc_type | DocTypeSchema | | optional


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
200 | [ApiResponseFor200](#stats_index_get.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#stats_index_get.ApiResponseFor404) | Not Found
503 | [ApiResponseFor503](#stats_index_get.ApiResponseFor503) | Service Unavailable
422 | [ApiResponseFor422](#stats_index_get.ApiResponseFor422) | Validation Error

#### stats_index_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**StatsIndex**](../../models/StatsIndex.md) |  | 


#### stats_index_get.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### stats_index_get.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### stats_index_get.ApiResponseFor422
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

