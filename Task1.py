import numpy as np

def calculate_expression(x, a):
    result = np.arccos(x**2) - a * (x / a**3)**(1/2) + (np.sin(np.pi/2))**3 / np.log2(x)
    return result

x_value = 0.5
a_value = 2.0  
result = calculate_expression(x_value, a_value)
print(result)
