#
# main for running the A1 Behavior trees assignment.
# CS 131 - Artificial Intelligence
#
# Edited by - Vivian Lau vlau02
# Last modified - 09/27/2023

import random

import bt_library as btl
from behavior_tree import tree_root

from globals import BATTERY_LEVEL, GENERAL_CLEANING, SPOT_CLEANING, DUSTY_SPOT_SENSOR, HOME_PATH

# Main body of the assignment
curBB = btl.Blackboard() # current version of blackboard
curBB.set_in_environment(BATTERY_LEVEL, 29)
curBB.set_in_environment(SPOT_CLEANING, False)
curBB.set_in_environment(GENERAL_CLEANING, False)
curBB.set_in_environment(DUSTY_SPOT_SENSOR, False)
curBB.set_in_environment(HOME_PATH, "")
curBB.set_in_environment("ALL_CLEAN", False)

done = False
percentClean = 0
totalTime = 0

# ask user to provide battery level
batteryLevelIn = int(input('Enter an integer representing the battery level: '))
print()
while batteryLevelIn > 100 or batteryLevelIn < 0:
    batteryLevelIn = int(input('Invalid battery level input, please try again: '))
    print()
curBB.set_in_environment(BATTERY_LEVEL, batteryLevelIn)

# ask user if want to request spot clean
spotCleanIn = input('Enter \'Y\' if want to request a spot clean (or any other key, if not): ')
print()
if spotCleanIn == 'Y':
    curBB.set_in_environment(SPOT_CLEANING, True)
    curBB.set_in_environment("ALL_CLEAN", False)

# ask user if want to request general cleaning
generalCleanIn = input('Enter \'Y\' if want to request '+
                       'a general clean (or any other key, if not): ')
print()
if generalCleanIn == 'Y':
    curBB.set_in_environment(GENERAL_CLEANING, True)
    curBB.set_in_environment("ALL_CLEAN", False)

while not done:
    # Each cycle in this while-loop is equivalent to 1 second time
    
    # if anything is running, don't change environment
    if not(curBB.get_in_states(23) == {'result': btl.ResultEnum.RUNNING, \
                                      'additional_information': None}):
        # simulate change in dusty spot sensor
        if random.randint(1,5) == 1:
            curBB.set_in_environment(DUSTY_SPOT_SENSOR, True)
            curBB.set_in_environment("ALL_CLEAN", False)
        else:
            curBB.set_in_environment(DUSTY_SPOT_SENSOR, False)
    
    # formatting
    print("----------------------------------------------------------------")
    
    # print total time
    print ("Total Time: ", totalTime)
    
    # formatting
    print("................................................................")
    
    # evaluate the tree
    result = tree_root.run(curBB)
    totalTime += 1 # increment timer
    
    # formatting
    print("................................................................")
    
    # simulate change in battery level
    # if docked (is running), then increase battery, otherwise decrease battery
    if curBB.get_in_states(3) == \
            {'result': btl.ResultEnum.RUNNING, 'additional_information': None}:
        curBB.set_in_environment(BATTERY_LEVEL, curBB.get_in_environment(BATTERY_LEVEL, 0) + 20)
    else:
        curBB.set_in_environment(BATTERY_LEVEL, curBB.get_in_environment(BATTERY_LEVEL, 0) - 2)
    
    # simulate change for floor cleaning
    # if cleaning floor action is running
    if curBB.get_in_states(16) == {'result': btl.ResultEnum.RUNNING, \
                                      'additional_information': None}:
        # increase percentage of floor that is clean
        percentClean += random.randint(8,15)
        
        # check if floor is all clean
        if percentClean >= 100:
            curBB.set_in_environment("ALL_CLEAN", True)
    
    # print battery level
    print("Battery Level After Evaluation:  ", curBB.get_in_environment(BATTERY_LEVEL, 0), "% \n")
    
    # if nothing was requested and robot is not in the middle of running tasks, then shut down
    if (curBB.get_in_environment(SPOT_CLEANING, None) == False and \
        curBB.get_in_environment(GENERAL_CLEANING, None) == False and \
        curBB.get_in_states(23) != {'result': btl.ResultEnum.RUNNING, \
                                    'additional_information': None}):
        done = True
        print("----------------------------------------------------------------")
        print ("No more requests detected.\n",
               "Thank you for using VIVIAN'S vacuum cleaning robot.")
    '''
    # check if user wants to exit
    doneIn = input('Enter \"exit\" to terminate the robot, otherwise enter any key: ')
    print()
    if doneIn == "exit":
        done = True
    '''