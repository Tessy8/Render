from motor import MOTOR
from sensor import SENSOR
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim

class ROBOT:

	def __init__(self):

		self.robotID = p.loadURDF("body.urdf")
		self.sensors = {}
		self.motors = {}
		pyrosim.Prepare_To_Simulate(self.robotID)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		

	def Prepare_To_Sense(self):
		for linkName in pyrosim.linkNamesToIndices:
			self.sensors[linkName] = SENSOR(linkName)


	def Sense(self, t):
		for sensor in self.sensors.values():
			sensor.Get_Value(t)

	def Prepare_To_Act(self):
		for jointName in pyrosim.jointNamesToIndices:
			self.motors[jointName] = MOTOR(jointName)

	def Act(self, i):
		for motor in self.motors.values():
			motor.Set_Value(self.robotID, i)



    
