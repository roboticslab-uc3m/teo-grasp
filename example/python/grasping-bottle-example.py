##
# @ingroup teo_grasp_examples_py
# \defgroup grasping-bottle-example grasping-bottle-example.py
#
# This is a first example of grasping with Teo using rightArm + trunk.
#
# <b>Legal</b> 
#
# Copyright: (C) 2017 Universidad Carlos III de Madrid
#
# Author: Raul de Santos Rico
#
# CopyPolicy: Released under the terms of the LGPLv2.1 or later, see license/LGPL.TXT

from openravepy import *
from numpy import *
import numpy, time
env=Environment()
env.SetViewer('qtcoin')
env.Load('/models/lab.env.xml')
robot = env.GetRobots()[0]
robot.SetActiveManipulator('rightArm_trunk')
target = env.GetKinBody('bottle')
gmodel = databases.grasping.GraspingModel(robot,target)

if not gmodel.load():
    gmodel.autogenerate()
    # print 'generating grasping model (one time computation)'
    # gmodel.init(friction=5,avoidlinks=[])
    # gmodel.generate(approachrays=gmodel.computeBoxApproachRays(delta=0.02))
    # gmodel.save()
else: print("gmodel loaded...")

validgrasps, validindicees = gmodel.computeValidGrasps(returnnum=50)
print("validgrasps is ",len(validgrasps), "validindicees is ", len(validindicees))
basemanip = interfaces.BaseManipulation(robot)
with env:
    initialvalues = robot.GetDOFValues(gmodel.manip.GetArmIndices())

cont = 0
# while 1:
for validgrasp in validgrasps: #random.permutation(validgrasps):
    print 'trying to grasp de object (attempt: %d)' %cont
    try:
        gmodel.moveToPreshape(validgrasp)
    	print "move robot arm to grasp"
    	Tgrasp = gmodel.getGlobalGraspTransform(validgrasp,collisionfree=False)	
    	traj = basemanip.MoveToHandPosition(matrices=[Tgrasp], outputtrajobj=True)	
    	robot.WaitForController(10)
	taskmanip = interfaces.TaskManipulation(robot)
	taskmanip.CloseFingers()
	robot.WaitForController(10)
	with env:
	    robot.Grab(target)	

	raveLogInfo('traj has %d waypoints, last waypoint is: %s'%(traj.GetNumWaypoints(),repr(traj.GetWaypoint(-1))))
        raw_input('press any key to release')
        taskmanip.ReleaseFingers(target=target)
        robot.WaitForController(10)
        print 'initial values'
        basemanip.MoveManipulator(initialvalues)
        robot.WaitForController(10)

	# break
    except planning_error,e:
 	print 'try again: ',e
    cont += 1
