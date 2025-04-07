import pandas as pd
import matplotlib.pyplot as plt

data_file = 'divan_prices.csv'
data = pd.read_csv(data_file)

plt.hist(data['Цена'])
plt.title('Гистограмма распределения цен на прямые диваны')
plt.xlabel('Цена')
plt.ylabel('Частота')
plt.show()

print(f'Средняя цена на диваны -', data['Цена'].mean())