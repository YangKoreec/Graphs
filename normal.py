import numpy as np
import scipy
import matplotlib.pyplot as plt
import pandas as pd

data = np.random.normal(0, 100, 2000)
x = np.linspace(-4, 4, 2000)
y = scipy.stats.norm.pdf(x, 0, 1)

mean = data.mean()
s = data.std()
new_data = (data - mean) / s

x = np.linspace(-4, 4, 2000)
y = scipy.stats.norm.pdf(x)

plt.plot(x, y, color="red")
plt.hist(new_data, bins=[-3, -2, -1, 0, 1, 2, 3], color="blue", density=True)
plt.title("Нормальное распределение")
plt.xlabel("Значение")
plt.ylabel("Количество")

plt.show()