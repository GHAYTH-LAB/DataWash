df["delivery type"] = "normal"
df.loc[(df["delivery"].str.contains(("Available instantly"),na=False)),"delivery type"]="instant"
df.loc[df["delivery"].str.contains("released",na=False),"delivery type"]="preorder"
df=df.drop(columns="delivery")
print(df["delivery type"])