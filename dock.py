#
# dock task implementation for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/28/2023

import bt_library as btl
from globals import BATTERY_LEVEL


class Dock(btl.Task):
    """
    Implementation of the Task "docking".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Docking")
        
        if blackboard.get_in_environment(BATTERY_LEVEL, 0) > 70:
            return self.report_succeeded(blackboard)
        else:
            return self.report_running(blackboard)
