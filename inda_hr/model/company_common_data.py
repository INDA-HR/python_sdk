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


class CompanyCommonData(schemas.DictSchema):
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
            def Name() -> typing.Type['BaseLocationsValueModelStrictStr']:
                return BaseLocationsValueModelStrictStr

            @staticmethod
            def Type() -> typing.Type['CompanyCommonType']:
                return CompanyCommonType

            @staticmethod
            def Size() -> typing.Type['Size']:
                return Size

            @staticmethod
            def Description(
            ) -> typing.Type['BaseLocationsValueModelStrictStr']:
                return BaseLocationsValueModelStrictStr

            class Headquarters(schemas.ListSchema):

                class MetaOapg:

                    @staticmethod
                    def items() -> typing.Type['Headquarter']:
                        return Headquarter

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Headquarter'],
                                       typing.List['Headquarter']],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'Headquarters':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> 'Headquarter':
                    return super().__getitem__(i)

            class Branches(schemas.ListSchema):

                class MetaOapg:

                    @staticmethod
                    def items() -> typing.Type['Branch']:
                        return Branch

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Branch'],
                                       typing.List['Branch']],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'Branches':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> 'Branch':
                    return super().__getitem__(i)

            class Industries(schemas.ListSchema):

                class MetaOapg:

                    @staticmethod
                    def items() -> typing.Type['CompanyCommonIndustry']:
                        return CompanyCommonIndustry

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CompanyCommonIndustry'],
                                       typing.List['CompanyCommonIndustry']],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'Industries':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> 'CompanyCommonIndustry':
                    return super().__getitem__(i)

            class Specialties(schemas.ListSchema):

                class MetaOapg:

                    @staticmethod
                    def items(
                    ) -> typing.Type['BaseLocationsValueModelStrictStr']:
                        return BaseLocationsValueModelStrictStr

                def __new__(
                    cls,
                    _arg: typing.Union[
                        typing.Tuple['BaseLocationsValueModelStrictStr'],
                        typing.List['BaseLocationsValueModelStrictStr']],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'Specialties':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self,
                                i: int) -> 'BaseLocationsValueModelStrictStr':
                    return super().__getitem__(i)

            @staticmethod
            def Founded() -> typing.Type['FoundationYear']:
                return FoundationYear

            @staticmethod
            def Logo() -> typing.Type['JobadLinkLink']:
                return JobadLinkLink

            @staticmethod
            def Link() -> typing.Type['JobadLinkLink']:
                return JobadLinkLink

            class Products(schemas.ListSchema):

                class MetaOapg:

                    @staticmethod
                    def items() -> typing.Type['Asset']:
                        return Asset

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Asset'],
                                       typing.List['Asset']],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'Products':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> 'Asset':
                    return super().__getitem__(i)

            class Services(schemas.ListSchema):

                class MetaOapg:

                    @staticmethod
                    def items() -> typing.Type['Asset']:
                        return Asset

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Asset'],
                                       typing.List['Asset']],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'Services':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> 'Asset':
                    return super().__getitem__(i)

            class RelatedCompanies(schemas.ListSchema):

                class MetaOapg:

                    @staticmethod
                    def items() -> typing.Type['RelatedCompany']:
                        return RelatedCompany

                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['RelatedCompany'],
                                       typing.List['RelatedCompany']],
                    _configuration: typing.Optional[
                        schemas.Configuration] = None,
                ) -> 'RelatedCompanies':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )

                def __getitem__(self, i: int) -> 'RelatedCompany':
                    return super().__getitem__(i)

            __annotations__ = {
                "Name": Name,
                "Type": Type,
                "Size": Size,
                "Description": Description,
                "Headquarters": Headquarters,
                "Branches": Branches,
                "Industries": Industries,
                "Specialties": Specialties,
                "Founded": Founded,
                "Logo": Logo,
                "Link": Link,
                "Products": Products,
                "Services": Services,
                "RelatedCompanies": RelatedCompanies,
            }

        additional_properties = schemas.NotAnyTypeSchema

    Name: 'BaseLocationsValueModelStrictStr'

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Name"]
    ) -> 'BaseLocationsValueModelStrictStr':
        ...

    @typing.overload
    def __getitem__(
            self,
            name: typing_extensions.Literal["Type"]) -> 'CompanyCommonType':
        ...

    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Size"]) -> 'Size':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Description"]
    ) -> 'BaseLocationsValueModelStrictStr':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Headquarters"]
    ) -> MetaOapg.properties.Headquarters:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Branches"]
    ) -> MetaOapg.properties.Branches:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Industries"]
    ) -> MetaOapg.properties.Industries:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Specialties"]
    ) -> MetaOapg.properties.Specialties:
        ...

    @typing.overload
    def __getitem__(
            self,
            name: typing_extensions.Literal["Founded"]) -> 'FoundationYear':
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["Logo"]) -> 'JobadLinkLink':
        ...

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["Link"]) -> 'JobadLinkLink':
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Products"]
    ) -> MetaOapg.properties.Products:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["Services"]
    ) -> MetaOapg.properties.Services:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["RelatedCompanies"]
    ) -> MetaOapg.properties.RelatedCompanies:
        ...

    def __getitem__(
        self,
        name: typing.Union[typing_extensions.Literal["Name"],
                           typing_extensions.Literal["Type"],
                           typing_extensions.Literal["Size"],
                           typing_extensions.Literal["Description"],
                           typing_extensions.Literal["Headquarters"],
                           typing_extensions.Literal["Branches"],
                           typing_extensions.Literal["Industries"],
                           typing_extensions.Literal["Specialties"],
                           typing_extensions.Literal["Founded"],
                           typing_extensions.Literal["Logo"],
                           typing_extensions.Literal["Link"],
                           typing_extensions.Literal["Products"],
                           typing_extensions.Literal["Services"],
                           typing_extensions.Literal["RelatedCompanies"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Name"]
    ) -> 'BaseLocationsValueModelStrictStr':
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Type"]
    ) -> typing.Union['CompanyCommonType', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Size"]
    ) -> typing.Union['Size', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Description"]
    ) -> typing.Union['BaseLocationsValueModelStrictStr', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Headquarters"]
    ) -> typing.Union[MetaOapg.properties.Headquarters, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Branches"]
    ) -> typing.Union[MetaOapg.properties.Branches, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Industries"]
    ) -> typing.Union[MetaOapg.properties.Industries, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Specialties"]
    ) -> typing.Union[MetaOapg.properties.Specialties, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Founded"]
    ) -> typing.Union['FoundationYear', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Logo"]
    ) -> typing.Union['JobadLinkLink', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Link"]
    ) -> typing.Union['JobadLinkLink', schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Products"]
    ) -> typing.Union[MetaOapg.properties.Products, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["Services"]
    ) -> typing.Union[MetaOapg.properties.Services, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["RelatedCompanies"]
    ) -> typing.Union[MetaOapg.properties.RelatedCompanies, schemas.Unset]:
        ...

    def get_item_oapg(
        self,
        name: typing.Union[typing_extensions.Literal["Name"],
                           typing_extensions.Literal["Type"],
                           typing_extensions.Literal["Size"],
                           typing_extensions.Literal["Description"],
                           typing_extensions.Literal["Headquarters"],
                           typing_extensions.Literal["Branches"],
                           typing_extensions.Literal["Industries"],
                           typing_extensions.Literal["Specialties"],
                           typing_extensions.Literal["Founded"],
                           typing_extensions.Literal["Logo"],
                           typing_extensions.Literal["Link"],
                           typing_extensions.Literal["Products"],
                           typing_extensions.Literal["Services"],
                           typing_extensions.Literal["RelatedCompanies"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        Name: 'BaseLocationsValueModelStrictStr',
        Type: typing.Union['CompanyCommonType', schemas.Unset] = schemas.unset,
        Size: typing.Union['Size', schemas.Unset] = schemas.unset,
        Description: typing.Union['BaseLocationsValueModelStrictStr',
                                  schemas.Unset] = schemas.unset,
        Headquarters: typing.Union[MetaOapg.properties.Headquarters, list,
                                   tuple, schemas.Unset] = schemas.unset,
        Branches: typing.Union[MetaOapg.properties.Branches, list, tuple,
                               schemas.Unset] = schemas.unset,
        Industries: typing.Union[MetaOapg.properties.Industries, list, tuple,
                                 schemas.Unset] = schemas.unset,
        Specialties: typing.Union[MetaOapg.properties.Specialties, list, tuple,
                                  schemas.Unset] = schemas.unset,
        Founded: typing.Union['FoundationYear', schemas.Unset] = schemas.unset,
        Logo: typing.Union['JobadLinkLink', schemas.Unset] = schemas.unset,
        Link: typing.Union['JobadLinkLink', schemas.Unset] = schemas.unset,
        Products: typing.Union[MetaOapg.properties.Products, list, tuple,
                               schemas.Unset] = schemas.unset,
        Services: typing.Union[MetaOapg.properties.Services, list, tuple,
                               schemas.Unset] = schemas.unset,
        RelatedCompanies: typing.Union[MetaOapg.properties.RelatedCompanies,
                                       list, tuple,
                                       schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CompanyCommonData':
        return super().__new__(
            cls,
            *_args,
            Name=Name,
            Type=Type,
            Size=Size,
            Description=Description,
            Headquarters=Headquarters,
            Branches=Branches,
            Industries=Industries,
            Specialties=Specialties,
            Founded=Founded,
            Logo=Logo,
            Link=Link,
            Products=Products,
            Services=Services,
            RelatedCompanies=RelatedCompanies,
            _configuration=_configuration,
        )


from inda_hr.model.asset import Asset
from inda_hr.model.base_locations_value_model_strict_str import BaseLocationsValueModelStrictStr
from inda_hr.model.branch import Branch
from inda_hr.model.company_common_industry import CompanyCommonIndustry
from inda_hr.model.company_common_type import CompanyCommonType
from inda_hr.model.foundation_year import FoundationYear
from inda_hr.model.headquarter import Headquarter
from inda_hr.model.jobad_link_link import JobadLinkLink
from inda_hr.model.related_company import RelatedCompany
from inda_hr.model.size import Size
