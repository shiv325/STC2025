# Handle missing data {'A' : [1, 2, np.nan], 'B' : [5, np.nan, np.nan]}

import numpy as np
import pandas as pd

data = {
    'A' : [1, 2, np.nan],
    'B' : [5, np.nan, np.nan]
}

df = pd.DataFrame(data)
print(df, "\n")

avgVal = df["A"].mean(axis = 0)
print(f"Avg => {avgVal}\n")

print(df.fillna(avgVal))