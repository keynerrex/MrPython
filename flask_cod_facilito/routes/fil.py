import random
import matplotlib.pyplot as plt


campana=[random.gauss(1,0.5) for i in range(1000)]
plt.hist(campana, bins=15)
plt.show() 