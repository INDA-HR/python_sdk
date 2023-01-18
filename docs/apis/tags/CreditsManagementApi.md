<a name="__pageTop"></a>
# inda_hr.apis.tags.credits_management_api.CreditsManagementApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_credits_post**](#search_credits_post) | **post** /hr/v2/index/{indexname}/credits/ | Search Credits

# **search_credits_post**
<a name="search_credits_post"></a>
> IndexCreditsInfo search_credits_post(indexnamesearch_credits_request)

Search Credits

Returns the available credits and the history of the API calls already made for the purchased services belonging to *indexname*.  This method will accept an application/json body with optional fields, which allow users to filter or aggregate data according to their needs.  In principle, API call names are the ones shown in this documentation; refer to each method section for additional  details and/or possible changes.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import credits_management_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.index_credits_info import IndexCreditsInfo
from inda_hr.model.search_credits_request import SearchCreditsRequest
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
    api_instance = credits_management_api.CreditsManagementApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    body = SearchCreditsRequest(
        info=[
            "info_example"
        ],
        history=SemanticHistoryBody(
            api_calls=[
                "api_calls_example"
            ],
            datetime=DateBody(
                begin="begin_example",
                end="end_example",
            ),
            group_by=[
                "group_by_example"
            ],
            scroll_id="scroll_id_example",
            detail=True,
            advanced=True,
            price=True,
        ),
    )
    try:
        # Search Credits
        api_response = api_instance.search_credits_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CreditsManagementApi->search_credits_post: %s\n" % e)
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
[**SearchCreditsRequest**](../../models/SearchCreditsRequest.md) |  | 


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
200 | [ApiResponseFor200](#search_credits_post.ApiResponseFor200) | Successful Response
404 | [ApiResponseFor404](#search_credits_post.ApiResponseFor404) | Not Found
400 | [ApiResponseFor400](#search_credits_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#search_credits_post.ApiResponseFor422) | Validation Error

#### search_credits_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**IndexCreditsInfo**](../../models/IndexCreditsInfo.md) |  | 


#### search_credits_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_credits_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### search_credits_post.ApiResponseFor422
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

