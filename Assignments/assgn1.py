import numpy as np
import pandas as pd
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Part 1

data = pd.read_csv("movie_genre_classification_final.csv")

ratings = data['Rating']

mean = np.mean(ratings)

variance = np.var(ratings)

std = np.std(ratings)

aboveMean = data[data["Rating"] > mean]
belowMean = data[data["Rating"] < mean]

# Part 2

print(data.head())
print(data.describe())
print(data.info())

data['Rating_Category'] = np.where(data['Rating'] > mean, 'High', 'Low')

# Part 3

budget50 = data["Budget_USD"][ : 50]
ratings50 = ratings[ : 50]
plt.scatter(budget50, ratings50)
plt.xlabel("Budget (USD)")
plt.ylabel("Ratings")
plt.show()

slope, intercept, r_value, p_value, std_err = linregress(budget50, ratings50)
regression_line = slope * budget50 + intercept
plt.scatter(budget50, ratings50, label='Data Points')
plt.plot(budget50, regression_line, color='red', label='Regression Line')
plt.xlabel("Budget (USD)")
plt.ylabel("Ratings")
plt.title("Movie Ratings vs Budget with Linear Regression")
plt.legend()
plt.savefig("ratings_vs_budget_regression.png")
plt.show()
