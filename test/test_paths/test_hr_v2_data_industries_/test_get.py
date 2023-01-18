# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import inda_hr
from inda_hr.paths.hr_v2_data_industries_ import get  # noqa: E501
from inda_hr import configuration, schemas, api_client

from .. import ApiTestMixin


class TestHrV2DataIndustries(ApiTestMixin, unittest.TestCase):
    """
    HrV2DataIndustries unit test stubs
        Get Industries  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
