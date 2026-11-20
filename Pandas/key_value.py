import pandas as pd

calories = {
    "day1": 420, "day2": 380, "day3": 390
}


df =  pd.Series(calories)
df =  pd.Series(calories,index = ["day1","day2"])
print(df)