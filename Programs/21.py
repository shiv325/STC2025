# Select all rows in DataFrame where Age > 30

import numpy as np
import pandas as pd

data = {
    "Name" : ["Luffy", "Zoro", "Nami", "Sanji", "Chopper", "Robin", "Franky", "Brook"],
    "Gender" : ["Male", "Male", "Female", "Male", "Male", "Female", "Male", "Male"],
    "Age" : [20, 22, 21, 22, 10, 31, 50, 70]
}

df = pd.DataFrame(data)
print(df)

print("\nDataFrame with Age > 30\n")
filtered = df[df["Age"] > 30]
print(filtered)