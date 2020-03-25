import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

np.random.seed(101)
tf.set_random_seed(101)

x = np.linspace(0, 50, 50)
y = np.linspace(0, 50, 50)

x += np.random.uniform(-4, 4, 50)
y += np.random.uniform(-4, 4, 50)

# n = len(x)
m, c = np.polyfit(x, y, 1)

# NOTE:
'''
m and c are coeffs we need to calculate from the training data

m = sum(x(i) - mean(x)) * (y(i) - mean(y))) / sum((x(i) - mean(x))^2)
c = mean(y) - m * mean(x)

'''
plt.scatter(x, y)
plt.plot(x, x * m + c)
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
