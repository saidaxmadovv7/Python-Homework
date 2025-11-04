##-----------------------------------------
##-----------------------------------------



import pandas as pd


url = "https://raw.githubusercontent.com/IslomovSH/python-homework/refs/heads/main/lesson-18/homework/task/tackoverflow_qa.csv"
df = pd.read_csv(url)

# Jadvalni tekshirish
print("Birinchi 5 qator:")
print(df.head())

print("\nJadval haqida umumiy ma'lumot:")
print(df.info())






import pandas as pd

url1 = "https://raw.githubusercontent.com/IslomovSH/python-homework/refs/heads/main/lesson-18/homework/task/tackoverflow_qa.csv"
url2 = "https://raw.githubusercontent.com/IslomovSH/python-homework/refs/heads/main/lesson-18/homework/task/titanic.csv"

df1 = pd.read_csv(url1)
df2 = pd.read_csv(url2)

print("tackoverflow_qa — birinchi fayl:")
print(df1.head(), "\n")
print("titanic — ikkinchi fayl:")
print(df2.head(), "\n")

print("titanic fayl haqida ma’lumot:")
print(df2.info())



df = pd.read_csv("https://raw.githubusercontent.com/IslomovSH/python-homework/refs/heads/main/lesson-18/homework/task/tackoverflow_qa.csv")
df.head()



df['creationdate'] = pd.to_datetime(df['creationdate'])


before_2014 = df[df['creationdate'] < '2014-01-01']
print(before_2014)



score_gt_50 = df[df['score'] > 50]
print(score_gt_50)






score_50_100 = df[(df['score'] >= 50) & (df['score'] <= 100)]
print(score_50_100)





answered_by_scott = df[df['ans_name'] == 'Scott Boston']
print(answered_by_scott)





users = ['User1', 'User2', 'User3', 'User4', 'User5']
answered_by_5 = df[df['ans_name'].isin(users)]
print(answered_by_5)





filtered_questions = df[
    (df['creationdate'] >= '2014-03-01') & 
    (df['creationdate'] <= '2014-10-31') & 
    (df['ans_name'] == 'Unutbu') & 
    (df['score'] < 5)
]
print(filtered_questions)







filtered_questions2 = df[
    ((df['score'] >= 5) & (df['score'] <= 10)) | 
    (df['viewcount'] > 10000)
]
print(filtered_questions2)





not_by_scott = df[df['ans_name'] != 'Scott Boston']
print(not_by_scott)







titanic_df = pd.read_csv("https://raw.githubusercontent.com/IslomovSH/python-homework/refs/heads/main/lesson-18/homework/task/titanic.csv")
titanic_df.head()






female_20_30 = titanic_df[
    (titanic_df['Sex'] == 'female') & 
    (titanic_df['Pclass'] == 1) & 
    (titanic_df['Age'] >= 20) & 
    (titanic_df['Age'] <= 30)
]
print(female_20_30)








fare_gt_100 = titanic_df[titanic_df['Fare'] > 100]
print(fare_gt_100)






survived_alone = titanic_df[
    (titanic_df['Survived'] == 1) & 
    (titanic_df['SibSp'] == 0) & 
    (titanic_df['Parch'] == 0)
]
print(survived_alone)






embarked_C_fare_gt_50 = titanic_df[
    (titanic_df['Embarked'] == 'C') & 
    (titanic_df['Fare'] > 50)
]
print(embarked_C_fare_gt_50)






both_family = titanic_df[
    (titanic_df['SibSp'] > 0) & 
    (titanic_df['Parch'] > 0)
]
print(both_family)







young_not_survived = titanic_df[
    (titanic_df['Age'] <= 15) & 
    (titanic_df['Survived'] == 0)
]
print(young_not_survived)






cabins_fare_gt_200 = titanic_df[
    (titanic_df['Cabin'].notna()) & 
    (titanic_df['Fare'] > 200)
]
print(cabins_fare_gt_200)






odd_passenger_id = titanic_df[titanic_df['PassengerId'] % 2 == 1]
print(odd_passenger_id)





unique_tickets = titanic_df[titanic_df.duplicated('Ticket', keep=False) == False]
print(unique_tickets)





miss_class1 = titanic_df[
    (titanic_df['Name'].str.contains('Miss')) & 
    (titanic_df['Pclass'] == 1)
]
print(miss_class1)







