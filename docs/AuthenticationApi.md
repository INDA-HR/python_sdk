# inda_hr.AuthenticationApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_in_post**](AuthenticationApi.md#log_in_post) | **POST** /hr/v2/auth/login/ | Log In


# **log_in_post**
> TokenResponse log_in_post(login_data)

Log In

 This method allows a user to log into the service and receive access credentials in the form of a bearer token. The token expires after  *ExpiresIn* seconds, as detailed in the response.  

### Example


```python
import time
import inda_hr
from inda_hr.api import authentication_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.login_data import LoginData
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.token_response import TokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.inda.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = inda_hr.Configuration(
    host = "https://api.inda.ai"
)


# Enter a context with an instance of the API client
with inda_hr.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = authentication_api.AuthenticationApi(api_client)
    login_data = LoginData(
        tenant="tenant_example",
        password="password_example",
        email="email_example",
    ) # LoginData | 

    # example passing only required values which don't have defaults set
    try:
        # Log In
        api_response = api_instance.log_in_post(login_data)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling AuthenticationApi->log_in_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_data** | [**LoginData**](LoginData.md)|  |

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login Successful |  -  |
**403** | Forbidden |  -  |
**503** | Service Unavailable |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

