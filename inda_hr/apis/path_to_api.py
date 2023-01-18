import typing_extensions

from inda_hr.paths import PathValues
from inda_hr.apis.paths.hr_v2_auth_login_ import HrV2AuthLogin
from inda_hr.apis.paths.hr_v2_index_indexname_credits_ import HrV2IndexIndexnameCredits
from inda_hr.apis.paths.hr_v2_keywords_search_autocomplete_ import HrV2KeywordsSearchAutocomplete
from inda_hr.apis.paths.hr_v2_parse_resume_data_ import HrV2ParseResumeData
from inda_hr.apis.paths.hr_v2_keywords_map_entity_ import HrV2KeywordsMapEntity
from inda_hr.apis.paths.hr_v2_keywords_bulk_map_entity_ import HrV2KeywordsBulkMapEntity
from inda_hr.apis.paths.hr_v2_parse_resume_text_ import HrV2ParseResumeText
from inda_hr.apis.paths.hr_v2_parse_resume_anonymize_ import HrV2ParseResumeAnonymize
from inda_hr.apis.paths.hr_v2_parse_jobad_skills_ import HrV2ParseJobadSkills
from inda_hr.apis.paths.hr_v2_parse_jobad_jobtitles_ import HrV2ParseJobadJobtitles
from inda_hr.apis.paths.hr_v2_parse_jobad_languages_ import HrV2ParseJobadLanguages
from inda_hr.apis.paths.hr_v2_occupations_similar_esco_ import HrV2OccupationsSimilarEsco
from inda_hr.apis.paths.hr_v2_occupations_description_match_esco_ import HrV2OccupationsDescriptionMatchEsco
from inda_hr.apis.paths.hr_v2_occupations_similar_esco_hierarchy_ import HrV2OccupationsSimilarEscoHierarchy
from inda_hr.apis.paths.hr_v2_occupations_mapping_esco_ import HrV2OccupationsMappingEsco
from inda_hr.apis.paths.hr_v2_occupations_mapping_istat_ import HrV2OccupationsMappingIstat
from inda_hr.apis.paths.hr_v2_occupations_mapping_onet_ import HrV2OccupationsMappingOnet
from inda_hr.apis.paths.hr_v2_occupations_mapping_isco_ import HrV2OccupationsMappingIsco
from inda_hr.apis.paths.hr_v2_occupations_similar_semantic_ import HrV2OccupationsSimilarSemantic
from inda_hr.apis.paths.hr_v2_skills_similar_esco_ import HrV2SkillsSimilarEsco
from inda_hr.apis.paths.hr_v2_skills_description_match_esco_ import HrV2SkillsDescriptionMatchEsco
from inda_hr.apis.paths.hr_v2_skills_similar_esco_hierarchy_ import HrV2SkillsSimilarEscoHierarchy
from inda_hr.apis.paths.hr_v2_skills_similar_semantic_ import HrV2SkillsSimilarSemantic
from inda_hr.apis.paths.hr_v2_skills_classification_ import HrV2SkillsClassification
from inda_hr.apis.paths.hr_v2_index_indexname_resume_ import HrV2IndexIndexnameResume
from inda_hr.apis.paths.hr_v2_index_indexname_resume_resume_id_ import HrV2IndexIndexnameResumeResumeId
from inda_hr.apis.paths.hr_v2_index_indexname_jobad_ import HrV2IndexIndexnameJobad
from inda_hr.apis.paths.hr_v2_index_indexname_jobad_jobad_id_ import HrV2IndexIndexnameJobadJobadId
from inda_hr.apis.paths.hr_v2_index_indexname_jobad_jobad_id_apply_ import HrV2IndexIndexnameJobadJobadIdApply
from inda_hr.apis.paths.hr_v2_index_indexname_jobad_jobad_id_applications_resume_resume_id_ import HrV2IndexIndexnameJobadJobadIdApplicationsResumeResumeId
from inda_hr.apis.paths.hr_v2_index_indexname_jobad_jobad_id_applications_resume_resume_id_hiring_pipeline_stage_ import HrV2IndexIndexnameJobadJobadIdApplicationsResumeResumeIdHiringPipelineStage
from inda_hr.apis.paths.hr_v2_company_ import HrV2Company
from inda_hr.apis.paths.hr_v2_company_company_id_ import HrV2CompanyCompanyId
from inda_hr.apis.paths.hr_v2_company_name_search_autocomplete_ import HrV2CompanyNameSearchAutocomplete
from inda_hr.apis.paths.hr_v2_index_indexname_resume_resume_id_status_ import HrV2IndexIndexnameResumeResumeIdStatus
from inda_hr.apis.paths.hr_v2_index_indexname_failures_ import HrV2IndexIndexnameFailures
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_import_aws_status_ import HrV2IndexIndexnameResumesImportAwsStatus
from inda_hr.apis.paths.hr_v2_index_indexname_jobad_jobad_id_applications_resume_resume_id_status_ import HrV2IndexIndexnameJobadJobadIdApplicationsResumeResumeIdStatus
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_search_full_text_ import HrV2IndexIndexnameResumesSearchFullText
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_search_semantic_ import HrV2IndexIndexnameResumesSearchSemantic
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_search_scroll_ import HrV2IndexIndexnameResumesSearchScroll
from inda_hr.apis.paths.hr_v2_keywords_search_semantic_ import HrV2KeywordsSearchSemantic
from inda_hr.apis.paths.hr_v2_index_indexname_resume_resume_id_keywords_search_semantic_ import HrV2IndexIndexnameResumeResumeIdKeywordsSearchSemantic
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_search_semantic_evidence_ import HrV2IndexIndexnameResumesSearchSemanticEvidence
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_matching_resume_resume_id_ import HrV2IndexIndexnameResumesMatchingResumeResumeId
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_matching_jobad_ import HrV2IndexIndexnameResumesMatchingJobad
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_matching_jobad_jobad_id_ import HrV2IndexIndexnameResumesMatchingJobadJobadId
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_matching_jobad_evidence_ import HrV2IndexIndexnameResumesMatchingJobadEvidence
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_matching_jobad_jobad_id_evidence_ import HrV2IndexIndexnameResumesMatchingJobadJobadIdEvidence
from inda_hr.apis.paths.hr_v2_index_indexname_jobads_matching_resume_ import HrV2IndexIndexnameJobadsMatchingResume
from inda_hr.apis.paths.hr_v2_index_indexname_jobads_matching_resume_resume_id_ import HrV2IndexIndexnameJobadsMatchingResumeResumeId
from inda_hr.apis.paths.hr_v2_index_indexname_jobads_matching_resume_evidence_ import HrV2IndexIndexnameJobadsMatchingResumeEvidence
from inda_hr.apis.paths.hr_v2_index_indexname_jobads_matching_resume_resume_id_evidence_ import HrV2IndexIndexnameJobadsMatchingResumeResumeIdEvidence
from inda_hr.apis.paths.hr_v2_index_indexname_jobads_search_full_text_ import HrV2IndexIndexnameJobadsSearchFullText
from inda_hr.apis.paths.hr_v2_index_indexname_jobad_jobad_id_applications_resumes_search_ import HrV2IndexIndexnameJobadJobadIdApplicationsResumesSearch
from inda_hr.apis.paths.hr_v2_index_indexname_resume_resume_id_applications_jobads_search_ import HrV2IndexIndexnameResumeResumeIdApplicationsJobadsSearch
from inda_hr.apis.paths.hr_v2_resume_career_occupation_recommendation_ import HrV2ResumeCareerOccupationRecommendation
from inda_hr.apis.paths.hr_v2_resume_career_occupation_skills_comparison_ import HrV2ResumeCareerOccupationSkillsComparison
from inda_hr.apis.paths.hr_v2_resume_career_occupation_activities_comparison_ import HrV2ResumeCareerOccupationActivitiesComparison
from inda_hr.apis.paths.hr_v2_resume_career_simulator_upskilling_ import HrV2ResumeCareerSimulatorUpskilling
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_import_aws_ import HrV2IndexIndexnameResumesImportAws
from inda_hr.apis.paths.hr_v2_index_indexname_stats_ import HrV2IndexIndexnameStats
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_latest_ import HrV2IndexIndexnameResumesLatest
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_customize_ import HrV2IndexIndexnameResumesCustomize
from inda_hr.apis.paths.hr_v2_index_indexname_resumes_mapping_ import HrV2IndexIndexnameResumesMapping
from inda_hr.apis.paths.hr_v2_index_indexname_resume_resume_id_document_ import HrV2IndexIndexnameResumeResumeIdDocument
from inda_hr.apis.paths.hr_v2_index_indexname_resume_resume_id_pic_ import HrV2IndexIndexnameResumeResumeIdPic
from inda_hr.apis.paths.hr_v2_index_indexname_resume_resume_id_text_ import HrV2IndexIndexnameResumeResumeIdText
from inda_hr.apis.paths.hr_v2_index_indexname_cache_ import HrV2IndexIndexnameCache
from inda_hr.apis.paths.hr_v2_index_indexname_jobads_ import HrV2IndexIndexnameJobads
from inda_hr.apis.paths.hr_v2_index_indexname_jobad_jobad_id_applications_resumes_ import HrV2IndexIndexnameJobadJobadIdApplicationsResumes
from inda_hr.apis.paths.hr_v2_index_indexname_resume_resume_id_applications_jobads_ import HrV2IndexIndexnameResumeResumeIdApplicationsJobads
from inda_hr.apis.paths.hr_v2_data_industries_ import HrV2DataIndustries
from inda_hr.apis.paths.hr_v2_data_company_size_ import HrV2DataCompanySize
from inda_hr.apis.paths.hr_v2_data_company_type_ import HrV2DataCompanyType
from inda_hr.apis.paths.hr_v2_data_contract_type_ import HrV2DataContractType
from inda_hr.apis.paths.hr_v2_data_employment_type_ import HrV2DataEmploymentType
from inda_hr.apis.paths.hr_v2_data_jobshift_type_ import HrV2DataJobshiftType
from inda_hr.apis.paths.hr_v2_data_salary_type_ import HrV2DataSalaryType
from inda_hr.apis.paths.hr_v2_data_salary_frequency_ import HrV2DataSalaryFrequency
from inda_hr.apis.paths.hr_v2_data_seniority_level_ import HrV2DataSeniorityLevel
from inda_hr.apis.paths.hr_v2_data_phone_label_ import HrV2DataPhoneLabel
from inda_hr.apis.paths.hr_v2_data_link_label_ import HrV2DataLinkLabel
from inda_hr.apis.paths.hr_v2_data_email_label_ import HrV2DataEmailLabel
from inda_hr.apis.paths.hr_v2_data_marital_status_ import HrV2DataMaritalStatus
from inda_hr.apis.paths.hr_v2_data_name_prefix_ import HrV2DataNamePrefix
from inda_hr.apis.paths.hr_v2_data_name_suffix_ import HrV2DataNameSuffix
from inda_hr.apis.paths.hr_v2_data_education_title_ import HrV2DataEducationTitle
from inda_hr.apis.paths.hr_v2_data_education_field_of_study_ import HrV2DataEducationFieldOfStudy
from inda_hr.apis.paths.hr_v2_data_patent_status_ import HrV2DataPatentStatus
from inda_hr.apis.paths.hr_v2_data_gender_ import HrV2DataGender
from inda_hr.apis.paths.hr_v2_data_protected_group_ import HrV2DataProtectedGroup
from inda_hr.apis.paths.hr_v2_data_disability_ import HrV2DataDisability
from inda_hr.apis.paths.hr_v2_data_job_function_ import HrV2DataJobFunction
from inda_hr.apis.paths.hr_v2_data_employment_remote_working_ import HrV2DataEmploymentRemoteWorking
from inda_hr.apis.paths.hr_v2_data_license_type_ import HrV2DataLicenseType
from inda_hr.apis.paths.hr_v2_data_license_type_license_type_code_ import HrV2DataLicenseTypeLicenseTypeCode
from inda_hr.apis.paths.hr_v2_university_name_search_autocomplete_ import HrV2UniversityNameSearchAutocomplete
from inda_hr.apis.paths.hr_v2_university_university_id_ import HrV2UniversityUniversityId
from inda_hr.apis.paths.hr_v2_feedback_index_indexname_resume_resume_id_parse_data_ import HrV2FeedbackIndexIndexnameResumeResumeIdParseData
from inda_hr.apis.paths.hr_v2_feedback_index_indexname_resume_resume_id_search_semantic_ import HrV2FeedbackIndexIndexnameResumeResumeIdSearchSemantic
from inda_hr.apis.paths.hr_v2_ import HrV2

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.HR_V2_AUTH_LOGIN_: HrV2AuthLogin,
        PathValues.HR_V2_INDEX_INDEXNAME_CREDITS_: HrV2IndexIndexnameCredits,
        PathValues.HR_V2_KEYWORDS_SEARCH_AUTOCOMPLETE_: HrV2KeywordsSearchAutocomplete,
        PathValues.HR_V2_PARSE_RESUME_DATA_: HrV2ParseResumeData,
        PathValues.HR_V2_KEYWORDS_MAP_ENTITY_: HrV2KeywordsMapEntity,
        PathValues.HR_V2_KEYWORDS_BULK_MAP_ENTITY_: HrV2KeywordsBulkMapEntity,
        PathValues.HR_V2_PARSE_RESUME_TEXT_: HrV2ParseResumeText,
        PathValues.HR_V2_PARSE_RESUME_ANONYMIZE_: HrV2ParseResumeAnonymize,
        PathValues.HR_V2_PARSE_JOBAD_SKILLS_: HrV2ParseJobadSkills,
        PathValues.HR_V2_PARSE_JOBAD_JOBTITLES_: HrV2ParseJobadJobtitles,
        PathValues.HR_V2_PARSE_JOBAD_LANGUAGES_: HrV2ParseJobadLanguages,
        PathValues.HR_V2_OCCUPATIONS_SIMILAR_ESCO_: HrV2OccupationsSimilarEsco,
        PathValues.HR_V2_OCCUPATIONS_DESCRIPTION_MATCH_ESCO_: HrV2OccupationsDescriptionMatchEsco,
        PathValues.HR_V2_OCCUPATIONS_SIMILAR_ESCO_HIERARCHY_: HrV2OccupationsSimilarEscoHierarchy,
        PathValues.HR_V2_OCCUPATIONS_MAPPING_ESCO_: HrV2OccupationsMappingEsco,
        PathValues.HR_V2_OCCUPATIONS_MAPPING_ISTAT_: HrV2OccupationsMappingIstat,
        PathValues.HR_V2_OCCUPATIONS_MAPPING_ONET_: HrV2OccupationsMappingOnet,
        PathValues.HR_V2_OCCUPATIONS_MAPPING_ISCO_: HrV2OccupationsMappingIsco,
        PathValues.HR_V2_OCCUPATIONS_SIMILAR_SEMANTIC_: HrV2OccupationsSimilarSemantic,
        PathValues.HR_V2_SKILLS_SIMILAR_ESCO_: HrV2SkillsSimilarEsco,
        PathValues.HR_V2_SKILLS_DESCRIPTION_MATCH_ESCO_: HrV2SkillsDescriptionMatchEsco,
        PathValues.HR_V2_SKILLS_SIMILAR_ESCO_HIERARCHY_: HrV2SkillsSimilarEscoHierarchy,
        PathValues.HR_V2_SKILLS_SIMILAR_SEMANTIC_: HrV2SkillsSimilarSemantic,
        PathValues.HR_V2_SKILLS_CLASSIFICATION_: HrV2SkillsClassification,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_: HrV2IndexIndexnameResume,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_: HrV2IndexIndexnameResumeResumeId,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_: HrV2IndexIndexnameJobad,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_: HrV2IndexIndexnameJobadJobadId,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLY_: HrV2IndexIndexnameJobadJobadIdApply,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLICATIONS_RESUME_RESUME_ID_: HrV2IndexIndexnameJobadJobadIdApplicationsResumeResumeId,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLICATIONS_RESUME_RESUME_ID_HIRINGPIPELINE_STAGE_: HrV2IndexIndexnameJobadJobadIdApplicationsResumeResumeIdHiringPipelineStage,
        PathValues.HR_V2_COMPANY_: HrV2Company,
        PathValues.HR_V2_COMPANY_COMPANY_ID_: HrV2CompanyCompanyId,
        PathValues.HR_V2_COMPANY_NAME_SEARCH_AUTOCOMPLETE_: HrV2CompanyNameSearchAutocomplete,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_STATUS_: HrV2IndexIndexnameResumeResumeIdStatus,
        PathValues.HR_V2_INDEX_INDEXNAME_FAILURES_: HrV2IndexIndexnameFailures,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_IMPORT_AWS_STATUS_: HrV2IndexIndexnameResumesImportAwsStatus,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLICATIONS_RESUME_RESUME_ID_STATUS_: HrV2IndexIndexnameJobadJobadIdApplicationsResumeResumeIdStatus,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_SEARCH_FULLTEXT_: HrV2IndexIndexnameResumesSearchFullText,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_SEARCH_SEMANTIC_: HrV2IndexIndexnameResumesSearchSemantic,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_SEARCH_SCROLL_: HrV2IndexIndexnameResumesSearchScroll,
        PathValues.HR_V2_KEYWORDS_SEARCH_SEMANTIC_: HrV2KeywordsSearchSemantic,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_KEYWORDS_SEARCH_SEMANTIC_: HrV2IndexIndexnameResumeResumeIdKeywordsSearchSemantic,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_SEARCH_SEMANTIC_EVIDENCE_: HrV2IndexIndexnameResumesSearchSemanticEvidence,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MATCHING_RESUME_RESUME_ID_: HrV2IndexIndexnameResumesMatchingResumeResumeId,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MATCHING_JOBAD_: HrV2IndexIndexnameResumesMatchingJobad,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MATCHING_JOBAD_JOBAD_ID_: HrV2IndexIndexnameResumesMatchingJobadJobadId,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MATCHING_JOBAD_EVIDENCE_: HrV2IndexIndexnameResumesMatchingJobadEvidence,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MATCHING_JOBAD_JOBAD_ID_EVIDENCE_: HrV2IndexIndexnameResumesMatchingJobadJobadIdEvidence,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_MATCHING_RESUME_: HrV2IndexIndexnameJobadsMatchingResume,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_MATCHING_RESUME_RESUME_ID_: HrV2IndexIndexnameJobadsMatchingResumeResumeId,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_MATCHING_RESUME_EVIDENCE_: HrV2IndexIndexnameJobadsMatchingResumeEvidence,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_MATCHING_RESUME_RESUME_ID_EVIDENCE_: HrV2IndexIndexnameJobadsMatchingResumeResumeIdEvidence,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_SEARCH_FULLTEXT_: HrV2IndexIndexnameJobadsSearchFullText,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLICATIONS_RESUMES_SEARCH_: HrV2IndexIndexnameJobadJobadIdApplicationsResumesSearch,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_APPLICATIONS_JOBADS_SEARCH_: HrV2IndexIndexnameResumeResumeIdApplicationsJobadsSearch,
        PathValues.HR_V2_RESUME_CAREER_OCCUPATION_RECOMMENDATION_: HrV2ResumeCareerOccupationRecommendation,
        PathValues.HR_V2_RESUME_CAREER_OCCUPATION_SKILLS_COMPARISON_: HrV2ResumeCareerOccupationSkillsComparison,
        PathValues.HR_V2_RESUME_CAREER_OCCUPATION_ACTIVITIES_COMPARISON_: HrV2ResumeCareerOccupationActivitiesComparison,
        PathValues.HR_V2_RESUME_CAREER_SIMULATOR_UPSKILLING_: HrV2ResumeCareerSimulatorUpskilling,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_IMPORT_AWS_: HrV2IndexIndexnameResumesImportAws,
        PathValues.HR_V2_INDEX_INDEXNAME_STATS_: HrV2IndexIndexnameStats,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_LATEST_: HrV2IndexIndexnameResumesLatest,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_CUSTOMIZE_: HrV2IndexIndexnameResumesCustomize,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MAPPING_: HrV2IndexIndexnameResumesMapping,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_DOCUMENT_: HrV2IndexIndexnameResumeResumeIdDocument,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_PIC_: HrV2IndexIndexnameResumeResumeIdPic,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_TEXT_: HrV2IndexIndexnameResumeResumeIdText,
        PathValues.HR_V2_INDEX_INDEXNAME_CACHE_: HrV2IndexIndexnameCache,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_: HrV2IndexIndexnameJobads,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLICATIONS_RESUMES_: HrV2IndexIndexnameJobadJobadIdApplicationsResumes,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_APPLICATIONS_JOBADS_: HrV2IndexIndexnameResumeResumeIdApplicationsJobads,
        PathValues.HR_V2_DATA_INDUSTRIES_: HrV2DataIndustries,
        PathValues.HR_V2_DATA_COMPANY_SIZE_: HrV2DataCompanySize,
        PathValues.HR_V2_DATA_COMPANY_TYPE_: HrV2DataCompanyType,
        PathValues.HR_V2_DATA_CONTRACT_TYPE_: HrV2DataContractType,
        PathValues.HR_V2_DATA_EMPLOYMENT_TYPE_: HrV2DataEmploymentType,
        PathValues.HR_V2_DATA_JOBSHIFT_TYPE_: HrV2DataJobshiftType,
        PathValues.HR_V2_DATA_SALARY_TYPE_: HrV2DataSalaryType,
        PathValues.HR_V2_DATA_SALARY_FREQUENCY_: HrV2DataSalaryFrequency,
        PathValues.HR_V2_DATA_SENIORITY_LEVEL_: HrV2DataSeniorityLevel,
        PathValues.HR_V2_DATA_PHONE_LABEL_: HrV2DataPhoneLabel,
        PathValues.HR_V2_DATA_LINK_LABEL_: HrV2DataLinkLabel,
        PathValues.HR_V2_DATA_EMAIL_LABEL_: HrV2DataEmailLabel,
        PathValues.HR_V2_DATA_MARITALSTATUS_: HrV2DataMaritalStatus,
        PathValues.HR_V2_DATA_NAME_PREFIX_: HrV2DataNamePrefix,
        PathValues.HR_V2_DATA_NAME_SUFFIX_: HrV2DataNameSuffix,
        PathValues.HR_V2_DATA_EDUCATION_TITLE_: HrV2DataEducationTitle,
        PathValues.HR_V2_DATA_EDUCATION_FIELDOFSTUDY_: HrV2DataEducationFieldOfStudy,
        PathValues.HR_V2_DATA_PATENT_STATUS_: HrV2DataPatentStatus,
        PathValues.HR_V2_DATA_GENDER_: HrV2DataGender,
        PathValues.HR_V2_DATA_PROTECTEDGROUP_: HrV2DataProtectedGroup,
        PathValues.HR_V2_DATA_DISABILITY_: HrV2DataDisability,
        PathValues.HR_V2_DATA_JOB_FUNCTION_: HrV2DataJobFunction,
        PathValues.HR_V2_DATA_EMPLOYMENT_REMOTEWORKING_: HrV2DataEmploymentRemoteWorking,
        PathValues.HR_V2_DATA_LICENSE_TYPE_: HrV2DataLicenseType,
        PathValues.HR_V2_DATA_LICENSE_TYPE_LICENSE_TYPE_CODE_: HrV2DataLicenseTypeLicenseTypeCode,
        PathValues.HR_V2_UNIVERSITY_NAME_SEARCH_AUTOCOMPLETE_: HrV2UniversityNameSearchAutocomplete,
        PathValues.HR_V2_UNIVERSITY_UNIVERSITY_ID_: HrV2UniversityUniversityId,
        PathValues.HR_V2_FEEDBACK_INDEX_INDEXNAME_RESUME_RESUME_ID_PARSE_DATA_: HrV2FeedbackIndexIndexnameResumeResumeIdParseData,
        PathValues.HR_V2_FEEDBACK_INDEX_INDEXNAME_RESUME_RESUME_ID_SEARCH_SEMANTIC_: HrV2FeedbackIndexIndexnameResumeResumeIdSearchSemantic,
        PathValues.HR_V2_: HrV2,
    }
)

