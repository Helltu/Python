import numpy as np

matrix_X = np.zeros((12, 3), dtype=int)

matrix_X[:, 0] = 1

matrix_X[:, 1] = np.random.randint(14, 26, size=12)

matrix_X[:, 2] = np.random.randint(60, 83, size=12)

vector_Y = np.random.uniform(13.5, 18.6, size=12)

print("Матрица X:")
print(matrix_X)

print("Вектор Y:")
print(vector_Y)

X_T = np.transpose(matrix_X)

X_T_X = np.dot(X_T, matrix_X)

X_T_X_inv = np.linalg.inv(X_T_X)

X_T_Y = np.dot(X_T, vector_Y)

vector_A = np.dot(X_T_X_inv, X_T_Y)

print("Вектор A:")
print(vector_A)

Y = np.dot(matrix_X, vector_A)

print("Значение Y:")
print(Y)

print("Отношение вектора Y к значениям проверки Y:")
print(vector_Y/Y)
