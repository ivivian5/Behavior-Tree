#
# Behavior Tree framework for A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# version 1.0.4 - copyright (c) 2023 Santini Fabrizio. All rights reserved.
# 
# Edited by - Vivian Lau vlau02
# Last modified - 09/28/2023

import bt_library as btl

from battery_less_than_30 import BatteryLessThan30
from dusty_spot import DustySpot
from general_clean_check import GeneralCleanCheck
from spot_check import Spot

from find_home import FindHome
from go_home import GoHome
from dock import Dock
from clean_spot import CleanSpot
from done_spot import DoneSpot
from clean_floor import CleanFloor
from done_general import DoneGeneral
from do_nothing import DoNothing

from globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH

from until_fail import UntilFail

from sequence import Sequence
from priority import Priority

###################################################################################################

#checks if battery is <30 and goes to charge if so
batterySeq = Sequence(
    [
        BatteryLessThan30(),
        FindHome(),
        GoHome(),
        Dock()
    ]
)

#checks if spot cleaning has been requested and do so if so
spotSeq = Sequence(
    [
        Spot(),
        btl.Timer(20, CleanSpot()),
        DoneSpot()
    ]
)

#checks if there is a dusty spot sensed from sensor and clean if so
dustySeq = Sequence(
    [
        DustySpot(),
        btl.Timer(35, CleanSpot())
    ]
)

#performs general cleaning if requested to do so
genCleanSeq = Sequence(
    [
        GeneralCleanCheck(),
        Sequence(
            [
                Priority(
                    [
                        dustySeq,
                        UntilFail(CleanFloor())
                    ]
                ),
                DoneGeneral()
            ]
        )
    ]
)

#whole tree
tree_root = Priority(
    [
        batterySeq,
        btl.Selection(
            [
                spotSeq,
                genCleanSeq
            ]
        ),
        DoNothing()
    ]
)
