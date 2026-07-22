import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score,recall_score,f1_score 
df=pd.read_csv(r"C:\Users\abidli\Desktop\cleaning datasets\datasets\raw\titanic.csv")
df["sex nature"]=df["Sex"].apply(lambda x: 1 if x=="male" else 0)
df.columns=(df.columns
            .str.lower()
            .str.strip()
            .str.replace("_"," "))
df = df[df["age"].notna() & df["age"].apply(float.is_integer)]
df=df.drop(columns="cabin")
df["embarked S"]=df["embarked"]=="S"
df["embarked C"]=df["embarked"]=="C"
df["embarked Q"]=df["embarked"]=="Q"
df=df.drop(columns=["embarked","name","sex","ticket"])
df[["embarked S","embarked C","embarked Q"]]=df[["embarked S","embarked C","embarked Q"]].astype(int)
df.to_csv("cleaned titanic.csv",index=False)
y=df["survived"]
X=df.drop(columns="survived")
X_train,X_test,y_train,y_test=train_test_split(X,y
                                               ,random_state=42
                                               ,test_size=0.2)
grid=GridSearchCV(
    estimator=RandomForestClassifier()
    ,param_grid={
        "n_estimators":[10,50,100,200]
        ,"max_depth":[5,10,7]
        ,"min_samples_split":[5,10,15]
        ,"min_samples_leaf":[5,10,15]
        }
    ,cv=5
    )
grid.fit(X_train,y_train)
predictions=grid.predict(X_test)
print("precision= ",precision_score(y_test,predictions),"recall= ",recall_score(y_test,predictions),"f1= ",f1_score(y_test,predictions))