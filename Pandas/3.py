import pandas as pd
print(pd.__version__)
dataset = {
    "cars":["volvo","maruti","tata"],
    "passing":[45,78,56]
}
df = pd.DataFrame(dataset)
print(df)

a = [4,5,6,7,8,9]
df = pd.Series(a,index=["a","b","c","d","e","f"])

print("this is 3rd index of series a ",a[3])

print(df["f"])