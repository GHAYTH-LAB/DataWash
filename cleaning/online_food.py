import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler,QuantileTransformer
from sklearn.metrics import precision_score,f1_score,recall_score
# Data preprocessing and data cleaning
df=pd.read_csv(r"C:\Users\abidli\Desktop\cleaning datasets\datasets\raw\onlinefoods.csv")
df=df.drop_duplicates()
df.columns=(df.columns
            .str.lower()
            .str.strip()
            )
df=df.drop(columns="unnamed: 12")
df["feedback"]=df["feedback"].str.strip()
df["male"]=df["gender"]=="Male"
df["female"]=df["gender"]=="Female"
df["male"]=df["male"].astype(int)
df["female"]=df["female"].astype(int)
df["single"]=df["marital status"]=="Single"
df["married"]=df["marital status"]=="Married"
df["prefer not to say"]=df["marital status"]=="Prefer not to say"
df[["single","married","prefer not to say"]]=df[["single","married","prefer not to say"]].astype(int)
df["student"]=df["occupation"]=="Student"
df["self employeed"]=df["occupation"]=="Self Employeed"
df["house wife"]=df["occupation"]=="House wife"
df["employee"]=df["occupation"]=="Employee"
df[["student","self employeed","house wife","employee"]]=df[["student","self employeed","house wife","employee"]].astype(int)
df=df.drop(columns=["gender","marital status","occupation"])
df["no monthly income"]=df["monthly income"]=="No Income"
df["monthly income from 25001 to 50000"]=df["monthly income"]=="25001 to 50000"
df["monthly income more than 50000"]=df["monthly income"]=="More than 50000"
df["monthly income from 10001 to 25000"]=df["monthly income"]=="10001 to 25000"
df["monthly income Below Rs 10000"]=df["monthly income"]=="Below Rs.10000"
df=df.drop(columns="monthly income")
df[["no monthly income","monthly income from 25001 to 50000","monthly income more than 50000","monthly income from 10001 to 25000","monthly income Below Rs 10000"]]=df[["no monthly income","monthly income from 25001 to 50000","monthly income more than 50000","monthly income from 10001 to 25000","monthly income Below Rs 10000"]].astype(int)
df["education post graduate"]=df["educational qualifications"]=="Post Graduate"
df["education graduate"]=df["educational qualifications"]=="Graduate"
df["education phd"]=df["educational qualifications"]=="Ph.D"
df["education uneducated"]=df["educational qualifications"]=="Uneducated"
df["education school"]=df["educational qualifications"]=="School"
df=df.drop(columns="educational qualifications")
df[["education post graduate","education graduate","education phd","education uneducated","education school"]]=df[["education post graduate","education graduate","education phd","education uneducated","education school"]].astype(int)
df["output"]=df["output"].apply(lambda x:0 if x=="No" else 1)
df["output"]=df["output"].astype(int)
df["feedback positive"]=df["feedback"]=="Positive"
df["feedback negative"]=df["feedback"]=="Negative"
df=df.drop(columns="feedback")
df[["feedback positive","feedback negative"]]=df[["feedback positive","feedback negative"]].astype(int)
df.to_csv("Cleaned online food dataset.csv",index=False)
y=df["output"]
X=df.drop(columns="output")
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.2)
scaler=QuantileTransformer(n_quantiles=100)
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
grid=GridSearchCV(
    estimator=RandomForestClassifier()
    ,param_grid={
        "n_estimators":[50,70,80,90,100,150,200,300]
        ,"max_depth":[3,5,7,10,8]
        ,"min_samples_leaf":[5,10,15]
        ,"min_samples_split":[5,10,15,20]
    }
    ,cv=5
)
grid.fit(X_train,y_train)
predictions=grid.predict(X_test)
print("evaluation : precision",precision_score(y_test,predictions,average="macro"),"recall= ",recall_score(y_test,predictions,average="macro"),"f1 score= ",f1_score(y_test,predictions,average="macro"))