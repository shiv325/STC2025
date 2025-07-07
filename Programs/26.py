import numpy as np
import pandas as pd

data = pd.read_csv("iris.csv")
print(data)
unique = data.drop_duplicates(subset=['sepal_length'])
print(unique)
setosa = data[data["species"] == "setosa"]
print(setosa)
maxPetalLength = data[data["petal_length"] == data["petal_length"].max()]
print(maxPetalLength)