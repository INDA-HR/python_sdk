"""
    INDA HR - INtelligent Data Analysis for HR

     # Introduction  **INDA (INtelligent Data Analysis)** is an [Intervieweb](https://www.intervieweb.it/hrm/)  AI solution provided as a RESTful API.  The INDA pricing model is *credits-based*, which means that a certain number of credits is associated to each API request. Hence, users have to purchase a certain amount of credits (established according to their needs) which will be reduced  at each API call. INDA accepts and processes a user's request only if their credits quota is grater than - or,  at least, equal to - the number of credits required by that request. To obtain further details on the pricing, please visit our [site](https://inda.ai) or contact us.    INDA HR embraces a wide range of functionalities to manage the main elements of a recruitment process:   + [**candidate**](https://api.inda.ai/hr/docs/v2/#tag/Resume-Management) (hereafter also referred to as **resume** or **applicant**), or rather a  person looking for a job;  + [**job advertisement**](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Management) (hereafter also referred to as **job ad**), which is a document   that collects all the main information and details about a job vacancy;  + [**application**](https://api.inda.ai/hr/docs/v2/#tag/Application-Management), that binds candidates to job ads; it is generated whenever a  candidate applies for a job.  Each of them has a specific set of methods that grants users the ability to create, read, update and delete the relative  documents, plus some special features based on AI approaches (such as *document parsing* or *semantic search*). They can be explored in their respective sections.  Data about the listed document types can be enriched by connecting them to other INDA supported entities, such as  [**companies**](https://api.inda.ai/hr/docs/v2/#tag/Company-Management) and [**universities**](https://api.inda.ai/hr/docs/v2/#tag/Universities), so that recruiters may  get a better and more detailed idea on the candidates' experiences and acquired skills.  All the functionalities mentioned above are meant to help recruiters during the talent acquisition process,  by exploiting the power of AI systems. Among the advantages a recruiter has by using this kind of systems, tackling the bias problem is surely one of the  most relevant. Bias in recruitment is a serious issue that affect both recruiters and candidates, since it may cause wrong hiring  decisions. As we care a lot about this problem, we are constantly working on reduce the bias in original data so that INDA  results may be as fair as possible. As of now, in order to tackle the bias issue, INDA automatically ignores specific fields (such as name, gender, age  and nationality) during the initial processing of each candidate data.  Furthermore, we decided to let users collect data of various types, including personal or sensitive details, but we  do not allow their usage if it is different from statistical purposes; our aim is to discourage recruiters from  focusing on candidates' personal information, and to put their attention on the candidate's skills and abilities.    We want to help recruiters to prevent any kind of bias while searching for the most valuable candidates they really need.    The following documentation is addressed both to developers, in order to provide all technical details for INDA integration, and to managers, to guide them in the exploration of the implementation possibilities.  The host of the API is [https://api.inda.ai/hr/v2/](https://api.inda.ai/hr/v2/). We recommend to check the API version and build (displayed near the documentation title). You can contact us at support@intervieweb.it in case of problems, suggestions, or particular needs.  The search panel on the left can be used to navigate through the documentation and provides an overview of the API structure. On the right, you can find (*i*) the url of the method, (*ii*) an example of request body (if present), and (*iii*) an example of response for each response code. Finally, in the central section of each API method, you can find (*i*) a general description of the purpose of the method, (*ii*) details on parameters and request body schema (if present), and (*iii*) details on response schema, error models, and error codes.    # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: info@intervieweb.it
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from inda_hr.api_client import ApiClient, Endpoint as _Endpoint
from inda_hr.model_utils import (  # noqa: F401
    check_allowed_values, check_validations, date, datetime, file_type,
    none_type, validate_and_convert_types)
from inda_hr.model.base_file import BaseFile
from inda_hr.model.base_file_doc import BaseFileDoc
from inda_hr.model.document_anonymization_response import DocumentAnonymizationResponse
from inda_hr.model.entity_input import EntityInput
from inda_hr.model.entity_mapping import EntityMapping
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.extraction_item import ExtractionItem
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.multi_entity_input import MultiEntityInput
from inda_hr.model.multi_entity_mapping import MultiEntityMapping
from inda_hr.model.text_response import TextResponse


class ResumeParsingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.anonymize_cv_post_endpoint = _Endpoint(
            settings={
                'response_type': (DocumentAnonymizationResponse, ),
                'auth': ['APIKey'],
                'endpoint_path': '/hr/v2/parse/resume/anonymize/',
                'operation_id': 'anonymize_cv_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'base_file_doc',
                    'src_lang',
                ],
                'required': [
                    'base_file_doc',
                ],
                'nullable': [],
                'enum': [
                    'src_lang',
                ],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {
                    ('src_lang', ): {
                        "IT": "it",
                        "EN": "en",
                        "FR": "fr",
                        "PT": "pt"
                    },
                },
                'openapi_types': {
                    'base_file_doc': (BaseFileDoc, ),
                    'src_lang': (str, ),
                },
                'attribute_map': {
                    'src_lang': 'src_lang',
                },
                'location_map': {
                    'base_file_doc': 'body',
                    'src_lang': 'query',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)
        self.bulk_map_entity_post_endpoint = _Endpoint(
            settings={
                'response_type': (MultiEntityMapping, ),
                'auth': ['APIKey'],
                'endpoint_path': '/hr/v2/keywords/bulk/map/entity/',
                'operation_id': 'bulk_map_entity_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'multi_entity_input',
                ],
                'required': [
                    'multi_entity_input',
                ],
                'nullable': [],
                'enum': [],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {},
                'openapi_types': {
                    'multi_entity_input': (MultiEntityInput, ),
                },
                'attribute_map': {},
                'location_map': {
                    'multi_entity_input': 'body',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)
        self.map_entity_post_endpoint = _Endpoint(settings={
            'response_type': (EntityMapping, ),
            'auth': ['APIKey'],
            'endpoint_path':
            '/hr/v2/keywords/map/entity/',
            'operation_id':
            'map_entity_post',
            'http_method':
            'POST',
            'servers':
            None,
        },
                                                  params_map={
                                                      'all': [
                                                          'entity_input',
                                                      ],
                                                      'required': [
                                                          'entity_input',
                                                      ],
                                                      'nullable': [],
                                                      'enum': [],
                                                      'validation': []
                                                  },
                                                  root_map={
                                                      'validations': {},
                                                      'allowed_values': {},
                                                      'openapi_types': {
                                                          'entity_input':
                                                          (EntityInput, ),
                                                      },
                                                      'attribute_map': {},
                                                      'location_map': {
                                                          'entity_input':
                                                          'body',
                                                      },
                                                      'collection_format_map':
                                                      {}
                                                  },
                                                  headers_map={
                                                      'accept':
                                                      ['application/json'],
                                                      'content_type':
                                                      ['application/json']
                                                  },
                                                  api_client=api_client)
        self.parse_resume_post_endpoint = _Endpoint(
            settings={
                'response_type': (ExtractionItem, ),
                'auth': ['APIKey'],
                'endpoint_path': '/hr/v2/parse/resume/data/',
                'operation_id': 'parse_resume_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'base_file',
                    'src_lang',
                    'dst_lang',
                    'graphics',
                ],
                'required': [
                    'base_file',
                ],
                'nullable': [],
                'enum': [
                    'src_lang',
                ],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {
                    ('src_lang', ): {
                        "IT": "it",
                        "EN": "en",
                        "FR": "fr",
                        "PT": "pt"
                    },
                },
                'openapi_types': {
                    'base_file': (BaseFile, ),
                    'src_lang': (str, ),
                    'dst_lang': (str, ),
                    'graphics': (bool, ),
                },
                'attribute_map': {
                    'src_lang': 'src_lang',
                    'dst_lang': 'dst_lang',
                    'graphics': 'graphics',
                },
                'location_map': {
                    'base_file': 'body',
                    'src_lang': 'query',
                    'dst_lang': 'query',
                    'graphics': 'query',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)
        self.text_extraction_post_endpoint = _Endpoint(
            settings={
                'response_type': (TextResponse, ),
                'auth': ['APIKey'],
                'endpoint_path': '/hr/v2/parse/resume/text/',
                'operation_id': 'text_extraction_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'base_file',
                ],
                'required': [
                    'base_file',
                ],
                'nullable': [],
                'enum': [],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {},
                'openapi_types': {
                    'base_file': (BaseFile, ),
                },
                'attribute_map': {},
                'location_map': {
                    'base_file': 'body',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)

    def anonymize_cv_post(self, base_file_doc, **kwargs):
        """Anonymize CV  # noqa: E501

         This method allows you to anonymize a CV/resume (only textual documents, not scanned documents or images) by  covering the main sensitive information in the document. Output is always a PDF file containing an anonymized copy of the source document.  Masked entities are: <code style='color: #333333; opacity: 0.9'>given name</code>, <code style='color: #333333; opacity: 0.9'>family name</code>, <code style='color: #333333; opacity: 0.9'>birthdate</code>, <code style='color: #333333; opacity: 0.9'>telephone numbers</code>, <code style='color: #333333; opacity: 0.9'>emails</code>, <code style='color: #333333; opacity: 0.9'>links</code>, <code style='color: #333333; opacity: 0.9'>gender</code>, <code style='color: #333333; opacity: 0.9'>nationality</code>, <code style='color: #333333; opacity: 0.9'>profile picture</code>.  Supported extensions: <code style='color: #333333; opacity: 0.9'>pdf</code>, <code style='color: #333333; opacity: 0.9'>doc</code>, <code style='color: #333333; opacity: 0.9'>docx</code>, <code style='color: #333333; opacity: 0.9'>odt</code>, <code style='color: #333333; opacity: 0.9'>txt</code>, <code style='color: #333333; opacity: 0.9'>html</code>, <code style='color: #333333; opacity: 0.9'>pptx</code>, <code style='color: #333333; opacity: 0.9'>rtf</code>.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.anonymize_cv_post(base_file_doc, async_req=True)
        >>> result = thread.get()

        Args:
            base_file_doc (BaseFileDoc):

        Keyword Args:
            src_lang (str): Language to use to interpret the text. If missing, language detection is performed.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            DocumentAnonymizationResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_spec_property_naming'] = kwargs.get('_spec_property_naming',
                                                     False)
        kwargs['_content_type'] = kwargs.get('_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['base_file_doc'] = \
            base_file_doc
        return self.anonymize_cv_post_endpoint.call_with_http_info(**kwargs)

    def bulk_map_entity_post(self, multi_entity_input, **kwargs):
        """Bulk Map Entity  # noqa: E501

         This method wraps the [Map Entity](https://api.inda.ai/hr/docs/v2/#operation/map_entity__POST) method and allows a user to send all the entities to be mapped in one API call, e.g., for pagination purposes. Note that the request does not raise any Validation Error on the input data but instead it returns all the errors in the response.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bulk_map_entity_post(multi_entity_input, async_req=True)
        >>> result = thread.get()

        Args:
            multi_entity_input (MultiEntityInput):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            MultiEntityMapping
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_spec_property_naming'] = kwargs.get('_spec_property_naming',
                                                     False)
        kwargs['_content_type'] = kwargs.get('_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['multi_entity_input'] = \
            multi_entity_input
        return self.bulk_map_entity_post_endpoint.call_with_http_info(**kwargs)

    def map_entity_post(self, entity_input, **kwargs):
        """Map Entity  # noqa: E501

         This method maps an input string (ideally an entity extracted with the [Parse Resume](https://api.inda.ai/hr/docs/v2/#operation/parse_resume__POST) method) to the most similar string among a list of strings chosen by the user *(AllowedOutputs)*.  Note that, after a best match has been identified, it is actually presented as output only when it passes a *similarity check*, which takes into account the similarity of this best match with the input string, but also the similarity of the other elements of *allowed outputs* with the input string (namely, if many allowed outputs have a comparable similarity level, the *similarity check* is not passed, because there is not a clear winner). When the severity check is passed, the *id* of the best match is given in output (see the payload and response examples on the right); otherwise, an empty string is returned instead of the *id*. The severity of the similarity check can be controlled via the *severity* parameter, which takes value between <code style='color: #333333; opacity: 0.9'>0</code> and <code style='color: #333333; opacity: 0.9'>1</code>: a user who prefers to obtain the best match also when there is not guarantee it actually corresponds to the input string should set *severity* to a low value (i.e., close to <code style='color: #333333; opacity: 0.9'>0</code>); vice versa, a user who prefers to have a response only when there is a high confidence in the correspondence should set *severity* to a large value (i.e., close to <code style='color: #333333; opacity: 0.9'>1</code>); an intermediate value (such as the default value <code style='color: #333333; opacity: 0.9'>0.5</code>) is appropriate in many situations.  The method has been specialized for different entity types, and for each of them it performs an analysis optimized over the specific type. The currently supported entity types are <code style='color: #333333; opacity: 0.9'>Data.EducationExperiences.Organization.OrganizationName</code> and <code style='color: #333333; opacity: 0.9'>Data.EducationExperiences.EducationTitle</code>. If the entity type is a string that does not match any of the supported entity types, the mapping is performed using a non-specialized method.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.map_entity_post(entity_input, async_req=True)
        >>> result = thread.get()

        Args:
            entity_input (EntityInput):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            EntityMapping
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_spec_property_naming'] = kwargs.get('_spec_property_naming',
                                                     False)
        kwargs['_content_type'] = kwargs.get('_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['entity_input'] = \
            entity_input
        return self.map_entity_post_endpoint.call_with_http_info(**kwargs)

    def parse_resume_post(self, base_file, **kwargs):
        """Parse Resume  # noqa: E501

         This method performs the *Information Extraction* from a resume, i.e., it recognizes the *named entities* contained in a given resume and reconstructs the relations between them, returning a structured information in the form of a json file. The method requires in input the *binary* and the *extension* of the file and automatically performs many steps: (*i*) Document Layout Analysis, (*ii*) Optical Character Recognition (if the input document is an image), (*iii*) Text Extraction, (*iv*) Named Entity Recognition, (*v*) Relation Extraction, and, finally, (*vi*) Face Recognition (which is carried out to identify, if present, the candidate photo).  The information provided in the output (see the schema below and the example on the right) can be used as structured data input for the [Add Resume](https://api.inda.ai/hr/docs/v2/#operation/add_resume__POST) method (some adjustments may be required).  The allowed file extensions are  <code style='color: #333333; opacity: 0.9'>pdf</code>, <code style='color: #333333; opacity: 0.9'>doc</code>, <code style='color: #333333; opacity: 0.9'>docx</code>, <code style='color: #333333; opacity: 0.9'>odt</code>, <code style='color: #333333; opacity: 0.9'>txt</code>, <code style='color: #333333; opacity: 0.9'>html</code>, <code style='color: #333333; opacity: 0.9'>pptx</code>, <code style='color: #333333; opacity: 0.9'>rtf</code>, <code style='color: #333333; opacity: 0.9'>jpg</code>, <code style='color: #333333; opacity: 0.9'>jpeg</code>, <code style='color: #333333; opacity: 0.9'>png</code>, <code style='color: #333333; opacity: 0.9'>tif</code>, <code style='color: #333333; opacity: 0.9'>tiff</code> .  Please consider to use the [Info Extraction Feedback](https://api.inda.ai/hr/docs/v2/#operation/info_extraction_feedback__POST) to inform us about differences  between user's expectations and the actual data provided as output by INDA engine. It is very useful to improve our algorithms' performances.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.parse_resume_post(base_file, async_req=True)
        >>> result = thread.get()

        Args:
            base_file (BaseFile):

        Keyword Args:
            src_lang (str): Optional. Language to use to extract data from the *Attachment.CV.File*.If missing, the detected language from the input file text is assumed as `src_lang`.. [optional]
            dst_lang (str): Optional. Destination language in which the following *Data* entities are translated: *Skills*, *WorkExperiences.Skills*, *JobTitles*, *WorkExperiences.PositionTitle* and *Languages*.If missing, the input or detected `src_lang` is assumed as `dst_lang`.. [optional]
            graphics (bool): Whether to read skill graphs such as bars, pie charts, and symbols.. [optional] if omitted the server will use the default value of False
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            ExtractionItem
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_spec_property_naming'] = kwargs.get('_spec_property_naming',
                                                     False)
        kwargs['_content_type'] = kwargs.get('_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['base_file'] = \
            base_file
        return self.parse_resume_post_endpoint.call_with_http_info(**kwargs)

    def text_extraction_post(self, base_file, **kwargs):
        """Text Extraction  # noqa: E501

         This method extracts the text from a resume by performing the first steps of [Parse Resume](https://api.inda.ai/hr/docs/v2/#operation/parse_resume__POST). In particular, the method requires in input the *binary* and the *extension* of the file and automatically performs (*i*) Document Layout Analysis, (*ii*) Optical Character Recognition (if the input document is an image), and (*iii*) Text Extraction.  The allowed file extensions are  <code style='color: #333333; opacity: 0.9'>pdf</code>, <code style='color: #333333; opacity: 0.9'>doc</code>, <code style='color: #333333; opacity: 0.9'>docx</code>, <code style='color: #333333; opacity: 0.9'>odt</code>, <code style='color: #333333; opacity: 0.9'>txt</code>, <code style='color: #333333; opacity: 0.9'>html</code>, <code style='color: #333333; opacity: 0.9'>pptx</code>, <code style='color: #333333; opacity: 0.9'>rtf</code>, <code style='color: #333333; opacity: 0.9'>jpg</code>, <code style='color: #333333; opacity: 0.9'>jpeg</code>, <code style='color: #333333; opacity: 0.9'>png</code>, <code style='color: #333333; opacity: 0.9'>tif</code>, <code style='color: #333333; opacity: 0.9'>tiff</code> .    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.text_extraction_post(base_file, async_req=True)
        >>> result = thread.get()

        Args:
            base_file (BaseFile):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            TextResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get('async_req', False)
        kwargs['_return_http_data_only'] = kwargs.get('_return_http_data_only',
                                                      True)
        kwargs['_preload_content'] = kwargs.get('_preload_content', True)
        kwargs['_request_timeout'] = kwargs.get('_request_timeout', None)
        kwargs['_check_input_type'] = kwargs.get('_check_input_type', True)
        kwargs['_check_return_type'] = kwargs.get('_check_return_type', True)
        kwargs['_spec_property_naming'] = kwargs.get('_spec_property_naming',
                                                     False)
        kwargs['_content_type'] = kwargs.get('_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['base_file'] = \
            base_file
        return self.text_extraction_post_endpoint.call_with_http_info(**kwargs)
