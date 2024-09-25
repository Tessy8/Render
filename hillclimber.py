from solution import SOLUTION
import constants as c
import copy

class HILLCLIMBER:

	def __init__(self):
		self.parent = SOLUTION()

	def Evolve(self):
		self.parent.Evaluate("DIRECT")
		self.parent.fitness = self.parent.Get_Fitness()
		for currentGeneration in range(c.numberOfGenerations):
			self.Evolve_For_One_Generation()		

	def Evolve_For_One_Generation(self):
		self.Spawn()
		self.Mutate()
		self.child.Evaluate("DIRECT")
		self.child.fitness = self.child.Get_Fitness()
		self.Print()
		self.Select()

	def Spawn(self):
		self.child = copy.deepcopy(self.parent)

	def Mutate(self):
		self.child.Mutate()

	def Select(self):
		if self.parent.fitness > self.child.fitness:
			self.parent = self.child

	def Print(self):
		print("Parent: " + str(self.parent.fitness) + "; Child: " + str(self.child.fitness))

	def Show_Best(self):
		self.parent.Evaluate("GUI")