# inda_hr.CreditsManagementApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_credits_post**](CreditsManagementApi.md#search_credits_post) | **POST** /hr/v2/index/{indexname}/credits/ | Search Credits


# **search_credits_post**
> IndexCreditsInfo search_credits_post(indexname, search_credits_request)

Search Credits

 Returns the available credits and the history of the API calls already made for the purchased services belonging to *indexname*.  This method will accept an application/json body with optional fields, which allow users to filter or aggregate data according to their needs.  In principle, API call names are the ones shown in this documentation; refer to each method section for additional  details and/or possible changes.  

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import credits_management_api
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
    indexname = "indexname_example" # str | 
    search_credits_request = SearchCreditsRequest(
        info=[
            "info_example",
        ],
        history=SemanticHistoryBody(
            api_calls=[
                "api_calls_example",
            ],
            datetime=DateBody(
                begin="begin_example",
                end="end_example",
            ),
            group_by=[
                "group_by_example",
            ],
            scroll_id="scroll_id_example",
            detail=True,
            advanced=True,
            price=True,
        ),
    ) # SearchCreditsRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Search Credits
        api_response = api_instance.search_credits_post(indexname, search_credits_request)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CreditsManagementApi->search_credits_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **search_credits_request** | [**SearchCreditsRequest**](SearchCreditsRequest.md)|  |

### Return type

[**IndexCreditsInfo**](IndexCreditsInfo.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | Not Found |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

