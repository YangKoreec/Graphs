import numpy as np
import matplotlib.pyplot as plt
import scipy

data = np.random.randint(-100, 100, 100)
normal_data = np.sort((data - data.mean()) / data.std())

x = scipy.stats.norm.ppf(np.linspace(0, 1, data.size))

plt.plot(x, x, color="red")
plt.scatter(x, normal_data, color="blue")
plt.title("График QQ-plot")
plt.xlabel("Теоретические квантили")
plt.ylabel('Выборочные квантили')
plt.grid(True, which='both')
plt.minorticks_on()

plt.show()