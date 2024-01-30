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

from comfy.api.models.queue_tuple_inner import QueueTupleInner

class TestQueueTupleInner(unittest.TestCase):
    """QueueTupleInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QueueTupleInner:
        """Test QueueTupleInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QueueTupleInner`
        """
        model = QueueTupleInner()
        if include_optional:
            return QueueTupleInner(
                extra_pnginfo = comfy.api.models.extra_data_extra_pnginfo.ExtraData_extra_pnginfo(
                    workflow = comfy.api.models.workflow.Workflow(
                        last_node_id = 56, 
                        last_link_id = 56, 
                        nodes = [
                            comfy.api.models.workflow_nodes_inner.Workflow_nodes_inner(
                                id = 56, 
                                type = '', 
                                pos = [
                                    1.337
                                    ], 
                                size = comfy.api.models.workflow_nodes_inner_size.Workflow_nodes_inner_size(
                                    0 = 1.337, 
                                    1 = 1.337, ), 
                                flags = {
                                    'key' : None
                                    }, 
                                order = 56, 
                                mode = 56, 
                                inputs = [
                                    comfy.api.models.workflow_nodes_inner_inputs_inner.Workflow_nodes_inner_inputs_inner(
                                        name = '', 
                                        type = '', 
                                        link = 56, )
                                    ], 
                                outputs = [
                                    comfy.api.models.workflow_nodes_inner_outputs_inner.Workflow_nodes_inner_outputs_inner(
                                        name = '', 
                                        type = '', 
                                        links = [
                                            56
                                            ], 
                                        slot_index = 56, )
                                    ], 
                                properties = comfy.api.models.properties.properties(), 
                                widgets_values = [
                                    ''
                                    ], )
                            ], 
                        links = [
                            [
                                null
                                ]
                            ], 
                        groups = [
                            None
                            ], 
                        config = comfy.api.models.config.config(), 
                        extra = comfy.api.models.extra.extra(), 
                        version = 1.337, ), )
            )
        else:
            return QueueTupleInner(
        )
        """

    def testQueueTupleInner(self):
        """Test QueueTupleInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
