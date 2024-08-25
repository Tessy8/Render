import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy

physicsClient = p.connect(p.GUI)

p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValue = numpy.zeros(1000)
frontLegSensorValue = numpy.zeros(1000)
#exit()

for i in range(1000):
    p.stepSimulation()
    # backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    backLegSensorValue[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Backleg")
    frontLegSensorValue[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("Frontleg")
    # print(f"BackLegTouch: {backLegTouch}")
    time.sleep(1/60)
    # print(f"Iteration: {i}")

# print(backLegSensorValue)
numpy.save('data/frontLegSensorValue.npy', numpy.array(frontLegSensorValue))
numpy.save('data/backLegSensorValue.npy', numpy.array(backLegSensorValue))

p.disconnect()
