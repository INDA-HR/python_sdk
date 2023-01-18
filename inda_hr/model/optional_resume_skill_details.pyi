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


class OptionalResumeSkillDetails(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            
            
            class TextPositions(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TextPosition']:
                        return TextPosition
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TextPosition'], typing.List['TextPosition']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'TextPositions':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TextPosition':
                    return super().__getitem__(i)
            RawValue = schemas.StrSchema
            
            
            class RawValues(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TextDetails']:
                        return TextDetails
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['TextDetails'], typing.List['TextDetails']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'RawValues':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TextDetails':
                    return super().__getitem__(i)
            IsValidated = schemas.BoolSchema
            EntityType = schemas.StrSchema
            ProficiencyLevel = schemas.StrSchema
            
            
            class Category(
                schemas.EnumBase,
                schemas.StrSchema
            ):
                
                @schemas.classproperty
                def HARD(cls):
                    return cls("hard")
                
                @schemas.classproperty
                def SOFT(cls):
                    return cls("soft")
                
                @schemas.classproperty
                def IT(cls):
                    return cls("IT")
                
                @schemas.classproperty
                def LANGUAGE(cls):
                    return cls("language")
        
            @staticmethod
            def Code() -> typing.Type['ResumeSkillCode']:
                return ResumeSkillCode
            
            
            class Score(
                schemas.NumberSchema
            ):
                pass
            __annotations__ = {
                "TextPositions": TextPositions,
                "RawValue": RawValue,
                "RawValues": RawValues,
                "IsValidated": IsValidated,
                "EntityType": EntityType,
                "ProficiencyLevel": ProficiencyLevel,
                "Category": Category,
                "Code": Code,
                "Score": Score,
            }
        additional_properties = schemas.NotAnyTypeSchema
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["TextPositions"]) -> MetaOapg.properties.TextPositions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RawValue"]) -> MetaOapg.properties.RawValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["RawValues"]) -> MetaOapg.properties.RawValues: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["IsValidated"]) -> MetaOapg.properties.IsValidated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["EntityType"]) -> MetaOapg.properties.EntityType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ProficiencyLevel"]) -> MetaOapg.properties.ProficiencyLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Category"]) -> MetaOapg.properties.Category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Code"]) -> 'ResumeSkillCode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["Score"]) -> MetaOapg.properties.Score: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["TextPositions"], typing_extensions.Literal["RawValue"], typing_extensions.Literal["RawValues"], typing_extensions.Literal["IsValidated"], typing_extensions.Literal["EntityType"], typing_extensions.Literal["ProficiencyLevel"], typing_extensions.Literal["Category"], typing_extensions.Literal["Code"], typing_extensions.Literal["Score"], ]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["TextPositions"]) -> typing.Union[MetaOapg.properties.TextPositions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RawValue"]) -> typing.Union[MetaOapg.properties.RawValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["RawValues"]) -> typing.Union[MetaOapg.properties.RawValues, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["IsValidated"]) -> typing.Union[MetaOapg.properties.IsValidated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["EntityType"]) -> typing.Union[MetaOapg.properties.EntityType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ProficiencyLevel"]) -> typing.Union[MetaOapg.properties.ProficiencyLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Category"]) -> typing.Union[MetaOapg.properties.Category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Code"]) -> typing.Union['ResumeSkillCode', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["Score"]) -> typing.Union[MetaOapg.properties.Score, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["TextPositions"], typing_extensions.Literal["RawValue"], typing_extensions.Literal["RawValues"], typing_extensions.Literal["IsValidated"], typing_extensions.Literal["EntityType"], typing_extensions.Literal["ProficiencyLevel"], typing_extensions.Literal["Category"], typing_extensions.Literal["Code"], typing_extensions.Literal["Score"], ]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        TextPositions: typing.Union[MetaOapg.properties.TextPositions, list, tuple, schemas.Unset] = schemas.unset,
        RawValue: typing.Union[MetaOapg.properties.RawValue, str, schemas.Unset] = schemas.unset,
        RawValues: typing.Union[MetaOapg.properties.RawValues, list, tuple, schemas.Unset] = schemas.unset,
        IsValidated: typing.Union[MetaOapg.properties.IsValidated, bool, schemas.Unset] = schemas.unset,
        EntityType: typing.Union[MetaOapg.properties.EntityType, str, schemas.Unset] = schemas.unset,
        ProficiencyLevel: typing.Union[MetaOapg.properties.ProficiencyLevel, str, schemas.Unset] = schemas.unset,
        Category: typing.Union[MetaOapg.properties.Category, str, schemas.Unset] = schemas.unset,
        Code: typing.Union['ResumeSkillCode', schemas.Unset] = schemas.unset,
        Score: typing.Union[MetaOapg.properties.Score, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OptionalResumeSkillDetails':
        return super().__new__(
            cls,
            *_args,
            TextPositions=TextPositions,
            RawValue=RawValue,
            RawValues=RawValues,
            IsValidated=IsValidated,
            EntityType=EntityType,
            ProficiencyLevel=ProficiencyLevel,
            Category=Category,
            Code=Code,
            Score=Score,
            _configuration=_configuration,
        )

from inda_hr.model.resume_skill_code import ResumeSkillCode
from inda_hr.model.text_details import TextDetails
from inda_hr.model.text_position import TextPosition
