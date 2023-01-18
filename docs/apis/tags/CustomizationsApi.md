<a name="__pageTop"></a>
# inda_hr.apis.tags.customizations_api.CustomizationsApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customize_resumes_post**](#customize_resumes_post) | **post** /hr/v2/index/{indexname}/resumes/customize/ | Customize Resumes
[**get_resume_customizations_get**](#get_resume_customizations_get) | **get** /hr/v2/index/{indexname}/resumes/mapping/ | Get Resume Customizations

# **customize_resumes_post**
<a name="customize_resumes_post"></a>
> CustomizedFields customize_resumes_post(indexnamecustom_fields)

Customize Resumes

 It is possible to customize the resume structure to add fields of various types to it. These can be useful to store user information or to use refined filters in queries.  Fields can be added at anytime but **they cannot be removed** and **field types cannot be changed**! This API call accepts a list of items under *Fields*, each item has the following properties:  + **Field**: Dot-notation position of the desired field in the items. + **Type**: One of the field types described below. + **Params**: Each field type accepts different parameters and they are explained in the code blocks below it.  **String types**  The family of types for long text and singular keywords.  + *keyword*: A short string value supporting only exact-match term queries  ``` {   \"Boost\": Optional[float]          # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[str]        # Items where this field is missing or null will be indexed with this value instead } ```  + *text*: Long varied sentences and pieces of text; tokenized and analyzed, it supports complex and generic match queries  ``` {   \"Boost\": Optional[float]          # Multiplicative score boost when executing queries on this field, defaults to 1.0 } ```  + *constant_keyword*: A keyword value that must be the same in all documents where it's present  ``` {   \"Value\": Optional[str]      # The value to assign to this field in documents, it will default to the value of the first indexed document if not provided } ```  + *wildcard*: Similar to keyword values, but optimized to support wildcard queries with glob-like patterns  ``` {   \"NullValue\": Optional[str]       # Items where this field is missing or null will be indexed with this value instead } ```  **Numbers**  Numeric types used to express amounts.  + *long*: Long (64bits) integer.  ``` {   \"Boost\": Optional[float]            # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[int]          # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]            # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]   # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *integer*: Normal (32bits) integer.  ``` {   \"Boost\": Optional[float]            # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[int]          # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]            # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]   # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *short*: Short (16bits) integer.  ``` {   \"Boost\": Optional[float]            # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[int]          # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]            # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]   # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *byte*: Single byte (8bits) integer.  ``` {   \"Boost\": Optional[float]            # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[int]          # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]            # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]   # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *double*: Double precision (64bits) floating point number.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[float]            # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]       # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *float*: Single precision (32bits) floating point number.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[float]            # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]       # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *half_float*: Half precision (16bits) floating point number.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[float]            # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]       # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *scaled_float*: A floating point number backed by a long integer, scaled by a fixed double factor.  ``` {   \"ScalingFactor\": float                  # Scaling factor   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[int]              # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]       # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  **Objects and relational types**  Representations of data structures, i.e. lists and maps/dictionaries.  + *object*: A JSON object.  ``` {   \"Dynamic\": Optional[bool]   # Whether the mapping for this object can be further modified in the future, defaults to true (and you should leave it like that) } ```  + *flattened*: An entire JSON object as a single field value.  ``` {   \"Dynamic\": Optional[bool]   # Whether the mapping for this object can be further modified in the future, defaults to true (and you should leave it like that)   \"Boost\": Optional[float]    # Multiplicative score boost when executing queries on this field and its subfields, defaults to 1.0 } ```  + *nested*: A JSON object that preserves the relationship between its subfields.  ``` {   \"Dynamic\": Optional[bool]   # Whether the mapping for this object can be further modified in the future, defaults to true (and you should leave it like that) } ```  **Range types**  Fields defined as ranges of values.  + *integer_range*: A range of integers (32bits).  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  + *long_range*: A range of long (64bits) integers.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  + *float_range*: A range of standard precision (32bits) floating point numbers.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  + *double_range*: A range of double precision (64bits) floating point numbers.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  + *date_range*: A range of dates, using ISO 8601 standard ([YYYY]-[MM]-[DD]T[HH]:[MM]:[SS].[ms]+[HH:MM]).  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  + *ip_range*: A range of IP addresses.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  **Spatial data types**  + *geo_point*: Latitude and longitude points, each field must be a map/dictionary containing \"lat\" (latitude) and \"lon\" (longitude) properties, expressed with signed floating point values.  ``` {   \"IgnoreMalformed\": Optional[bool]          # Whether malformed and values should be ignored or throw an exception, which is the default   \"NullValue\": Optional[geo_point]           # Items where this field is missing or null will be indexed with this value instead } ```  + *point*: Arbitrary cartesian points, each field must be a map/dictionary containing \"x\" and \"y\" properties, expressed with signed floating point values.  ``` {   \"IgnoreMalformed\": Optional[bool]          # Whether malformed and values should be ignored or throw an exception, which is the default   \"NullValue\": Optional[point]               # Items where this field is missing or null will be indexed with this value instead } ```  **Other types**  + *binary*: Binary value encoded as a Base64 string.  + *boolean*: true and false values.  ``` {   \"Boost\": Optional[float]          # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[bool]      # Items where this field is missing or null will be indexed with this value instead } ```  + *date*: Date type, using ISO 8601 standard ([YYYY]-[MM]-[DD]T[HH]:[MM]:[SS].[ms]+[HH:MM]).  ``` {   \"Boost\": Optional[float]              # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Format\": Optional[str]               # Date format, if different from ISO 8601 (which is the default), we STRONGLY recommend to leave this untouched   \"Locale\": Optional[str]               # Locale to use for dates names or abbreviations, defaults to index locale if present or host locale otherwise   \"IgnoreMalformed\": Optional[bool]     # If true, malformed dates are ignored. If false they throw an exception. Defaults to false.   \"NullValue\": Optional[date]           # Items where this field is missing or null will be indexed with this value instead } ```  + *alias*: Defines an alias for an existing field.  ``` {   \"Path\": str          # Dot-notation position of the field the alias refers to } ```  + *ip*: IPv4 and IPv6 addresses.  ``` {   \"Boost\": Optional[float]          # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[ip]         # Items where this field is missing or null will be indexed with this value instead } ```  + *histogram*: Pre-aggregated numerical values.  + *dense_vector*: Records dense vectors of float values.  ``` {   \"Dims\": int          # The dimensionality of the vector, up to a maximum of 512 } ```  + *rank_feature*: Records a numeric feature to boost hits at query time.  ``` {   \"PositiveScoreImpact\": Optional[bool]          # Determines whether the rank_feature value affects score positively or negatively, defaults to true (positive) } ```  + *rank_features*: Records multiple named numeric features to boost hits at query time.  ``` {   \"PositiveScoreImpact\": Optional[bool]          # Determines whether the rank_feature value affects score positively or negatively, defaults to true (positive) } ``` 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import customizations_api
from inda_hr.model.custom_fields import CustomFields
from inda_hr.model.customized_fields import CustomizedFields
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
    api_instance = customizations_api.CustomizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    body = CustomFields(
        fields=[
            CustomField(
                field="field_example",
                type="type_example",
                params=dict(),
            )
        ],
    )
    try:
        # Customize Resumes
        api_response = api_instance.customize_resumes_post(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CustomizationsApi->customize_resumes_post: %s\n" % e)
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
[**CustomFields**](../../models/CustomFields.md) |  | 


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
200 | [ApiResponseFor200](#customize_resumes_post.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#customize_resumes_post.ApiResponseFor422) | Validation Error

#### customize_resumes_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**CustomizedFields**](../../models/CustomizedFields.md) |  | 


#### customize_resumes_post.ApiResponseFor422
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

# **get_resume_customizations_get**
<a name="get_resume_customizations_get"></a>
> MappingResponse get_resume_customizations_get(indexname)

Get Resume Customizations

 A function to retrieve previously customized mappings from indices. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import customizations_api
from inda_hr.model.mapping_response import MappingResponse
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
    api_instance = customizations_api.CustomizationsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
    }
    try:
        # Get Resume Customizations
        api_response = api_instance.get_resume_customizations_get(
            path_params=path_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CustomizationsApi->get_resume_customizations_get: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

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
200 | [ApiResponseFor200](#get_resume_customizations_get.ApiResponseFor200) | Successful Response
422 | [ApiResponseFor422](#get_resume_customizations_get.ApiResponseFor422) | Validation Error

#### get_resume_customizations_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MappingResponse**](../../models/MappingResponse.md) |  | 


#### get_resume_customizations_get.ApiResponseFor422
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

