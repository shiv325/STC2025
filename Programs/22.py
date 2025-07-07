# Calculate sum and mean of DataFrame column

import numpy as np
import pandas as pd

data = {
    "Gadgets" : ["Laptop", "Smartphone", "XBOX", "PS5"],
    "Price" : [54000, 12000, 15000, 27000]
}

df = pd.DataFrame(data)
print(df, "\n")

print(f"Total Cost => {df["Price"].sum(axis = 0)}")
print(f"Total Cost => {df["Price"].mean(axis = 0)}")