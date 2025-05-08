import numpy as np
import scipy
import matplotlib.pyplot as plt

x_mas = np.random.randint(-1000, 1000, 100)
y_mas = np.random.randint(-1000, 1000, 100)

b1, b0, r, p, std_b1 = scipy.stats.linregress(x_mas, y_mas)

y_ = np.array([b1 * x + b0 for x in x_mas])
e = y_mas - y_

plt.plot(range(-1000, 1000), np.full(2000, 0), color="red")
plt.scatter(x_mas, e, color="blue")
plt.title("Ошибки предсказаний")
plt.xlabel("Значения")
plt.ylabel("Ошибки")

plt.show()