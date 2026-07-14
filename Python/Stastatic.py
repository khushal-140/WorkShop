import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sns
# import seaborn as pl
# data={"studentname":["Amit","Rahel","Smir"],
#       "english":[50,60,70],
#       "science":[40,50,70],
#       "math":[70,80,90]
#       }
# df=pd.DataFrame(data)
# print(df)
#df.to_excel("info.xlsx",index=False)
df=pd.read_excel("info.xlsx")
print(df["english"]+df["science"]+df["math"])
print(df["english"].mean())
print(df["english"].median())
print(df["english"].mode())
print(df["english"].std())
print(df["english"].var())
#pl.bar(df["studentname"],df["english"])
#
#pl.show()
sns.barplot(x=[70,75,80,82,90,95,100])
pl.show()