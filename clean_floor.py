#
# clean floor task implementation for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/28/2023

import bt_library as btl


class CleanFloor(btl.Task):
    """
    Implementation of the Task "cleaning floor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Cleaning Floor")
        
        # if the clean key has the True value then no need to clean more
        if blackboard.get_in_environment("ALL_CLEAN", True):
            return self.report_failed(blackboard)
        else:
            return self.report_succeeded(blackboard)
