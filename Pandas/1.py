import pandas as pd

print(pd.__version__)
mydataset = {
    "cars" : ["volvo","alto","maruti"],
    "passing" : [3,7,2]
}
df = pd.DataFrame(mydataset)

print(df)