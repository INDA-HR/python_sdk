# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.application_management_api import ApplicationManagementApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from inda_hr.api.application_management_api import ApplicationManagementApi
from inda_hr.api.authentication_api import AuthenticationApi
from inda_hr.api.clear_cache_api import ClearCacheApi
from inda_hr.api.company_management_api import CompanyManagementApi
from inda_hr.api.credits_management_api import CreditsManagementApi
from inda_hr.api.customizations_api import CustomizationsApi
from inda_hr.api.esco_api import ESCOApi
from inda_hr.api.failures_api import FailuresApi
from inda_hr.api.feedback_api import FeedbackApi
from inda_hr.api.job_ad_knowledge_extraction_api import JobAdKnowledgeExtractionApi
from inda_hr.api.job_ad_management_api import JobAdManagementApi
from inda_hr.api.job_ad_search_api import JobAdSearchApi
from inda_hr.api.job_ad_to_resumes_api import JobAdToResumesApi
from inda_hr.api.keywords_search_api import KeywordsSearchApi
from inda_hr.api.mapping_career_causeways_api import MappingCareerCausewaysApi
from inda_hr.api.occupations_api import OccupationsApi
from inda_hr.api.resume_import_api import ResumeImportApi
from inda_hr.api.resume_management_api import ResumeManagementApi
from inda_hr.api.resume_parsing_api import ResumeParsingApi
from inda_hr.api.resume_search_api import ResumeSearchApi
from inda_hr.api.resume_to_job_ads_api import ResumeToJobAdsApi
from inda_hr.api.resume_to_resumes_api import ResumeToResumesApi
from inda_hr.api.skills_api import SkillsApi
from inda_hr.api.standardized_data_api import StandardizedDataApi
from inda_hr.api.starting_with_indices_api import StartingWithIndicesApi
from inda_hr.api.universities_api import UniversitiesApi
from inda_hr.api.utilities_api import UtilitiesApi
