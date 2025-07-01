import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

plt.figure(figsize=(10, 5))
plt.suptitle("testjlsdf")
# Первый подграфик (1-я строка, 2 столбца, 1-я позиция)
plt.subplot(2, 1, 1)
plt.plot(x, np.sin(x))
plt.title("Синус")

# Второй подграфик (1-я строка, 2 столбца, 2-я позиция)
plt.subplot(2, 1, 2)
plt.plot(x, np.cos(x))
plt.title("Косинус")

plt.tight_layout()
plt.show()