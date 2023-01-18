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
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.found_docs_response import FoundDocsResponse
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.similar_docs_search_query import SimilarDocsSearchQuery


class ResumeToResumesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.similar_resumes_post_endpoint = _Endpoint(
            settings={
                'response_type': (FoundDocsResponse, ),
                'auth': ['APIKey'],
                'endpoint_path':
                '/hr/v2/index/{indexname}/resumes/matching/resume/{resume_id}/',
                'operation_id': 'similar_resumes_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'indexname',
                    'resume_id',
                    'similar_docs_search_query',
                    'size',
                    'offset',
                    'min_score',
                    'dst_lang',
                ],
                'required': [
                    'indexname',
                    'resume_id',
                    'similar_docs_search_query',
                ],
                'nullable': [],
                'enum': [
                    'dst_lang',
                ],
                'validation': [
                    'size',
                    'offset',
                    'min_score',
                    'dst_lang',
                ]
            },
            root_map={
                'validations': {
                    ('size', ): {
                        'inclusive_maximum': 20,
                    },
                    ('offset', ): {
                        'inclusive_maximum': 20,
                        'inclusive_minimum': 0,
                    },
                    ('min_score', ): {
                        'inclusive_minimum': 0.0,
                    },
                    ('dst_lang', ): {
                        'max_items': 6,
                        'min_items': 0,
                    },
                },
                'allowed_values': {
                    ('dst_lang', ): {
                        "ES": "es",
                        "DE": "de",
                        "PT": "pt",
                        "FR": "fr",
                        "EN": "en",
                        "IT": "it"
                    },
                },
                'openapi_types': {
                    'indexname': (str, ),
                    'resume_id': (str, ),
                    'similar_docs_search_query': (SimilarDocsSearchQuery, ),
                    'size': (int, ),
                    'offset': (int, ),
                    'min_score': (float, ),
                    'dst_lang': ([str], ),
                },
                'attribute_map': {
                    'indexname': 'indexname',
                    'resume_id': 'resume_id',
                    'size': 'size',
                    'offset': 'offset',
                    'min_score': 'min_score',
                    'dst_lang': 'dst_lang',
                },
                'location_map': {
                    'indexname': 'path',
                    'resume_id': 'path',
                    'similar_docs_search_query': 'body',
                    'size': 'query',
                    'offset': 'query',
                    'min_score': 'query',
                    'dst_lang': 'query',
                },
                'collection_format_map': {
                    'dst_lang': 'multi',
                }
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)

    def similar_resumes_post(self, indexname, resume_id,
                             similar_docs_search_query, **kwargs):
        """Similar Resumes  # noqa: E501

        Setting as arguments the number *size* of documents to be retrieved and the number *offset* to be skipped, this method returns similar documents to resume *resume_id* in the index *indexname*.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.similar_resumes_post(indexname, resume_id, similar_docs_search_query, async_req=True)
        >>> result = thread.get()

        Args:
            indexname (str):
            resume_id (str):
            similar_docs_search_query (SimilarDocsSearchQuery):

        Keyword Args:
            size (int): Number of documents to return.. [optional] if omitted the server will use the default value of 5
            offset (int): Number of documents to skip.. [optional] if omitted the server will use the default value of 0
            min_score (float): Optional. Minimum pertinence score.. [optional] if omitted the server will use the default value of 0
            dst_lang ([str]): Results languages. If left empty then the results will not be filtered by language and the they will contain multi-language results.. [optional]
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
            FoundDocsResponse
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
        kwargs['indexname'] = \
            indexname
        kwargs['resume_id'] = \
            resume_id
        kwargs['similar_docs_search_query'] = \
            similar_docs_search_query
        return self.similar_resumes_post_endpoint.call_with_http_info(**kwargs)
