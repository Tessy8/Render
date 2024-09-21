import numpy
import pybullet as p
import pyrosim.pyrosim as pyrosim

rangeValue = 1000

class SENSOR:

	def __init__(self, link):
		self.linkName = link
		self.values = numpy.zeros(rangeValue)


	def Get_Value(self, t):
		self.values = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
		# print(self.values)

	def Save_Values(self):
		numpy.save('data/SensorValue.npy', numpy.array(self.values))

		