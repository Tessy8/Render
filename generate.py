import pyrosim.pyrosim as pyrosim

length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.4

pyrosim.Start_SDF("boxes.sdf")
for k in range(5):
	for j in range(5):
		for i in range(10):
			length = 0.9*length
			width = 0.9*width
			height = 0.9*height
			pyrosim.Send_Cube(name="Box", pos=[x,y,z], size=[length,width,height])
			z = z + height
		z = 0.4
		length = 1
		width = 1
		height = 1
		x = x + length + 0.5
	x = 0
	y = y + width + 0.5
pyrosim.End()
