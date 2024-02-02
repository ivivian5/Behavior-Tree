#
# done spot task implementation for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Author - Vivian Lau vlau02
# Last Modified - 09/28/2023

import bt_library as btl
from globals import SPOT_CLEANING


class DoneSpot(btl.Task):
    """
    Implementation of the Task "Done Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message("Spot Done")

        blackboard.set_in_environment(SPOT_CLEANING, False)
        
        return self.report_succeeded(blackboard)
