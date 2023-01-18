<a name="__pageTop"></a>
# inda_hr.apis.tags.resume_to_resumes_api.ResumeToResumesApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**similar_resumes_post**](#similar_resumes_post) | **post** /hr/v2/index/{indexname}/resumes/matching/resume/{resume_id}/ | Similar Resumes

# **similar_resumes_post**
<a name="similar_resumes_post"></a>
> FoundDocsResponse similar_resumes_post(indexnameresume_idsimilar_docs_search_query)

Similar Resumes

Setting as arguments the number *size* of documents to be retrieved and the number *offset* to be skipped, this method returns similar documents to resume *resume_id* in the index *indexname*.

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_to_resumes_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.found_docs_response import FoundDocsResponse
from inda_hr.model.similar_docs_search_query import SimilarDocsSearchQuery
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
    api_instance = resume_to_resumes_api.ResumeToResumesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
    }
    body = SimilarDocsSearchQuery(
        query_filters=QueryFilters(
            must=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value=dict(),
                )
            ],
            should=[
                FilterField()
            ],
            must_not=[
                FilterField()
            ],
            filter=[
                FilterField()
            ],
        ),
    )
    try:
        # Similar Resumes
        api_response = api_instance.similar_resumes_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeToResumesApi->similar_resumes_post: %s\n" % e)

    # example passing only optional values
    path_params = {
        'indexname': "indexname_example",
        'resume_id': "resume_id_example",
    }
    query_params = {
        'size': 5,
        'offset': 0,
        'min_score': 0,
        'dst_lang': [
        "es"
    ],
    }
    body = SimilarDocsSearchQuery(
        query_filters=QueryFilters(
            must=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value=dict(),
                )
            ],
            should=[
                FilterField()
            ],
            must_not=[
                FilterField()
            ],
            filter=[
                FilterField()
            ],
        ),
    )
    try:
        # Similar Resumes
        api_response = api_instance.similar_resumes_post(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeToResumesApi->similar_resumes_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
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
[**SimilarDocsSearchQuery**](../../models/SimilarDocsSearchQuery.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
size | SizeSchema | | optional
offset | OffsetSchema | | optional
min_score | MinScoreSchema | | optional
dst_lang | DstLangSchema | | optional


# SizeSchema

Number of documents to return.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Number of documents to return. | if omitted the server will use the default value of 5

# OffsetSchema

Number of documents to skip.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Number of documents to skip. | if omitted the server will use the default value of 0

# MinScoreSchema

Optional. Minimum pertinence score.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Optional. Minimum pertinence score. | if omitted the server will use the default value of 0

# DstLangSchema

Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | must be one of ["es", "de", "pt", "fr", "en", "it", ] 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
indexname | IndexnameSchema | | 
resume_id | ResumeIdSchema | | 

# IndexnameSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ResumeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#similar_resumes_post.ApiResponseFor200) | Successfully Found Similar Docs
400 | [ApiResponseFor400](#similar_resumes_post.ApiResponseFor400) | Bad Request
404 | [ApiResponseFor404](#similar_resumes_post.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#similar_resumes_post.ApiResponseFor422) | Validation Error

#### similar_resumes_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**FoundDocsResponse**](../../models/FoundDocsResponse.md) |  | 


#### similar_resumes_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### similar_resumes_post.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### similar_resumes_post.ApiResponseFor422
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

