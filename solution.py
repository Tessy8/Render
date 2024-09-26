import os
import numpy
import pyrosim.pyrosim as pyrosim
import time
import constants as c

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

class SOLUTION:

	def __init__(self, nextAvailableID):
		self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons) * 2 - 1
		self.myID = nextAvailableID

	'''
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
	'''

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
		pyrosim.Send_Cube(name="Torso", pos=[0,0,1], size=[length,width,height])
		pyrosim.Send_Joint(name="Torso_Backleg", parent="Torso", child="Backleg", type="revolute", position=[0,-0.5,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="Backleg", pos=[0,-0.5,0], size=[length-0.8,width,height-0.8])
		pyrosim.Send_Joint(name="Torso_Frontleg", parent="Torso", child="Frontleg", type="revolute", position=[0,0.5,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="Frontleg", pos=[0,0.5,0], size=[length-0.8,width,height-0.8])
		pyrosim.Send_Joint(name="Backleg_Backarm", parent="Backleg", child="Backarm", type="revolute", position=[0,-1,0], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="Backarm", pos=[0,0,-0.5], size=[length-0.8,width-0.8,height])
		pyrosim.Send_Joint(name="Frontleg_Frontarm", parent="Frontleg", child="Frontarm", type="revolute", position=[0,1,0], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="Frontarm", pos=[0,0,-0.5], size=[length-0.8,width-0.8,height])
		pyrosim.Send_Joint(name="Torso_Leftleg", parent="Torso", child="Leftleg", type="revolute", position=[-0.5,0,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="Leftleg", pos=[-0.5,0,0], size=[length,width-0.8,height-0.8])
		pyrosim.Send_Joint(name="Torso_Rightleg", parent="Torso", child="Rightleg", type="revolute", position=[0.5,0,1], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="Rightleg", pos=[0.5,0,0], size=[length,width-0.8,height-0.8])
		pyrosim.Send_Joint(name="Leftleg_Leftarm", parent="Leftleg", child="Leftarm", type="revolute", position=[-1,0,0], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="Leftarm", pos=[0,0,-0.5], size=[length-0.8,width-0.8,height])
		pyrosim.Send_Joint(name="Rightleg_Rightarm", parent="Rightleg", child="Rightarm", type="revolute", position=[1,0,0], jointAxis = "1 0 0")
		pyrosim.Send_Cube(name="Rightarm", pos=[0,0,-0.5], size=[length-0.8,width-0.8,height])
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
		pyrosim.Send_Sensor_Neuron(name=3, linkName="Leftleg")		
		pyrosim.Send_Sensor_Neuron(name=4, linkName="Rightleg")
		pyrosim.Send_Sensor_Neuron(name=5, linkName="Backarm")
		pyrosim.Send_Sensor_Neuron(name=6, linkName="Frontarm")
		pyrosim.Send_Sensor_Neuron(name=7, linkName="Leftarm")		
		pyrosim.Send_Sensor_Neuron(name=8, linkName="Rightarm")
		pyrosim.Send_Motor_Neuron(name=9, jointName="Torso_Backleg")
		pyrosim.Send_Motor_Neuron(name=10, jointName="Torso_Frontleg")
		pyrosim.Send_Motor_Neuron(name=11, jointName="Torso_Leftleg")
		pyrosim.Send_Motor_Neuron(name=12, jointName="Torso_Rightleg")
		pyrosim.Send_Motor_Neuron(name=13, jointName="Backleg_Backarm")
		pyrosim.Send_Motor_Neuron(name=14, jointName="Frontleg_Frontarm")
		pyrosim.Send_Motor_Neuron(name=15, jointName="Leftleg_Leftarm")
		pyrosim.Send_Motor_Neuron(name=16, jointName="Rightleg_Rightarm")
		for currentRow in range(c.numSensorNeurons):
			for currentColumn in range(c.numMotorNeurons):
				pyrosim.Send_Synapse(sourceNeuronName=currentRow, targetNeuronName=currentColumn+9, weight=self.weights[currentRow][currentColumn])
		while not os.path.exists("brain " + str(self.myID) + ".nndf"):
			time.sleep(0.01)
		pyrosim.End()

	def Mutate(self):
		randomRow = numpy.random.randint(0, c.numSensorNeurons-1)
		randomColumn = numpy.random.randint(0, c.numMotorNeurons-1)
		self.weights[randomRow][randomColumn] = numpy.random.random() * 2 - 1

	def Set_ID(self, childID):
		self.myID = childID	