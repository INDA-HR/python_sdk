<a name="__pageTop"></a>
# inda_hr.apis.tags.occupations_api.OccupationsApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**similar_jobtitles_get**](#similar_jobtitles_get) | **get** /hr/v2/occupations/similar/semantic/ | Similar JobTitles

# **similar_jobtitles_get**
<a name="similar_jobtitles_get"></a>
> SimilarEntitiesResponse similar_jobtitles_get(query)

Similar JobTitles

 This method returns the *size* most similar job titles found in the knowledge base with respect to the input *jobtitle*.  The similarity of each result to the input job title is rated with a score between <code style='color: #333333; opacity: 0.9'>0</code> (minimum similarity) and <code style='color: #333333; opacity: 0.9'>1</code> (maximum similarity). This method can be used to perform a *keyword expansion*: expanding a job title with its synonyms or semantically similar job titles may be useful, for instance, to improve a job description or to perform a more flexible search with respect to a traditional word match or boolean search system.  This method returns a dictionary with keys *Hits* (the number of job titles returned) and *Out*, which is a list of dictionaries with two keys: the first key (*Term*) contains the proposed job title, while the second one (*Score*)  contains its similarity score, as described above. The parameter *min_score* set the threshold for the similarity score, below which the output skills are discarded; its default value is <code style='color: #333333; opacity: 0.9'>0.5</code>.  Note that the number of retrieved similar job titles may be smaller than *size* when the minimum score is larger than <code style='color: #333333; opacity: 0.9'>0</code> or when the searched job title is particularly uncommon. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import occupations_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.similar_entities_response import SimilarEntitiesResponse
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
    api_instance = occupations_api.OccupationsApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
        'query': "query_example",
    }
    try:
        # Similar JobTitles
        api_response = api_instance.similar_jobtitles_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling OccupationsApi->similar_jobtitles_get: %s\n" % e)

    # example passing only optional values
    query_params = {
        'size': 10,
        'min_score': 0.5,
        'query': "query_example",
        'src_lang': "it",
        'dst_lang': "it",
    }
    try:
        # Similar JobTitles
        api_response = api_instance.similar_jobtitles_get(
            query_params=query_params,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling OccupationsApi->similar_jobtitles_get: %s\n" % e)
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
size | SizeSchema | | optional
min_score | MinScoreSchema | | optional
query | QuerySchema | | 
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional


# SizeSchema

Number of similar job titles to return.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  | Number of similar job titles to return. | if omitted the server will use the default value of 10

# MinScoreSchema

Minimum pertinence score.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int, float,  | decimal.Decimal,  | Minimum pertinence score. | if omitted the server will use the default value of 0.5

# QuerySchema

Input job title to be analyzed

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Input job title to be analyzed | 

# SrcLangSchema

Optional. Language of the input job titles.If missing, the detected language is assumed as `src_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Language of the input job titles.If missing, the detected language is assumed as &#x60;src_lang&#x60;. | must be one of ["it", "en", "es", "pt", "de", "fr", ] 

# DstLangSchema

Optional. Destination language in which the output job titles are translated.If missing, the input or detected `src_lang` is assumed as `dst_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Destination language in which the output job titles are translated.If missing, the input or detected &#x60;src_lang&#x60; is assumed as &#x60;dst_lang&#x60;. | must be one of ["it", "en", "es", "pt", "de", "fr", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#similar_jobtitles_get.ApiResponseFor200) | Request Successfully Processed
400 | [ApiResponseFor400](#similar_jobtitles_get.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#similar_jobtitles_get.ApiResponseFor422) | Validation Error

#### similar_jobtitles_get.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**SimilarEntitiesResponse**](../../models/SimilarEntitiesResponse.md) |  | 


#### similar_jobtitles_get.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### similar_jobtitles_get.ApiResponseFor422
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

