import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\abidli\Desktop\cleaning datasets\datasets\raw\FashionDataset.csv")
df=df.drop(columns="Unnamed: 0")
df=df.replace("Nan",np.nan)
df=df.drop_duplicates()
df["SellPrice"]=df["SellPrice"].astype(float)
df=df.fillna({
    "BrandName":df["BrandName"].mode()[0]
    ,"Deatils":df["Deatils"].mode()[0]
    ,"SellPrice":df["SellPrice"].median()
})
df=df.dropna(subset=["MRP","Discount","Sizes"])
df.columns=(df.columns
            .str.lower()
            .str.strip()
            )
df=df.rename(columns={
    "deatils":"details"
})
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
df=df.rename(columns={"category":"category women"})
df["category women"]=df["category women"].str.split("-",n=1).str[0]
df["sellprice"]=df["sellprice"].astype(int)
df.to_csv("fasion dataset cleaned.csv",index=False)
