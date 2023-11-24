import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def func1(x, y):
    return np.power(x, 0.25) + np.power(y, 0.25)

def func2(x, y):
    return x**2 - y ** 2

def func3(x, y):
    return 2*x+3*y

def func4(x, y):
    return x**2 + y ** 2

def func5(x, y):
    return 2 + 2*x + 2*y - x**2 - y ** 2

import numpy as np
import matplotlib.pyplot as plt

# Создаем массив значений x и y
x_values = np.linspace(-10, 10, 100)
y_values = np.linspace(-10, 10, 100)

# Создаем сетку точек для x и y
x_grid, y_grid = np.meshgrid(x_values, y_values)

#Создаем трехмерные графики
fig = plt.figure(figsize=(15, 10))

# Функция 1: f(x, y) = x^(1/4) + y^(1/4)
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(x_grid, y_grid, func1(x_grid, y_grid), cmap='viridis')
ax1.set_title('func1: x^(1/4) + y^(1/4)')

# Функция 2: f(x, y) = x^2 - y^2
ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(x_grid, y_grid, func2(x_grid, y_grid), cmap='viridis')
ax2.set_title('func2: x^2 - y^2')

# Функция 3: f(x, y) = 2*x + 3*y
ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(x_grid, y_grid, func3(x_grid, y_grid), cmap='viridis')
ax3.set_title('func3: 2*x + 3*y')

# Функция 4: f(x, y) = x^2 + y^2
ax4 = fig.add_subplot(234, projection='3d')
ax4.plot_surface(x_grid, y_grid, func4(x_grid, y_grid), cmap='viridis')
ax4.set_title('func4: x^2 + y^2')

# Функция 5: f(x, y) = 2 + 2*x + 2*y - x^2 - y^2
ax5 = fig.add_subplot(235, projection='3d')
ax5.plot_surface(x_grid, y_grid, func5(x_grid, y_grid), cmap='viridis')
ax5.set_title('func5: 2 + 2*x + 2*y - x^2 - y^2')

# Показываем графики
plt.show()

