#
# Sequence Composite node implementation for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/27/2023

from bt_library.blackboard import Blackboard
from bt_library.common import ResultEnum
from bt_library.composite import Composite, NodeListType


class Sequence(Composite):
    """
    Specific implementation of the selection composite.
    """

    def __init__(self, children: NodeListType):
        """
        Default constructor.

        :param children: List of children for this node
        """
        super().__init__(children)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.
        Children nodes are evaluated in order (from left to right) and returns 
        failed as soon as one child fails and running if child is running. 
        Otherwise, succeeded.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution (failed, running, or succeeded state)
        """
        child_position = self.additional_information(blackboard, 0)

        # children evaluated in order from left to right
        while child_position < len(self.children): 
            child = self.children[child_position]

            result_child = child.run(blackboard)
            
            if result_child == ResultEnum.FAILED:
                return self.report_failed(blackboard, 0)
            elif result_child == ResultEnum.RUNNING:
                return self.report_running(blackboard, child_position)

            child_position = child_position + 1

        return self.report_succeeded(blackboard, 0)
