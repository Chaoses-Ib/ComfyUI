# coding: utf-8

"""
    comfyui

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from comfy.api.models.get_queue200_response import GetQueue200Response

class TestGetQueue200Response(unittest.TestCase):
    """GetQueue200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetQueue200Response:
        """Test GetQueue200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetQueue200Response`
        """
        model = GetQueue200Response()
        if include_optional:
            return GetQueue200Response(
                queue_running = [
                    [
                        null
                        ]
                    ],
                queue_pending = [
                    [
                        null
                        ]
                    ]
            )
        else:
            return GetQueue200Response(
        )
        """

    def testGetQueue200Response(self):
        """Test GetQueue200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
