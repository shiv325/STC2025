# Visualize random numbers as histogram using both matplotlib and seaborn

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

vals = np.arange(0, 10)
freq = np.random.randint(1, 10, size=10)

plt.bar(vals, freq)
plt.title("Random Numbers Freq")
plt.xlabel("Number")
plt.ylabel("Frequency")
plt.show()

data = np.random.randn(200)

sns.histplot(data, bins = 10)
plt.title("Seaborn Histogram of Frequencies")
plt.xlabel("Number")
plt.ylabel("Count")
plt.show()
