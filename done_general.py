#
# done general task implementation for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/28/2023

import bt_library as btl
from globals import GENERAL_CLEANING


class DoneGeneral(btl.Task):
    """
    Implementation of the Task "general done".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("General Done")

        blackboard.set_in_environment(GENERAL_CLEANING, False)
        
        return self.report_succeeded(blackboard)
