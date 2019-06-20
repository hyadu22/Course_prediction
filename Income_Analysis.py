# import panda package
import pandas as pd

# import matplotlib package
import matplotlib.pyplot as plt

import seaborn as sns
# Read csv file
data = pd.read_csv('appdata.csv')

# find the missing value
print(data.shape)

# Drop Columns
data.drop(['Essay 1 - Score 3','Essay 2 - Score 3','Essay 3 - Score 3'],axis='columns',inplace=True)
data.drop(['Major'],axis='columns',inplace=True)
data.dropna(subset=['Education'],axis='rows',inplace=True)

# Drop Duplicates
data.drop_duplicates(subset='Fake Email Address',keep=False,inplace=True)

# Remove NAN to mean
data['Essay 1 - Score 1'].fillna(data['Essay 1 - Score 1'].mean(),inplace=True)
data['Essay 1 - Score 2'].fillna(data['Essay 1 - Score 2'].mean(),inplace=True)
data['Essay 2 - Score 1'].fillna(data['Essay 2 - Score 1'].mean(),inplace=True)
data['Essay 2 - Score 2'].fillna(data['Essay 2 - Score 2'].mean(),inplace=True)
data['Essay 3 - Score 1'].fillna(data['Essay 3 - Score 1'].mean(),inplace=True)
data['Essay 3 - Score 2'].fillna(data['Essay 3 - Score 2'].mean(),inplace=True)
data['Max Essay Score'].fillna(data['Max Essay Score'].mean(),inplace=True)
data['Average Essay Score'].fillna(data['Average Essay Score'].value_counts(normalize=True).mean(),inplace=True)

# round the data
#print(data.isnull().sum())

# change the datatype float to int
data['Essay 1 - Score 1']=data['Essay 1 - Score 1'].astype(int)
data['Essay 1 - Score 2']=data['Essay 1 - Score 2'].replace('2.9974522292993635','3').astype(int)
data['Essay 2 - Score 1']=data['Essay 2 - Score 1'].replace('2.867438867438867','3')
#print(data['Essay 2 - Score 1'].mean())
#print(data['Essay 2 - Score 1'].tail(50))

#print(data.round(),decimals=1)
#print(data.dtypes)
# change the datatype
#data['Essay 1 - Score 1']=data['Essay 1 - Score 1'].replace('NaN',essay_score1)


# count of students who enrolled for the course are male/female
plt.bar(data['Gender'],data['Education'])
plt.xlabel('Students Gender')
plt.ylabel('Education')
plt.show()

# age group enrolled and completed
data['Enrollment Status'].value_counts().plot()
plt.xlabel('Enrollment Status')
plt.ylabel('Number of Student')
plt.show()

sns.swarmplot(x=data['Income'],y=data[data['Enrollment Status']== 'Completed'],data=data)

#data.boxplot(column=data['Income'])
#plt.show()