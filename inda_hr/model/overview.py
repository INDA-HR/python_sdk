# coding: utf-8
"""
    INDA HR - INtelligent Data Analysis for HR

     # Introduction  **INDA (INtelligent Data Analysis)** is an [Intervieweb](https://www.intervieweb.it/hrm/)  AI solution provided as a RESTful API.  The INDA pricing model is *credits-based*, which means that a certain number of credits is associated to each API request. Hence, users have to purchase a certain amount of credits (established according to their needs) which will be reduced  at each API call. INDA accepts and processes a user's request only if their credits quota is grater than - or,  at least, equal to - the number of credits required by that request. To obtain further details on the pricing, please visit our [site](https://inda.ai) or contact us.    INDA HR embraces a wide range of functionalities to manage the main elements of a recruitment process:   + [**candidate**](https://api.inda.ai/hr/docs/v2/#tag/Resume-Management) (hereafter also referred to as **resume** or **applicant**), or rather a  person looking for a job;  + [**job advertisement**](https://api.inda.ai/hr/docs/v2/#tag/JobAd-Management) (hereafter also referred to as **job ad**), which is a document   that collects all the main information and details about a job vacancy;  + [**application**](https://api.inda.ai/hr/docs/v2/#tag/Application-Management), that binds candidates to job ads; it is generated whenever a  candidate applies for a job.  Each of them has a specific set of methods that grants users the ability to create, read, update and delete the relative  documents, plus some special features based on AI approaches (such as *document parsing* or *semantic search*). They can be explored in their respective sections.  Data about the listed document types can be enriched by connecting them to other INDA supported entities, such as  [**companies**](https://api.inda.ai/hr/docs/v2/#tag/Company-Management) and [**universities**](https://api.inda.ai/hr/docs/v2/#tag/Universities), so that recruiters may  get a better and more detailed idea on the candidates' experiences and acquired skills.  All the functionalities mentioned above are meant to help recruiters during the talent acquisition process,  by exploiting the power of AI systems. Among the advantages a recruiter has by using this kind of systems, tackling the bias problem is surely one of the  most relevant. Bias in recruitment is a serious issue that affect both recruiters and candidates, since it may cause wrong hiring  decisions. As we care a lot about this problem, we are constantly working on reduce the bias in original data so that INDA  results may be as fair as possible. As of now, in order to tackle the bias issue, INDA automatically ignores specific fields (such as name, gender, age  and nationality) during the initial processing of each candidate data.  Furthermore, we decided to let users collect data of various types, including personal or sensitive details, but we  do not allow their usage if it is different from statistical purposes; our aim is to discourage recruiters from  focusing on candidates' personal information, and to put their attention on the candidate's skills and abilities.    We want to help recruiters to prevent any kind of bias while searching for the most valuable candidates they really need.    The following documentation is addressed both to developers, in order to provide all technical details for INDA integration, and to managers, to guide them in the exploration of the implementation possibilities.  The host of the API is [https://api.inda.ai/hr/v2/](https://api.inda.ai/hr/v2/). We recommend to check the API version and build (displayed near the documentation title). You can contact us at support@intervieweb.it in case of problems, suggestions, or particular needs.  The search panel on the left can be used to navigate through the documentation and provides an overview of the API structure. On the right, you can find (*i*) the url of the method, (*ii*) an example of request body (if present), and (*iii*) an example of response for each response code. Finally, in the central section of each API method, you can find (*i*) a general description of the purpose of the method, (*ii*) details on parameters and request body schema (if present), and (*iii*) details on response schema, error models, and error codes.    # noqa: E501

    The version of the OpenAPI document: 2.32211
    Contact: info@intervieweb.it
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from inda_hr import schemas  # noqa: F401


class Overview(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "Name",
        }

        class properties:

            @staticmethod
            def Name() -> typing.Type['UniversityAdmissionsValueModelStr']:
                return UniversityAdmissionsValueModelStr

            @staticmethod
            def AltName() -> typing.Type['UniversityAdmissionsValueModelStr']:
                return UniversityAdmissionsValueModelStr

            @staticmethod
            def Acronym() -> typing.Type['UniversityAdmissionsValueModelStr']:
                return UniversityAdmissionsValueModelStr

            @staticmethod
            def Description(
            ) -> typing.Type['UniversityAdmissionsValueModelStr']:
                return UniversityAdmissionsValueModelStr

            @staticmethod
            def Founded() -> typing.Type['ValueModelUnionDatetimeDate']:
                return ValueModelUnionDatetimeDate

            @staticmethod
            def Motto() -> typing.Type['UniversityAdmissionsValueModelStr']:
                return UniversityAdmissionsValueModelStr

            @staticmethod
            def Colours() -> typing.Type['UniversityAdmissionsValueModelStr']:
                return UniversityAdmissionsValueModelStr

            @staticmethod
            def Rank() -> typing.Type['Rank']:
                return Rank

            __annotations__ = {
                "Name": Name,
                "AltName": AltName,
                "Acronym": Acronym,
                "Description": Description,
                "Founded": Founded,
                "Motto": Motto,
                "Colours": Colours,
                "Rank": Rank,
            }

        additional_properties = schemas.NotAnyTypeSchema

    Name: 'UniversityAdmissionsValueModelStr'

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Name"]
    ) -> 'UniversityAdmissionsValueModelStr':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["AltName"]
    ) -> 'UniversityAdmissionsValueModelStr':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Acronym"]
    ) -> 'UniversityAdmissionsValueModelStr':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Description"]
    ) -> 'UniversityAdmissionsValueModelStr':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Founded"]
    ) -> 'ValueModelUnionDatetimeDate':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Motto"]
    ) -> 'UniversityAdmissionsValueModelStr':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Colours"]
    ) -> 'UniversityAdmissionsValueModelStr':
        ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Rank"]) -> 'Rank':
        ...

    def __getitem__(
        self, name: typing.Union[typing_extensions.Literal["Name"],
                                 typing_extensions.Literal["AltName"],
                                 typing_extensions.Literal["Acronym"],
                                 typing_extensions.Literal["Description"],
                                 typing_extensions.Literal["Founded"],
                                 typing_extensions.Literal["Motto"],
                                 typing_extensions.Literal["Colours"],
                                 typing_extensions.Literal["Rank"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Name"]
    ) -> 'UniversityAdmissionsValueModelStr':
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["AltName"]
    ) -> typing.Union['UniversityAdmissionsValueModelStr', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Acronym"]
    ) -> typing.Union['UniversityAdmissionsValueModelStr', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Description"]
    ) -> typing.Union['UniversityAdmissionsValueModelStr', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Founded"]
    ) -> typing.Union['ValueModelUnionDatetimeDate', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Motto"]
    ) -> typing.Union['UniversityAdmissionsValueModelStr', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Colours"]
    ) -> typing.Union['UniversityAdmissionsValueModelStr', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Rank"]
    ) -> typing.Union['Rank', schemas.Unset]:
        ...

    def get_item_oapg(
        self, name: typing.Union[typing_extensions.Literal["Name"],
                                 typing_extensions.Literal["AltName"],
                                 typing_extensions.Literal["Acronym"],
                                 typing_extensions.Literal["Description"],
                                 typing_extensions.Literal["Founded"],
                                 typing_extensions.Literal["Motto"],
                                 typing_extensions.Literal["Colours"],
                                 typing_extensions.Literal["Rank"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Name: 'UniversityAdmissionsValueModelStr',
        AltName: typing.Union['UniversityAdmissionsValueModelStr',
                              schemas.Unset] = schemas.unset,
        Acronym: typing.Union['UniversityAdmissionsValueModelStr',
                              schemas.Unset] = schemas.unset,
        Description: typing.Union['UniversityAdmissionsValueModelStr',
                                  schemas.Unset] = schemas.unset,
        Founded: typing.Union['ValueModelUnionDatetimeDate',
                              schemas.Unset] = schemas.unset,
        Motto: typing.Union['UniversityAdmissionsValueModelStr',
                            schemas.Unset] = schemas.unset,
        Colours: typing.Union['UniversityAdmissionsValueModelStr',
                              schemas.Unset] = schemas.unset,
        Rank: typing.Union['Rank', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'Overview':
        return super().__new__(
            cls,
            *_args,
            Name=Name,
            AltName=AltName,
            Acronym=Acronym,
            Description=Description,
            Founded=Founded,
            Motto=Motto,
            Colours=Colours,
            Rank=Rank,
            _configuration=_configuration,
        )


from inda_hr.model.rank import Rank
from inda_hr.model.university_admissions_value_model_str import UniversityAdmissionsValueModelStr
from inda_hr.model.value_model_union_datetime_date import ValueModelUnionDatetimeDate
