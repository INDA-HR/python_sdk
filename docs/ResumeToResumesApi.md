# inda_hr.ResumeToResumesApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**similar_resumes_post**](ResumeToResumesApi.md#similar_resumes_post) | **POST** /hr/v2/index/{indexname}/resumes/matching/resume/{resume_id}/ | Similar Resumes


# **similar_resumes_post**
> FoundDocsResponse similar_resumes_post(indexname, resume_id, similar_docs_search_query)

Similar Resumes

Setting as arguments the number *size* of documents to be retrieved and the number *offset* to be skipped, this method returns similar documents to resume *resume_id* in the index *indexname*.

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import resume_to_resumes_api
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
    indexname = "indexname_example" # str | 
    resume_id = "resume_id_example" # str | 
    similar_docs_search_query = SimilarDocsSearchQuery(
        query_filters=QueryFilters(
            must=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            should=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            must_not=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
            filter=[
                FilterField(
                    field="field_example",
                    type="type_example",
                    value={},
                ),
            ],
        ),
    ) # SimilarDocsSearchQuery | 
    size = 5 # int | Number of documents to return. (optional) if omitted the server will use the default value of 5
    offset = 0 # int | Number of documents to skip. (optional) if omitted the server will use the default value of 0
    min_score = 0 # float | Optional. Minimum pertinence score. (optional) if omitted the server will use the default value of 0
    dst_lang = [
        "es",
    ] # [str] | Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Similar Resumes
        api_response = api_instance.similar_resumes_post(indexname, resume_id, similar_docs_search_query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeToResumesApi->similar_resumes_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Similar Resumes
        api_response = api_instance.similar_resumes_post(indexname, resume_id, similar_docs_search_query, size=size, offset=offset, min_score=min_score, dst_lang=dst_lang)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeToResumesApi->similar_resumes_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **indexname** | **str**|  |
 **resume_id** | **str**|  |
 **similar_docs_search_query** | [**SimilarDocsSearchQuery**](SimilarDocsSearchQuery.md)|  |
 **size** | **int**| Number of documents to return. | [optional] if omitted the server will use the default value of 5
 **offset** | **int**| Number of documents to skip. | [optional] if omitted the server will use the default value of 0
 **min_score** | **float**| Optional. Minimum pertinence score. | [optional] if omitted the server will use the default value of 0
 **dst_lang** | **[str]**| Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results. | [optional]

### Return type

[**FoundDocsResponse**](FoundDocsResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully Found Similar Docs |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

