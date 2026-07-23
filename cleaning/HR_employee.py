import pandas as pd
import numpy as np
df=pd.read_csv(r"C:\Users\abidli\Desktop\cleaning datasets\datasets\raw\HR-Employee-Attrition.csv")
df.columns=(df.columns
            .str.strip()
            .str.lower()

)
df["attrition"]=df["attrition"].apply(lambda x:True if x==1 else False)
df["attrition"]=df["attrition"].astype(int)
df["businesstravel"]=(df["businesstravel"]
                      .str.replace("-","_")
                      )
df["businesstravel"]=df["businesstravel"].replace("Non_Travel","Travel_Non")
df["businesstravel"]=df["businesstravel"].str.lower()
df["businesstravel"]=df["businesstravel"].str.split("_",n=1).str[1]
#Removing outliers
Q1=df["dailyrate"].quantile(0.25)
Q3=df["dailyrate"].quantile(0.75)
IQR=Q3-Q1
Lower_band=Q1-1.5*IQR
Higher_band=Q3+1.5*IQR
df=df[(df["dailyrate"]>=Lower_band) & (df["dailyrate"]<=Higher_band)]
df["department"]=df["department"].str.lower()
df["educationfield"]=(df["educationfield"]
                       .str.lower()
                       .str.strip())
df["educationfield"]=df["educationfield"].replace("other",np.nan)
df=df.dropna(subset="educationfield")
df=df.drop(columns="employeecount")
df["jobrole"]=(df["jobrole"]
               .str.strip()
               .str.lower())
df["maritalstatus"]=(df["maritalstatus"]
                    .str.strip()
                    .str.lower())
#Removing outliers
Q1=df["monthlyincome"].quantile(0.25)
Q3=df["monthlyincome"].quantile(0.75)
IQR=Q3-Q1
Lower_band=Q1-1.5*IQR
Higher_band=Q3+1.5*IQR
df=df[(df["monthlyincome"]>Lower_band) & (df["monthlyincome"]<Higher_band)]
df=df.drop(columns="over18")
df["overtime"]=(df["overtime"]
                .str.strip()
                .str.lower())
df["overtime"]=df["overtime"].apply(lambda x:1 if x=="yes" else 0)
df["overtime"]=df["overtime"].astype(int)
df=df.drop(columns="standardhours")
df=df.rename(columns={"yearsatcompany":"experience"})
df.to_csv("Cleaned Employee attrition dataset.csv",index=False)
