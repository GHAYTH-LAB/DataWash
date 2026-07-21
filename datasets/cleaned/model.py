import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score
from sklearn.preprocessing import  StandardScaler
df=pd.read_csv(r"C:\Users\abidli\Desktop\cleaning datasets\datasets\cleaned\cleaned dataset credit customres.csv")
y=df["duration"]
X=df.drop(columns="duration")
X_train,X_test,y_train,y_test=train_test_split(X,y
                                               ,random_state=42
                                               ,test_size=0.2
                                               )
scaler=StandardScaler()
X_train=scaler.fit_transform(X_train)
X_test=scaler.transform(X_test)
model=KNeighborsRegressor(n_neighbors=7,
    weights='uniform',
    algorithm='auto',
    leaf_size=30,
    p=2,
    metric='minkowski',
    n_jobs=-1
)
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("Evaluation: \n")
print("mean squared error= ",mean_squared_error(y_test,predictions),"absolute error= ",mean_absolute_error(y_test,predictions),"r2 score= \n",r2_score(y_test,predictions))




