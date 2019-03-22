class Matrix(object):
	def __init__(self, *valuesInput):
		self.values=valuesInput
	def add(self, matrix):
		newValues = []
		for i in range(len(self.values)):
			newValues.append(self.values[i]+matrix.values[i])
		return Matrix(newValues)
	def __str__(self):
		return str(self.values)