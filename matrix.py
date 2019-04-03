from math import sqrt

class Matrix(object):
	@staticmethod 
	def check_arguments(num_of_arguments):
		dimension = sqrt(num_of_arguments)
		if dimension.is_integer():
			return int(dimension)
		else:
			raise ValueError("Wrong number of arguments")

	@staticmethod
	def check_dimension(left, right):
		if left.dimension != right.dimension:
			raise ValueError("Wrong dimensions")

	def __init__(self, *values_input):
		self.counter = 0
		self.dimension = Matrix.check_arguments(len(values_input))
		self.values = []
		for i in range(self.dimension):
			self.values.append([j for j in values_input[i*self.dimension:(i+1)*self.dimension]])

	def __add__(self, matrix_or_value):
		if isinstance(matrix_or_value, Matrix):
			newValues = []
			Matrix.check_dimension(self, matrix_or_value)
			for i in range(self.dimension):
				for j in range(self.dimension):
					newValues.append(self.values[i][j] + matrix_or_value.values[i][j])
			return Matrix(*newValues)
		elif isinstance(matrix_or_value, int) or isinstance(matrix_or_value, float):
			added_matrix = Matrix(*[matrix_or_value for i in range(self.dimension**2)])
			return self + added_matrix
		else:
			raise ValueError("Can't add this to matrix :(")

	def add(self, matrix_or_value):
		return self + matrix_or_value

	def  __radd__(self, matrix_or_value):
		return self + matrix_or_value

	def __iadd__(self, matrix_or_value):
		if isinstance(matrix_or_value, Matrix):
			newValues = []
			Matrix.check_dimension(self, matrix_or_value)
			for i in range(self.dimension):
				for j in range(self.dimension):
					self.values[i][j] += matrix_or_value.values[i][j]
			return self
		elif isinstance(matrix_or_value, int) or isinstance(matrix_or_value, float):
			for i in range(self.dimension):
				for j in range(self.dimension):
					self.values[i][j] += matrix_or_value
			return self
		else:
			raise ValueError("Can't add this to matrix :(")
	
	def __sub__(self, matrix_or_value):
		if isinstance(matrix_or_value, Matrix):
			newValues = []
			Matrix.check_dimension(self, matrix_or_value)
			for i in range(self.dimension):
				for j in range(self.dimension):
					newValues.append(self.values[i][j] - matrix_or_value.values[i][j])
			return Matrix(*newValues)
		elif isinstance(matrix_or_value, int) or isinstance(matrix_or_value, float):
			subed_matrix=Matrix(*[matrix_or_value for i in range(self.dimension**2)])
			return self - subed_matrix
		else:
			raise ValueError("Can't sub this to matrix :(")

	def __rsub__(self, matrix_or_value):
		if isinstance(matrix_or_value, Matrix):
			newValues = []
			Matrix.check_dimension(self, matrix_or_value)
			for i in range(self.dimension):
				for j in range(self.dimension):
					newValues.append(matrix_or_value.values[i][j] - self.values[i][j])
			return Matrix(*newValues)
		elif isinstance(matrix_or_value, int) or isinstance(matrix_or_value, float):
			subed_matrix=Matrix(*[matrix_or_value for i in range(self.dimension**2)])
			return subed_matrix - self
		else:
			raise ValueError("Can't sub this to matrix :(")

	def sub(self, matrix_or_value):
		return self - matrix_or_value

	def __matmul__(self, matrix_or_value):
		if isinstance(matrix_or_value, Matrix):
			newValues = []
			Matrix.check_dimension(self, matrix_or_value)
			for i in range(self.dimension):
				for j in range(self.dimension):
					help_value = 0.0
					for k in range(self.dimension):
						help_value += self.values[i][k] * matrix_or_value.values[k][j] 
					newValues.append(help_value)
			return Matrix(*newValues)
		else:
			raise ValueError("Can't mul this to matrix :(")

	def __str__(self):
		return str(self.values)

	def __iter__(self):
		return self

	def __next__(self):
		if self.counter >= self.dimension:
			self.counter = 0
			raise StopIteration()
		val = [i for i in self.values[self.counter]]
		self.counter += 1
		return val
