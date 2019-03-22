#!/usr/bin/env python3
import Matrix as matrix


if __name__ == "__main__":
	matrix_1 = matrix.Matrix(4,5,6,7)
	print("matrix1 =",matrix_1)
	matrix_2 = matrix.Matrix(2,2,2,1)
	print("matrix2 =",matrix_2)
	matrix_3 = matrix_2.add(matrix_1)
	print("sum of matrix1 and matrix2 = ",matrix_3)