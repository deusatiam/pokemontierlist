### TEST: OPENING AN IMAGE USING AN ADDRESS FROM A PANDAS DATAFRAME

import pandas as pd
import numpy as np

df = pd.read_csv("resources/starter9.csv")

bulba = df.iloc(0)[0]

print(bulba['Icon'])
print(bulba['Sugimori'])