import numpy as np
import matplotlib.pyplot as plt

random_x = np.random.rand(5)  # массив из 5 случайных чисел
random_y = np.random.rand(5)  # массив из 5 случайных чисел

plt.scatter(random_x, random_y)
plt.title('Диаграмма рассеяния случайных чисел')
plt.xlabel('Ось x')
plt.ylabel('Ось y')
plt.show()