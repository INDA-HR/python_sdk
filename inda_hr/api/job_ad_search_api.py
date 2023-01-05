"""
    INDA HR - INtelligent Data Analysis for HR

     # Introduction  **INDA (INtelligent Data Analysis)** is an [Intervieweb](https://www.intervieweb.it/hrm/)  AI solution provided as a RESTful API.  The INDA pricing model is *credits-based*, which means that a certain number of credits is associated to each API request. Hence, users have to purchase a certain amount of credits (established according to their needs) which will be reduced  at each API call. INDA accepts and processes a user's request only if their credits quota is grater than - or,  at least, equal to - the number of credits required by that request. To obtain further details on the pricing, please visit our [site](https://inda.ai) or contact us.    INDA HR embraces a wide range of functionalities to manage the main elements of a recruitment process:   + [**candidate**](https://api.inda.ai/hr/docs/v2/#tag/Resume-Management) (hereafter also referred to as **resume** or **applicant**), or rather a  person looking for a job;  + [**job advertisement**](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Management) (hereafter also referred to as **job ad**), which is a document   that collects all the main information and details about a job vacancy;  + [**application**](https://api.inda.ai/hr/docs/v2/#tag/Application-Management), that binds candidates to job ads; it is generated whenever a  candidate applies for a job.  Each of them has a specific set of methods that grants users the ability to create, read, update and delete the relative  documents, plus some special features based on AI approaches (such as *document parsing* or *semantic search*). They can be explored in their respective sections.  Data about the listed document types can be enriched by connecting them to other INDA supported entities, such as  [**companies**](https://api.inda.ai/hr/docs/v2/#tag/Company-Management) and [**universities**](https://api.inda.ai/hr/docs/v2/#tag/Universities), so that recruiters may  get a better and more detailed idea on the candidates' experiences and acquired skills.  All the functionalities mentioned above are meant to help recruiters during the talent acquisition process,  by exploiting the power of AI systems. Among the advantages a recruiter has by using this kind of systems, tackling the bias problem is surely one of the  most relevant. Bias in recruitment is a serious issue that affect both recruiters and candidates, since it may cause wrong hiring  decisions. As we care a lot about this problem, we are constantly working on reduce the bias in original data so that INDA  results may be as fair as possible. As of now, in order to tackle the bias issue, INDA automatically ignores specific fields (such as name, gender, age  and nationality) during the initial processing of each candidate data.  Furthermore, we decided to let users collect data of various types, including personal or sensitive details, but we  do not allow their usage if it is different from statistical purposes; our aim is to discourage recruiters from  focusing on candidates' personal information, and to put their attention on the candidate's skills and abilities.    We want to help recruiters to prevent any kind of bias while searching for the most valuable candidates they really need.    The following documentation is addressed both to developers, in order to provide all technical details for INDA integration, and to managers, to guide them in the exploration of the implementation possibilities.  The host of the API is [https://api.inda.ai/hr/v2/](https://api.inda.ai/hr/v2/). We recommend to check the API version and build (displayed near the documentation title). You can contact us at support@intervieweb.it in case of problems, suggestions, or particular needs.  The search panel on the left can be used to navigate through the documentation and provides an overview of the API structure. On the right, you can find (*i*) the url of the method, (*ii*) an example of request body (if present), and (*iii*) an example of response for each response code. Finally, in the central section of each API method, you can find (*i*) a general description of the purpose of the method, (*ii*) details on parameters and request body schema (if present), and (*iii*) details on response schema, error models, and error codes.    # noqa: E501

    The version of the OpenAPI document: 2.32211
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
from inda_hr.model.found_job_ads_response import FoundJobAdsResponse
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.job_ad_full_text_search import JobAdFullTextSearch
from inda_hr.model.job_ad_search_query import JobAdSearchQuery


class JobAdSearchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.full_text_search_on_jobads_post_endpoint = _Endpoint(
            settings={
                'response_type': (FoundJobAdsResponse, ),
                'auth': ['APIKey'],
                'endpoint_path':
                '/hr/v2/index/{indexname}/jobads/search/full-text/',
                'operation_id': 'full_text_search_on_jobads_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'indexname',
                    'default_operator',
                    'cache',
                    'cache_time',
                    'size',
                    'offset',
                    'min_score',
                    'search_id',
                    'job_ad_full_text_search',
                ],
                'required': [
                    'indexname',
                ],
                'nullable': [],
                'enum': [
                    'default_operator',
                ],
                'validation': [
                    'cache_time',
                    'size',
                    'offset',
                    'min_score',
                ]
            },
            root_map={
                'validations': {
                    ('cache_time', ): {
                        'inclusive_maximum': 600,
                    },
                    ('size', ): {
                        'inclusive_maximum': 1000,
                    },
                    ('offset', ): {
                        'inclusive_minimum': 0,
                    },
                    ('min_score', ): {
                        'inclusive_minimum': 0.0,
                    },
                },
                'allowed_values': {
                    ('default_operator', ): {
                        "AND": "AND",
                        "OR": "OR"
                    },
                },
                'openapi_types': {
                    'indexname': (str, ),
                    'default_operator': (str, ),
                    'cache': (bool, ),
                    'cache_time': (int, ),
                    'size': (int, ),
                    'offset': (int, ),
                    'min_score': (float, ),
                    'search_id': (str, ),
                    'job_ad_full_text_search': (JobAdFullTextSearch, ),
                },
                'attribute_map': {
                    'indexname': 'indexname',
                    'default_operator': 'default_operator',
                    'cache': 'cache',
                    'cache_time': 'cache_time',
                    'size': 'size',
                    'offset': 'offset',
                    'min_score': 'min_score',
                    'search_id': 'search_id',
                },
                'location_map': {
                    'indexname': 'path',
                    'default_operator': 'query',
                    'cache': 'query',
                    'cache_time': 'query',
                    'size': 'query',
                    'offset': 'query',
                    'min_score': 'query',
                    'search_id': 'query',
                    'job_ad_full_text_search': 'body',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)
        self.search_applications_post_endpoint = _Endpoint(
            settings={
                'response_type': (FoundJobAdsResponse, ),
                'auth': ['APIKey'],
                'endpoint_path':
                '/hr/v2/index/{indexname}/resume/{resume_id}/applications/jobads/search/',
                'operation_id': 'search_applications_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'indexname',
                    'resume_id',
                    'cache_time',
                    'size',
                    'search_id',
                    'job_ad_search_query',
                ],
                'required': [
                    'indexname',
                    'resume_id',
                ],
                'nullable': [],
                'enum': [],
                'validation': [
                    'cache_time',
                    'size',
                ]
            },
            root_map={
                'validations': {
                    ('cache_time', ): {
                        'inclusive_maximum': 600,
                    },
                    ('size', ): {
                        'inclusive_maximum': 1000,
                    },
                },
                'allowed_values': {},
                'openapi_types': {
                    'indexname': (str, ),
                    'resume_id': (str, ),
                    'cache_time': (int, ),
                    'size': (int, ),
                    'search_id': (str, ),
                    'job_ad_search_query': (JobAdSearchQuery, ),
                },
                'attribute_map': {
                    'indexname': 'indexname',
                    'resume_id': 'resume_id',
                    'cache_time': 'cache_time',
                    'size': 'size',
                    'search_id': 'search_id',
                },
                'location_map': {
                    'indexname': 'path',
                    'resume_id': 'path',
                    'cache_time': 'query',
                    'size': 'query',
                    'search_id': 'query',
                    'job_ad_search_query': 'body',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)

    def full_text_search_on_jobads_post(self, indexname, **kwargs):
        """Full-Text Search on JobAds  # noqa: E501

        This is the most common way to search a text document through the job advertisements stored in the index *indexname*.  This function takes as input a list of objects containing the terms you wish to search for, please consider that tokens (individual words) grouped together in the same *QueryTerms* element will be queried separately in an **OR** clause, whereas different *QueryTerms* elements will be joined by an **AND** clause. To put it in words, the query will retrieve documents that match at least one word from each element in *QueryTerms*.  This behaviour can be modified in one of two ways:  + The **default_operator** query parameter, which defaults to OR, can be set to AND in order to only find documents that contain ALL of the tokens in a given *query_terms* element. + The **\"** (double quotes) operator, which can be used to wrap strings made up of multiple tokens in order to find documents that contain those words exactly in the order they are presented (sentence match). Remember to escape double quotes in your JSON inputs with a backslash.  Each *QueryTerms* element can be negated with the parameter **Exclude** set to *true*. This is equivalent to setting it in a **NOT** clause.  It's also possible to use wildcards to perform jolly searches, the supported wildcards are:  + \\*: Can be used to match any number of characters in the middle (ad\\*ment) or at the end (doc\\*) of a word. + ?: Can be used to match a single character in any position (?xample).  All queries are case-insensitive and have some amount of fuzziness by default, meaning that typos and character transpositions will be included in the matches. Additionally, filters can be added to form boolean queries on indexed fields. For a comprehensive list and explanation of filters, see the [*Query Filters*](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) section, the structure is the same.  Query parameters are used to specify the *offset* and *size* of the search. The method uses *cache* = <code style='color: #333333; opacity: 0.9'>true</code> by default, meaning that it will cache automatically each search for *cache_time* seconds. When caching is active, *offset* is ignored; in order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  The use of caching is highly recommended to improve the performances.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.full_text_search_on_jobads_post(indexname, async_req=True)
        >>> result = thread.get()

        Args:
            indexname (str):

        Keyword Args:
            default_operator (str): Optional. Change this to *AND* if you wish documents to match ALLof the tokens in a single query_terms element.. [optional] if omitted the server will use the default value of "OR"
            cache (bool): Optional. Whether the search results should be cached or not.. [optional] if omitted the server will use the default value of True
            cache_time (int): Optional. Seconds. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>false</code>.. [optional] if omitted the server will use the default value of 300
            size (int): Optional. Number of documents to return.. [optional] if omitted the server will use the default value of 50
            offset (int): Optional. Number of documents to skip. Ignored if *cache* is <code style='color: #333333; opacity: 0.9'>true</code>.. [optional] if omitted the server will use the default value of 0
            min_score (float): Optional. Minimum pertinence score.. [optional] if omitted the server will use the default value of 0
            search_id (str): Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used.. [optional]
            job_ad_full_text_search (JobAdFullTextSearch): [optional]
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
            FoundJobAdsResponse
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
        return self.full_text_search_on_jobads_post_endpoint.call_with_http_info(
            **kwargs)

    def search_applications_post(self, indexname, resume_id, **kwargs):
        """Search Applications  # noqa: E501

        This method is meant to return those job advertisements that the resume of ID *resume_id* have applied to, if they respect the given query.  Users may specify [query filters](https://api.inda.ai/hr/docs/v2/#tag/Query-Filters) to apply on both [Applications](https://api.inda.ai/hr/docs/v2/#tag/Application-Management) and [JobAds](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Management) indexed fields.  Query parameters are used to specify the *cache_time* and *size* of the search. The method will automatically cache each search for *cache_time* seconds. In order to navigate or scroll the entire search response (in chunks of size *size*, as specified in the first search), this method should be used through the *search_id*. When *search_id* is provided, other query parameters are ignored, except *cache_time*.  Note that a new *search_id* is provided for every scroll. Search IDs are not unique but it is strongly recommended to update the *search_id* at every call of this method with the *SearchID* of the last response. If the *SearchID* is missing or equal to <code style='color: #333333; opacity: 0.9'>null</code>, the scroll has ended.  Beware that the scroll can ONLY go forward in the search cache because it is meant to review large searches.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_applications_post(indexname, resume_id, async_req=True)
        >>> result = thread.get()

        Args:
            indexname (str):
            resume_id (str):

        Keyword Args:
            cache_time (int): Optional. Seconds.. [optional] if omitted the server will use the default value of 300
            size (int): Optional. Number of documents to return.. [optional] if omitted the server will use the default value of 50
            search_id (str): Both the initial search request and each subsequent scroll request returns a *SearchID*. The *SearchID* may or may not  change between requests; however, only the most recently received *SearchID* should be used.. [optional]
            job_ad_search_query (JobAdSearchQuery): [optional]
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
            FoundJobAdsResponse
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
        return self.search_applications_post_endpoint.call_with_http_info(
            **kwargs)
