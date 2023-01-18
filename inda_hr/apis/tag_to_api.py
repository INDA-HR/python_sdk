import typing_extensions

from inda_hr.apis.tags import TagValues
from inda_hr.apis.tags.authentication_api import AuthenticationApi
from inda_hr.apis.tags.knowledge_extraction_api import KnowledgeExtractionApi
from inda_hr.apis.tags.resume_parsing_api import ResumeParsingApi
from inda_hr.apis.tags.job_ad_knowledge_extraction_api import JobAdKnowledgeExtractionApi
from inda_hr.apis.tags.skills_api import SkillsApi
from inda_hr.apis.tags.occupations_api import OccupationsApi
from inda_hr.apis.tags.esco_api import ESCOApi
from inda_hr.apis.tags.index_management_api import IndexManagementApi
from inda_hr.apis.tags.starting_with_indices_api import StartingWithIndicesApi
from inda_hr.apis.tags.credits_management_api import CreditsManagementApi
from inda_hr.apis.tags.customizations_api import CustomizationsApi
from inda_hr.apis.tags.failures_api import FailuresApi
from inda_hr.apis.tags.standardized_data_api import StandardizedDataApi
from inda_hr.apis.tags.universities_api import UniversitiesApi
from inda_hr.apis.tags.company_management_api import CompanyManagementApi
from inda_hr.apis.tags.resume_management_api import ResumeManagementApi
from inda_hr.apis.tags.job_ad_management_api import JobAdManagementApi
from inda_hr.apis.tags.application_management_api import ApplicationManagementApi
from inda_hr.apis.tags.search_api import SearchApi
from inda_hr.apis.tags.query_filters_api import QueryFiltersApi
from inda_hr.apis.tags.keywords_search_api import KeywordsSearchApi
from inda_hr.apis.tags.resume_search_api import ResumeSearchApi
from inda_hr.apis.tags.job_ad_search_api import JobAdSearchApi
from inda_hr.apis.tags.advanced_matching_api import AdvancedMatchingApi
from inda_hr.apis.tags.resume_to_resumes_api import ResumeToResumesApi
from inda_hr.apis.tags.job_ad_to_resumes_api import JobAdToResumesApi
from inda_hr.apis.tags.resume_to_job_ads_api import ResumeToJobAdsApi
from inda_hr.apis.tags.mapping_career_causeways_api import MappingCareerCausewaysApi
from inda_hr.apis.tags.utilities_api import UtilitiesApi
from inda_hr.apis.tags.feedback_api import FeedbackApi
from inda_hr.apis.tags.successful_execution_api import SuccessfulExecutionApi
from inda_hr.apis.tags.errors_api import ErrorsApi
from inda_hr.apis.tags.clear_cache_api import ClearCacheApi
from inda_hr.apis.tags.resume_import_api import ResumeImportApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.KNOWLEDGE_EXTRACTION: KnowledgeExtractionApi,
        TagValues.RESUME_PARSING: ResumeParsingApi,
        TagValues.JOB_AD_KNOWLEDGE_EXTRACTION: JobAdKnowledgeExtractionApi,
        TagValues.SKILLS: SkillsApi,
        TagValues.OCCUPATIONS: OccupationsApi,
        TagValues.ESCO: ESCOApi,
        TagValues.INDEX_MANAGEMENT: IndexManagementApi,
        TagValues.STARTING_WITH_INDICES: StartingWithIndicesApi,
        TagValues.CREDITS_MANAGEMENT: CreditsManagementApi,
        TagValues.CUSTOMIZATIONS: CustomizationsApi,
        TagValues.FAILURES: FailuresApi,
        TagValues.STANDARDIZED_DATA: StandardizedDataApi,
        TagValues.UNIVERSITIES: UniversitiesApi,
        TagValues.COMPANY_MANAGEMENT: CompanyManagementApi,
        TagValues.RESUME_MANAGEMENT: ResumeManagementApi,
        TagValues.JOB_AD_MANAGEMENT: JobAdManagementApi,
        TagValues.APPLICATION_MANAGEMENT: ApplicationManagementApi,
        TagValues.SEARCH: SearchApi,
        TagValues.QUERY_FILTERS: QueryFiltersApi,
        TagValues.KEYWORDS_SEARCH: KeywordsSearchApi,
        TagValues.RESUME_SEARCH: ResumeSearchApi,
        TagValues.JOB_AD_SEARCH: JobAdSearchApi,
        TagValues.ADVANCED_MATCHING: AdvancedMatchingApi,
        TagValues.RESUME_TO_RESUMES: ResumeToResumesApi,
        TagValues.JOB_AD_TO_RESUMES: JobAdToResumesApi,
        TagValues.RESUME_TO_JOB_ADS: ResumeToJobAdsApi,
        TagValues.MAPPING_CAREER_CAUSEWAYS: MappingCareerCausewaysApi,
        TagValues.UTILITIES: UtilitiesApi,
        TagValues.FEEDBACK: FeedbackApi,
        TagValues.SUCCESSFUL_EXECUTION: SuccessfulExecutionApi,
        TagValues.ERRORS: ErrorsApi,
        TagValues.CLEAR_CACHE: ClearCacheApi,
        TagValues.RESUME_IMPORT: ResumeImportApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.KNOWLEDGE_EXTRACTION: KnowledgeExtractionApi,
        TagValues.RESUME_PARSING: ResumeParsingApi,
        TagValues.JOB_AD_KNOWLEDGE_EXTRACTION: JobAdKnowledgeExtractionApi,
        TagValues.SKILLS: SkillsApi,
        TagValues.OCCUPATIONS: OccupationsApi,
        TagValues.ESCO: ESCOApi,
        TagValues.INDEX_MANAGEMENT: IndexManagementApi,
        TagValues.STARTING_WITH_INDICES: StartingWithIndicesApi,
        TagValues.CREDITS_MANAGEMENT: CreditsManagementApi,
        TagValues.CUSTOMIZATIONS: CustomizationsApi,
        TagValues.FAILURES: FailuresApi,
        TagValues.STANDARDIZED_DATA: StandardizedDataApi,
        TagValues.UNIVERSITIES: UniversitiesApi,
        TagValues.COMPANY_MANAGEMENT: CompanyManagementApi,
        TagValues.RESUME_MANAGEMENT: ResumeManagementApi,
        TagValues.JOB_AD_MANAGEMENT: JobAdManagementApi,
        TagValues.APPLICATION_MANAGEMENT: ApplicationManagementApi,
        TagValues.SEARCH: SearchApi,
        TagValues.QUERY_FILTERS: QueryFiltersApi,
        TagValues.KEYWORDS_SEARCH: KeywordsSearchApi,
        TagValues.RESUME_SEARCH: ResumeSearchApi,
        TagValues.JOB_AD_SEARCH: JobAdSearchApi,
        TagValues.ADVANCED_MATCHING: AdvancedMatchingApi,
        TagValues.RESUME_TO_RESUMES: ResumeToResumesApi,
        TagValues.JOB_AD_TO_RESUMES: JobAdToResumesApi,
        TagValues.RESUME_TO_JOB_ADS: ResumeToJobAdsApi,
        TagValues.MAPPING_CAREER_CAUSEWAYS: MappingCareerCausewaysApi,
        TagValues.UTILITIES: UtilitiesApi,
        TagValues.FEEDBACK: FeedbackApi,
        TagValues.SUCCESSFUL_EXECUTION: SuccessfulExecutionApi,
        TagValues.ERRORS: ErrorsApi,
        TagValues.CLEAR_CACHE: ClearCacheApi,
        TagValues.RESUME_IMPORT: ResumeImportApi,
    }
)
