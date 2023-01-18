# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from inda_hr.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    AUTHENTICATION = "Authentication"
    KNOWLEDGE_EXTRACTION = "Knowledge Extraction"
    RESUME_PARSING = "Resume Parsing"
    JOB_AD_KNOWLEDGE_EXTRACTION = "JobAd Knowledge Extraction"
    SKILLS = "Skills"
    OCCUPATIONS = "Occupations"
    ESCO = "ESCO"
    INDEX_MANAGEMENT = "Index Management"
    STARTING_WITH_INDICES = "Starting with Indices"
    CREDITS_MANAGEMENT = "Credits Management"
    CUSTOMIZATIONS = "Customizations"
    FAILURES = "Failures"
    STANDARDIZED_DATA = "Standardized Data"
    UNIVERSITIES = "Universities"
    COMPANY_MANAGEMENT = "Company Management"
    RESUME_MANAGEMENT = "Resume Management"
    JOB_AD_MANAGEMENT = "JobAd Management"
    APPLICATION_MANAGEMENT = "Application Management"
    SEARCH = "Search"
    QUERY_FILTERS = "Query Filters"
    KEYWORDS_SEARCH = "Keywords Search"
    RESUME_SEARCH = "Resume Search"
    JOB_AD_SEARCH = "JobAd Search"
    ADVANCED_MATCHING = "Advanced Matching"
    RESUME_TO_RESUMES = "Resume to Resumes"
    JOB_AD_TO_RESUMES = "JobAd to Resumes"
    RESUME_TO_JOB_ADS = "Resume to JobAds"
    MAPPING_CAREER_CAUSEWAYS = "Mapping Career Causeways"
    UTILITIES = "Utilities"
    FEEDBACK = "Feedback"
    SUCCESSFUL_EXECUTION = "Successful Execution"
    ERRORS = "Errors"
    CLEAR_CACHE = "Clear Cache"
    RESUME_IMPORT = "Resume Import"
