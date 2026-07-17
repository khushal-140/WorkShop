import pandas as pd


data = {
    "Name": ["Khushal", "Rahul", "Amit", "Rahul"],
    "Marks": [90, None, 88, None],
    "City": ["Diu", "Surat", None, "Surat"]
}

df = pd.DataFrame(data)
print(df.isnull().sum())
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].median())
df["City"] = df["City"].fillna(df["City"].mode()[0])
print(df["Marks"])
print(df["City"])
df.replace("Diu","Daman")
print(df["City"])
