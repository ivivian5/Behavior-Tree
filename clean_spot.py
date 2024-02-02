#
# clean spot task implementation for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/28/2023

import bt_library as btl


class CleanSpot(btl.Task):
    """
    Implementation of the Task "cleaning spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Cleaning Spot")
        
        return self.report_succeeded(blackboard)
