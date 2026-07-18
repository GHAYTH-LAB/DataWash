import pandas as pd
df=pd.read_csv(r"C:\Users\abidli\Desktop\cleaning datasets\datasets\raw\netflix1.csv")
print(df.shape)
print("---------")
#check for duplicates and na values (0 for both cases)
"""print(df.isna().sum())
print(df.duplicated.sum())"""
#standarizing columns names
print(df.columns)
df.columns=df.columns.str.strip()
df.columns=df.columns.str.lower()
df.columns=df.columns.str.replace("_"," ")
#checking for types
df["date added"]=pd.to_datetime(df["date added"])
print(df.dtypes)
#checking for outliers
Q1=df["release year"].quantile(0.25)
Q3=df["release year"].quantile(0.75)
IQR=Q3-Q1
Lower_band=Q1-1.5*IQR
Higher_band=Q3+1.5*IQR
print(df.shape)
df=df[(df["release year"]>Lower_band) & (df["release year"]<Higher_band)]
print(df.shape)
#some feature engineering (extracting day and month and year from release year column)
df["day"]=df["date added"].dt.day
df["month"]=df["date added"].dt.month
df["year"]=df["date added"].dt.year
df=df.drop(columns="date added")
print(df.columns)
print((df["director"]=="Not Given").sum())
print(df.shape)
df["director"]=(df["director"]
                .replace("Not Given","unknown")
                .str.lower()
                .str.replace(",","")
                .str.strip()
                .str.replace(".","")
                )
df["type"]=df["type"].str.lower()
df["title"]=(df["title"]
             .str.replace(":","")
             .str.replace("-","")
             .str.replace(",","")
             .str.replace(".","")
             .str.lower()
             )
df["country"]=(df["country"]
               .replace("Not Given","unknown")
               .str.lower())
df["listed in"]=(df["listed in"]
                 .str.replace(",","")
                 .str.replace("'","")
                 .str.replace(".","")
                 .str.lower()
)

df.to_csv("Cleaned netflix dataset.csv",index=False)