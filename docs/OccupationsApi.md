# inda_hr.OccupationsApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**similar_jobtitles_get**](OccupationsApi.md#similar_jobtitles_get) | **GET** /hr/v2/occupations/similar/semantic/ | Similar JobTitles


# **similar_jobtitles_get**
> SimilarEntitiesResponse similar_jobtitles_get(query)

Similar JobTitles

 This method returns the *size* most similar job titles found in the knowledge base with respect to the input *jobtitle*.  The similarity of each result to the input job title is rated with a score between <code style='color: #333333; opacity: 0.9'>0</code> (minimum similarity) and <code style='color: #333333; opacity: 0.9'>1</code> (maximum similarity). This method can be used to perform a *keyword expansion*: expanding a job title with its synonyms or semantically similar job titles may be useful, for instance, to improve a job description or to perform a more flexible search with respect to a traditional word match or boolean search system.  This method returns a dictionary with keys *Hits* (the number of job titles returned) and *Out*, which is a list of dictionaries with two keys: the first key (*Term*) contains the proposed job title, while the second one (*Score*)  contains its similarity score, as described above. The parameter *min_score* set the threshold for the similarity score, below which the output skills are discarded; its default value is <code style='color: #333333; opacity: 0.9'>0.5</code>.  Note that the number of retrieved similar job titles may be smaller than *size* when the minimum score is larger than  <code style='color: #333333; opacity: 0.9'>0</code> or when the searched job title is particularly uncommon. 

### Example

* Bearer Authentication (APIKey):

```python
import time
import inda_hr
from inda_hr.api import occupations_api
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
    query = "query_example" # str | Input job title to be analyzed
    size = 10 # int | Number of similar job titles to return. (optional) if omitted the server will use the default value of 10
    min_score = 0.5 # float | Minimum pertinence score. (optional) if omitted the server will use the default value of 0.5
    lang = "it" # str | Language of the jobtitle. (optional) if omitted the server will use the default value of "it"

    # example passing only required values which don't have defaults set
    try:
        # Similar JobTitles
        api_response = api_instance.similar_jobtitles_get(query)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling OccupationsApi->similar_jobtitles_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Similar JobTitles
        api_response = api_instance.similar_jobtitles_get(query, size=size, min_score=min_score, lang=lang)
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling OccupationsApi->similar_jobtitles_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**| Input job title to be analyzed |
 **size** | **int**| Number of similar job titles to return. | [optional] if omitted the server will use the default value of 10
 **min_score** | **float**| Minimum pertinence score. | [optional] if omitted the server will use the default value of 0.5
 **lang** | **str**| Language of the jobtitle. | [optional] if omitted the server will use the default value of "it"

### Return type

[**SimilarEntitiesResponse**](SimilarEntitiesResponse.md)

### Authorization

[APIKey](../README.md#APIKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request Successfully Processed |  -  |
**400** | Bad Request |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

