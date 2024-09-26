from motor import MOTOR
from sensor import SENSOR
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import os
import constants as c

class ROBOT:

	def __init__(self, solutionID):

		self.robotID = p.loadURDF("body.urdf")
		self.solutionID = solutionID
		self.sensors = {}
		self.motors = {}
		pyrosim.Prepare_To_Simulate(self.robotID)
		self.Prepare_To_Sense()
		self.Prepare_To_Act()
		self.nn = NEURAL_NETWORK("brain " + str(solutionID) + ".nndf")
		os.system("rm 'brain " + str(solutionID) + ".nndf'")

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
		for neuronName in self.nn.Get_Neuron_Names():
			if self.nn.Is_Motor_Neuron(neuronName):
				jointName = self.nn.Get_Motor_Neurons_Joint(neuronName)
				desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
				self.motors[jointName.encode('utf-8')].Set_Value(self.robotID, desiredAngle)
				# print(neuronName + " " + jointName + " " + str(desiredAngle))

	def Get_Fitness(self):
		stateOfLinkZero = p.getLinkState(self.robotID, 0)
		positionOfLinkZero = stateOfLinkZero[0]
		xCoordinateOfLinkZero = positionOfLinkZero[0]
		f = open("tmp" + str(self.solutionID) + ".txt", "w")
		f.write(str(xCoordinateOfLinkZero))
		f.close()	
		os.system("mv tmp" + str(self.solutionID) + ".txt" + " " + "fitness" + str(self.solutionID) + ".txt")

	def Think(self):
		self.nn.Update()
		# self.nn.Print()


    
