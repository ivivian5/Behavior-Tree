#
# Priority Composite node implementation for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/27/2023

from bt_library.blackboard import Blackboard
from bt_library.common import ResultEnum
from bt_library.composite import Composite, NodeListType


class Priority(Composite):
    """
    Specific implementation of the selection composite.
    """

    def __init__(self, children: NodeListType):
        """
        Default constructor.

        :param children: List of children nodes for this node
                         Assumes that the children are in order of 
                         priority where index 0 is highest priority
        """
        super().__init__(children)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.
        Children nodes are evaluated in order (by priority) and returns 
        failed if all child fail and running if child is running. 

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution (failed, running, or succeeded state)
        """
        # go to priority child
        child_position = 0

        # children evaluated in order by priority
        while child_position < len(self.children):
            child = self.children[child_position]

            result_child = child.run(blackboard)
            if result_child == ResultEnum.SUCCEEDED:
                return self.report_succeeded(blackboard)

            if result_child == ResultEnum.RUNNING:
                return self.report_running(blackboard)

            child_position = child_position + 1

        return self.report_failed(blackboard)
