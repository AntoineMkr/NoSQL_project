import json,csv
import pandas as pd
from getData import fetchNewData 

print(fetchNewData())
data = pd.read_csv("paris-air-quality.csv")
data = data.sort_values(by=['date'], ascending = False)
