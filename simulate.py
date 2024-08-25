import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
# p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

rangeValue = 1000
amplitudeBackLeg = numpy.pi/4.0
frequencyBackLeg = 10
phaseOffsetBackLeg = numpy.pi
amplitudeFrontLeg = numpy.pi/4.0
frequencyFrontLeg = 50
phaseOffsetFrontLeg = 0
backLegSensorValue = numpy.zeros(rangeValue)
frontLegSensorValue = numpy.zeros(rangeValue)
# targetAngles = numpy.sin(numpy.linspace(0, 2.0*numpy.pi, rangeValue))
# targetAngles = ((-targetAngles + 1) / 2.0) * (numpy.pi / 2.0) - (numpy.pi / 4.0)
targetAnglesBackLeg = amplitudeBackLeg*numpy.sin(frequencyBackLeg*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetBackLeg)
targetAnglesFrontLeg = amplitudeFrontLeg*numpy.sin(frequencyFrontLeg*numpy.linspace(0, 2.0*numpy.pi, rangeValue) + phaseOffsetFrontLeg)
# numpy.save('data/targetAnglesBackLeg.npy', numpy.array(targetAnglesBackLeg))
# numpy.save('data/targetAnglesFrontLeg.npy', numpy.array(targetAnglesFrontLeg))
# exit()

for i in range(rangeValue):
    p.stepSimulation()
    # backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    backLegSensorValue[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValue[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    # pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_Backleg', controlMode=p.POSITION_CONTROL, targetPosition=random.uniform(-numpy.pi/2.0, numpy.pi/2.0), maxForce=50)
    # pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_Frontleg', controlMode=p.POSITION_CONTROL, targetPosition=random.uniform(-numpy.pi/2.0, numpy.pi/2.0), maxForce=50)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_Backleg', controlMode=p.POSITION_CONTROL, targetPosition=targetAnglesBackLeg[i], maxForce=50)
    pyrosim.Set_Motor_For_Joint(bodyIndex=robotId, jointName=b'Torso_Frontleg', controlMode=p.POSITION_CONTROL, targetPosition=targetAnglesFrontLeg[i], maxForce=50)
    # print(f"BackLegTouch: {backLegTouch}")
    time.sleep(1/50)
    # print(f"Iteration: {i}")

# print(backLegSensorValue)
# numpy.save('data/frontLegSensorValue.npy', numpy.array(frontLegSensorValue))
# numpy.save('data/backLegSensorValue.npy', numpy.array(backLegSensorValue))

p.disconnect()
