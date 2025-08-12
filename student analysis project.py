# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 23:42:59 2025

@author: Deivangh
"""

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

df=pd.read_csv("StudentsPerformance.csv")

print(df)

''' 1) to find out how many null values are present''' 

print(df.info()) #no null values


''' 2)  Do students who complete the test preparation course perform
 better than those who don’t?'''
 
class_stats=df.groupby('test preparation course').agg({'math score':'mean','reading score':'mean','writing score':'mean'})
print(class_stats)

class_stats.plot(kind='bar', figsize=(8,5), colormap='viridis')
plt.title("Average Scores by Test Preparation Course")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--')
plt.show()


'''3) Does parental level of education impact student scores?'''

class_parental=df.groupby('parental level of education').agg({'math score':'mean','reading score':'mean','writing score':'mean'})
print(class_parental)

class_parental.plot(kind='bar', figsize=(10,6), colormap='Set2')
plt.title("Average Scores by Parental Level of Education")
plt.ylabel("Average Score")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()


'''4) Is there a gender gap in student performance? '''

gender_stat=df.groupby('gender').agg({'math score':'mean','reading score':'mean','writing score':'mean'})

print(gender_stat)


gender_stat.T.plot(kind='line', marker='o')
plt.title("Comparison of Scores Between Genders")
plt.ylabel("Average Score")
plt.xlabel("Subjects")
plt.grid(True)
plt.show()


''' 5) to find top 10 performing students.'''

df['average_score']=df[['math score','reading score','writing score']].mean(axis=1)

top_10=df.sort_values('average_score',ascending=False)

print(top_10.head(10))


'''6) To mark the student :
    a) Need improvemnet
    b) Average 
    c) Good 
    d) Excellent 
as per student average marks 

'''

df['grade'] = pd.cut(df['average_score'], bins=[0, 60, 70, 80, 100], labels=['Needs Improvement', 'Average', 'Good', 'Excellent'])



''' 7) Which group (A to E) performs best overall? '''

class_group=df.groupby('race/ethnicity').agg({'math score':'mean','reading score':'mean','writing score':'mean'})

print(class_group)


class_group.plot(kind='bar', figsize=(10,6), colormap='Accent')
plt.title("Average Scores by Student Group (A to E)")
plt.ylabel("Average Score")
plt.xlabel("Race/Ethnicity Group")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()
