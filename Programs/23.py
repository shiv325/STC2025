# Replace missing values in DataFrame with column mean

import numpy as np
import pandas as pd

data = {
    "Gadgets" : ["Laptop", "Smartphone", "XBOX", "PS5"],
    "Price" : [54000, np.nan, np.nan, 27000]
}

df = pd.DataFrame(data)
print(df, "\n")

avgVal = df["Price"].mean(axis = 0)
print(f"Total Cost => {avgVal}\n")

print(df.fillna(avgVal))