path_to_api = PathToApi(
    {
        PathValues.HR_V2_AUTH_LOGIN_: HrV2AuthLogin,
        PathValues.HR_V2_INDEX_INDEXNAME_CREDITS_: HrV2IndexIndexnameCredits,
        PathValues.HR_V2_KEYWORDS_SEARCH_AUTOCOMPLETE_: HrV2KeywordsSearchAutocomplete,
        PathValues.HR_V2_PARSE_RESUME_DATA_: HrV2ParseResumeData,
        PathValues.HR_V2_KEYWORDS_MAP_ENTITY_: HrV2KeywordsMapEntity,
        PathValues.HR_V2_KEYWORDS_BULK_MAP_ENTITY_: HrV2KeywordsBulkMapEntity,
        PathValues.HR_V2_PARSE_RESUME_TEXT_: HrV2ParseResumeText,
        PathValues.HR_V2_PARSE_RESUME_ANONYMIZE_: HrV2ParseResumeAnonymize,
        PathValues.HR_V2_PARSE_JOBAD_SKILLS_: HrV2ParseJobadSkills,
        PathValues.HR_V2_PARSE_JOBAD_JOBTITLES_: HrV2ParseJobadJobtitles,
        PathValues.HR_V2_PARSE_JOBAD_LANGUAGES_: HrV2ParseJobadLanguages,
        PathValues.HR_V2_OCCUPATIONS_SIMILAR_ESCO_: HrV2OccupationsSimilarEsco,
        PathValues.HR_V2_OCCUPATIONS_DESCRIPTION_MATCH_ESCO_: HrV2OccupationsDescriptionMatchEsco,
        PathValues.HR_V2_OCCUPATIONS_SIMILAR_ESCO_HIERARCHY_: HrV2OccupationsSimilarEscoHierarchy,
        PathValues.HR_V2_OCCUPATIONS_MAPPING_ESCO_: HrV2OccupationsMappingEsco,
        PathValues.HR_V2_OCCUPATIONS_MAPPING_ISTAT_: HrV2OccupationsMappingIstat,
        PathValues.HR_V2_OCCUPATIONS_MAPPING_ONET_: HrV2OccupationsMappingOnet,
        PathValues.HR_V2_OCCUPATIONS_MAPPING_ISCO_: HrV2OccupationsMappingIsco,
        PathValues.HR_V2_OCCUPATIONS_SIMILAR_SEMANTIC_: HrV2OccupationsSimilarSemantic,
        PathValues.HR_V2_SKILLS_SIMILAR_ESCO_: HrV2SkillsSimilarEsco,
        PathValues.HR_V2_SKILLS_DESCRIPTION_MATCH_ESCO_: HrV2SkillsDescriptionMatchEsco,
        PathValues.HR_V2_SKILLS_SIMILAR_ESCO_HIERARCHY_: HrV2SkillsSimilarEscoHierarchy,
        PathValues.HR_V2_SKILLS_SIMILAR_SEMANTIC_: HrV2SkillsSimilarSemantic,
        PathValues.HR_V2_SKILLS_CLASSIFICATION_: HrV2SkillsClassification,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_: HrV2IndexIndexnameResume,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_: HrV2IndexIndexnameResumeResumeId,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_: HrV2IndexIndexnameJobad,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_: HrV2IndexIndexnameJobadJobadId,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLY_: HrV2IndexIndexnameJobadJobadIdApply,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLICATIONS_RESUME_RESUME_ID_: HrV2IndexIndexnameJobadJobadIdApplicationsResumeResumeId,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLICATIONS_RESUME_RESUME_ID_HIRINGPIPELINE_STAGE_: HrV2IndexIndexnameJobadJobadIdApplicationsResumeResumeIdHiringPipelineStage,
        PathValues.HR_V2_COMPANY_: HrV2Company,
        PathValues.HR_V2_COMPANY_COMPANY_ID_: HrV2CompanyCompanyId,
        PathValues.HR_V2_COMPANY_NAME_SEARCH_AUTOCOMPLETE_: HrV2CompanyNameSearchAutocomplete,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_STATUS_: HrV2IndexIndexnameResumeResumeIdStatus,
        PathValues.HR_V2_INDEX_INDEXNAME_FAILURES_: HrV2IndexIndexnameFailures,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_IMPORT_AWS_STATUS_: HrV2IndexIndexnameResumesImportAwsStatus,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLICATIONS_RESUME_RESUME_ID_STATUS_: HrV2IndexIndexnameJobadJobadIdApplicationsResumeResumeIdStatus,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_SEARCH_FULLTEXT_: HrV2IndexIndexnameResumesSearchFullText,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_SEARCH_SEMANTIC_: HrV2IndexIndexnameResumesSearchSemantic,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_SEARCH_SCROLL_: HrV2IndexIndexnameResumesSearchScroll,
        PathValues.HR_V2_KEYWORDS_SEARCH_SEMANTIC_: HrV2KeywordsSearchSemantic,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_KEYWORDS_SEARCH_SEMANTIC_: HrV2IndexIndexnameResumeResumeIdKeywordsSearchSemantic,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_SEARCH_SEMANTIC_EVIDENCE_: HrV2IndexIndexnameResumesSearchSemanticEvidence,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MATCHING_RESUME_RESUME_ID_: HrV2IndexIndexnameResumesMatchingResumeResumeId,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MATCHING_JOBAD_: HrV2IndexIndexnameResumesMatchingJobad,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MATCHING_JOBAD_JOBAD_ID_: HrV2IndexIndexnameResumesMatchingJobadJobadId,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MATCHING_JOBAD_EVIDENCE_: HrV2IndexIndexnameResumesMatchingJobadEvidence,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MATCHING_JOBAD_JOBAD_ID_EVIDENCE_: HrV2IndexIndexnameResumesMatchingJobadJobadIdEvidence,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_MATCHING_RESUME_: HrV2IndexIndexnameJobadsMatchingResume,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_MATCHING_RESUME_RESUME_ID_: HrV2IndexIndexnameJobadsMatchingResumeResumeId,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_MATCHING_RESUME_EVIDENCE_: HrV2IndexIndexnameJobadsMatchingResumeEvidence,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_MATCHING_RESUME_RESUME_ID_EVIDENCE_: HrV2IndexIndexnameJobadsMatchingResumeResumeIdEvidence,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_SEARCH_FULLTEXT_: HrV2IndexIndexnameJobadsSearchFullText,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLICATIONS_RESUMES_SEARCH_: HrV2IndexIndexnameJobadJobadIdApplicationsResumesSearch,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_APPLICATIONS_JOBADS_SEARCH_: HrV2IndexIndexnameResumeResumeIdApplicationsJobadsSearch,
        PathValues.HR_V2_RESUME_CAREER_OCCUPATION_RECOMMENDATION_: HrV2ResumeCareerOccupationRecommendation,
        PathValues.HR_V2_RESUME_CAREER_OCCUPATION_SKILLS_COMPARISON_: HrV2ResumeCareerOccupationSkillsComparison,
        PathValues.HR_V2_RESUME_CAREER_OCCUPATION_ACTIVITIES_COMPARISON_: HrV2ResumeCareerOccupationActivitiesComparison,
        PathValues.HR_V2_RESUME_CAREER_SIMULATOR_UPSKILLING_: HrV2ResumeCareerSimulatorUpskilling,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_IMPORT_AWS_: HrV2IndexIndexnameResumesImportAws,
        PathValues.HR_V2_INDEX_INDEXNAME_STATS_: HrV2IndexIndexnameStats,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_LATEST_: HrV2IndexIndexnameResumesLatest,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_CUSTOMIZE_: HrV2IndexIndexnameResumesCustomize,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUMES_MAPPING_: HrV2IndexIndexnameResumesMapping,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_DOCUMENT_: HrV2IndexIndexnameResumeResumeIdDocument,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_PIC_: HrV2IndexIndexnameResumeResumeIdPic,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_TEXT_: HrV2IndexIndexnameResumeResumeIdText,
        PathValues.HR_V2_INDEX_INDEXNAME_CACHE_: HrV2IndexIndexnameCache,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBADS_: HrV2IndexIndexnameJobads,
        PathValues.HR_V2_INDEX_INDEXNAME_JOBAD_JOBAD_ID_APPLICATIONS_RESUMES_: HrV2IndexIndexnameJobadJobadIdApplicationsResumes,
        PathValues.HR_V2_INDEX_INDEXNAME_RESUME_RESUME_ID_APPLICATIONS_JOBADS_: HrV2IndexIndexnameResumeResumeIdApplicationsJobads,
        PathValues.HR_V2_DATA_INDUSTRIES_: HrV2DataIndustries,
        PathValues.HR_V2_DATA_COMPANY_SIZE_: HrV2DataCompanySize,
        PathValues.HR_V2_DATA_COMPANY_TYPE_: HrV2DataCompanyType,
        PathValues.HR_V2_DATA_CONTRACT_TYPE_: HrV2DataContractType,
        PathValues.HR_V2_DATA_EMPLOYMENT_TYPE_: HrV2DataEmploymentType,
        PathValues.HR_V2_DATA_JOBSHIFT_TYPE_: HrV2DataJobshiftType,
        PathValues.HR_V2_DATA_SALARY_TYPE_: HrV2DataSalaryType,
        PathValues.HR_V2_DATA_SALARY_FREQUENCY_: HrV2DataSalaryFrequency,
        PathValues.HR_V2_DATA_SENIORITY_LEVEL_: HrV2DataSeniorityLevel,
        PathValues.HR_V2_DATA_PHONE_LABEL_: HrV2DataPhoneLabel,
        PathValues.HR_V2_DATA_LINK_LABEL_: HrV2DataLinkLabel,
        PathValues.HR_V2_DATA_EMAIL_LABEL_: HrV2DataEmailLabel,
        PathValues.HR_V2_DATA_MARITALSTATUS_: HrV2DataMaritalStatus,
        PathValues.HR_V2_DATA_NAME_PREFIX_: HrV2DataNamePrefix,
        PathValues.HR_V2_DATA_NAME_SUFFIX_: HrV2DataNameSuffix,
        PathValues.HR_V2_DATA_EDUCATION_TITLE_: HrV2DataEducationTitle,
        PathValues.HR_V2_DATA_EDUCATION_FIELDOFSTUDY_: HrV2DataEducationFieldOfStudy,
        PathValues.HR_V2_DATA_PATENT_STATUS_: HrV2DataPatentStatus,
        PathValues.HR_V2_DATA_GENDER_: HrV2DataGender,
        PathValues.HR_V2_DATA_PROTECTEDGROUP_: HrV2DataProtectedGroup,
        PathValues.HR_V2_DATA_DISABILITY_: HrV2DataDisability,
        PathValues.HR_V2_DATA_JOB_FUNCTION_: HrV2DataJobFunction,
        PathValues.HR_V2_DATA_EMPLOYMENT_REMOTEWORKING_: HrV2DataEmploymentRemoteWorking,
        PathValues.HR_V2_DATA_LICENSE_TYPE_: HrV2DataLicenseType,
        PathValues.HR_V2_DATA_LICENSE_TYPE_LICENSE_TYPE_CODE_: HrV2DataLicenseTypeLicenseTypeCode,
        PathValues.HR_V2_UNIVERSITY_NAME_SEARCH_AUTOCOMPLETE_: HrV2UniversityNameSearchAutocomplete,
        PathValues.HR_V2_UNIVERSITY_UNIVERSITY_ID_: HrV2UniversityUniversityId,
        PathValues.HR_V2_FEEDBACK_INDEX_INDEXNAME_RESUME_RESUME_ID_PARSE_DATA_: HrV2FeedbackIndexIndexnameResumeResumeIdParseData,
        PathValues.HR_V2_FEEDBACK_INDEX_INDEXNAME_RESUME_RESUME_ID_SEARCH_SEMANTIC_: HrV2FeedbackIndexIndexnameResumeResumeIdSearchSemantic,
        PathValues.HR_V2_: HrV2,
    }
)
