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
from inda_hr.model.delete_job_ad_response import DeleteJobAdResponse
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.get_job_ad_response import GetJobAdResponse
from inda_hr.model.get_job_ads_response import GetJobAdsResponse
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.job_ad_id_response import JobAdIDResponse
from inda_hr.model.job_ad_request import JobAdRequest
from inda_hr.model.patch_job_ad_request import PatchJobAdRequest
from inda_hr.model.patch_job_ad_response import PatchJobAdResponse


class JobAdManagementApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.add_jobad_post_endpoint = _Endpoint(
            settings={
                'response_type': (JobAdIDResponse, ),
                'auth': ['APIKey'],
                'endpoint_path': '/hr/v2/index/{indexname}/jobad/',
                'operation_id': 'add_jobad_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'indexname',
                    'job_ad_request',
                    'src_lang',
                    'dst_lang',
                    'jobad_id',
                ],
                'required': [
                    'indexname',
                    'job_ad_request',
                ],
                'nullable': [],
                'enum': [
                    'src_lang',
                    'dst_lang',
                ],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {
                    ('src_lang', ): {
                        "PT": "pt",
                        "IT": "it",
                        "EN": "en",
                        "DE": "de",
                        "FR": "fr",
                        "ES": "es"
                    },
                    ('dst_lang', ): {
                        "PT": "pt",
                        "IT": "it",
                        "EN": "en",
                        "DE": "de",
                        "FR": "fr",
                        "ES": "es"
                    },
                },
                'openapi_types': {
                    'indexname': (str, ),
                    'job_ad_request': (JobAdRequest, ),
                    'src_lang': (str, ),
                    'dst_lang': (str, ),
                    'jobad_id': (str, ),
                },
                'attribute_map': {
                    'indexname': 'indexname',
                    'src_lang': 'src_lang',
                    'dst_lang': 'dst_lang',
                    'jobad_id': 'jobad_id',
                },
                'location_map': {
                    'indexname': 'path',
                    'job_ad_request': 'body',
                    'src_lang': 'query',
                    'dst_lang': 'query',
                    'jobad_id': 'query',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)
        self.delete_jobad_delete_endpoint = _Endpoint(
            settings={
                'response_type': (DeleteJobAdResponse, ),
                'auth': ['APIKey'],
                'endpoint_path': '/hr/v2/index/{indexname}/jobad/{jobad_id}/',
                'operation_id': 'delete_jobad_delete',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'indexname',
                    'jobad_id',
                ],
                'required': [
                    'indexname',
                    'jobad_id',
                ],
                'nullable': [],
                'enum': [],
                'validation': []
            },
            root_map={
                'validations': {},
                'allowed_values': {},
                'openapi_types': {
                    'indexname': (str, ),
                    'jobad_id': (str, ),
                },
                'attribute_map': {
                    'indexname': 'indexname',
                    'jobad_id': 'jobad_id',
                },
                'location_map': {
                    'indexname': 'path',
                    'jobad_id': 'path',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': [],
            },
            api_client=api_client)
        self.get_jobad_get_endpoint = _Endpoint(settings={
            'response_type': (GetJobAdResponse, ),
            'auth': ['APIKey'],
            'endpoint_path':
            '/hr/v2/index/{indexname}/jobad/{jobad_id}/',
            'operation_id':
            'get_jobad_get',
            'http_method':
            'GET',
            'servers':
            None,
        },
                                                params_map={
                                                    'all': [
                                                        'indexname',
                                                        'jobad_id',
                                                    ],
                                                    'required': [
                                                        'indexname',
                                                        'jobad_id',
                                                    ],
                                                    'nullable': [],
                                                    'enum': [],
                                                    'validation': []
                                                },
                                                root_map={
                                                    'validations': {},
                                                    'allowed_values': {},
                                                    'openapi_types': {
                                                        'indexname': (str, ),
                                                        'jobad_id': (str, ),
                                                    },
                                                    'attribute_map': {
                                                        'indexname':
                                                        'indexname',
                                                        'jobad_id': 'jobad_id',
                                                    },
                                                    'location_map': {
                                                        'indexname': 'path',
                                                        'jobad_id': 'path',
                                                    },
                                                    'collection_format_map':
                                                    {}
                                                },
                                                headers_map={
                                                    'accept':
                                                    ['application/json'],
                                                    'content_type': [],
                                                },
                                                api_client=api_client)
        self.get_jobads_get_endpoint = _Endpoint(
            settings={
                'response_type': (GetJobAdsResponse, ),
                'auth': ['APIKey'],
                'endpoint_path': '/hr/v2/index/{indexname}/jobads/',
                'operation_id': 'get_jobads_get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'indexname',
                    'cache',
                    'cache_time',
                    'offset',
                    'search_id',
                    'size',
                ],
                'required': [
                    'indexname',
                ],
                'nullable': [],
                'enum': [],
                'validation': [
                    'cache_time',
                    'offset',
                    'size',
                ]
            },
            root_map={
                'validations': {
                    ('cache_time', ): {
                        'inclusive_maximum': 600,
                    },
                    ('offset', ): {
                        'inclusive_minimum': 0,
                    },
                    ('size', ): {
                        'inclusive_maximum': 1000,
                    },
                },
                'allowed_values': {},
                'openapi_types': {
                    'indexname': (str, ),
                    'cache': (bool, ),
                    'cache_time': (int, ),
                    'offset': (int, ),
                    'search_id': (str, ),
                    'size': (int, ),
                },
                'attribute_map': {
                    'indexname': 'indexname',
                    'cache': 'cache',
                    'cache_time': 'cache_time',
                    'offset': 'offset',
                    'search_id': 'search_id',
                    'size': 'size',
                },
                'location_map': {
                    'indexname': 'path',
                    'cache': 'query',
                    'cache_time': 'query',
                    'offset': 'query',
                    'search_id': 'query',
                    'size': 'query',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': [],
            },
            api_client=api_client)
        self.patch_jobad_patch_endpoint = _Endpoint(
            settings={
                'response_type': (PatchJobAdResponse, ),
                'auth': ['APIKey'],
                'endpoint_path': '/hr/v2/index/{indexname}/jobad/{jobad_id}/',
                'operation_id': 'patch_jobad_patch',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'indexname',
                    'jobad_id',
                    'patch_job_ad_request',
                    'src_lang',
                ],
                'required': [
                    'indexname',
                    'jobad_id',
                    'patch_job_ad_request',
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
                        "PT": "pt",
                        "IT": "it",
                        "EN": "en",
                        "DE": "de",
                        "FR": "fr",
                        "ES": "es"
                    },
                },
                'openapi_types': {
                    'indexname': (str, ),
                    'jobad_id': (str, ),
                    'patch_job_ad_request': (PatchJobAdRequest, ),
                    'src_lang': (str, ),
                },
                'attribute_map': {
                    'indexname': 'indexname',
                    'jobad_id': 'jobad_id',
                    'src_lang': 'src_lang',
                },
                'location_map': {
                    'indexname': 'path',
                    'jobad_id': 'path',
                    'patch_job_ad_request': 'body',
                    'src_lang': 'query',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)

    def add_jobad_post(self, indexname, job_ad_request, **kwargs):
        """Add JobAd  # noqa: E501

         This method adds a job advertisement to *indexname* and assigns it a *JobAdID* (namely, a Unique Universal ID or UUID4). This method requires an application/json as content type body.  On the right, we provide an example of input structure; further details are available in dedicated sections.  Note that it is mandatory for users to have previously added information about the employer through the  [Add Company](https://api.inda.ai/hr/docs/v2/#operation/add_company__POST) method; the returned *ID* is the required *EmployerID* of job advertisement data. Obviously, one may skip this step if employer company data already exists.  Furthermore, also *Skills* is a required field, since it is necessary to perform the  [Match Resume](https://api.inda.ai/hr/docs/v2/#operation/match_resumes__POST).  Users may leverage the [Extract Skills from JobAd](https://api.inda.ai/hr/docs/v2/#operation/extract_skills_from_jobad__POST) method and allow INDA to automatically extract skills by analyzing the job advertisement data. It is **highly recommended** to validate the retrieved skills before injecting them to *Add JobAd* requests.  Entities among skills, job titles and languages are automatically mapped by INDAto the adopted knowledge base, so that users can leverage on standardized values.Original values and entity IDs are available in *Details.RawValues* and *Details.Code*, respectively.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_jobad_post(indexname, job_ad_request, async_req=True)
        >>> result = thread.get()

        Args:
            indexname (str):
            job_ad_request (JobAdRequest):

        Keyword Args:
            src_lang (str): Job Description language. If left empty each section's language will detected automatically.. [optional]
            dst_lang (str): Extracted entities destination language. If left empty is assumed to be equal to the Job Description language.. [optional]
            jobad_id (str): [optional]
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
            JobAdIDResponse
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
        kwargs['job_ad_request'] = \
            job_ad_request
        return self.add_jobad_post_endpoint.call_with_http_info(**kwargs)

    def delete_jobad_delete(self, indexname, jobad_id, **kwargs):
        """Delete JobAd  # noqa: E501

         This method removes the job advertisement associated with *jobad_id* from the index *indexname*.  Note that when a job advertisement is deleted, the same happens to all its related applications.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_jobad_delete(indexname, jobad_id, async_req=True)
        >>> result = thread.get()

        Args:
            indexname (str):
            jobad_id (str):

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
            DeleteJobAdResponse
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
        kwargs['jobad_id'] = \
            jobad_id
        return self.delete_jobad_delete_endpoint.call_with_http_info(**kwargs)

    def get_jobad_get(self, indexname, jobad_id, **kwargs):
        """Get JobAd  # noqa: E501

         This method returns the information related to the job advertisement stored with id *jobad_id* in the index *indexname*.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_jobad_get(indexname, jobad_id, async_req=True)
        >>> result = thread.get()

        Args:
            indexname (str):
            jobad_id (str):

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
            GetJobAdResponse
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
        kwargs['jobad_id'] = \
            jobad_id
        return self.get_jobad_get_endpoint.call_with_http_info(**kwargs)

    def get_jobads_get(self, indexname, **kwargs):
        """Get JobAds  # noqa: E501

         This method returns a list of UUID4 associated to the job advertisements stored in the index *indexname*.  Query parameters are used to specify the *offset* and *size* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored; in order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  The use of caching is highly recommended to improve the performances.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_jobads_get(indexname, async_req=True)
        >>> result = thread.get()

        Args:
            indexname (str):

        Keyword Args:
            cache (bool): Optional. Whether the search results should be cached or not.. [optional] if omitted the server will use the default value of True
            cache_time (int): Optional. Seconds.Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>false</code>.. [optional] if omitted the server will use the default value of 300
            offset (int): Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>.. [optional] if omitted the server will use the default value of 0
            search_id (str): Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used. Other query parameters are uselesswhen *SearchID* is used.. [optional]
            size (int): Optional. Number of documents to return.. [optional] if omitted the server will use the default value of 50
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
            GetJobAdsResponse
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
        return self.get_jobads_get_endpoint.call_with_http_info(**kwargs)

    def patch_jobad_patch(self, indexname, jobad_id, patch_job_ad_request,
                          **kwargs):
        """Patch JobAd  # noqa: E501

         This method updates the information related to the job advertisement stored with id *job_ad_id*.  This method accepts an application/json body with the same structure as [Add JobAd](https://api.inda.ai/hr/docs/v2/#operation/add_jobad__POST), however in this case all fields are optional.  Fields that contain differences between the corresponding original ones are substituted, while new fields are added. Bear in mind that lists are considered as singular value, therefore to modify an entry in a list it is necessary to insert the full list.  Entities among skills, job titles and languages are automatically mapped by INDAto the adopted knowledge base, so that users can leverage on standardized values.Original values and entity IDs are available in *Details.RawValues* and *Details.Code*, respectively.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_jobad_patch(indexname, jobad_id, patch_job_ad_request, async_req=True)
        >>> result = thread.get()

        Args:
            indexname (str):
            jobad_id (str):
            patch_job_ad_request (PatchJobAdRequest):

        Keyword Args:
            src_lang (str): Job Description language. If left empty each section's language will detected automatically.. [optional]
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
            PatchJobAdResponse
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
        kwargs['jobad_id'] = \
            jobad_id
        kwargs['patch_job_ad_request'] = \
            patch_job_ad_request
        return self.patch_jobad_patch_endpoint.call_with_http_info(**kwargs)
