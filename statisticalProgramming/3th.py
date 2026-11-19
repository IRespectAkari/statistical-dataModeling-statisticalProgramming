import pandas as pd

df1 = pd.read_csv("titanic.csv", index_col=0)
df2 = pd.DataFrame()

# df2 = df1[df1['Age'] >= 20]
# print(df2)

print(f"df1['Age']\n{df1['Age']}")
print("---")

print(f"# df1['Age'] >= 20\n{df1['Age'] >= 20}")
print("---")

print(f"df1[df1['Age'] >= 20] \n {df1[df1['Age'] >= 20]}")
print("---")

print(f"df1['Age'].isnull().sum()\n{df1['Age'].isnull().sum()}")
print("---")

print(f"df1[df1['Sex'] == 'female']\n{df1[df1['Sex'] == 'female']}")
print("---")

print(f"{df1[df1['Sex'] == 'female']}")
print("---")

print("生存者のみ")
print(f"{df1[df1['Survived'] == 1]}")
print("---")
