from math import sqrt

class Matrix(object):
	@staticmethod 
	def check_dimension(num_of_arguments):
		dimension = sqrt(num_of_arguments)
		print(dimension)
		print("dim")
		if dimension.is_integer():
			return int(dimension)
		else:
			raise ValueError ("Wrong number of arguments")

	def __init__(self, *values_input):
		self.dimension = Matrix.check_dimension(len(values_input))
		self.values = []
		for i in range(self.dimension):
			self.values.append([j for j in values_input[i*self.dimension:(i+1)*self.dimension]])

	def add(self, matrix):
		newValues = []
		for i in range(self.dimension):
			for j in range(self.dimension):
				newValues.append(self.values[i][j]+matrix.values[i][j])
		print(newValues)
		return Matrix(*newValues)

	def __str__(self):
		return str(self.values)