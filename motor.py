import pybullet as p
import constants as c
import numpy
import pyrosim.pyrosim as pyrosim

class MOTOR:

	def __init__(self, joint):
		self.jointName = joint
		# self.Prepare_To_Act()

	'''
	def Prepare_To_Act(self):
		self.amplitude = c.amplitudeBackLeg
		self.frequency = c.frequencyBackLeg
		self.offset = c.phaseOffsetBackLeg
		if self.jointName == b'Torso_Backleg':
			self.motorValues = self.amplitude*numpy.sin(self.frequency*numpy.linspace(0, 2.0*numpy.pi, c.rangeValue) + self.offset)
		elif self.jointName == b'Torso_Frontleg':
			self.motorValues = self.amplitude*numpy.sin(self.frequency/2.0*numpy.linspace(0, 2.0*numpy.pi, c.rangeValue) + self.offset)	
	'''
		
	def Set_Value(self, robot, desiredAngle):
	 	pyrosim.Set_Motor_For_Joint(bodyIndex=robot, jointName=self.jointName, controlMode=p.POSITION_CONTROL, targetPosition=desiredAngle, maxForce=50)
	    	
	'''
	def Save_Values(self):
		numpy.save('data/MotorValue.npy', numpy.array(self.motorValues))
	'''