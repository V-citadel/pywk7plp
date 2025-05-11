import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns

#error handling 
try:
    df = pd.read_csv('students.csv')
except FileNotFoundError:
    print("Error: The file 'student_habits_performance' was not found.Please check again the directory")
    exit()

#to display the first five rows 

print("First 5 rows of the  dataset: ")
print (df.head ())
print("\n")

#structure of the dataset
print("Missing values:")
df.info()
print ("\n")

#checking for missing values

print("missing values: ")
print(df.isnull().sum())

#cleaning the data

df=df.dropna()
df=df.drop_duplicates()

print("\n")

# Descriptive statistics
print("\n Descriptive Statistics:")
print(df.describe())


age_col = 'age'      
hours_col = 'study_hours_per_day'        

if age_col in df.columns and hours_col in df.columns:
    grouped = df.groupby(age_col)[hours_col].mean()
    print(f"\n Mean of '{hours_col}' grouped by '{age_col}':")
    print(grouped)
else:
    print("\n Please update 'age_col' and 'hours_col' to match your dataset.")


# Line Chart 

avg_score_by_age = df.groupby('age')['exam_score'].mean().reset_index()

plt.figure(figsize=(10,5))
plt.plot(avg_score_by_age['age'], avg_score_by_age['exam_score'], marker='o')
plt.title(' Average Exam Score by Age')
plt.xlabel('Age')
plt.ylabel('Average Exam Score')
plt.grid(True)
plt.show()

# Bar Chart
sns.barplot(x=age_col , y=hours_col, data=df)
plt.title(f'Average {hours_col} per {age_col }')
plt.xticks(rotation=45)
plt.show()

# Histogram
sns.histplot(df[hours_col], bins=20, kde=True)
plt.title(f'Distribution of {hours_col}')
plt.xlabel(hours_col)
plt.ylabel('Frequency')
plt.show()

# Scatter Plot

age_col  = 'Sales'
hours_col = 'Profit'

if age_col  in df.columns and hours_col in df.columns:
    sns.scatterplot(x=age_col , y=hours_col, data=df, hue=age_col )
    plt.title(f'{age_col } vs {hours_col}')
    plt.xlabel(age_col )
    plt.ylabel(hours_col)
    plt.legend(title=age_col )
    plt.show()
else:
    print("\n Please upage 'age_col ' and 'hours_col' to numeric columns in your dataset.")





