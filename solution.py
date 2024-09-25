import os
import numpy
import pyrosim.pyrosim as pyrosim
import time

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

class SOLUTION:

	def __init__(self, nextAvailableID):
		self.weights = numpy.random.rand(3,2) * 2 - 1
		self.myID = nextAvailableID

	def Evaluate(self, mode):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("start /B python simulate.py " + mode + " " + str(self.myID))
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):
			time.sleep(0.01)
		f = open("fitness" + str(self.myID) + ".txt", "r")
		self.fitness = float(f.read())
		print(str(self.fitness))
		f.close()
		return self.fitness

	def Start_Simulation(self, mode):
		self.Create_World()
		self.Create_Body()
		self.Create_Brain()
		os.system("start /B python simulate.py " + mode + " " + str(self.myID))

	def Wait_For_Simulation_To_End(self):
		while not os.path.exists("fitness" + str(self.myID) + ".txt"):
			time.sleep(0.01)
		f = open("fitness" + str(self.myID) + ".txt", "r")
		self.fitness = float(f.read())
		f.close()
		os.system("rm fitness" + str(self.myID) + ".txt'")
		return self.fitness

	def Create_World(self):
		pyrosim.Start_SDF("world.sdf")
		pyrosim.Send_Cube(name="Box", pos=[x+5,y,z], size=[length,width,height])
		while not os.path.exists("world.sdf"):
			time.sleep(0.01)
		pyrosim.End()

	def Create_Body(self):
		pyrosim.Start_URDF("body.urdf")
		pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[length,width,height])
		pyrosim.Send_Joint(name="Torso_Backleg", parent="Torso", child="Backleg", type="revolute", position=[1,0,1])
		pyrosim.Send_Cube(name="Backleg", pos=[-0.5,0,-0.5], size=[length,width,height])
		pyrosim.Send_Joint(name="Torso_Frontleg", parent="Torso", child="Frontleg", type="revolute", position=[2,0,1])
		pyrosim.Send_Cube(name="Frontleg", pos=[0.5,0,-0.5], size=[length,width,height])
		while not os.path.exists("body.sdf"):
			time.sleep(0.01)
		pyrosim.End()

	'''
	def Get_Fitness(self):
		f = open("fitness" + str(self.myID) + ".txt", "r")
		self.fitness = float(f.read())
		print(str(self.fitness))
		f.close()
		return self.fitness
	'''

	def Create_Brain(self):
		pyrosim.Start_NeuralNetwork("brain " + str(self.myID) + ".nndf")
		pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
		pyrosim.Send_Sensor_Neuron(name=1, linkName="Backleg")
		pyrosim.Send_Sensor_Neuron(name=2, linkName="Frontleg")
		pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Backleg")
		pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Frontleg")
		for currentRow in (0, 1, 2):
			for currentColumn in (0, 1):
				pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+3, weight=self.weights[currentRow][currentColumn])
		while not os.path.exists("brain " + str(self.myID) + ".nndf"):
			time.sleep(0.01)
		pyrosim.End()

	def Mutate(self):
		randomRow = numpy.random.randint(0, 2)
		randomColumn = numpy.random.randint(0, 1)
		self.weights[randomRow][randomColumn] = numpy.random.random() * 2 - 1

	def Set_ID(self, childID):
		self.myID = childID	