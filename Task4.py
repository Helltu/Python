import numpy as np
import math
import matplotlib.pyplot as plt

def func(x, c):
    return  np.power(np.abs(2*x-c), 3/5)+0.567

values = list()

for c in np.arange(-10, 1, 0.5):
    value = func(12.1, c)
    print(f'При х=12.1 и с={c} f={value}')
    values.append(value)
    
print(f'Наиблольший элемент массива {np.max(values)}')
print(f'Наименьший элемент массива {np.min(values)}')
print(f'Среднее значение элементов массива {np.average(values)}')
print(f'Количество элементов массива {len(values)}')

plt.plot(np.arange(-10, 1, 0.5), values, label='f(x)')
plt.axhline(np.average(values), color='red', linestyle='--', label='Среднее значение')

# Добавляем метки и легенду
plt.xlabel('Значения c')
plt.ylabel('Значения функции')
plt.title('График функции и среднего значения')
plt.legend()

# Показываем график
plt.show()
