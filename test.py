import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Пример данных
data = np.random.normal(0, 1, 100)

# Квантиль-данные
theoretical_quantiles = np.linspace(0, 1, len(data))
sample_quantiles = np.sort(data)
theoretical_values = stats.norm.ppf(theoretical_quantiles)

print(data.min())

# Строим графиr
plt.scatter(theoretical_values, sample_quantiles)
plt.plot(theoretical_values, theoretical_values, color='red', linestyle='--')  # линия идеала
plt.xlabel('Теоретические квантили')
plt.ylabel('Выборочные квантили')
plt.title('QQ plot')
plt.grid(True)
plt.show()