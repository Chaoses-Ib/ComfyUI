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

from comfy.api.models.upload_image200_response import UploadImage200Response

class TestUploadImage200Response(unittest.TestCase):
    """UploadImage200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UploadImage200Response:
        """Test UploadImage200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UploadImage200Response`
        """
        model = UploadImage200Response()
        if include_optional:
            return UploadImage200Response(
                name = ''
            )
        else:
            return UploadImage200Response(
        )
        """

    def testUploadImage200Response(self):
        """Test UploadImage200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
