<a name="__pageTop"></a>
# inda_hr.apis.tags.resume_parsing_api.ResumeParsingApi

All URIs are relative to *https://api.inda.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**anonymize_cv_post**](#anonymize_cv_post) | **post** /hr/v2/parse/resume/anonymize/ | Anonymize CV
[**bulk_map_entity_post**](#bulk_map_entity_post) | **post** /hr/v2/keywords/bulk/map/entity/ | Bulk Map Entity
[**map_entity_post**](#map_entity_post) | **post** /hr/v2/keywords/map/entity/ | Map Entity
[**parse_resume_post**](#parse_resume_post) | **post** /hr/v2/parse/resume/data/ | Parse Resume
[**text_extraction_post**](#text_extraction_post) | **post** /hr/v2/parse/resume/text/ | Text Extraction

# **anonymize_cv_post**
<a name="anonymize_cv_post"></a>
> DocumentAnonymizationResponse anonymize_cv_post(base_file_doc)

Anonymize CV

 This method allows you to anonymize a CV/resume (only textual documents, not scanned documents or images) by  covering the main sensitive information in the document. Output is always a PDF file containing an anonymized copy of the source document.  Masked entities are: <code style='color: #333333; opacity: 0.9'>given name</code>, <code style='color: #333333; opacity: 0.9'>family name</code>, <code style='color: #333333; opacity: 0.9'>birthdate</code>, <code style='color: #333333; opacity: 0.9'>telephone numbers</code>, <code style='color: #333333; opacity: 0.9'>emails</code>, <code style='color: #333333; opacity: 0.9'>links</code>, <code style='color: #333333; opacity: 0.9'>gender</code>, <code style='color: #333333; opacity: 0.9'>nationality</code>, <code style='color: #333333; opacity: 0.9'>profile picture</code>.  Supported extensions: <code style='color: #333333; opacity: 0.9'>pdf</code>, <code style='color: #333333; opacity: 0.9'>doc</code>, <code style='color: #333333; opacity: 0.9'>docx</code>, <code style='color: #333333; opacity: 0.9'>odt</code>, <code style='color: #333333; opacity: 0.9'>txt</code>, <code style='color: #333333; opacity: 0.9'>html</code>, <code style='color: #333333; opacity: 0.9'>pptx</code>, <code style='color: #333333; opacity: 0.9'>rtf</code>.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_parsing_api
from inda_hr.model.document_anonymization_response import DocumentAnonymizationResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_file_doc import BaseFileDoc
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
    api_instance = resume_parsing_api.ResumeParsingApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = BaseFileDoc(
        file=open('/path/to/file', 'rb'),
        file_ext="file_ext_example",
    )
    try:
        # Anonymize CV
        api_response = api_instance.anonymize_cv_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeParsingApi->anonymize_cv_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'src_lang': "it",
    }
    body = BaseFileDoc(
        file=open('/path/to/file', 'rb'),
        file_ext="file_ext_example",
    )
    try:
        # Anonymize CV
        api_response = api_instance.anonymize_cv_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeParsingApi->anonymize_cv_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseFileDoc**](../../models/BaseFileDoc.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional


# SrcLangSchema

Language to use to interpret the text. If missing, language detection is performed.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Language to use to interpret the text. If missing, language detection is performed. | must be one of ["it", "en", "fr", "pt", ] 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#anonymize_cv_post.ApiResponseFor200) | Document Successfully Processed
422 | [ApiResponseFor422](#anonymize_cv_post.ApiResponseFor422) | Unprocessable Entity
415 | [ApiResponseFor415](#anonymize_cv_post.ApiResponseFor415) | Unsupported Media Type
500 | [ApiResponseFor500](#anonymize_cv_post.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#anonymize_cv_post.ApiResponseFor503) | Service Unavailable
400 | [ApiResponseFor400](#anonymize_cv_post.ApiResponseFor400) | Bad Request

#### anonymize_cv_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**DocumentAnonymizationResponse**](../../models/DocumentAnonymizationResponse.md) |  | 


#### anonymize_cv_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### anonymize_cv_post.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### anonymize_cv_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### anonymize_cv_post.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### anonymize_cv_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **bulk_map_entity_post**
<a name="bulk_map_entity_post"></a>
> MultiEntityMapping bulk_map_entity_post(multi_entity_input)

Bulk Map Entity

 This method wraps the [Map Entity](https://api.inda.ai/hr/docs/v2/#operation/map_entity__POST) method and allows a user to send all the entities to be mapped in one API call, e.g., for pagination purposes. Note that the request does not raise any Validation Error on the input data but instead it returns all the errors in the response. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_parsing_api
from inda_hr.model.multi_entity_mapping import MultiEntityMapping
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.multi_entity_input import MultiEntityInput
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
    api_instance = resume_parsing_api.ResumeParsingApi(api_client)

    # example passing only required values which don't have defaults set
    body = MultiEntityInput(
        entities=[
            IdEntityInput(
                entity_id="entity_id_example",
                entity=EntityInput(
                    input_language="it",
                    output_language="it",
                    entity_type="entity_type_example",
                    allowed_outputs=[
                        AllowedOutput(
                            id="id_example",
                            value="value_example",
                        )
                    ],
                    input_string="input_string_example",
                    severity=0.5,
                ),
            )
        ],
    )
    try:
        # Bulk Map Entity
        api_response = api_instance.bulk_map_entity_post(
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeParsingApi->bulk_map_entity_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MultiEntityInput**](../../models/MultiEntityInput.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#bulk_map_entity_post.ApiResponseFor200) | Entities Successfully Mapped
422 | [ApiResponseFor422](#bulk_map_entity_post.ApiResponseFor422) | Validation Error

#### bulk_map_entity_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MultiEntityMapping**](../../models/MultiEntityMapping.md) |  | 


#### bulk_map_entity_post.ApiResponseFor422
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

# **map_entity_post**
<a name="map_entity_post"></a>
> EntityMapping map_entity_post(entity_input)

Map Entity

 This method maps an input string (ideally an entity extracted with the [Parse Resume](https://api.inda.ai/hr/docs/v2/#operation/parse_resume__POST) method) to the most similar string among a list of strings chosen by the user *(AllowedOutputs)*.  Note that, after a best match has been identified, it is actually presented as output only when it passes a *similarity check*, which takes into account the similarity of this best match with the input string, but also the similarity of the other elements of *allowed outputs* with the input string (namely, if many allowed outputs have a comparable similarity level, the *similarity check* is not passed, because there is not a clear winner). When the severity check is passed, the *id* of the best match is given in output (see the payload and response examples on the right); otherwise, an empty string is returned instead of the *id*. The severity of the similarity check can be controlled via the *severity* parameter, which takes value between <code style='color: #333333; opacity: 0.9'>0</code> and <code style='color: #333333; opacity: 0.9'>1</code>: a user who prefers to obtain the best match also when there is not guarantee it actually corresponds to the input string should set *severity* to a low value (i.e., close to <code style='color: #333333; opacity: 0.9'>0</code>); vice versa, a user who prefers to have a response only when there is a high confidence in the correspondence should set *severity* to a large value (i.e., close to <code style='color: #333333; opacity: 0.9'>1</code>); an intermediate value (such as the default value <code style='color: #333333; opacity: 0.9'>0.5</code>) is appropriate in many situations.  The method has been specialized for different entity types, and for each of them it performs an analysis optimized over the specific type. The currently supported entity types are <code style='color: #333333; opacity: 0.9'>Data.EducationExperiences.Organization.OrganizationName</code> and <code style='color: #333333; opacity: 0.9'>Data.EducationExperiences.EducationTitle</code>. If the entity type is a string that does not match any of the supported entity types, the mapping is performed using a non-specialized method. 

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_parsing_api
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.entity_input import EntityInput
from inda_hr.model.entity_mapping import EntityMapping
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
    api_instance = resume_parsing_api.ResumeParsingApi(api_client)

    # example passing only required values which don't have defaults set
    body = EntityInput(
        input_language="it",
        output_language="it",
        entity_type="entity_type_example",
        allowed_outputs=[
            AllowedOutput(
                id="id_example",
                value="value_example",
            )
        ],
        input_string="input_string_example",
        severity=0.5,
    )
    try:
        # Map Entity
        api_response = api_instance.map_entity_post(
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeParsingApi->map_entity_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityInput**](../../models/EntityInput.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#map_entity_post.ApiResponseFor200) | Entity Successfully Mapped
400 | [ApiResponseFor400](#map_entity_post.ApiResponseFor400) | Bad Request
422 | [ApiResponseFor422](#map_entity_post.ApiResponseFor422) | Validation Error

#### map_entity_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**EntityMapping**](../../models/EntityMapping.md) |  | 


#### map_entity_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### map_entity_post.ApiResponseFor422
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

# **parse_resume_post**
<a name="parse_resume_post"></a>
> ExtractionItem parse_resume_post(base_file)

Parse Resume

 This method performs the *Information Extraction* from a resume, i.e., it recognizes the *named entities* contained in a given resume and reconstructs the relations between them, returning a structured information in the form of a json file. The method requires in input the *binary* and the *extension* of the file and automatically performs many steps: (*i*) Document Layout Analysis, (*ii*) Optical Character Recognition (if the input document is an image), (*iii*) Text Extraction, (*iv*) Named Entity Recognition, (*v*) Relation Extraction, and, finally, (*vi*) Face Recognition (which is carried out to identify, if present, the candidate photo).  The information provided in the output (see the schema below and the example on the right) can be used as structured data input for the [Add Resume](https://api.inda.ai/hr/docs/v2/#operation/add_resume__POST) method (some adjustments may be required).  The allowed file extensions are  <code style='color: #333333; opacity: 0.9'>pdf</code>, <code style='color: #333333; opacity: 0.9'>doc</code>, <code style='color: #333333; opacity: 0.9'>docx</code>, <code style='color: #333333; opacity: 0.9'>odt</code>, <code style='color: #333333; opacity: 0.9'>txt</code>, <code style='color: #333333; opacity: 0.9'>html</code>, <code style='color: #333333; opacity: 0.9'>pptx</code>, <code style='color: #333333; opacity: 0.9'>rtf</code>, <code style='color: #333333; opacity: 0.9'>jpg</code>, <code style='color: #333333; opacity: 0.9'>jpeg</code>, <code style='color: #333333; opacity: 0.9'>png</code>, <code style='color: #333333; opacity: 0.9'>tif</code>, <code style='color: #333333; opacity: 0.9'>tiff</code> .  Please consider to use the [Info Extraction Feedback](https://api.inda.ai/hr/docs/v2/#operation/info_extraction_feedback__POST) to inform us about differences  between user's expectations and the actual data provided as output by INDA engine. It is very useful to improve our algorithms' performances.  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_parsing_api
from inda_hr.model.extraction_item import ExtractionItem
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_file import BaseFile
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
    api_instance = resume_parsing_api.ResumeParsingApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = BaseFile(
        file=open('/path/to/file', 'rb'),
        file_ext="file_ext_example",
    )
    try:
        # Parse Resume
        api_response = api_instance.parse_resume_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeParsingApi->parse_resume_post: %s\n" % e)

    # example passing only optional values
    query_params = {
        'src_lang': "it",
        'dst_lang': "dst_lang_example",
        'graphics': False,
    }
    body = BaseFile(
        file=open('/path/to/file', 'rb'),
        file_ext="file_ext_example",
    )
    try:
        # Parse Resume
        api_response = api_instance.parse_resume_post(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeParsingApi->parse_resume_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseFile**](../../models/BaseFile.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
src_lang | SrcLangSchema | | optional
dst_lang | DstLangSchema | | optional
graphics | GraphicsSchema | | optional


# SrcLangSchema

Optional. Language to use to extract data from the *Attachment.CV.File*.If missing, the detected language from the input file text is assumed as `src_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Language to use to extract data from the *Attachment.CV.File*.If missing, the detected language from the input file text is assumed as &#x60;src_lang&#x60;. | must be one of ["it", "en", "fr", "pt", ] 

# DstLangSchema

Optional. Destination language in which the following *Data* entities are translated: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the input or detected `src_lang` is assumed as `dst_lang`.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  | Optional. Destination language in which the following *Data* entities are translated: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the input or detected &#x60;src_lang&#x60; is assumed as &#x60;dst_lang&#x60;. | 

# GraphicsSchema

Whether to read skill graphs such as bars, pie charts, and symbols.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
bool,  | BoolClass,  | Whether to read skill graphs such as bars, pie charts, and symbols. | if omitted the server will use the default value of False

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#parse_resume_post.ApiResponseFor200) | Document Successfully Processed
422 | [ApiResponseFor422](#parse_resume_post.ApiResponseFor422) | Unprocessable Entity
415 | [ApiResponseFor415](#parse_resume_post.ApiResponseFor415) | Unsupported Media Type
500 | [ApiResponseFor500](#parse_resume_post.ApiResponseFor500) | Internal Server Error
503 | [ApiResponseFor503](#parse_resume_post.ApiResponseFor503) | Service Unavailable
400 | [ApiResponseFor400](#parse_resume_post.ApiResponseFor400) | Bad Request

#### parse_resume_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ExtractionItem**](../../models/ExtractionItem.md) |  | 


#### parse_resume_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### parse_resume_post.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### parse_resume_post.ApiResponseFor500
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor500ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor500ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### parse_resume_post.ApiResponseFor503
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor503ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor503ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### parse_resume_post.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **text_extraction_post**
<a name="text_extraction_post"></a>
> TextResponse text_extraction_post(base_file)

Text Extraction

 This method extracts the text from a resume by performing the first steps of [Parse Resume](https://api.inda.ai/hr/docs/v2/#operation/parse_resume__POST). In particular, the method requires in input the *binary* and the *extension* of the file and automatically performs (*i*) Document Layout Analysis, (*ii*) Optical Character Recognition (if the input document is an image), and (*iii*) Text Extraction.  The allowed file extensions are  <code style='color: #333333; opacity: 0.9'>pdf</code>, <code style='color: #333333; opacity: 0.9'>doc</code>, <code style='color: #333333; opacity: 0.9'>docx</code>, <code style='color: #333333; opacity: 0.9'>odt</code>, <code style='color: #333333; opacity: 0.9'>txt</code>, <code style='color: #333333; opacity: 0.9'>html</code>, <code style='color: #333333; opacity: 0.9'>pptx</code>, <code style='color: #333333; opacity: 0.9'>rtf</code>, <code style='color: #333333; opacity: 0.9'>jpg</code>, <code style='color: #333333; opacity: 0.9'>jpeg</code>, <code style='color: #333333; opacity: 0.9'>png</code>, <code style='color: #333333; opacity: 0.9'>tif</code>, <code style='color: #333333; opacity: 0.9'>tiff</code> .  

### Example

* Bearer Authentication (APIKey):
```python
import inda_hr
from inda_hr.apis.tags import resume_parsing_api
from inda_hr.model.text_response import TextResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.base_file import BaseFile
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
    api_instance = resume_parsing_api.ResumeParsingApi(api_client)

    # example passing only required values which don't have defaults set
    body = BaseFile(
        file=open('/path/to/file', 'rb'),
        file_ext="file_ext_example",
    )
    try:
        # Text Extraction
        api_response = api_instance.text_extraction_post(
            body=body,
        )
        pprint(api_response)
    except inda_hr.ApiException as e:
        print("Exception when calling ResumeParsingApi->text_extraction_post: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**BaseFile**](../../models/BaseFile.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#text_extraction_post.ApiResponseFor200) | Successfully Parsed Text
422 | [ApiResponseFor422](#text_extraction_post.ApiResponseFor422) | Unprocessable Entity
415 | [ApiResponseFor415](#text_extraction_post.ApiResponseFor415) | Unsupported Media Type

#### text_extraction_post.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**TextResponse**](../../models/TextResponse.md) |  | 


#### text_extraction_post.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


#### text_extraction_post.ApiResponseFor415
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor415ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor415ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**ErrorModel**](../../models/ErrorModel.md) |  | 


### Authorization

[APIKey](../../../README.md#APIKey)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

