import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5


def Create_World():
	pyrosim.Start_SDF("world.sdf")
	pyrosim.Send_Cube(name="Box", pos=[x+5,y,z], size=[length,width,height])
	pyrosim.End()

'''
def Create_Robot():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Link0_Link1", parent="Link0", child="Link1", type="revolute", position=[0,0,1])
	pyrosim.Send_Cube(name="Link1", pos=[0,0,0.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Link1_Link2", parent="Link1", child="Link2", type="revolute", position=[0,0,1])
	pyrosim.Send_Cube(name="Link2", pos=[0,0,0.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Link2_Link3", parent="Link2", child="Link3", type="revolute", position=[0,0.5,0.5])
	pyrosim.Send_Cube(name="Link3", pos=[0,0.5,0], size=[length,width,height])
	pyrosim.Send_Joint(name="Link3_Link4", parent="Link3", child="Link4", type="revolute", position=[0,1,0])
	pyrosim.Send_Cube(name="Link4", pos=[0,0.5,0], size=[length,width,height])
	pyrosim.Send_Joint(name="Link4_Link5", parent="Link4", child="Link5", type="revolute", position=[0,0.5,-0.5])
	pyrosim.Send_Cube(name="Link5", pos=[0,0,-0.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Link5_Link6", parent="Link5", child="Link6", type="revolute", position=[0,0,-1])
	pyrosim.Send_Cube(name="Link6", pos=[0,0,-0.5], size=[length,width,height])
	pyrosim.End()
'''

'''
def Create_Robot2():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Torso_Backleg", parent="Torso", child="Backleg", type="revolute", position=[1,0,1])
	pyrosim.Send_Cube(name="Backleg", pos=[-0.5,0,-0.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Torso_Frontleg", parent="Torso", child="Frontleg", type="revolute", position=[2,0,1])
	pyrosim.Send_Cube(name="Frontleg", pos=[0.5,0,-0.5], size=[length,width,height])
	pyrosim.End()
'''

def Generate_Body():
	pyrosim.Start_URDF("body.urdf")
	pyrosim.Send_Cube(name="Torso", pos=[1.5,0,1.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Torso_Backleg", parent="Torso", child="Backleg", type="revolute", position=[1,0,1])
	pyrosim.Send_Cube(name="Backleg", pos=[-0.5,0,-0.5], size=[length,width,height])
	pyrosim.Send_Joint(name="Torso_Frontleg", parent="Torso", child="Frontleg", type="revolute", position=[2,0,1])
	pyrosim.Send_Cube(name="Frontleg", pos=[0.5,0,-0.5], size=[length,width,height])
	pyrosim.End()


def Generate_Brain():
	pyrosim.Start_NeuralNetwork("brain.nndf")
	pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
	pyrosim.Send_Sensor_Neuron(name=1, linkName="Backleg")
	pyrosim.Send_Sensor_Neuron(name=2, linkName="Frontleg")
	pyrosim.Send_Motor_Neuron(name=3, jointName="Torso_Backleg")
	pyrosim.Send_Motor_Neuron(name=4, jointName="Torso_Frontleg")
	pyrosim.End()

Create_World()
Generate_Body()
Generate_Brain()

'''
# for k in range(5):
# 	for j in range(5):
# 		for i in range(10):
#			length = 0.9*length
#			width = 0.9*width
#			height = 0.9*height
#			pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
#			z = z + height
#		z = 0.4
#		length = 1
#		width = 1
#		height = 1
#		x = x + length + 0.5
#	x = 0
#	y = y + width + 0.5
'''