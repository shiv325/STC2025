# Sort DataFrame by specific column

import numpy as np
import pandas as pd

data = {
    "Gadgets" : ["Laptop", "Smartphone", "XBOX", "PS5"],
    "Price" : [54000, 12000, 15000, 27000]
}

df = pd.DataFrame(data)
print(df, "\n")

print(df.sort_values("Price", axis = 0))