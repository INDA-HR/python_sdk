# inda_hr.UniversitiesApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_university_get**](UniversitiesApi.md#get_university_get) | **GET** /hr/v2/university/{university_id}/ | Get University
[**university_autocomplete_get**](UniversitiesApi.md#university_autocomplete_get) | **GET** /hr/v2/university/name/search/autocomplete/ | University Autocomplete


# **get_university_get**
> GetUniversityResponse get_university_get(university_id)

Get University

This method retrieves the *university'* full data through a UUID *university_id*.

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import universities_api
from inda_hr.model.get_university_response import GetUniversityResponse
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
    api_instance = universities_api.UniversitiesApi(api_client)
    university_id = "university_id_example" # str | 
    minimal = False # bool | If set to True the API returns only the Overview of the University. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get University
        api_response = api_instance.get_university_get(university_id)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UniversitiesApi->get_university_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get University
        api_response = api_instance.get_university_get(university_id, minimal=minimal)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UniversitiesApi->get_university_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **university_id** | **str**|  |
 **minimal** | **bool**| If set to True the API returns only the Overview of the University. | [optional] if omitted the server will use the default value of False

### Return type

[**GetUniversityResponse**](GetUniversityResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Found University |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **university_autocomplete_get**
> UniversityAutocompleteResponse university_autocomplete_get(term)

University Autocomplete

This method performs an autocomplete search based on the best matching *universities'* official name, alternative name  and acronym. It returns a minimal set of data for each *university* and its *ID*, which it is meant to be used as  *university_id* to retrieve the full data through the [Get University](https://api.inda.ai/hr/docs/v2/#operation/get_university__GET) method.  You can personalize both the autocomplete algorithm used to retrieve the list *universities* and the location search  filters. The latter allows to perform searches on both the *university'* headquarter and branches geo location. At least one of the two should match the user geo location query in order to show the *university* into the result  response.

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import universities_api
from inda_hr.model.university_autocomplete_response import UniversityAutocompleteResponse
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
    api_instance = universities_api.UniversitiesApi(api_client)
    term = "term_example" # str | Token to be completed
    size = 10 # int | Response size. (optional) if omitted the server will use the default value of 10
    token_order = "any" # str | Whether to autocomplete the term in a sequential way or not. The default *any* value guarantees good performances as well as flexible results. (optional) if omitted the server will use the default value of "any"
    fuzzy = False # bool | Fuzzy search. If *True* performs a fuzzy search with max edits set to 2. (optional) if omitted the server will use the default value of False
    city = [
        "city_example",
    ] # [str] | Generally performing better using original language queries. (optional)
    country = [
        "country_example",
    ] # [str] | Generally performing better using english queries. (optional)
    country_code = [
        "AW",
    ] # [str] | Standard upper case Country Codes. (optional)
    lat = -90.0 # float |  (optional)
    lon = -180.0 # float |  (optional)
    pivot = 30 # int | When results are *pivot* kilometers away from *origin*, which is the geo point corresponding to the tuple *(lat, lon)*, have score 0.5. (optional) if omitted the server will use the default value of 30
    include_branches = True # bool | Whether to include *University*'s branches in the location filtering or not. (optional) if omitted the server will use the default value of True

    # example passing only required values which don't have defaults set
    try:
        # University Autocomplete
        api_response = api_instance.university_autocomplete_get(term)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UniversitiesApi->university_autocomplete_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # University Autocomplete
        api_response = api_instance.university_autocomplete_get(term, size=size, token_order=token_order, fuzzy=fuzzy, city=city, country=country, country_code=country_code, lat=lat, lon=lon, pivot=pivot, include_branches=include_branches)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UniversitiesApi->university_autocomplete_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **term** | **str**| Token to be completed |
 **size** | **int**| Response size. | [optional] if omitted the server will use the default value of 10
 **token_order** | **str**| Whether to autocomplete the term in a sequential way or not. The default *any* value guarantees good performances as well as flexible results. | [optional] if omitted the server will use the default value of "any"
 **fuzzy** | **bool**| Fuzzy search. If *True* performs a fuzzy search with max edits set to 2. | [optional] if omitted the server will use the default value of False
 **city** | **[str]**| Generally performing better using original language queries. | [optional]
 **country** | **[str]**| Generally performing better using english queries. | [optional]
 **country_code** | **[str]**| Standard upper case Country Codes. | [optional]
 **lat** | **float**|  | [optional]
 **lon** | **float**|  | [optional]
 **pivot** | **int**| When results are *pivot* kilometers away from *origin*, which is the geo point corresponding to the tuple *(lat, lon)*, have score 0.5. | [optional] if omitted the server will use the default value of 30
 **include_branches** | **bool**| Whether to include *University*&#39;s branches in the location filtering or not. | [optional] if omitted the server will use the default value of True

### Return type

[**UniversityAutocompleteResponse**](UniversityAutocompleteResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Found Universities |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

