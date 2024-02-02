#
# go home task implementation for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/28/2023

import bt_library as btl
from globals import HOME_PATH, BATTERY_LEVEL


class GoHome(btl.Task):
    """
    Implementation of the Task "Go Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Going home")

        # if there is a path and enough battery, go home
        if blackboard.get_in_environment(HOME_PATH, "UNDEFINED") != "UNDEFINED":
            return self.report_succeeded(blackboard)
        else:
            return self.report_failed(blackboard)
