import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\abidli\Desktop\cleaning datasets\datasets\raw\amazon_product.csv")
df=df.drop(columns=["product_availability","unit_price","unit_count","product_title","product_url","product_photo","Unnamed: 0","asin"])
df.columns=(df.columns
            .str.lower()
            .str.strip()
            .str.replace("_"," ")
            )
df["product price"]=df["product price"].str.split("$",n=1).str[1]
df["product price"]=df["product price"].astype(float)
df["product original price"]=df["product original price"].str.split("$",n=1).str[1]
df["product original price"]=df["product original price"].astype(float)
df=df.fillna({
    "product original price":df["product original price"].median()
})
df["discount pourcentage"]=((df["product original price"]-df["product price"])/df["product original price"])*100
df=df[(df["discount pourcentage"]>=0)]
df.loc[(df["discount pourcentage"]>99),"discount pourcentage"]=df["discount pourcentage"].median()
df=df.drop(columns="currency")
df=df.fillna({
    "product star rating":df["product star rating"].median()
})
df["product minimum offer price"]=df["product minimum offer price"].str.split("$",n=1).str[1]
df["product minimum offer price"]=df["product minimum offer price"].astype(float)
df["is best seller"]=df["is best seller"].apply(lambda x:1 if x==True else 0)
df["is best seller"]=df["is best seller"].astype(int)
df["is amazon choice"]=df["is amazon choice"].apply(lambda x:1 if x==True else 0)
df["is amazon choice"]=df["is amazon choice"].astype(int)
df["is prime"]=df["is prime"].apply(lambda x:1 if x==True else False)
df["is prime"]=df["is prime"].astype(int)
df["climate pledge friendly"]=df["climate pledge friendly"].apply(lambda x:1 if x==True else 0)
df["climate pledge friendly"]=df["climate pledge friendly"].astype(int)
df["sales volume in k"]=(df["sales volume"]
                         .str.split("+",n=1).str[0]
                         .str.strip()
                         )
df=df[df["sales volume in k"].str.contains(r"^\d",na=False)]
df[["number", "unit"]] = df["sales volume"].str.extract(r"(\d+)(K)?")
df["sales volume in k"] = df["number"].astype(int)
df.loc[df["unit"] == "K", "sales volume in k"] *= 1000
df = df.drop(columns=["number", "unit","sales volume"])
df["delivery"]=df["delivery"].str.lower()
df["delivery type"] ="normal"
df.loc[(df["delivery"].str.contains(("available instantly"),na=False)),"delivery type"]="instant"
df.loc[df["delivery"].str.contains("released",na=False),"delivery type"]="preorder"
df=df.drop(columns="delivery")
df["normal delivery"]=df["delivery type"]=="normal"
df["preorder delivery"]=df["delivery type"]=="preorder"
df["normal delivery"]=df["normal delivery"].astype(int)
df["preorder delivery"]=df["preorder delivery"].astype(int)
df=df.drop(columns="delivery type")
df["has variations"]=df["has variations"].astype(int)
df.to_csv("Cleaned version of amazon product.csv",index=False)