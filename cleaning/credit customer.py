import pandas as pd
df=pd.read_csv(r"C:\Users\abidli\Desktop\cleaning datasets\datasets\raw\credit_customers-selected-columns.csv")
print(df.shape)
df.columns=(df.columns
            .str.lower()
            .str.strip()
            .str.replace("_"," "))
df["checking status < 0"]=df["checking status"]=="<0"
df["checking status between 0 and 200"]=df["checking status"]=="0<=X<200"
df["checking status does not exist"]=df["checking status"]=="no checking"
df["checking status < 0"]=df["checking status < 0"].astype(int)
df["checking status between 0 and 200"]=df["checking status between 0 and 200"].astype(int)
df["checking status does not exist"]=df["checking status does not exist"].astype(int)
df=df.drop(columns="checking status")
print(df.columns)
print(df.info())
df["existing paid"]=df["credit history"]=="existing paid"
df["critical/other existing credit"]=df["credit history"]=="critical/other existing credit"
df["no credits/all paid"]=df["credit history"]=="no credits/all paid"
df["all paid"]=df["credit history"]=="all paid"
df["delayed previously"]=df["credit history"]=="delayed previously"
cols = ["existing paid", "critical/other existing credit",
        "no credits/all paid", "all paid", "delayed previously"]
df[cols] = df[cols].astype(int)
df=df.drop(columns="credit history")
df["purpose radio/tv"]=df["purpose"]=="radio/tv"
df["purpose new car"]=df["purpose"]=="new car"
df["purpose furniture/equipment"]=df["purpose"]=="furniture/equipment"
df["purpose used car"]=df["purpose"]=="used car"
df["purpose business"]=df["purpose"]=="business"
df["purpose education"]=df["purpose"]=="education"
df["purpose repairs"]=df["purpose"]=="repairs"
df["purpose domestic appliance"]=df["purpose"]=="domestic appliance"
df["purpose other"]=df["purpose"]=="other"
df["purpose retraining"]=df["purpose"]=="retraining"
df=df.drop(columns="purpose")
purpose_cols = ["purpose radio/tv","purpose new car","purpose furniture/equipment",
                "purpose used car","purpose business","purpose education",
                "purpose repairs","purpose domestic appliance","purpose other",
                "purpose retraining"]
df[purpose_cols] = df[purpose_cols].astype(int)
df["credit amount"]=df["credit amount"].astype(int)
print(df["credit amount"])
df=df.drop(columns="credit amount")
df["no known savings"]=df["savings status"]=="no known savings"
df["savings <100"]=df["savings status"]=="<100"
df["savings 100<=X<500"]=df["savings status"]=="100<=X<500"
df["savings 500<=X<1000"]=df["savings status"]=="500<=X<1000"
df["savings >=1000"]=df["savings status"]==">=1000"
df["employment between 1 and 4"]=df["employment"]=="1<=X<4"
df["employment >7"]=df["employment"]==">=7"
df["emploment between 4 and 7"]=df["employment"]=="4<=X<7"
df["employment <1"]=df["employment"]=="<1"
df["unemployed"]=df["employment"]=="unemployed"
cols = [
    "no known savings", "savings <100", "savings 100<=X<500",
    "savings 500<=X<1000", "savings >=1000",
    "employment between 1 and 4", "employment >7",
    "emploment between 4 and 7", "employment <1", "unemployed"
]
df[cols] = df[cols].astype(int)
print(df.columns)
print(df.shape)
df=df.drop(columns="employment")
Q1=df["installment commitment"].quantile(0.25)
Q3=df["installment commitment"].quantile(0.75)
IQR=Q3-Q1
Lower_band=Q1-1.5*IQR
Higher_band=Q3+1.5*IQR
df=df[(df["installment commitment"]>=Lower_band) & (df["installment commitment"]<=Higher_band) ]
df["male single"]=df["personal status"]=="male single"
df["female divorced or dependent or married"]=df["personal status"]=="female div/dep/mar"
df["male married or widowed"]=df["personal status"]=="male mar/wid"
df["male div or sep"]=df["personal status"]=="male div/sep"
cols = [
    "male single",
    "female divorced or dependent or married",
    "male married or widowed",
    "male div or sep"
]
df[cols] = df[cols].astype(int)
df=df.drop(columns="personal status")
df["other parties none"] = df["other parties"] == "none"
df["other parties guarantor"] = df["other parties"] == "guarantor"
df["other parties co applicant"] = df["other parties"] == "co applicant"
cols = ["other parties none", "other parties guarantor", "other parties co applicant"]
df[cols] = df[cols].astype(int)
df = df.drop(columns="other parties")
df.to_csv("cleaned dataset credit customres.csv",index=False)