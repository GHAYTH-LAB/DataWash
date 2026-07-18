import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\abidli\Desktop\cleaning datasets\datasets\raw\FashionDataset.csv")
#checking my dataset at first
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
df=df.drop(columns="Unnamed: 0")
print(df.duplicated().sum())
df=df.replace("Nan",np.nan)
print(df.isna().sum())
df=df.drop_duplicates()
df["SellPrice"]=df["SellPrice"].astype(float)
print(df.dtypes)
df=df.fillna({
    "BrandName":df["BrandName"].mode()[0]
    ,"Deatils":df["Deatils"].mode()[0]
    ,"SellPrice":df["SellPrice"].median()
})
df=df.dropna(subset=["MRP","Discount","Sizes"])
print(df.columns)
df.columns=(df.columns
            .str.lower()
            .str.strip()
            )
df=df.rename(columns={
    "deatils":"details"
})
print(df.columns)
Q1=df['sellprice'].quantile(0.25)
Q3=df["sellprice"].quantile(0.75)
IQR=Q3-Q1
lower_band=Q1-1.5*IQR
Higher_band=Q3+1.5*IQR
df=df[(df["sellprice"]>=lower_band) &(df["sellprice"]<=Higher_band)]
df["details"]=(df["details"]
                .str.replace("-","")
                .str.strip()
                )
df["sizes"] = (df["sizes"]
               .str.split(":", n=1).str[1]
               .str.replace("_","")
               .str.replace(",","")
            )
df["mrp"]=df["mrp"].str.split("\n",n=1).str[1]
df["mrp"]=df["mrp"].astype(int)
df=df.rename(columns={"discount":"discount%"})
df["discount%"]=df["discount%"].str.split("%",n=1).str[0]
print(df["discount%"])
df=df.rename(columns={"category":"category women"})
df["category women"]=df["category women"].str.split("-",n=1).str[0]
print(df["category women"])
df["sellprice"]=df["sellprice"].astype(int)
df.to_csv("fasion dataset cleaned.csv",index=False)