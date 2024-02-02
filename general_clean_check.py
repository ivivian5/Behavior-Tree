#
# general cleaning condition implementation 
# for A1 Behavior trees assignment
#
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/27/2023

import bt_library as btl
from globals import GENERAL_CLEANING


class GeneralCleanCheck(btl.Condition):
    """
    Implementation of the condition "general cleaning".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking if doing general cleaning")

        if blackboard.get_in_environment(GENERAL_CLEANING, 0) == True:
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
