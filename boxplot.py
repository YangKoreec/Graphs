import numpy as np
import matplotlib.pyplot as plt

data = [np.random.randint(-1000 * i, 100, 1000) for i in range(3)]

plt.boxplot(data)
plt.show()