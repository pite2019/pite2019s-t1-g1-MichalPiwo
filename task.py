#!/usr/bin/env python3
import matrix as matrix


if __name__ == "__main__":
	matrix_1 = matrix.Matrix(1, 1, 1, 1)
	print("matrix1 =", matrix_1)

	matrix_2 = matrix.Matrix(2, 2, 2, 2)
	print("matrix2 =", matrix_2)

	matrix_3 = matrix_2.add(matrix_1)
	print("sum of matrix1 and matrix2 = ", matrix_3)
	
	matrix_3 = matrix_2 + matrix_1
	print("sum of matrix1 and matrix2 = ", matrix_3)

	matrix_3 =  2 + matrix_1
	print("sum of matrix1 and 2 = ", matrix_3)

	matrix_3 =  matrix_1 + 2
	print("sum of 2 and matrix1 = ", matrix_3)

	matrix_3 = matrix_2.sub(matrix_1)
	print("sub matrix2 and matrix1 = ", matrix_3)

	matrix_3 = matrix_1.sub(matrix_2)
	print("sub matrix1 and matrix2 = ", matrix_3)

	matrix_3 = matrix_2 - matrix_1
	print("sub matrix2 and matrix1 = ", matrix_3)

	matrix_3 = matrix_1 - matrix_2
	print("sub matrix1 and matrix2 = ", matrix_3)

	matrix_3 = matrix_1 - 1
	print("sub matrix1 and 1 = ", matrix_3)

	matrix_1 += matrix_2
	print("matrix1+=matrix2 =", matrix_1)

	matrix_1 += -2
	print("matrix1+ = -2 =", matrix_1)

	matrix_3 = matrix_1 @ matrix_2
	print("matrix1 multiplid by matrix2 =", matrix_3)

	print("matrix1:")
	for i in matrix_1:
		print(i)

	print("matrix1:")
	for i in matrix_1:
		print(i)