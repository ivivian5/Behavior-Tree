#
# until fail Decorator node implementation for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/27/2023

import bt_library as btl


class UntilFail(btl.Decorator):

    def __init__(self, child: btl.TreeNode):
        """
        Default constructor.

        :param child: Child associated to the decorator
        """
        super().__init__(child)

    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
        
        # Evaluate the child
        self.print_message("Running following until fail")
        result_child = self.child.run(blackboard)

        # If the child failed, return that it is a success
        if result_child == btl.ResultEnum.FAILED:
            return self.report_succeeded(blackboard)

        # If the child didn't fail, then return running to 
        # evaluate the child again
        return self.report_running(blackboard, 0)
