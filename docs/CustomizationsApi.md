# inda_hr.CustomizationsApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**customize_resumes_post**](CustomizationsApi.md#customize_resumes_post) | **POST** /hr/v2/index/{indexname}/resumes/customize/ | Customize Resumes
[**get_resume_customizations_get**](CustomizationsApi.md#get_resume_customizations_get) | **GET** /hr/v2/index/{indexname}/resumes/mapping/ | Get Resume Customizations


# **customize_resumes_post**
> CustomizedFields customize_resumes_post(indexname, custom_fields)

Customize Resumes

 It is possible to customize the resume structure to add fields of various types to it. These can be useful to store user information or to use refined filters in queries.  Fields can be added at anytime but **they cannot be removed** and **field types cannot be changed**! This API call accepts a list of items under *Fields*, each item has the following properties:  + **Field**: Dot-notation position of the desired field in the items. + **Type**: One of the field types described below. + **Params**: Each field type accepts different parameters and they are explained in the code blocks below it.  **String types**  The family of types for long text and singular keywords.  + *keyword*: A short string value supporting only exact-match term queries  ``` {   \"Boost\": Optional[float]          # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[str]        # Items where this field is missing or null will be indexed with this value instead } ```  + *text*: Long varied sentences and pieces of text; tokenized and analyzed, it supports complex and generic match queries  ``` {   \"Boost\": Optional[float]          # Multiplicative score boost when executing queries on this field, defaults to 1.0 } ```  + *constant_keyword*: A keyword value that must be the same in all documents where it's present  ``` {   \"Value\": Optional[str]      # The value to assign to this field in documents, it will default to the value of the first indexed document if not provided } ```  + *wildcard*: Similar to keyword values, but optimized to support wildcard queries with glob-like patterns  ``` {   \"NullValue\": Optional[str]       # Items where this field is missing or null will be indexed with this value instead } ```  **Numbers**  Numeric types used to express amounts.  + *long*: Long (64bits) integer.  ``` {   \"Boost\": Optional[float]            # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[int]          # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]            # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]   # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *integer*: Normal (32bits) integer.  ``` {   \"Boost\": Optional[float]            # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[int]          # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]            # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]   # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *short*: Short (16bits) integer.  ``` {   \"Boost\": Optional[float]            # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[int]          # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]            # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]   # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *byte*: Single byte (8bits) integer.  ``` {   \"Boost\": Optional[float]            # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[int]          # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]            # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]   # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *double*: Double precision (64bits) floating point number.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[float]            # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]       # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *float*: Single precision (32bits) floating point number.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[float]            # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]       # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *half_float*: Half precision (16bits) floating point number.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[float]            # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]       # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  + *scaled_float*: A floating point number backed by a long integer, scaled by a fixed double factor.  ``` {   \"ScalingFactor\": float                  # Scaling factor   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[int]              # Items where this field is missing or null will be indexed with this value instead   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true   \"IgnoreMalformed\": Optional[bool]       # Whether malformed and uncastable values should be ignored or throw an exception, which is the default } ```  **Objects and relational types**  Representations of data structures, i.e. lists and maps/dictionaries.  + *object*: A JSON object.  ``` {   \"Dynamic\": Optional[bool]   # Whether the mapping for this object can be further modified in the future, defaults to true (and you should leave it like that) } ```  + *flattened*: An entire JSON object as a single field value.  ``` {   \"Dynamic\": Optional[bool]   # Whether the mapping for this object can be further modified in the future, defaults to true (and you should leave it like that)   \"Boost\": Optional[float]    # Multiplicative score boost when executing queries on this field and its subfields, defaults to 1.0 } ```  + *nested*: A JSON object that preserves the relationship between its subfields.  ``` {   \"Dynamic\": Optional[bool]   # Whether the mapping for this object can be further modified in the future, defaults to true (and you should leave it like that) } ```  **Range types**  Fields defined as ranges of values.  + *integer_range*: A range of integers (32bits).  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  + *long_range*: A range of long (64bits) integers.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  + *float_range*: A range of standard precision (32bits) floating point numbers.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  + *double_range*: A range of double precision (64bits) floating point numbers.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  + *date_range*: A range of dates, using ISO 8601 standard ([YYYY]-[MM]-[DD]T[HH]:[MM]:[SS].[ms]+[HH:MM]).  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  + *ip_range*: A range of IP addresses.  ``` {   \"Boost\": Optional[float]                # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Coerce\": Optional[bool]                # Whether ambiguous values should be cast to the required field type, e.g.: str(\"20\") to int(20), defaults to true } ```  **Spatial data types**  + *geo_point*: Latitude and longitude points, each field must be a map/dictionary containing \"lat\" (latitude) and \"lon\" (longitude) properties, expressed with signed floating point values.  ``` {   \"IgnoreMalformed\": Optional[bool]          # Whether malformed and values should be ignored or throw an exception, which is the default   \"NullValue\": Optional[geo_point]           # Items where this field is missing or null will be indexed with this value instead } ```  + *point*: Arbitrary cartesian points, each field must be a map/dictionary containing \"x\" and \"y\" properties, expressed with signed floating point values.  ``` {   \"IgnoreMalformed\": Optional[bool]          # Whether malformed and values should be ignored or throw an exception, which is the default   \"NullValue\": Optional[point]               # Items where this field is missing or null will be indexed with this value instead } ```  **Other types**  + *binary*: Binary value encoded as a Base64 string.  + *boolean*: true and false values.  ``` {   \"Boost\": Optional[float]          # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[bool]      # Items where this field is missing or null will be indexed with this value instead } ```  + *date*: Date type, using ISO 8601 standard ([YYYY]-[MM]-[DD]T[HH]:[MM]:[SS].[ms]+[HH:MM]).  ``` {   \"Boost\": Optional[float]              # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"Format\": Optional[str]               # Date format, if different from ISO 8601 (which is the default), we STRONGLY recommend to leave this untouched   \"Locale\": Optional[str]               # Locale to use for dates names or abbreviations, defaults to index locale if present or host locale otherwise   \"IgnoreMalformed\": Optional[bool]     # If true, malformed dates are ignored. If false they throw an exception. Defaults to false.   \"NullValue\": Optional[date]           # Items where this field is missing or null will be indexed with this value instead } ```  + *alias*: Defines an alias for an existing field.  ``` {   \"Path\": str          # Dot-notation position of the field the alias refers to } ```  + *ip*: IPv4 and IPv6 addresses.  ``` {   \"Boost\": Optional[float]          # Multiplicative score boost when executing queries on this field, defaults to 1.0   \"NullValue\": Optional[ip]         # Items where this field is missing or null will be indexed with this value instead } ```  + *histogram*: Pre-aggregated numerical values.  + *dense_vector*: Records dense vectors of float values.  ``` {   \"Dims\": int          # The dimensionality of the vector, up to a maximum of 512 } ```  + *rank_feature*: Records a numeric feature to boost hits at query time.  ``` {   \"PositiveScoreImpact\": Optional[bool]          # Determines whether the rank_feature value affects score positively or negatively, defaults to true (positive) } ```  + *rank_features*: Records multiple named numeric features to boost hits at query time.  ``` {   \"PositiveScoreImpact\": Optional[bool]          # Determines whether the rank_feature value affects score positively or negatively, defaults to true (positive) } ``` 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import customizations_api
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
    indexname = "indexname_example" # str | 
    custom_fields = CustomFields(
        fields=[
            CustomField(
                field="field_example",
                type="type_example",
                params={},
            ),
        ],
    ) # CustomFields | 

    # example passing only required values which don't have defaults set
    try:
        # Customize Resumes
        api_response = api_instance.customize_resumes_post(indexname, custom_fields)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CustomizationsApi->customize_resumes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **custom_fields** | [**CustomFields**](CustomFields.md)|  |

### Return type

[**CustomizedFields**](CustomizedFields.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_resume_customizations_get**
> MappingResponse get_resume_customizations_get(indexname)

Get Resume Customizations

 A function to retrieve previously customized mappings from indices. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import customizations_api
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
    indexname = "indexname_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get Resume Customizations
        api_response = api_instance.get_resume_customizations_get(indexname)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling CustomizationsApi->get_resume_customizations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |

### Return type

[**MappingResponse**](MappingResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

