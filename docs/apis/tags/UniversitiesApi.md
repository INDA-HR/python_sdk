<a name="__pageTop"></a>
# inda_hr.apis.tags.universities_api.UniversitiesApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_university_get**](#get_university_get) | **get** /hr/v2/university/{university_id}/ | Get University
[**university_autocomplete_get**](#university_autocomplete_get) | **get** /hr/v2/university/name/search/autocomplete/ | University Autocomplete

# **get_university_get**
<a name="get_university_get"></a>
> GetUniversityResponse get_university_get(university_id)

Get University

This method retrieves the *university'* full data through a UUID *university_id*.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import universities_api
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

    # example passing only required values which don't have defaults set
    path_params = {
        'university_id': "university_id_example",
    }
    query_params = {
    }
    try:
        # Get University
        api_response = api_instance.get_university_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UniversitiesApi->get_university_get: %s\n" % e)

    # example passing only optional values
    path_params = {
        'university_id': "university_id_example",
    }
    query_params = {
        'minimal': False,
    }
    try:
        # Get University
        api_response = api_instance.get_university_get(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UniversitiesApi->get_university_get: %s\n" % e)
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
minimal | MinimalSchema | | optional


# MinimalSchema

If set to True the API returns only the Overview of the University.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | If set to True the API returns only the Overview of the University. | if omitted the server will use the default value of False

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
university_id | UniversityIdSchema | | 

# UniversityIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_university_get.ApiResponseFor200) | Successfully Found University
422 | [ApiResponseFor422](#get_university_get.ApiResponseFor422) | Validation Error

#### get_university_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**GetUniversityResponse**](../../models/GetUniversityResponse.md) |  | 


#### get_university_get.ApiResponseFor422
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

# **university_autocomplete_get**
<a name="university_autocomplete_get"></a>
> UniversityAutocompleteResponse university_autocomplete_get(term)

University Autocomplete

This method performs an autocomplete search based on the best matching *universities'* official name, alternative name  and acronym. It returns a minimal set of data for each *university* and its *ID*, which it is meant to be used as  *university_id* to retrieve the full data through the [Get University](https://api.inda.ai/hr/docs/v2/#operation/get_university__GET) method.  You can personalize both the autocomplete algorithm used to retrieve the list *universities* and the location search  filters. The latter allows to perform searches on both the *university'* headquarter and branches geo location. At least one of the two should match the user geo location query in order to show the *university* into the result  response.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import universities_api
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

    # example passing only required values which don't have defaults set
    query_params = {
        'term': "term_example",
    }
    try:
        # University Autocomplete
        api_response = api_instance.university_autocomplete_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UniversitiesApi->university_autocomplete_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'term': "term_example",
        'size': 10,
        'token_order': "any",
        'fuzzy': False,
        'city': [
        "city_example"
    ],
        'country': [
        "country_example"
    ],
        'country_code': [
        "AW"
    ],
        'lat': -90.0,
        'lon': -180.0,
        'pivot': 30,
        'include_branches': True,
    }
    try:
        # University Autocomplete
        api_response = api_instance.university_autocomplete_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling UniversitiesApi->university_autocomplete_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
term | TermSchema | | 
size | SizeSchema | | optional
token_order | TokenOrderSchema | | optional
fuzzy | FuzzySchema | | optional
city | CitySchema | | optional
country | CountrySchema | | optional
country_code | CountryCodeSchema | | optional
lat | LatSchema | | optional
lon | LonSchema | | optional
pivot | PivotSchema | | optional
include_branches | IncludeBranchesSchema | | optional


# TermSchema

Token to be completed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Token to be completed | 

# SizeSchema

Response size.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Response size. | if omitted the server will use the default value of 10

# TokenOrderSchema

Whether to autocomplete the term in a sequential way or not. The default *any* value guarantees good performances as well as flexible results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Whether to autocomplete the term in a sequential way or not. The default *any* value guarantees good performances as well as flexible results. | must be one of ["any", "sequential", ] if omitted the server will use the default value of "any"

# FuzzySchema

Fuzzy search. If *True* performs a fuzzy search with max edits set to 2.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Fuzzy search. If *True* performs a fuzzy search with max edits set to 2. | if omitted the server will use the default value of False

# CitySchema

Generally performing better using original language queries.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Generally performing better using original language queries. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# CountrySchema

Generally performing better using english queries.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Generally performing better using english queries. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# CountryCodeSchema

Standard upper case Country Codes.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Standard upper case Country Codes. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["AW", "AF", "AO", "AI", "AX", "AL", "AD", "AE", "AR", "AM", "AS", "AQ", "TF", "AG", "AU", "AT", "AZ", "BI", "BE", "BJ", "BQ", "BF", "BD", "BG", "BH", "BS", "BA", "BL", "BY", "BZ", "BM", "BO", "BR", "BB", "BN", "BT", "BV", "BW", "CF", "CA", "CC", "CH", "CL", "CN", "CI", "CM", "CD", "CG", "CK", "CO", "KM", "CV", "CR", "CU", "CW", "CX", "KY", "CY", "CZ", "DE", "DJ", "DM", "DK", "DO", "DZ", "EC", "EG", "ER", "EH", "ES", "EE", "ET", "FI", "FJ", "FK", "FR", "FO", "FM", "GA", "GB", "GE", "GG", "GH", "GI", "GN", "GP", "GM", "GW", "GQ", "GR", "GD", "GL", "GT", "GF", "GU", "GY", "HK", "HM", "HN", "HR", "HT", "HU", "ID", "IM", "IN", "IO", "IE", "IR", "IQ", "IS", "IL", "IT", "JM", "JE", "JO", "JP", "KZ", "KE", "KG", "KH", "KI", "KN", "KR", "KW", "LA", "LB", "LR", "LY", "LC", "LI", "LK", "LS", "LT", "LU", "LV", "MO", "MF", "MA", "MC", "MD", "MG", "MV", "MX", "MH", "MK", "ML", "MT", "MM", "ME", "MN", "MP", "MZ", "MR", "MS", "MQ", "MU", "MW", "MY", "YT", "NA", "NC", "NE", "NF", "NG", "NI", "NU", "NL", "NO", "NP", "NR", "NZ", "OM", "PK", "PA", "PN", "PE", "PH", "PW", "PG", "PL", "PR", "KP", "PT", "PY", "PS", "PF", "QA", "RE", "RO", "RU", "RW", "SA", "SD", "SN", "SG", "GS", "SH", "SJ", "SB", "SL", "SV", "SM", "SO", "PM", "RS", "SS", "ST", "SR", "SK", "SI", "SE", "SZ", "SX", "SC", "SY", "TC", "TD", "TG", "TH", "TJ", "TK", "TM", "TL", "TO", "TT", "TN", "TR", "TV", "TW", "TZ", "UG", "UA", "UM", "UY", "US", "UZ", "VA", "VC", "VE", "VG", "VI", "VN", "VU", "WF", "WS", "YE", "ZA", "ZM", "ZW", ] 

# LatSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# LonSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  |  | 

# PivotSchema

When results are *pivot* kilometers away from *origin*, which is the geo point corresponding to the tuple *(lat, lon)*, have score 0.5.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | When results are *pivot* kilometers away from *origin*, which is the geo point corresponding to the tuple *(lat, lon)*, have score 0.5. | if omitted the server will use the default value of 30

# IncludeBranchesSchema

Whether to include *University*'s branches in the location filtering or not.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Whether to include *University*&#x27;s branches in the location filtering or not. | if omitted the server will use the default value of True

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#university_autocomplete_get.ApiResponseFor200) | Successfully Found Universities
422 | [ApiResponseFor422](#university_autocomplete_get.ApiResponseFor422) | Validation Error

#### university_autocomplete_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**UniversityAutocompleteResponse**](../../models/UniversityAutocompleteResponse.md) |  | 


#### university_autocomplete_get.ApiResponseFor422
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

