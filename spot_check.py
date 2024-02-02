#
# spot checkin condition implementation 
# for A1 Behavior trees assignment
#
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/27/2023

import bt_library as btl
from globals import SPOT_CLEANING


class Spot(btl.Condition):
    """
    Implementation of the condition "spot checking".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking if requested cleaning spot")

        if blackboard.get_in_environment(SPOT_CLEANING, 0) == True:
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
