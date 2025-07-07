# Create Pandas DataFrame from list of dictionary

import numpy as np
import pandas as pd

data = {
    "Anime" : ["Bleach", "Naruto", "Dragon Ball Z", "One Piece"],
    "Character" : ["Ichigo", "Itachi", "Son Goku", "Trafalgar Law"]
}

df = pd.DataFrame(data)
print(df)