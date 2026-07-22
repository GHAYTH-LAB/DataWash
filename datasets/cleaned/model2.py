import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
df=pd.read_csv(r"C:\Users\abidli\Desktop\cleaning datasets\datasets\cleaned\Cleaned version of amazon product.csv")
y=df["sales volume in k"]
X=df.drop(columns="sales volume in k")
X_train,X_test,y_train,y_test=train_test_split(X,y
                                               ,random_state=42
                                               ,test_size=0.2)
scale=StandardScaler()
X_train=scale.fit_transform(X_train)
X_test=scale.transform(X_test)
model=RandomForestRegressor(n_estimators=50
                            ,random_state=42
                            ,max_depth=5
                            )
model.fit(X_train,y_train)
predictions=model.predict(X_test)
print("mean_absolute error= ",mean_absolute_error(y_test,predictions),"mean_squared error= ",mean_squared_error(y_test,predictions),"f1= ",r2_score(y_test,predictions))
