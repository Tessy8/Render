import pybullet_data
import pybullet as p
import time
import pyrosim.pyrosim as pyrosim
import numpy
import random
import constants as c

from world import WORLD
from robot import ROBOT


class SIMULATION:

	def __init__(self):
		self.physicsClient = p.connect(p.GUI)

		p.setAdditionalSearchPath(pybullet_data.getDataPath())

		p.setGravity(0,0,-9.8)

		#pyrosim.Prepare_To_Simulate(robotId)

		self.world = WORLD()
		self.robot = ROBOT()


	def Run(self):
		for i in range(c.rangeValue):
			p.stepSimulation()
			self.robot.Sense(i)
			self.robot.Think()
			self.robot.Act(i)
			time.sleep(1/20)
		

	def __del__(self):
		p.disconnect()
