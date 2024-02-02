#
# checking for dusty spot condition implementation 
# for A1 Behavior trees assignment
#
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/27/2023

import bt_library as btl
from globals import DUSTY_SPOT_SENSOR


class DustySpot(btl.Condition):
    """
    Implementation of the condition "sensor detcted dusty spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Checking if sensed dusty spot")

        if blackboard.get_in_environment(DUSTY_SPOT_SENSOR, 0) == True:
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
