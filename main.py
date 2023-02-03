import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Reading Data

df = pd.read_csv("vgsales.csv")
display(df.head())
display(f"Size of dataset : { df.shape} ")
display(df.info())

print("---------------------")
df.describe()
df.describe(include="object")
#checking for null value
(df.isnull().sum()/len(df.index)) * 100
display(df[df["Publisher"].isnull()].shape[0])
df[df["Publisher"].isnull()]


#EDA

df.head()
cat_features = ["Platform", "Year", "Genre", "Publisher"]
num_features = ["NA_Sales", "EU_Sales", "JP_Sales", "Other_Sales", "Global_Sales"]

fig, axis = plt.subplots(4,1,figsize=(20,20))
fig.tight_layout(pad=10.0)
col_number = 0

for i in range(4):
    sns.countplot(ax=axis[i], x=df[cat_features[col_number]])
    axis[i].set_xlabel(cat_features[col_number], fontsize=14);
    axis[i].set_ylabel('Count', fontsize=14);
    axis[i].set_title(f'Distribution of { cat_features[col_number] }', fontsize=16)
    col_number += 1
plt.show()


top_20 = df.groupby('Publisher', as_index=False)['Name'].count().sort_values(by='Name', ascending=False).head(10)


fig, axis = plt.subplots(figsize=(20,10))

top_20.rename(columns ={'Name':'Count'}, inplace=True)
sns.barplot(x=top_20['Publisher'], y=top_20['Count'], ax=axis)
axis.set_xticklabels(axis.get_xticklabels(), rotation=45)
for p in axis.patches:
    h, w, x = p.get_height(), p.get_width(), p.get_x()
    xy = (x + w / 2., h / 2)
    text = f'{h:0.2f}'
    axis.annotate(text=text, xy=xy, ha='center', va='center')
plt.show()


#plotting numeric data to find any relation
fig, axis = plt.subplots(3,2,figsize=(20,20))
fig.tight_layout(pad=7.0)
col_number = 0
for i in range(0,3):
    for j in range(0,2):
        if(col_number > len(num_features)-1):
            break
        sns.histplot(ax=axis[i,j], x=df[num_features[col_number]])
        axis[i,j].set_xlabel(num_features[col_number], fontsize=14);
        axis[i,j].set_title(f'Distribution of { num_features[col_number] }', fontsize=16)
        col_number += 1

plt.show()