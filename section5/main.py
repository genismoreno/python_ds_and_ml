import numpy as np

zeros = np.zeros(10)
print(zeros)

ones = np.ones(10)
print(ones)

fives = np.ones(10) * 5
print(fives)

from_10_to_50 = np.arange(10, 51)
print(from_10_to_50)

from_0_to_8 = np.arange(0, 9).reshape(3, 3)
print(from_0_to_8)

identity_matrix = np.eye(3)
print(identity_matrix)

random = np.random.random(1)
print(random)

normal_dist = np.random.normal(size=25)
print(normal_dist)

matrix = np.arange(0.01, 1.01, step=0.01).reshape(10, 10)
print(matrix)

linear_space_points = np.linspace(0, 1, num=20)
print(linear_space_points)

mat = np.arange(1, 26).reshape(5, 5)
print(mat)

mat2 = mat[2:, 1:]
print(mat2)

mat3 = mat[3][4]
print(mat3)

mat4 = mat[:3, 1:2]
print(mat4)

mat5 = mat[-1]
print(mat5)

mat6 = mat[-2:]
print(mat6)

sum = np.sum(mat)
print(sum)

std = np.std(mat)
print(std)

cols_sum = np.sum(mat, axis=0)
print(cols_sum)