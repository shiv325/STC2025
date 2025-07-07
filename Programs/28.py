# Plot bar chart of favourite fruits and their quantities

import matplotlib.pyplot as plt

fruits = ["Apple", "Mango", "Orange", "Litchi"]
quantities = [100, 200, 500, 1000]

plt.bar(fruits, quantities)
plt.title("Fruits & Quantites")
plt.xlabel("Fruits")
plt.ylabel("Quantity")
plt.show()