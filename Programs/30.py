# Use seaborn to plot scatter plot from built-in "tips" dataset

import seaborn as sns
import matplotlib.pyplot as plt

# Load the built-in "tips" dataset
tips = sns.load_dataset("tips")

# Create a scatter plot: total_bill vs tip
sns.scatterplot(data=tips, x="total_bill", y="tip")

plt.title("Scatter Plot of Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()