import os
from hillclimber import HILLCLIMBER


hc = HILLCLIMBER()
hc.Evolve()
hc.Show_Best()

'''
for i in (0,1,2,3,4):
	os.system("python generate.py")
	os.system("python simulate.py")
'''