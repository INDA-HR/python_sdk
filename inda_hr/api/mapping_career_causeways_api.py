"""
    INDA HR - INtelligent Data Analysis for HR

     # Introduction  **INDA (INtelligent Data Analysis)** is an [Intervieweb](https://www.intervieweb.it/hrm/)  AI solution provided as a RESTful API.  The INDA pricing model is *credits-based*, which means that a certain number of credits is associated to each API request. Hence, users have to purchase a certain amount of credits (established according to their needs) which will be reduced  at each API call. INDA accepts and processes a user's request only if their credits quota is grater than - or,  at least, equal to - the number of credits required by that request. To obtain further details on the pricing, please visit our [site](https://inda.ai) or contact us.    INDA HR embraces a wide range of functionalities to manage the main elements of a recruitment process:   + [**candidate**](https://api.inda.ai/hr/docs/v2/#tag/Resume-Management) (hereafter also referred to as **resume** or **applicant**), or rather a  person looking for a job;  + [**job advertisement**](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Management) (hereafter also referred to as **job ad**), which is a document   that collects all the main information and details about a job vacancy;  + [**application**](https://api.inda.ai/hr/docs/v2/#tag/Application-Management), that binds candidates to job ads; it is generated whenever a  candidate applies for a job.  Each of them has a specific set of methods that grants users the ability to create, read, update and delete the relative  documents, plus some special features based on AI approaches (such as *document parsing* or *semantic search*). They can be explored in their respective sections.  Data about the listed document types can be enriched by connecting them to other INDA supported entities, such as  [**companies**](https://api.inda.ai/hr/docs/v2/#tag/Company-Management) and [**universities**](https://api.inda.ai/hr/docs/v2/#tag/Universities), so that recruiters may  get a better and more detailed idea on the candidates' experiences and acquired skills.  All the functionalities mentioned above are meant to help recruiters during the talent acquisition process,  by exploiting the power of AI systems. Among the advantages a recruiter has by using this kind of systems, tackling the bias problem is surely one of the  most relevant. Bias in recruitment is a serious issue that affect both recruiters and candidates, since it may cause wrong hiring  decisions. As we care a lot about this problem, we are constantly working on reduce the bias in original data so that INDA  results may be as fair as possible. As of now, in order to tackle the bias issue, INDA automatically ignores specific fields (such as name, gender, age  and nationality) during the initial processing of each candidate data.  Furthermore, we decided to let users collect data of various types, including personal or sensitive details, but we  do not allow their usage if it is different from statistical purposes; our aim is to discourage recruiters from  focusing on candidates' personal information, and to put their attention on the candidate's skills and abilities.    We want to help recruiters to prevent any kind of bias while searching for the most valuable candidates they really need.    The following documentation is addressed both to developers, in order to provide all technical details for INDA integration, and to managers, to guide them in the exploration of the implementation possibilities.  The host of the API is [https://api.inda.ai/hr/v2/](https://api.inda.ai/hr/v2/). We recommend to check the API version and build (displayed near the documentation title). You can contact us at support@intervieweb.it in case of problems, suggestions, or particular needs.  The search panel on the left can be used to navigate through the documentation and provides an overview of the API structure. On the right, you can find (*i*) the url of the method, (*ii*) an example of request body (if present), and (*iii*) an example of response for each response code. Finally, in the central section of each API method, you can find (*i*) a general description of the purpose of the method, (*ii*) details on parameters and request body schema (if present), and (*iii*) details on response schema, error models, and error codes.    # noqa: E501

    The version of the OpenAPI document: 2.28194
    Contact: info@intervieweb.it
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401

from inda_hr.api_client import ApiClient, Endpoint as _Endpoint
from inda_hr.model_utils import (  # noqa: F401
    check_allowed_values, check_validations, date, datetime, file_type,
    none_type, validate_and_convert_types)
from inda_hr.model.career_transition_request import CareerTransitionRequest
from inda_hr.model.error_model import ErrorModel
from inda_hr.model.http_validation_error import HTTPValidationError
from inda_hr.model.occupation_skills_comparison_request import OccupationSkillsComparisonRequest
from inda_hr.model.occupations_skills_comparison import OccupationsSkillsComparison
from inda_hr.model.transition_recommendations import TransitionRecommendations
from inda_hr.model.upskilling import Upskilling
from inda_hr.model.upskilling_request import UpskillingRequest
from inda_hr.model.work_activity_comparison import WorkActivityComparison
from inda_hr.model.work_activity_comparison_request import WorkActivityComparisonRequest


class MappingCareerCausewaysApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.career_recommendation_post_endpoint = _Endpoint(
            settings={
                'response_type': (TransitionRecommendations, ),
                'auth': ['APIKey'],
                'endpoint_path':
                '/hr/v2/resume/career/occupation/recommendation/',
                'operation_id': 'career_recommendation_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'career_transition_request',
                    'lang',
                    'min_score',
                ],
                'required': [
                    'career_transition_request',
                ],
                'nullable': [],
                'enum': [
                    'lang',
                ],
                'validation': [
                    'min_score',
                ]
            },
            root_map={
                'validations': {
                    ('min_score', ): {
                        'inclusive_maximum': 1.0,
                        'inclusive_minimum': 0.0,
                    },
                },
                'allowed_values': {
                    ('lang', ): {
                        "BG": "bg",
                        "CS": "cs",
                        "DA": "da",
                        "DE": "de",
                        "EL": "el",
                        "EN": "en",
                        "ES": "es",
                        "ET": "et",
                        "FI": "fi",
                        "FR": "fr",
                        "HR": "hr",
                        "HU": "hu",
                        "IT": "it",
                        "LT": "lt",
                        "LV": "lv",
                        "NL": "nl",
                        "PL": "pl",
                        "PT": "pt",
                        "RO": "ro",
                        "SK": "sk",
                        "SL": "sl",
                        "SV": "sv"
                    },
                },
                'openapi_types': {
                    'career_transition_request': (CareerTransitionRequest, ),
                    'lang': (str, ),
                    'min_score': (float, ),
                },
                'attribute_map': {
                    'lang': 'lang',
                    'min_score': 'min_score',
                },
                'location_map': {
                    'career_transition_request': 'body',
                    'lang': 'query',
                    'min_score': 'query',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)
        self.occupation_activities_comparison_post_endpoint = _Endpoint(
            settings={
                'response_type': (WorkActivityComparison, ),
                'auth': ['APIKey'],
                'endpoint_path':
                '/hr/v2/resume/career/occupation/activities/comparison/',
                'operation_id': 'occupation_activities_comparison_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'work_activity_comparison_request',
                    'lang',
                    'min_score',
                ],
                'required': [
                    'work_activity_comparison_request',
                ],
                'nullable': [],
                'enum': [
                    'lang',
                ],
                'validation': [
                    'min_score',
                ]
            },
            root_map={
                'validations': {
                    ('min_score', ): {
                        'inclusive_maximum': 1.0,
                        'inclusive_minimum': 0.0,
                    },
                },
                'allowed_values': {
                    ('lang', ): {
                        "BG": "bg",
                        "CS": "cs",
                        "DA": "da",
                        "DE": "de",
                        "EL": "el",
                        "EN": "en",
                        "ES": "es",
                        "ET": "et",
                        "FI": "fi",
                        "FR": "fr",
                        "HR": "hr",
                        "HU": "hu",
                        "IT": "it",
                        "LT": "lt",
                        "LV": "lv",
                        "NL": "nl",
                        "PL": "pl",
                        "PT": "pt",
                        "RO": "ro",
                        "SK": "sk",
                        "SL": "sl",
                        "SV": "sv"
                    },
                },
                'openapi_types': {
                    'work_activity_comparison_request':
                    (WorkActivityComparisonRequest, ),
                    'lang': (str, ),
                    'min_score': (float, ),
                },
                'attribute_map': {
                    'lang': 'lang',
                    'min_score': 'min_score',
                },
                'location_map': {
                    'work_activity_comparison_request': 'body',
                    'lang': 'query',
                    'min_score': 'query',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)
        self.occupation_skill_comparison_post_endpoint = _Endpoint(
            settings={
                'response_type': (OccupationsSkillsComparison, ),
                'auth': ['APIKey'],
                'endpoint_path':
                '/hr/v2/resume/career/occupation/skills/comparison/',
                'operation_id': 'occupation_skill_comparison_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'occupation_skills_comparison_request',
                    'lang',
                    'min_score',
                ],
                'required': [
                    'occupation_skills_comparison_request',
                ],
                'nullable': [],
                'enum': [
                    'lang',
                ],
                'validation': [
                    'min_score',
                ]
            },
            root_map={
                'validations': {
                    ('min_score', ): {
                        'inclusive_maximum': 1.0,
                        'inclusive_minimum': 0.0,
                    },
                },
                'allowed_values': {
                    ('lang', ): {
                        "BG": "bg",
                        "CS": "cs",
                        "DA": "da",
                        "DE": "de",
                        "EL": "el",
                        "EN": "en",
                        "ES": "es",
                        "ET": "et",
                        "FI": "fi",
                        "FR": "fr",
                        "HR": "hr",
                        "HU": "hu",
                        "IT": "it",
                        "LT": "lt",
                        "LV": "lv",
                        "NL": "nl",
                        "PL": "pl",
                        "PT": "pt",
                        "RO": "ro",
                        "SK": "sk",
                        "SL": "sl",
                        "SV": "sv"
                    },
                },
                'openapi_types': {
                    'occupation_skills_comparison_request':
                    (OccupationSkillsComparisonRequest, ),
                    'lang': (str, ),
                    'min_score': (float, ),
                },
                'attribute_map': {
                    'lang': 'lang',
                    'min_score': 'min_score',
                },
                'location_map': {
                    'occupation_skills_comparison_request': 'body',
                    'lang': 'query',
                    'min_score': 'query',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)
        self.upskilling_simulator_post_endpoint = _Endpoint(
            settings={
                'response_type': (Upskilling, ),
                'auth': ['APIKey'],
                'endpoint_path': '/hr/v2/resume/career/simulator/upskilling/',
                'operation_id': 'upskilling_simulator_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'upskilling_request',
                    'lang',
                    'min_score',
                ],
                'required': [
                    'upskilling_request',
                ],
                'nullable': [],
                'enum': [
                    'lang',
                ],
                'validation': [
                    'min_score',
                ]
            },
            root_map={
                'validations': {
                    ('min_score', ): {
                        'inclusive_maximum': 1.0,
                        'inclusive_minimum': 0.0,
                    },
                },
                'allowed_values': {
                    ('lang', ): {
                        "BG": "bg",
                        "CS": "cs",
                        "DA": "da",
                        "DE": "de",
                        "EL": "el",
                        "EN": "en",
                        "ES": "es",
                        "ET": "et",
                        "FI": "fi",
                        "FR": "fr",
                        "HR": "hr",
                        "HU": "hu",
                        "IT": "it",
                        "LT": "lt",
                        "LV": "lv",
                        "NL": "nl",
                        "PL": "pl",
                        "PT": "pt",
                        "RO": "ro",
                        "SK": "sk",
                        "SL": "sl",
                        "SV": "sv"
                    },
                },
                'openapi_types': {
                    'upskilling_request': (UpskillingRequest, ),
                    'lang': (str, ),
                    'min_score': (float, ),
                },
                'attribute_map': {
                    'lang': 'lang',
                    'min_score': 'min_score',
                },
                'location_map': {
                    'upskilling_request': 'body',
                    'lang': 'query',
                    'min_score': 'query',
                },
                'collection_format_map': {}
            },
            headers_map={
                'accept': ['application/json'],
                'content_type': ['application/json']
            },
            api_client=api_client)

    def career_recommendation_post(self, career_transition_request, **kwargs):
        """Career Recommendation  # noqa: E501

         This method provides an ordered list of recommended jobs transition, given an origin occupation. First, the algorithm  calculates the ESCO occupation that best matches the input job title. The ESCO match is provided  only if the match score is higher than `min_score`.  Viability, salary, and automation risk define the transition recommendations, and the user can select them by the *TransitionType* field: - `viable`: the algorithm recommends all similar occupations, ordered by similarity. No other considerations are made. - `desirable`: the algorithm recommends all similar occupations that offer comparable or higher pay levels. - `safe_desirable`: the algorithm recommends the subset of roles that will likely reduce    a worker's exposure to automation risk among the `desirable` transition.   - `strictly_safe_desirable`: the algorithm recommends among the `desirable` transition, the subset of roles with    lower automation risk and higher prevalence of bottleneck tasks.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.career_recommendation_post(career_transition_request, async_req=True)
        >>> result = thread.get()

        Args:
            career_transition_request (CareerTransitionRequest):

        Keyword Args:
            lang (str): Output language.. [optional] if omitted the server will use the default value of "it"
            min_score (float): Minimum similarity score for ESCO mapping.. [optional] if omitted the server will use the default value of 0.2
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
            async_req (bool): execute request asynchronously

        Returns:
            TransitionRecommendations
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
        kwargs['career_transition_request'] = \
            career_transition_request
        return self.career_recommendation_post_endpoint.call_with_http_info(
            **kwargs)

    def occupation_activities_comparison_post(self,
                                              work_activity_comparison_request,
                                              **kwargs):
        """Occupation Activities Comparison  # noqa: E501

         This method provides a detailed comparison of the principal activities of the origin and destination occupation.  For each activity, the method shows the gap between the two occupations.   The activity comparison is based n the skill ESCO level. It ranges from one to three,  and it is related to the specificity of the activity.     # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.occupation_activities_comparison_post(work_activity_comparison_request, async_req=True)
        >>> result = thread.get()

        Args:
            work_activity_comparison_request (WorkActivityComparisonRequest):

        Keyword Args:
            lang (str): Output language.. [optional] if omitted the server will use the default value of "it"
            min_score (float): Minimum similarity score for ESCO mapping.. [optional] if omitted the server will use the default value of 0.2
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
            async_req (bool): execute request asynchronously

        Returns:
            WorkActivityComparison
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
        kwargs['work_activity_comparison_request'] = \
            work_activity_comparison_request
        return self.occupation_activities_comparison_post_endpoint.call_with_http_info(
            **kwargs)

    def occupation_skill_comparison_post(self,
                                         occupation_skills_comparison_request,
                                         **kwargs):
        """Occupation Skill Comparison  # noqa: E501

         This method provides a detailed comparison of the skills of the origin and destination occupations.  Such comparison helps compare the skill gaps among the occupations. Each skill of the origin occupation  is mapped to the most similar skill of the destination occupation. The mapping is one to one.   Skills are split in: - `essential`: only the most relevant skills for such occupation are considered according to ESCO Classification; - `optional`: both essential and optional skills are considered according to ESCO Classification.    # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.occupation_skill_comparison_post(occupation_skills_comparison_request, async_req=True)
        >>> result = thread.get()

        Args:
            occupation_skills_comparison_request (OccupationSkillsComparisonRequest):

        Keyword Args:
            lang (str): Output language.. [optional] if omitted the server will use the default value of "it"
            min_score (float): Minimum similarity score for ESCO mapping.. [optional] if omitted the server will use the default value of 0.2
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
            async_req (bool): execute request asynchronously

        Returns:
            OccupationsSkillsComparison
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
        kwargs['occupation_skills_comparison_request'] = \
            occupation_skills_comparison_request
        return self.occupation_skill_comparison_post_endpoint.call_with_http_info(
            **kwargs)

    def upskilling_simulator_post(self, upskilling_request, **kwargs):
        """Upskilling simulator  # noqa: E501

         Learning and getting new skills usually leads to new job opportunities. Given an origin occupation and a list of acquired skills,  this method provides an updated ordered list of recommended jobs transition based on your occupation skills and your acquired skills.  First, the algorithm  calculates the ESCO occupation that best matches the input job title and ESCO skills that best fits the input skills list.  The ESCO match is provided  only if the match score is higher than `min_score`.    Viability, salary, and automation risk define the transition recommendations, and the user can select them by the *TransitionType* field: - `viable`: the algorithm recommends all similar occupations, ordered by similarity. No other considerations are made; - `desirable`: the algorithm recommends all similar occupations that offer comparable or higher pay levels; - `safe_desirable`: the algorithm recommends the subset of roles that will likely reduce     a worker's exposure to automation risk among the `desirable` transition;   - `strictly_safe_desirable`: the algorithm recommends among the `desirable` transition, the subset of roles with     lower automation risk and higher prevalence of bottleneck tasks.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upskilling_simulator_post(upskilling_request, async_req=True)
        >>> result = thread.get()

        Args:
            upskilling_request (UpskillingRequest):

        Keyword Args:
            lang (str): Output language.. [optional] if omitted the server will use the default value of "it"
            min_score (float): Minimum similarity score for ESCO mapping.. [optional] if omitted the server will use the default value of 0.2
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
            async_req (bool): execute request asynchronously

        Returns:
            Upskilling
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
        kwargs['upskilling_request'] = \
            upskilling_request
        return self.upskilling_simulator_post_endpoint.call_with_http_info(
            **kwargs)