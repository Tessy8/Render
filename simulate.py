from simulation import SIMULATION
import constants as c

simulation = SIMULATION()
simulation.Run()



'''
import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c


for i in range(c.rangeValue):
    p.stepSimulation()
    c.backLegSensorValue[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    c.frontLegSensorValue[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_Backleg', controlMode=p.POSITION_CONTROL, targetPosition=c.targetAnglesBackLeg[i], maxForce=50)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_Frontleg', controlMode=p.POSITION_CONTROL, targetPosition=c.targetAnglesFrontLeg[i], maxForce=50)
    time.sleep(1/50)
    

p.disconnect()
'''