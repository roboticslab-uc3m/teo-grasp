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

env = Environment()
env.SetViewer('qtcoin')
env.Load('/usr/local/share/teo-grasp/contexts/models/lab.env.xml')
robot = env.GetRobots()[0]
robot.SetActiveManipulator('leftArm_trunk')
target = env.GetKinBody('bottle')
gmodel = databases.grasping.GraspingModel(robot, target)

if not gmodel.load():
    # gmodel.autogenerate()
    print 'generating grasping model (one time computation)'
    gmodel.init(friction=0.8, avoidlinks=[])
    gmodel.generate(approachrays=gmodel.computeBoxApproachRays(delta=0.08, normalanglerange=0,
                                                               directiondelta=0.40000000000000002))  # cuanto mas aumenta delta, menos rayos se generan para el grasp
    gmodel.save()
else:
    print("gmodel loaded...")

validgrasps, validindicees = gmodel.computeValidGrasps(checkgrasper=True, checkik=True)
print("validgrasps is ", len(validgrasps), "validindicees is ", len(validindicees))
basemanip = interfaces.BaseManipulation(robot)
with env:
    initialvalues = robot.GetDOFValues(gmodel.manip.GetArmIndices())

cont = 0
# while 1:
for validgrasp in validgrasps:  # random.permutation(validgrasps):
    print 'trying to grasp de object (attempt: %d)' % cont
    try:
        gmodel.showgrasp(validgrasp, collisionfree=False, delay=0.5)  # show the grasp
        # gmodel.moveToPreshape(validgrasp) # move to the preshape 
        print "moving robot arm to grasp"
        Tgrasp = gmodel.getGlobalGraspTransform(validgrasp, collisionfree=False)  # get the grasp transform
        traj = basemanip.MoveToHandPosition(matrices=[Tgrasp], outputtrajobj=True)  # move the robot to the grasp

        raveLogInfo('traj has %d waypoints' % traj.GetNumWaypoints())
        for waypoint in range(0, traj.GetNumWaypoints()):
            print("WayPoint: "+str(waypoint))
            data = traj.GetWaypoint(waypoint)
            for x in range(0,8): # it shows 0-7 joint values
                print('Joint number '+str(x)+' value: '+repr(data[x]*57.2958)) # 1 radians -> 57.2958 degrees
        # print("WayPoint "+str(waypoint)+": "+repr(data))

        robot.WaitForController(10)
        taskmanip = interfaces.TaskManipulation(robot)
        taskmanip.CloseFingers()
        robot.WaitForController(10)
        with env:
            robot.Grab(target)

        raw_input('press any key to release')

        taskmanip.ReleaseFingers(target=target)  # liberarDedos() -> abre la mano
        robot.WaitForController(10)
        print 'initial values'
        basemanip.MoveManipulator(initialvalues)
        robot.WaitForController(10)

    # break
    except planning_error, e:
        print 'try again: ', e
    cont += 1
