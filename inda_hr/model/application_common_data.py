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


class ApplicationCommonData(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:

        class properties:

            @staticmethod
            def Objective() -> typing.Type['BaseBenefitsValueModelStrictStr']:
                return BaseBenefitsValueModelStrictStr

            @staticmethod
            def ProfessionalSummary(
            ) -> typing.Type['BaseBenefitsValueModelStrictStr']:
                return BaseBenefitsValueModelStrictStr

            @staticmethod
            def DesiredEmployment() -> typing.Type['ResumeEmployment']:
                return ResumeEmployment

            class DesiredContracts(schemas.ListSchema):

                class MetaOapg:

                    @staticmethod
                    def items() -> typing.Type['ResumeContract']:
                        return ResumeContract

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ResumeContract'],
                                       typing.List['ResumeContract']],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'DesiredContracts':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> 'ResumeContract':
                    return super().__getitem__(i)

            @staticmethod
            def DesiredSalary() -> typing.Type['ResumeSalary']:
                return ResumeSalary

            class DesiredBenefits(schemas.ListSchema):

                class MetaOapg:

                    @staticmethod
                    def items() -> typing.Type['ResumeBenefit']:
                        return ResumeBenefit

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ResumeBenefit'],
                                       typing.List['ResumeBenefit']],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'DesiredBenefits':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> 'ResumeBenefit':
                    return super().__getitem__(i)

            class DesiredLocations(schemas.ListSchema):

                class MetaOapg:

                    @staticmethod
                    def items() -> typing.Type['BaseLocationsLocation']:
                        return BaseLocationsLocation

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['BaseLocationsLocation'],
                                       typing.List['BaseLocationsLocation']],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'DesiredLocations':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> 'BaseLocationsLocation':
                    return super().__getitem__(i)

            @staticmethod
            def RelocationPreferences(
            ) -> typing.Type['RelocationPreferences']:
                return RelocationPreferences

            @staticmethod
            def RemoteWorking() -> typing.Type['JobAdRemoteWorking']:
                return JobAdRemoteWorking

            @staticmethod
            def JobShift() -> typing.Type['JobShift']:
                return JobShift

            class OriginLinks(schemas.ListSchema):

                class MetaOapg:

                    @staticmethod
                    def items() -> typing.Type['JobadLinkLink']:
                        return JobadLinkLink

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['JobadLinkLink'],
                                       typing.List['JobadLinkLink']],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'OriginLinks':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> 'JobadLinkLink':
                    return super().__getitem__(i)

            __annotations__ = {
                "Objective": Objective,
                "ProfessionalSummary": ProfessionalSummary,
                "DesiredEmployment": DesiredEmployment,
                "DesiredContracts": DesiredContracts,
                "DesiredSalary": DesiredSalary,
                "DesiredBenefits": DesiredBenefits,
                "DesiredLocations": DesiredLocations,
                "RelocationPreferences": RelocationPreferences,
                "RemoteWorking": RemoteWorking,
                "JobShift": JobShift,
                "OriginLinks": OriginLinks,
            }

        additional_properties = schemas.NotAnyTypeSchema

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Objective"]
    ) -> 'BaseBenefitsValueModelStrictStr':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["ProfessionalSummary"]
    ) -> 'BaseBenefitsValueModelStrictStr':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["DesiredEmployment"]
    ) -> 'ResumeEmployment':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["DesiredContracts"]
    ) -> MetaOapg.properties.DesiredContracts:
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["DesiredSalary"]
    ) -> 'ResumeSalary':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["DesiredBenefits"]
    ) -> MetaOapg.properties.DesiredBenefits:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["DesiredLocations"]
    ) -> MetaOapg.properties.DesiredLocations:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["RelocationPreferences"]
    ) -> 'RelocationPreferences':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["RemoteWorking"]
    ) -> 'JobAdRemoteWorking':
        ...

    @typing.overload
    def __getitem__(self,
                    name: typing_extensions.Literal["JobShift"]) -> 'JobShift':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["OriginLinks"]
    ) -> MetaOapg.properties.OriginLinks:
        ...

    def __getitem__(
        self,
        name: typing.Union[typing_extensions.Literal["Objective"],
                           typing_extensions.Literal["ProfessionalSummary"],
                           typing_extensions.Literal["DesiredEmployment"],
                           typing_extensions.Literal["DesiredContracts"],
                           typing_extensions.Literal["DesiredSalary"],
                           typing_extensions.Literal["DesiredBenefits"],
                           typing_extensions.Literal["DesiredLocations"],
                           typing_extensions.Literal["RelocationPreferences"],
                           typing_extensions.Literal["RemoteWorking"],
                           typing_extensions.Literal["JobShift"],
                           typing_extensions.Literal["OriginLinks"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Objective"]
    ) -> typing.Union['BaseBenefitsValueModelStrictStr', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["ProfessionalSummary"]
    ) -> typing.Union['BaseBenefitsValueModelStrictStr', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["DesiredEmployment"]
    ) -> typing.Union['ResumeEmployment', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["DesiredContracts"]
    ) -> typing.Union[MetaOapg.properties.DesiredContracts, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["DesiredSalary"]
    ) -> typing.Union['ResumeSalary', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["DesiredBenefits"]
    ) -> typing.Union[MetaOapg.properties.DesiredBenefits, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["DesiredLocations"]
    ) -> typing.Union[MetaOapg.properties.DesiredLocations, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["RelocationPreferences"]
    ) -> typing.Union['RelocationPreferences', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["RemoteWorking"]
    ) -> typing.Union['JobAdRemoteWorking', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["JobShift"]
    ) -> typing.Union['JobShift', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["OriginLinks"]
    ) -> typing.Union[MetaOapg.properties.OriginLinks, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[typing_extensions.Literal["Objective"],
                           typing_extensions.Literal["ProfessionalSummary"],
                           typing_extensions.Literal["DesiredEmployment"],
                           typing_extensions.Literal["DesiredContracts"],
                           typing_extensions.Literal["DesiredSalary"],
                           typing_extensions.Literal["DesiredBenefits"],
                           typing_extensions.Literal["DesiredLocations"],
                           typing_extensions.Literal["RelocationPreferences"],
                           typing_extensions.Literal["RemoteWorking"],
                           typing_extensions.Literal["JobShift"],
                           typing_extensions.Literal["OriginLinks"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Objective: typing.Union['BaseBenefitsValueModelStrictStr',
                                schemas.Unset] = schemas.unset,
        ProfessionalSummary: typing.Union['BaseBenefitsValueModelStrictStr',
                                          schemas.Unset] = schemas.unset,
        DesiredEmployment: typing.Union['ResumeEmployment',
                                        schemas.Unset] = schemas.unset,
        DesiredContracts: typing.Union[MetaOapg.properties.DesiredContracts,
                                       list, tuple,
                                       schemas.Unset] = schemas.unset,
        DesiredSalary: typing.Union['ResumeSalary',
                                    schemas.Unset] = schemas.unset,
        DesiredBenefits: typing.Union[MetaOapg.properties.DesiredBenefits,
                                      list, tuple,
                                      schemas.Unset] = schemas.unset,
        DesiredLocations: typing.Union[MetaOapg.properties.DesiredLocations,
                                       list, tuple,
                                       schemas.Unset] = schemas.unset,
        RelocationPreferences: typing.Union['RelocationPreferences',
                                            schemas.Unset] = schemas.unset,
        RemoteWorking: typing.Union['JobAdRemoteWorking',
                                    schemas.Unset] = schemas.unset,
        JobShift: typing.Union['JobShift', schemas.Unset] = schemas.unset,
        OriginLinks: typing.Union[MetaOapg.properties.OriginLinks, list, tuple,
                                  schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ApplicationCommonData':
        return super().__new__(
            cls,
            *_args,
            Objective=Objective,
            ProfessionalSummary=ProfessionalSummary,
            DesiredEmployment=DesiredEmployment,
            DesiredContracts=DesiredContracts,
            DesiredSalary=DesiredSalary,
            DesiredBenefits=DesiredBenefits,
            DesiredLocations=DesiredLocations,
            RelocationPreferences=RelocationPreferences,
            RemoteWorking=RemoteWorking,
            JobShift=JobShift,
            OriginLinks=OriginLinks,
            _configuration=_configuration,
        )


from inda_hr.model.base_benefits_value_model_strict_str import BaseBenefitsValueModelStrictStr
from inda_hr.model.base_locations_location import BaseLocationsLocation
from inda_hr.model.job_ad_remote_working import JobAdRemoteWorking
from inda_hr.model.job_shift import JobShift
from inda_hr.model.jobad_link_link import JobadLinkLink
from inda_hr.model.relocation_preferences import RelocationPreferences
from inda_hr.model.resume_benefit import ResumeBenefit
from inda_hr.model.resume_contract import ResumeContract
from inda_hr.model.resume_employment import ResumeEmployment
from inda_hr.model.resume_salary import ResumeSalary
