import os
from parallelHillClimber import PARALLEL_HILLCLIMBER


phc = PARALLEL_HILLCLIMBER()
phc.Evolve()
phc.Show_Best()

'''
for i in (0,1,2,3,4):
	os.system("python generate.py")
	os.system("python simulate.py")
'''